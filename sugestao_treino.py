msgerro = ""
perguntasR = {}
def perguntas(objetivo):
    global perguntasR
    if objetivo == 1:
        perguntasR = {
            "pergunta1" : "Em uma escala de 1 a 5, o quanto você quer emagrecer?",
            "pergunta2" : "De 1 a 5, o quanto você gosta de atividades aeróbicas?",
            "pergunta3" : "De 1 a 5, o quanto você se sente confiante em manter uma rotina consistente?",
            "pergunta4" : "De 1 a 5, qual sua motivação em aumentar seu gasto calórico diário?"
        }
        return perguntasR
    elif objetivo == 2:
        perguntasR = {
            "pergunta1": "Em uma escala de 1 a 5, o quanto você quer ganhar massa muscular?",
            "pergunta2": "De 1 a 5, o quanto você gosta de treinos de força?",
            "pergunta3": "De 1 a 5, o quanto você está disposto(a) a manter consistência nos treinos?",
            "pergunta4": "De 1 a 5, o quanto você se preocupa em aumentar cargas progressivamente?"
        }
        return perguntasR
    elif objetivo == 3:
        perguntasR = {
            "pergunta1": "Em uma escala de 1 a 5, o quanto você quer definição muscular?",
            "pergunta2": "De 1 a 5, o quanto você gosta de treinos que misturam força e cardio?",
            "pergunta3": "De 1 a 5, o quanto você está disposto(a) a manter uma dieta equilibrada para definição?",
            "pergunta4": "De 1 a 5, o quanto você gosta de treinos com alta queima calórica, como circuitos ou HIIT?"
        }
        return perguntasR
    return None



def gerar_plano_emagrecimento(peso, altura, p1, p2, p3, p4, objetivo):
    resultado = ""
    global msgerro
    
    try:
        peso = float(peso)
        altura = float(altura)
        imc = peso / (altura ** 2)
    except (ValueError, ZeroDivisionError):
        msgerro = f"Erro: valores inválidos para peso ou altura."
        return msgerro

    if imc < 18.5:
        estado_fisico = "abaixo do peso"
    elif 18.5 <= imc < 25:
        estado_fisico = "peso normal"
    elif 25 <= imc < 30:
        estado_fisico = "sobrepeso"
    else:
        estado_fisico = "obesidade"

    resultado += f"Seu IMC é: {imc:.2f} - Estado físico: {estado_fisico}<br>"

    try:
        respostas = list(map(int, [p1, p2, p3, p4]))
        if not all(1 <= r <= 5 for r in respostas):
            msgerro = f"Erro: todas as respostas devem estar entre 1 e 5."
            return msgerro
    except ValueError:
        msgerro = f"Erro: as respostas devem ser números inteiros entre 1 e 5."
        return msgerro

    pontuacao = sum(respostas)
    objetivo = int(objetivo)
    
    if objetivo == 1:
        resultado += f"Sua pontuação de motivação: {pontuacao}<br>"
        resultado += f"Seu objetivo é emagrecimento. Seu estado físico atual é: {estado_fisico}.<br><br>"

        if pontuacao <= 10:
            resultado += "=== PLANO LEVE (INICIANTE) ===<br><br>"
            resultado += "- Caminhada leve 3x por semana por 30 minutos<br>"
            resultado += "- Redução de alimentos processados e açúcares<br>"
            resultado += "- Incluir mais frutas e vegetais na dieta<br>"
            resultado += "- Beber pelo menos 2L de água por dia<br>"
            resultado += "- Dormir 7-8 horas por noite<br><br>"

        elif 11 <= pontuacao <= 14:
            resultado += "=== PLANO MÉDIO (INTERMEDIÁRIO) ===<br>"
            resultado += "- Caminhada rápida ou corrida leve 4x por semana por 40 minutos<br>"
            resultado += "- Treino funcional em casa 2x por semana<br>"
            resultado += "- Dieta com déficit calórico moderado<br>"
            resultado += "- Acompanhamento com nutricionista se possível<br>"
            resultado += "- Controle de porções e evitar comer por ansiedade<br>"

        else:
            resultado += "=== PLANO AVANÇADO (ALTA QUEIMA) ===<br>"
            resultado += "- Corrida, HIIT ou bicicleta 5x por semana<br>"
            resultado += "- Musculação ou treino funcional 3x por semana<br>"
            resultado += "- Dieta com déficit calórico bem calculado<br>"
            resultado += "- Controle rigoroso da alimentação com acompanhamento<br>"
            resultado += "- Técnicas de mindfulness para controle emocional<br>"

            
    elif objetivo == 2:
        resultado +=f"Seu objetivo é hipertrofia. Seu estado físico atual é: {estado_fisico}.<br><br>"

        if pontuacao <= 10:
            resultado +="=== PLANO LEVE (INICIANTE) ===<br>"
            resultado += "Frequência: 3x por semana (Full Body)<br>"
            resultado +="ROTINA DE TREINO:<br>"
            resultado += "Dia 1 - Full Body:<br>"
            resultado += "   - Agachamento livre 3x10-12 (60s descanso)<br>"
            resultado += "   - Supino reto com halteres 3x10-12 (60s)<br>"
            resultado += "   - Remada curvada 3x10-12 (60s)<br>"
            resultado += "   - Leg press 45° 3x12-15 (45s)<br>"
            resultado += "   - Rosca direta 3x12-15 (45s)<br>"
            resultado += "   - Prancha abdominal 3x30s (30s)<br>"

            resultado +="Dia 2 - Descanso ou cardio leve<br>"

            resultado +="Dia 3 - Full Body:<br>"
            resultado += "   - Stiff 3x10-12 (60s)<br>"
            resultado += "   - Desenvolvimento militar 3x10-12 (60s)<br>"
            resultado += "   - Puxada frontal 3x10-12 (60s)<br>"
            resultado += "   - Mesa flexora 3x12-15 (45s)<br>"
            resultado += "   - Tríceps testa 3x12-15 (45s)<br>"
            resultado += "   - Abdominal infra 3x15 (30s)<br>"

        elif 11 <= pontuacao <= 14:
            resultado +="=== PLANO MÉDIO (INTERMEDIÁRIO) ===<br>"
            resultado += "Frequência: 4-5x por semana (Split AB)<br>"
            resultado +="ROTINA DE TREINO:<br>"
            resultado += "Dia A - Superiores:"
            resultado += "   - Supino reto 4x8-10 (90s)<br>"
            resultado += "   - Remada máquina 4x8-10 (90s)<br>"
            resultado += "   - Desenvolvimento halteres 4x10-12 (60s)<br>"
            resultado += "   - Crucifixo inverso 4x12-15 (45s)<br>"
            resultado += "   - Rosca martelo 4x10-12 (45s)<br>"
            resultado += "   - Tríceps pulley 4x12-15 (45s)<br>"

            resultado +="Dia B - Inferiores:"
            resultado += "   - Agachamento livre 4x8-10 (120s)<br>"
            resultado += "   - Leg press 45° 4x10-12 (90s)<br>"
            resultado += "   - Stiff barra 4x8-10 (90s)<br>"
            resultado += "   - Cadeira extensora 4x12-15 (45s)<br>"
            resultado += "   - Panturrilha em pé 4x15-20 (30s)<br>"
            resultado += "   - Abdominal oblíquo 4x15 (30s)<br>"

            resultado +="Dia C - Descanso<br>"

            resultado +="Dia D - Superiores (Volume):<br>"
            resultado += "   - Barra fixa 4xMAX (90s)<br>"
            resultado += "   - Crucifixo máquina 4x12-15 (60s)<br>"
            resultado += "   - Elevação lateral 4x15-20 (45s)<br>"
            resultado += "   - Rosca direta W 4x10-12 (45s)<br>"
            resultado += "   - Tríceps francês 4x12-15 (45s)<br>"

            resultado +="Dia E - Inferiores (Intensidade):<br>"
            resultado += "   - Agachamento hack 4x8-10 (120s)<br>"
            resultado += "   - Afundo búlgaro 4x10-12 (90s)<br>"
            resultado += "   - Mesa flexora 4x12-15 (60s)<br>"
            resultado += "   - Gêmeos sentado 4x20-25 (30s)<br>"
            resultado += "   - Prancha 4x45s (30s)<br>"

        else:
            resultado +="=== PLANO AVANÇADO ===<br>"
            resultado += "Frequência: 5-6x por semana (Split ABCDE)<br>"
            resultado +="ROTINA DE TREINO:<br>"
            resultado += "Dia A - Peito/Tríceps:<br>"
            resultado += "   - Supino inclinado 5x6-8 (120s)<br>"
            resultado += "   - Supino reto com halteres 4x8-10 (90s)<br>"
            resultado += "   - Peck deck 4x12-15 (60s)<br>"
            resultado += "   - Mergulho 4xMAX (60s)<br>"
            resultado += "   - Tríceps francês 4x10-12 (45s)<br>"
            resultado += "   - Corda 4x15-20 (30s)<br>"

            resultado +="Dia B - Costas/Bíceps:<br>"
            resultado += "   - Barra fixa peso 5x6-8 (120s)<br>"
            resultado += "   - Remada curvada 4x8-10 (90s)<br>"
            resultado += "   - Pulley frente 4x10-12 (60s)<br>"
            resultado += "   - Rosca direta 4x8-10 (60s)<br>"
            resultado += "   - Rosca concentrada 4x12-15 (45s)<br>"

            resultado +="Dia C - Pernas:<br>"
            resultado += "   - Agachamento livre 5x5 (180s)<br>"
            resultado += "   - Leg press 5x8-10 (120s)<br>"
            resultado += "   - Stiff 4x8-10 (90s)<br>"
            resultado += "   - Cadeira extensora 4x12-15 (60s)<br>"
            resultado += "   - Panturrilha 5x20-25 (30s)<br>"

            resultado +="Dia D - Ombros/Trapézio:"
            resultado += "   - Desenvolvimento militar 5x6-8 (120s)<br>"
            resultado += "   - Elevação lateral 5x12-15 (60s)<br>"
            resultado += "   - Crucifixo inverso 4x15-20 (45s)<br>"
            resultado += "   - Encolhimento barra 4x12-15 (45s)<br>"

            resultado +="Dia E - Braços/Abdômen:<br>"
            resultado += "   - Rosca scott 5x8-10 (60s)<br>"
            resultado += "   - Tríceps testa 5x8-10 (60s)<br>"
            resultado += "   - Rosca martelo 4x12-15 (45s)<br>"
            resultado += "   - Tríceps corda 4x15-20 (45s)<br>"
            resultado += "   - Abdominal supra 5x20 (30s)<br>"
            resultado += "   - Prancha lateral 4x30s (30s)<br>"

            
    elif objetivo == 3:
        resultado +=f"Seu objetivo é definição muscular. Seu estado físico atual é: {estado_fisico}.<br><br>"

        if pontuacao <= 10:
            resultado +="=== PLANO LEVE (INICIANTE) ===<br>"
            resultado += "Frequência: 3x por semana (2 força + 1 cardio)<br>"
            resultado +="ROTINA DE TREINO:<br>"
            resultado += "Dia 1 - Full Body:<br>"
            resultado += "   - Agachamento goblet 4x12-15 (60s)<br>"
            resultado += "   - Flexão de braços 4xMAX (60s)<br>"
            resultado += "   - Remada máquina 4x12-15 (60s)<br>"
            resultado += "   - Abdominal supra 4x15 (30s)<br>"

            resultado +="Dia 2 - Cardio (30 min):<br>"
            resultado += "   - Esteira (alternar 2 min caminhada / 1 min trote)<br>"
            resultado += "   OU bicicleta (resistência moderada)<br>"

            resultado +="Dia 3 - Full Body:<br>"
            resultado += "   - Afundo estático 4x10 perna (60s)<br>"
            resultado += "   - Puxada frontal 4x12-15 (60s)<br>"
            resultado += "   - Elevação lateral 4x15 (45s)<br>"
            resultado += "   - Prancha 4x30s (30s)"

        elif 11 <= pontuacao <= 14:
            resultado +="=== PLANO MÉDIO (INTERMEDIÁRIO) ===<br>"
            resultado += "Frequência: 4-5x por semana (3 força + 2 HIIT)<br>"
            resultado +="ROTINA DE TREINO:<br>"
            resultado += "Dia A - Superiores:<br>"
            resultado += "   - Supino reto 4x10-12 (60s)<br>"
            resultado += "   - Barra fixa 4xMAX (60s)<br>"
            resultado += "   - Desenvolvimento halteres 4x12-15 (45s)<br>"
            resultado += "   - Rosca direta 4x12-15 (45s)<br>"
            resultado += "   - Tríceps corda 4x15-20 (45s)<br>"

            resultado +="Dia B - Inferiores:<br>"
            resultado += "   - Agachamento sumô 4x12-15 (60s)<br>"
            resultado += "   - Leg press 45° 4x15-20 (60s)<br>"
            resultado += "   - Stiff 4x12-15 (60s)<br>"
            resultado += "   - Panturrilha 4x20-25 (30s)<br>"

            resultado +="Dia C - HIIT (20 min):<br>"
            resultado += "   - 8 rounds de 30s trabalho / 30s descanso<br>"
            resultado += "   - Burpees / Escalador / Salto corda / Polichinelo<br>"

            resultado +="Dia D - Full Body (Circuito):<br>"
            resultado += "   - 3 voltas sem descanso entre exercícios:<br>"
            resultado += "   • Kettlebell swing x15<br>"
            resultado += "   • Flexão diamante x12<br>"
            resultado += "   • Agachamento salto x15<br>"
            resultado += "   • Prancha com rotação x10 lado<br>"
            resultado += "   • Mountain climber x20<br>"
            resultado += "   (Descanso 60s entre voltas)<br>"

            resultado +="Dia E - Cardio em Jejum (opcional):<br>"
            resultado += "   - 30 min caminhada em rampa<br>"


        else:
            resultado +="=== PLANO AVANÇADO ===<br>"
            resultado += "Frequência: 5-6x por semana (4 força + 2 HIIT)<br>"
            resultado +="ROTINA DE TREINO:<br>"
            resultado += "Dia A - Peito/Tríceps (Volume):<br>"
            resultado += "   - Supino inclinado 5x10-12 (60s)<br>"
            resultado += "   - Supino declinado 4x12-15 (60s)<br>"
            resultado += "   - Peck deck 4x15-20 (45s)<br>"
            resultado += "   - Tríceps testa 4x12-15 (45s)<br>"
            resultado += "   - Corda 4x20-25 (30s)<br>"

            resultado +="Dia B - Costas/Bíceps (Densidade):<br>"
            resultado += "   - Barra fixa 5xMAX (60s)<br>"
            resultado += "   - Remada curvada 4x12-15 (60s)<br>"
            resultado += "   - Face pull 4x15-20 (45s)<br>"
            resultado += "   - Rosca martelo 4x15-20 (45s)<br>"
            resultado += "   - Rosca concentrada 4x12-15 (30s)<br>"

            resultado +="Dia C - HIIT Metabólico (25 min):<br>"
            resultado += "   - 10 rounds de 40s trabalho / 20s descanso<br>"
            resultado += "   - Kettlebell swing / Box jump / Burpees / Corda naval<br>"

            resultado +="Dia D - Pernas (Intensidade):<br>"
            resultado += "   - Agachamento frontal 5x8-10 (90s)<br>"
            resultado += "   - Leg press 5x15-20 (60s)<br>"
            resultado += "   - Stiff 4x12-15 (60s)<br>"
            resultado += "   - Cadeira extensora 4x20-25 (45s)<br>"
            resultado += "   - Panturrilha 5x25-30 (30s)<br>"

            resultado +="Dia E - Ombros/Abdômen (Super Set):<br>"
            resultado += "   - Desenvolvimento Arnold 4x12-15 (60s)<br>"
            resultado += "   - Elevação lateral 4x15-20 (45s)<br>"
            resultado += "   - Crucifixo inverso 4x20 (45s)<br>"
            resultado += "   - Abdominal infra + supra (4x20+20)<br>"
            resultado += "   - Prancha lateral 4x30s lado<br>"

            resultado +="Dia F - HIIT Cardio (30 min):<br>"
            resultado += "   - Esteira (1 min sresultado += / 1 min caminhada)<br>"
            resultado += "   OU natação (tiros de 50m)<br>"

    else:
        print("erro")


    resultado += "<br>Lembre-se: o mais importante é a consistência. Busque ajuda profissional se possível."



    return resultado





