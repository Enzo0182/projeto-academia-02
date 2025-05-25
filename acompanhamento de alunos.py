# quem fez? Wanderley o brabooooo
aluno = {
    "wanderley": {
        "email": "wanderleylacerda@icloud.com",
        "objetivo": 'ficar saradaooo',
        "treino1": ["biceps com 100 kg ,30 repetiçoes", "supino inclinado 100 kg cada lado , 50 repetiçoes"]

    },
    "Mikael": {
        "email": "mikaelestripadordeporco@icloud.com",
        "objetivo": "crescer o gluteo pra ficar bonito de tanga",
        "treino1": ["agachamento com a barra 300 kg", "elevaçao pelvica com 150 kg"]
    }
}


def acompanhamento_de_aluno():
    nome = input('digite o nome do aluno para o acompanhamento:')
    if nome in aluno:
        aluno_guardou = aluno[nome]
        print('\n Dados do aluno:')
        print(f'nome do aluno: {nome}')
        print(f'email: {aluno_guardou["email"]}')
        print(f"objetivo:{aluno_guardou['objetivo']}")
        print('treinos realizado:')
        if aluno_guardou["treino1"]:
            for i, treino in enumerate(aluno_guardou['treino1'], start=1):
                print(f'    {i}, {treino}')
        else:
            print('ta faltando academia pra ir pro k2')
    else:
        print('aluno nao foi encontrado')


acompanhamento_de_aluno()
