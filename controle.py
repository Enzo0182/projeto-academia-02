import interface

alunos = {
    "igor": {"status": "pago"},
    "nathy": {"status": "não pago"},
    "thiago": {"status": "pago"}
}

def verificar_nome(aluno):
    if aluno in alunos:
        situacao = alunos[aluno]['status'] == 'pago'
        if situacao:
            print("Aluno em dia, acesso autorizado.")
            return "Aluno em dia, acesso autorizado."
        else:
            print("Aluno inadimplente, acesso negado.")

            return "Aluno inadimplente, acesso negado."
    else:
        print("Aluno não encontrado.")
        return "Aluno não encontrado."
