function enviar_dados() {
    var objetivo =parseInt(document.querySelector("#objetivo").value)

    fetch('/sugestao_treino', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ objetivo })
    })
    .then(response => response.json())
    .then(data => {
      console.log(data.pergunta1)
      document.getElementById("label1").textContent = data.pergunta1;
      document.getElementById("label2").textContent = data.pergunta2;
      document.getElementById("label3").textContent = data.pergunta3;
      document.getElementById("label4").textContent = data.pergunta4;


    mudarPergunta()
  });
}
function mudarPergunta(){
  const pergunta1 = document.getElementById("p1")
  const pergunta2 = document.getElementById("p2")
  const pergunta3 = document.getElementById("p3")
  const pergunta4 = document.getElementById("p4")

  
  const label1 = document.getElementById("label1")
  const label2 = document.getElementById("label2")
  const label3 = document.getElementById("label3")
  const label4 = document.getElementById("label4")


  pergunta1.style.display = "inline"
  pergunta2.style.display = "inline"
  pergunta3.style.display = "inline"
  pergunta4.style.display = "inline"

  label1.style.display = "block"
  label2.style.display = "block"
  label3.style.display = "block"
  label4.style.display = "block"

}
