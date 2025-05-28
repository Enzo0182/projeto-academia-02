from flask import Flask, request, render_template, session, redirect, url_for, jsonify
import controle, Batida_de_ponto,acompanhamento_de_alunos, cadastro_de_aluno,sugestao_treino

app = Flask(__name__)
app.secret_key = 'Fametro_Gym2025#'

texto = ""
nome = ""
@app.route("/", methods = ["GET"])
def index():
    texto = ""
    return render_template("index.html")

@app.route("/controle", methods=["GET", "POST"])
def controle_aluno():
    global nome
    global texto
    if request.method == "POST":
        nome = request.form["nome"].lower()
        texto = controle.verificar_nome(nome)
        print("Texto final:", texto)
    return render_template("controle.html", texto = texto)

@app.route("/bater_ponto", methods=["GET", "POST"])
def bater_ponto():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        tentativa_atual = session.get("tentativa_atual", 1)

        resposta = Batida_de_ponto.bater_ponto(usuario, senha, tentativa_atual)

        if "Ponto registrado com sucesso" in resposta:
            session.pop("tentativa_atual", None)  # Zera tentativas após sucesso
            return render_template("resultado_batida_ponto.html", resposta=resposta)
        elif "Número máximo de tentativas atingido. Registro de ponto não realizado." in resposta:
            session.pop("tentativa_atual", None)  # Zera tentativas após sucesso
            return render_template("resultado_batida_ponto.html", resposta=resposta)
        else:
            session["tentativa_atual"] = tentativa_atual + 1
            return render_template("batida_ponto.html", texto=resposta)


    else:
        if session.get("tentativa_atual") is None:
            session["tentativa_atual"] = 1
    return render_template("batida_ponto.html")

@app.route("/sugestao_treino", methods=["GET", "POST"])
def sugestao_treinof():
    global resultado

    if request.method == "POST" and request.is_json:
        objetivo = int(request.get_json().get('objetivo'))
        perguntas = sugestao_treino.perguntas(objetivo)

        resposta = {
            "pergunta1": perguntas['pergunta1'],
            "pergunta2": perguntas['pergunta2'],
            "pergunta3": perguntas['pergunta3'],
            "pergunta4": perguntas['pergunta4']

        }


        return jsonify(resposta)
    elif request.method == "POST":
        dados = request.form
        print(int(dados["objetivo"]))
        resposta = sugestao_treino.msgerro

        if "Erro: valores inválidos para peso ou altura." in resposta:

            return render_template("sugestao.html", resposta=resposta)
        elif "Número máximo de tentativas atingido. Registro de ponto não realizado." in resposta:

            return render_template("sugestao.html", resposta=resposta)
        elif "Erro: todas as respostas devem estar entre 1 e 5." in resposta:
            return render_template("sugestao.html", resposta = resposta)
        resultado = sugestao_treino.gerar_plano_emagrecimento(
            dados["peso"],
            dados["altura"],
            dados["p1"],
            dados["p2"],
            dados["p3"],
            dados["p4"],
            dados["objetivo"]
        )
        return render_template("resultado_sugestao.html", resposta= resultado)
    else:
        pergunta1 = None
        pergunta2 = None
        pergunta3 = None
        pergunta4 = None
        pergunta5 = None
    return render_template("sugestao.html", pergunta1=pergunta1, pergunta2=pergunta2,
                           pergunta3=pergunta3, pergunta4=pergunta4, pergunta5=pergunta5,)

@app.route("/acompanhamento", methods=["GET", "POST"])
def acompanhamento():
    if request.method == "POST":
        nomeAluno = request.form["nome"]
        resposta = acompanhamento_de_alunos.acompanhamento_de_aluno(nomeAluno)
        return render_template("acompanhamento.html", aluno = resposta)
    return render_template("acompanhamento.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nomeCadastro = request.form.get("nome")
        idade = request.form.get("idade")
        telefone = request.form.get("telefone")
        email = request.form.get("email")
        cpf = request.form.get("cpf")
        objetivo = request.form.get("objetivo")
        cadastro_de_aluno.adicionar_aluno(nomeCadastro, idade, telefone, email, cpf, objetivo)
        return render_template("cadastro.html")
    return render_template("cadastro.html")

@app.route("/alunos")
def alunos():
    lista = cadastro_de_aluno.listar_alunos()
    return render_template("lista_aluno.html", resposta=f'{lista}<br>')


if __name__ == '__main__':
    app.run(debug= True)
