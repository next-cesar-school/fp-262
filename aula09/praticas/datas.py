from datetime import datetime, timedelta


agora = datetime.now()
print(agora)  # Data e hora atual

amanha = agora + timedelta(days=1)
print(amanha)  # Data e hora de amanhã

data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print(data_formatada)  # Exibe data formatada
