# Simulação de banco de dados de funcionários
funcionarios = {
    "renata": {"senha": "1234", "cargo": "recepcionista"},
    "lucas": {"senha": "4321", "cargo": "personal"}
}
# #Repetições caso falso
# def bater_ponto(tentativas_max=5):
#     print("=== Batida de Ponto ===")
#
#     tentativas = 0
#     while tentativas < tentativas_max:
#         usuario = input("Nome do funcionário: ").lower()
#         senha = input("Senha: ")
#
#         if usuario in funcionarios and funcionarios[usuario]["senha"] == senha:
#             print(f"\n Ponto registrado com sucesso!")
#             print(f"Bem-vindo(a), {usuario.title()} ({funcionarios[usuario]['cargo'].title()})")
#             return True
#         else:
#             tentativas += 1
#             print(f"\n Dados incorretos. Tentativas restantes: {tentativas_max - tentativas}\n")
#
#     print(" Número máximo de tentativas atingido. Registro de ponto não realizado.")
#     return False
#
# # Execução
# if bater_ponto():
#     print("Registro de ponto finalizado com sucesso.")
# else:
#     print("Encerrando processo.")



# Para uso com Flask
def bater_ponto(usuario, senha, tentativa_atual=1, tentativas_max=5):
    usuario = usuario.strip().lower()
    senha = senha.strip()

    if tentativa_atual >= tentativas_max:
        return "Número máximo de tentativas atingido. Registro de ponto não realizado."

    if usuario in funcionarios and funcionarios[usuario]["senha"] == senha:
        cargo = funcionarios[usuario]["cargo"].title()
        nome = usuario.title()
        return f"Ponto registrado com sucesso!<br>Bem-vindo(a), {nome} ({cargo})"
    else:
        restantes = tentativas_max - tentativa_atual
        return f"Dados incorretos. Tentativas restantes: {restantes}"
