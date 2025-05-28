# quem fez? Wanderley o brabooooo
# alunos = {
#     "wanderley": {
#         "email": "wanderleylacerda@icloud.com",
#         "objetivo": 'ficar saradaooo',
#         "treino1": ["biceps com 100 kg ,30 repetiçoes", "supino inclinado 100 kg cada lado , 50 repetiçoes"]
#
#     },
#     "Mikael": {
#         "email": "mikaelestripadordeporco@icloud.com",
#         "objetivo": "crescer o gluteo pra ficar bonito de tanga",
#         "treino1": ["agachamento com a barra 300 kg", "elevaçao pelvica com 150 kg"]
#     }
# }


def acompanhamento_de_aluno(nome):
    alunos = {
        "wanderley": {
            "email": "wanderleylacerda@icloud.com",
            "objetivo": 'ficar saradaooo',
            "treino1": ["biceps com 100 kg ,30 repetiçoes", "supino inclinado 100 kg cada lado , 50 repetiçoes"]
        },
        "mikael": {
            "email": "mikaelestripadordeporco@icloud.com",
            "objetivo": "crescer o gluteo pra ficar bonito de tanga",
            "treino1": ["agachamento com a barra 300 kg", "elevaçao pelvica com 150 kg"]
        }
    }

    nome_lower = nome.lower()
    if nome_lower in alunos:
        aluno_guardou = alunos[nome_lower]
        treinos = aluno_guardou.get("treino1", [])
        return {
            "encontrado": True,
            "titulo": 'Dados do aluno:',
            "nome": f'nome do aluno: {nome}',
            "email": f'email: {aluno_guardou["email"]}',
            "objetivo": f"objetivo: {aluno_guardou['objetivo']}",
            "mensagem": 'treinos realizados:' if treinos else "Tá faltando academia pra ir pro k2",
            "treinos": treinos
        }
    else:
        #print('aluno nao foi encontrado')
        return {
            "encontrado": False,
            "mensagem": 'aluno não foi encontrado'
        }



#acompanhamento_de_aluno()

# print('\n Dados do aluno:')
        # print(f'nome do aluno: {nome}')
        # print(f'email: {aluno_guardou["email"]}')
        # print(f"objetivo:{aluno_guardou['objetivo']}")
        # print('treinos realizado:')
        # if aluno_guardou["treino1"]:
        #    for i, treino in enumerate(aluno_guardou['treino1'], start=1):
        #        print(f'    {i}, {treino}')
        # else:
        #    print('ta faltando academia pra ir pro k2')