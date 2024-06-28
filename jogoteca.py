from flask import Flask, render_template, request, redirect, session, flash, url_for

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris','Puzzel','Atari')
jogo2 = Jogo('God Of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombate', 'Luta', 'PS2')

lista = [jogo1, jogo2, jogo3]

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario('Matheus Menecucci','MM','alohomora')
usuario2 = Usuario("Camila Ferreira", "Mila", "paozinho")
usuario3 = Usuario("Guilherme Louro", "Cake", "python_eh_vida")

#dicionário com chave e valor
usuarios = {usuario1.nickname: usuario1,
            usuario2.nickname: usuario2,
            usuario3.nickname: usuario3 }

#inicialiazar a aplicação flask
app = Flask(__name__)
app.secret_key = 'alura'

#definir rotas
@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos = lista)

#definindo outra rota
@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    #renderizando a pagina html
    return render_template('novo.html',titulo='Novo Jogo')


@app.route('/criar', methods = ['POST',])
def criar():
    #pegando o que está nas tags nome, categoria e console
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)

    lista.append(jogo)

    #redirecionando para a rota /
    return redirect(url_for('index'))

@app.route('/login')
def login():
    #armazenando o que está na variavel proxima e jogando no forms
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods = ['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session["usuario_logado"] = usuario.nickname
            # mensagem rapida pro usuário
            flash(session['usuario_logado'] + ' logado com sucesso!')

            # pegando a váriavel proxima
            proxima_pagina = request.form['proxima']

            # redirecionando a pagina para página armazenada na variavel próxima
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

#debug is true para não precisar recarregar sempre que modificarmos o código
app.run(debug=True)