# === MENU INICIAL ===
# Mostra as opções de objetivo para o usuário

print("Escolha o número correspondente ao seu objetivo.")
print("[1] Emagrecimento")
print("[2] Hipertrofia")
print("[3] Definição muscular")

# Loop equivalente ao "enquanto verdadeiro faça" no Portugol
# Valida se o usuário digitou 1, 2 ou 3

while True:
    try:  # Tenta converter o input para número inteiro
        objetivo = int(input("Digite aqui: "))   # Se estiver entre as opções válidas
        if objetivo in [1, 2, 3]:
            break #sai do loop, interrompa no portugol
        else:
            print("Por favor, digite 1, 2 ou 3.")
    except ValueError: # Se não conseguir converter (usuário digitou texto)
        print("Digite um número válido.")

# === ENTRADA DE DADOS ===
# Loop para validar peso e altura (devem ser números positivos)

while True:
    try:
        peso = float(input("Digite seu peso (kg): "))
        altura = float(input("Digite sua altura (m): "))
        if peso > 0 and altura > 0: # Verifica se são valores positivos
            break
        else:
            print("Peso e altura precisam ser maiores que zero.")
    except ValueError:  # Se o usuário digitar algo não numérico
        print("Digite valores válidos para peso e altura.")

# Cálculo do IMC
imc = peso / (altura ** 2)

if imc < 18.5:
    estado_fisico = "Abaixo do peso"
elif imc < 25:
    estado_fisico = "Peso normal"
elif imc < 30:
    estado_fisico = "Sobrepeso"
else:
    estado_fisico = "Obesidade"

if objetivo == 1:  
    # Todas as perguntas seguem o mesmo padrão:
    # Loop infinito até receber um número entre 1 e 5
   
    while True:
        try:
            p1 = int(input("Em uma escala de 1 a 5, o quanto você quer emagrecer? "))
            if 1 <= p1 <= 5:
                break
            else:
                print("Por favor, digite um número de 1 a 5.")
        except ValueError:
            print("Digite um número válido.")
    
    
    while True:
        try:
            p2 = int(input("De 1 a 5, o quanto você gosta de atividades aeróbicas? "))
            if 1 <= p2 <= 5:
                break
            else:
                print("Por favor, digite um número de 1 a 5.")
        except ValueError:
            print("Digite um número válido.")
    
    
    while True:
        try:
            p3 = int(input("De 1 a 5, o quanto você se sente confiante em manter uma rotina consistente? "))
            if 1 <= p3 <= 5:
                break
            else:
                print("Por favor, digite um número de 1 a 5.")
        except ValueError:
            print("Digite um número válido.")
    
    
    while True:
        try:
            p4 = int(input("De 1 a 5, qual sua motivação em aumentar seu gasto calórico diário? "))
            if 1 <= p4 <= 5:
                break
            else:
                print("Por favor, digite um número de 1 a 5.")
        except ValueError:
            print("Digite um número válido.")
    
    pontuacao = p1 + p2 + p3 + p4 #soma das respostas

    print(f"\nSeu objetivo é emagrecimento. Seu estado físico atual é: {estado_fisico}.") # "/n" pula uma linha

    if pontuacao <= 10:
        print("\n=== PLANO LEVE (INICIANTE) ===")
        print("Frequência: 2 a 3x por semana")
        print("Duração: 30-40 minutos por sessão")
        print("\nESTRUTURA DO TREINO:")
        print("1. Aquecimento (5-10 min):")
        print("   - Caminhada leve ou esteira (velocidade 5.0 km/h)")
        print("   - Mobilidade articular (ombros, quadril, joelhos)")
        print("\n2. Circuito Funcional (2 voltas):")
        print("   - Agachamento livre (3x12 reps) - descanso 30s")
        print("   - Flexão de braços na parede (3x10 reps) - descanso 30s")
        print("   - Prancha abdominal (3x20 segundos) - descanso 30s")
        print("   - Elevação de calcanhares (3x15 reps) - descanso 30s")
        print("\n3. Cardio Leve (10-15 min):")
        print("   - Caminhada em rampa (esteira inclinada 5%)")
        print("   OU bicicleta ergométrica (resistência leve)")
        print("\n4. Alongamento (5 min):")
        print("   - Panturrilhas, peitoral, isquiotibiais")

    elif 11 <= pontuacao <= 14:
        print("\n=== PLANO MÉDIO (INTERMEDIÁRIO) ===")
        print("Frequência: 3 a 4x por semana")
        print("Duração: 45-60 minutos por sessão")
        print("\nESTRUTURA DO TREINO:")
        print("1. Aquecimento Dinâmico (10 min):")
        print("   - Polichinelos (3x20 reps)")
        print("   - Agachamento com peso corporal (3x15 reps)")
        print("   - Burpees modificados (3x10 reps)")
        print("\n2. Treino em Circuito (3 voltas):")
        print("   - Agachamento com salto (4x15 reps) - descanso 45s")
        print("   - Flexão de braços (4x12 reps) - descanso 45s")
        print("   - Abdominal supra (4x20 reps) - descanso 45s")
        print("   - Afundo alternado (4x10 reps perna) - descanso 45s")
        print("   - Prancha com elevação de quadril (4x30 seg) - descanso 45s")
        print("\n3. HIIT (15-20 min):")
        print("   - 30s trabalho / 30s descanso (8 rounds)")
        print("   - Corrida estacionária / Escalador / Polichinelo / Salto vertical")
        print("\n4. Alongamento (5-10 min):")
        print("   - Foco em cadeia posterior e mobilidade torácica")

    else:
        print("\n=== PLANO AVANÇADO (ALTA QUEIMA) ===")
        print("Frequência: 4 a 5x por semana")
        print("Duração: 60-75 minutos por sessão")
        print("\nESTRUTURA DO TREINO:")
        print("1. Aquecimento Específico (15 min):")
        print("   - Corda naval (5 min)")
        print("   - Mobilidade completa + alongamento dinâmico")
        print("\n2. Circuito Metabólico (5 voltas):")
        print("   - Agachamento com salto + overhead press (4x20 reps) - descanso 30s")
        print("   - Burpees completo (4x15 reps) - descanso 30s")
        print("   - Mountain climber (4x30 reps) - descanso 30s")
        print("   - Kettlebell swing (4x25 reps) - descanso 30s")
        print("   - Box jump (4x12 reps) - descanso 30s")
        print("\n3. HIIT Intenso (20-25 min):")
        print("   - Tabata protocol (8 rounds de 20s/10s)")
        print("   - Esteira sprint (1 min max / 1 min caminhada)")
        print("\n4. Alongamento + Liberação Miofascial (10-15 min):")
        print("   - Rolamento com foam roller (pernas, costas)")
        print("   - Alongamento estático profundo")

# [Os outros objetivos (2-Hipertrofia e 3-Definição) seguem a mesma lógica...]

elif objetivo == 2:  
    while True:
        try:
            p1 = int(input("Em uma escala de 1 a 5, o quanto você quer ganhar massa muscular? "))
            if 1 <= p1 <= 5:
                break
            else:
                print("Por favor, digite um número de 1 a 5.")
        except ValueError:
            print("Digite um número válido.")
    

    while True:
        try:
            p2 = int(input("De 1 a 5, o quanto você gosta de treinos de força? "))
            if 1 <= p2 <= 5:
                break
            else:
                print("Por favor, digite um número de 1 a 5.")
        except ValueError:
            print("Digite um número válido.")
    
    
    while True:
        try:
            p3 = int(input("De 1 a 5, o quanto você está disposto(a) a manter consistência nos treinos? "))
            if 1 <= p3 <= 5:
                break
            else:
                print("Por favor, digite um número de 1 a 5.")
        except ValueError:
            print("Digite um número válido.")
    
   
    while True:
        try:
            p4 = int(input("De 1 a 5, o quanto você se preocupa em aumentar cargas progressivamente? "))
            if 1 <= p4 <= 5:
                break
            else:
                print("Por favor, digite um número de 1 a 5.")
        except ValueError:
            print("Digite um número válido.")
    
    pontuacao = p1 + p2 + p3 + p4

    print(f"\nSeu objetivo é hipertrofia. Seu estado físico atual é: {estado_fisico}.")

    if pontuacao <= 10:
        print("\n=== PLANO LEVE (INICIANTE) ===")
        print("Frequência: 3x por semana (Full Body)")
        print("\nROTINA DE TREINO:")
        print("Dia 1 - Full Body:")
        print("   - Agachamento livre 3x10-12 (60s descanso)")
        print("   - Supino reto com halteres 3x10-12 (60s)")
        print("   - Remada curvada 3x10-12 (60s)")
        print("   - Leg press 45° 3x12-15 (45s)")
        print("   - Rosca direta 3x12-15 (45s)")
        print("   - Prancha abdominal 3x30s (30s)")
        
        print("\nDia 2 - Descanso ou cardio leve")
        
        print("\nDia 3 - Full Body:")
        print("   - Stiff 3x10-12 (60s)")
        print("   - Desenvolvimento militar 3x10-12 (60s)")
        print("   - Puxada frontal 3x10-12 (60s)")
        print("   - Mesa flexora 3x12-15 (45s)")
        print("   - Tríceps testa 3x12-15 (45s)")
        print("   - Abdominal infra 3x15 (30s)")

    elif 11 <= pontuacao <= 14:
        print("\n=== PLANO MÉDIO (INTERMEDIÁRIO) ===")
        print("Frequência: 4-5x por semana (Split AB)")
        print("\nROTINA DE TREINO:")
        print("Dia A - Superiores:")
        print("   - Supino reto 4x8-10 (90s)")
        print("   - Remada máquina 4x8-10 (90s)")
        print("   - Desenvolvimento halteres 4x10-12 (60s)")
        print("   - Crucifixo inverso 4x12-15 (45s)")
        print("   - Rosca martelo 4x10-12 (45s)")
        print("   - Tríceps pulley 4x12-15 (45s)")
        
        print("\nDia B - Inferiores:")
        print("   - Agachamento livre 4x8-10 (120s)")
        print("   - Leg press 45° 4x10-12 (90s)")
        print("   - Stiff barra 4x8-10 (90s)")
        print("   - Cadeira extensora 4x12-15 (45s)")
        print("   - Panturrilha em pé 4x15-20 (30s)")
        print("   - Abdominal oblíquo 4x15 (30s)")
        
        print("\nDia C - Descanso")
        
        print("\nDia D - Superiores (Volume):")
        print("   - Barra fixa 4xMAX (90s)")
        print("   - Crucifixo máquina 4x12-15 (60s)")
        print("   - Elevação lateral 4x15-20 (45s)")
        print("   - Rosca direta W 4x10-12 (45s)")
        print("   - Tríceps francês 4x12-15 (45s)")
        
        print("\nDia E - Inferiores (Intensidade):")
        print("   - Agachamento hack 4x8-10 (120s)")
        print("   - Afundo búlgaro 4x10-12 (90s)")
        print("   - Mesa flexora 4x12-15 (60s)")
        print("   - Gêmeos sentado 4x20-25 (30s)")
        print("   - Prancha 4x45s (30s)")

    else:
        print("\n=== PLANO AVANÇADO ===")
        print("Frequência: 5-6x por semana (Split ABCDE)")
        print("\nROTINA DE TREINO:")
        print("Dia A - Peito/Tríceps:")
        print("   - Supino inclinado 5x6-8 (120s)")
        print("   - Supino reto com halteres 4x8-10 (90s)")
        print("   - Peck deck 4x12-15 (60s)")
        print("   - Mergulho 4xMAX (60s)")
        print("   - Tríceps francês 4x10-12 (45s)")
        print("   - Corda 4x15-20 (30s)")
        
        print("\nDia B - Costas/Bíceps:")
        print("   - Barra fixa peso 5x6-8 (120s)")
        print("   - Remada curvada 4x8-10 (90s)")
        print("   - Pulley frente 4x10-12 (60s)")
        print("   - Rosca direta 4x8-10 (60s)")
        print("   - Rosca concentrada 4x12-15 (45s)")
        
        print("\nDia C - Pernas:")
        print("   - Agachamento livre 5x5 (180s)")
        print("   - Leg press 5x8-10 (120s)")
        print("   - Stiff 4x8-10 (90s)")
        print("   - Cadeira extensora 4x12-15 (60s)")
        print("   - Panturrilha 5x20-25 (30s)")
        
        print("\nDia D - Ombros/Trapézio:")
        print("   - Desenvolvimento militar 5x6-8 (120s)")
        print("   - Elevação lateral 5x12-15 (60s)")
        print("   - Crucifixo inverso 4x15-20 (45s)")
        print("   - Encolhimento barra 4x12-15 (45s)")
        
        print("\nDia E - Braços/Abdômen:")
        print("   - Rosca scott 5x8-10 (60s)")
        print("   - Tríceps testa 5x8-10 (60s)")
        print("   - Rosca martelo 4x12-15 (45s)")
        print("   - Tríceps corda 4x15-20 (45s)")
        print("   - Abdominal supra 5x20 (30s)")
        print("   - Prancha lateral 4x30s (30s)")

elif objetivo == 3:  
    
    while True:
        try:
            p1 = int(input("Em uma escala de 1 a 5, o quanto você quer definição muscular? "))
            if 1 <= p1 <= 5:
                break
            else:
                print("Por favor, digite um número de 1 a 5.")
        except ValueError:
            print("Digite um número válido.")
    
    
    while True:
        try:
            p2 = int(input("De 1 a 5, o quanto você gosta de treinos que misturam força e cardio? "))
            if 1 <= p2 <= 5:
                break
            else:
                print("Por favor, digite um número de 1 a 5.")
        except ValueError:
            print("Digite um número válido.")
    
    
    while True:
        try:
            p3 = int(input("De 1 a 5, o quanto você está disposto(a) a manter uma dieta equilibrada para definição? "))
            if 1 <= p3 <= 5:
                break
            else:
                print("Por favor, digite um número de 1 a 5.")
        except ValueError:
            print("Digite um número válido.")
    
    
    while True:
        try:
            p4 = int(input("De 1 a 5, o quanto você gosta de treinos com alta queima calórica, como circuitos ou HIIT? "))
            if 1 <= p4 <= 5:
                break
            else:
                print("Por favor, digite um número de 1 a 5.")
        except ValueError:
            print("Digite um número válido.")
    
    pontuacao = p1 + p2 + p3 + p4

    print(f"\nSeu objetivo é definição muscular. Seu estado físico atual é: {estado_fisico}.")

    if pontuacao <= 10:
        print("\n=== PLANO LEVE (INICIANTE) ===")
        print("Frequência: 3x por semana (2 força + 1 cardio)")
        print("\nROTINA DE TREINO:")
        print("Dia 1 - Full Body:")
        print("   - Agachamento goblet 4x12-15 (60s)")
        print("   - Flexão de braços 4xMAX (60s)")
        print("   - Remada máquina 4x12-15 (60s)")
        print("   - Abdominal supra 4x15 (30s)")
        
        print("\nDia 2 - Cardio (30 min):")
        print("   - Esteira (alternar 2 min caminhada / 1 min trote)")
        print("   OU bicicleta (resistência moderada)")
        
        print("\nDia 3 - Full Body:")
        print("   - Afundo estático 4x10 perna (60s)")
        print("   - Puxada frontal 4x12-15 (60s)")
        print("   - Elevação lateral 4x15 (45s)")
        print("   - Prancha 4x30s (30s)")

    elif 11 <= pontuacao <= 14:
        print("\n=== PLANO MÉDIO (INTERMEDIÁRIO) ===")
        print("Frequência: 4-5x por semana (3 força + 2 HIIT)")
        print("\nROTINA DE TREINO:")
        print("Dia A - Superiores:")
        print("   - Supino reto 4x10-12 (60s)")
        print("   - Barra fixa 4xMAX (60s)")
        print("   - Desenvolvimento halteres 4x12-15 (45s)")
        print("   - Rosca direta 4x12-15 (45s)")
        print("   - Tríceps corda 4x15-20 (45s)")
        
        print("\nDia B - Inferiores:")
        print("   - Agachamento sumô 4x12-15 (60s)")
        print("   - Leg press 45° 4x15-20 (60s)")
        print("   - Stiff 4x12-15 (60s)")
        print("   - Panturrilha 4x20-25 (30s)")
        
        print("\nDia C - HIIT (20 min):")
        print("   - 8 rounds de 30s trabalho / 30s descanso")
        print("   - Burpees / Escalador / Salto corda / Polichinelo")
        
        print("\nDia D - Full Body (Circuito):")
        print("   - 3 voltas sem descanso entre exercícios:")
        print("   • Kettlebell swing x15")
        print("   • Flexão diamante x12")
        print("   • Agachamento salto x15")
        print("   • Prancha com rotação x10 lado")
        print("   • Mountain climber x20")
        print("   (Descanso 60s entre voltas)")
        
        print("\nDia E - Cardio em Jejum (opcional):")
        print("   - 30 min caminhada em rampa")

    else:
        print("\n=== PLANO AVANÇADO ===")
        print("Frequência: 5-6x por semana (4 força + 2 HIIT)")
        print("\nROTINA DE TREINO:")
        print("Dia A - Peito/Tríceps (Volume):")
        print("   - Supino inclinado 5x10-12 (60s)")
        print("   - Supino declinado 4x12-15 (60s)")
        print("   - Peck deck 4x15-20 (45s)")
        print("   - Tríceps testa 4x12-15 (45s)")
        print("   - Corda 4x20-25 (30s)")
        
        print("\nDia B - Costas/Bíceps (Densidade):")
        print("   - Barra fixa 5xMAX (60s)")
        print("   - Remada curvada 4x12-15 (60s)")
        print("   - Face pull 4x15-20 (45s)")
        print("   - Rosca martelo 4x15-20 (45s)")
        print("   - Rosca concentrada 4x12-15 (30s)")
        
        print("\nDia C - HIIT Metabólico (25 min):")
        print("   - 10 rounds de 40s trabalho / 20s descanso")
        print("   - Kettlebell swing / Box jump / Burpees / Corda naval")
        
        print("\nDia D - Pernas (Intensidade):")
        print("   - Agachamento frontal 5x8-10 (90s)")
        print("   - Leg press 5x15-20 (60s)")
        print("   - Stiff 4x12-15 (60s)")
        print("   - Cadeira extensora 4x20-25 (45s)")
        print("   - Panturrilha 5x25-30 (30s)")
        
        print("\nDia E - Ombros/Abdômen (Super Set):")
        print("   - Desenvolvimento Arnold 4x12-15 (60s)")
        print("   - Elevação lateral 4x15-20 (45s)")
        print("   - Crucifixo inverso 4x20 (45s)")
        print("   - Abdominal infra + supra (4x20+20)")
        print("   - Prancha lateral 4x30s lado")
        
        print("\nDia F - HIIT Cardio (30 min):")
        print("   - Esteira (1 min sprint / 1 min caminhada)")
        print("   OU natação (tiros de 50m)")