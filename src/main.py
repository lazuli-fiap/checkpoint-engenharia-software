from flask import Flask, render_template, request, redirect, url_for, flash, session
from src.auth.cadastro import registrar_usuario
from src.auth.login import autenticar_usuario
from src.data.database import get_connection
import os
from datetime import datetime

# Set templates and static folder relative to current file
app = Flask(__name__, template_folder='views', static_folder='static')
app.secret_key = 'super_secret_key_checkpoint2'

# ----------- Rotas Principais -----------

@app.route('/')
def index():
    if 'usuario_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

# ----------- Rotas de Autenticação -----------

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        sucesso, msg = registrar_usuario(nome, email, senha)
        if sucesso:
            flash(msg, 'success')
            return redirect(url_for('login'))
        else:
            flash(msg, 'error')
            
    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        usuario, msg = autenticar_usuario(email, senha)
        if usuario:
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            flash(msg, 'success')
            return redirect(url_for('dashboard'))
        else:
            flash(msg, 'error')
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("Logout realizado com sucesso.", 'success')
    return redirect(url_for('login'))

# ----------- Rotas do Sistema (Dashboard e Reservas) -----------

@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        flash('Faça login para acessar o sistema.', 'error')
        return redirect(url_for('login'))
        
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM laboratorios ORDER BY nome ASC")
    laboratorios = cursor.fetchall()
    conn.close()
    
    return render_template('dashboard.html', laboratorios=laboratorios)

@app.route('/novo_laboratorio', methods=['POST'])
def novo_laboratorio():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
        
    nome = request.form.get('nome')
    if not nome:
        flash("O nome do laboratório é obrigatório.", "error")
        return redirect(url_for('dashboard'))
        
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO laboratorios (nome) VALUES (?)", (nome,))
        conn.commit()
        flash("Laboratório adicionado com sucesso!", "success")
    except Exception as e:
        if "UNIQUE constraint" in str(e):
            flash("Já existe um laboratório com este nome.", "error")
        else:
            flash("Erro ao adicionar laboratório.", "error")
    finally:
        conn.close()
        
    return redirect(url_for('dashboard'))

@app.route('/reservar', methods=['POST'])
def reservar():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
        
    usuario_id = session['usuario_id']
    lab_id = request.form.get('lab_id')
    data_hora_str = request.form.get('data_hora')
    
    if not lab_id or not data_hora_str:
        flash("Preencha todos os campos da reserva.", "error")
        return redirect(url_for('dashboard'))
        
    try:
        # datetime-local retorna algo como 2026-05-15T10:30
        data_hora_obj = datetime.strptime(data_hora_str, '%Y-%m-%dT%H:%M')
        data_formatada = data_hora_obj.strftime('%d/%m/%Y %H:%M')
        
        conn = get_connection()
        cursor = conn.cursor()
        
        # Verifica conflito de horário
        cursor.execute("SELECT id FROM reservas WHERE laboratorio_id = ? AND data_hora = ?", (lab_id, data_formatada))
        if cursor.fetchone():
            flash("Este horário já está reservado para este laboratório.", "error")
            conn.close()
            return redirect(url_for('dashboard'))
            
        cursor.execute("INSERT INTO reservas (usuario_id, laboratorio_id, data_hora) VALUES (?, ?, ?)", 
                       (usuario_id, lab_id, data_formatada))
        conn.commit()
        conn.close()
        
        flash("Reserva realizada com sucesso!", "success")
        return redirect(url_for('reservas'))
        
    except ValueError:
        flash("Formato de data/hora inválido.", "error")
        return redirect(url_for('dashboard'))

@app.route('/reservas')
def reservas():
    if 'usuario_id' not in session:
        flash('Faça login para acessar o sistema.', 'error')
        return redirect(url_for('login'))
        
    usuario_id = session['usuario_id']
    
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT r.id, l.nome as nome_lab, r.data_hora 
        FROM reservas r
        JOIN laboratorios l ON r.laboratorio_id = l.id
        WHERE r.usuario_id = ?
        ORDER BY r.data_hora ASC
    """
    cursor.execute(query, (usuario_id,))
    minhas_reservas = cursor.fetchall()
    conn.close()
    
    return render_template('reservas.html', reservas=minhas_reservas)

@app.route('/cancelar_reserva/<int:reserva_id>', methods=['POST'])
def cancelar_reserva(reserva_id):
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
        
    usuario_id = session['usuario_id']
    
    conn = get_connection()
    cursor = conn.cursor()
    # Garante que só o dono pode cancelar
    cursor.execute("DELETE FROM reservas WHERE id = ? AND usuario_id = ?", (reserva_id, usuario_id))
    conn.commit()
    conn.close()
    
    flash("Reserva cancelada com sucesso.", "success")
    return redirect(url_for('reservas'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
