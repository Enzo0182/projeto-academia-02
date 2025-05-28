# Cadastro simples de aluno para academia
# class Aluno:
#     def __init__(self, nome, idade, telefone, email, cpf, objetivo):
#         self.nome = nome
#         self.idade = idade
#         self.telefone = telefone
#         self.email = email
#         self.cpf = cpf
#         self.objetivo = objetivo
#
#     def __str__(self):
#         return f"Nome: {self.nome}, Idade: {self.idade}, Objetivo: {self.objetivo}"
#
# # Lista para armazenar os alunos cadastrados
# alunos = []
#
# def cadastrar_aluno():
#     print("\n--- Cadastro de Novo Aluno ---")
#     nome = input("Nome completo: ")
#     idade = input("Idade: ")
#     telefone = input("Telefone: ")
#     email = input("E-mail: ")
#     cpf = input("CPF: ")
#     objetivo = input("Objetivo (Emagrecimento, Hipertrofia, Condicionamento, etc.): ")
#
#     aluno = Aluno(nome, idade, telefone, email, cpf, objetivo)
#     alunos.append(aluno)
#     print(f"\nAluno {nome} cadastrado com sucesso!")
#
# def listar_alunos():
#     print("\n--- Alunos Cadastrados ---")
#     for i, aluno in enumerate(alunos, start=1):
#         print(f"{i}. {aluno}")
#
# # Menu simples
# while True:
#     print("\n1. Cadastrar Aluno")
#     print("2. Listar Alunos")
#     print("3. Sair")
#     opcao = input("Escolha uma opção: ")
#
#     if opcao == '1':
#         cadastrar_aluno()
#     elif opcao == '2':
#         listar_alunos()
#     elif opcao == '3':
#         print("Encerrando o sistema.")
#         break
#     else:
#         print("Opção inválida, tente novamente.")


class Aluno:
    def __init__(self, nome, idade, telefone, email, cpf, objetivo):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.objetivo = objetivo

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Objetivo: {self.objetivo}"

# Lista global para armazenar alunos em memória
alunos = []

def adicionar_aluno(nome, idade, telefone, email, cpf, objetivo):
    aluno = Aluno(nome, idade, telefone, email, cpf, objetivo)
    alunos.append(aluno)

def listar_alunos():
    return [str(aluno) for aluno in alunos]


