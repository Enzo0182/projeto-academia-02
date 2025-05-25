from flask import Flask, request, render_template
import controle

app = Flask(__name__)

texto = ""
nome = ""
@app.route("/", methods=["GET", "POST"])
def formulario():
    global nome
    global texto
    if request.method == "POST":
        nome = request.form["nome"].lower()
        texto = controle.verificar_nome(nome)
        print("Texto final:", texto)
    return render_template("form.html", texto = texto)

if __name__ == '__main__':
    app.run(debug= True)
