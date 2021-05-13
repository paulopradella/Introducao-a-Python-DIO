#Aprenda a utilizar informações de data,
# horário e relacionar datas diferentes
from datetime import time
#criar com um horário pré determinado
horario = time(hour=15, minute=18, second=30)
print(horario)#resultado: 15:15:30
horario_str = horario.strftime('%H:%M:%S')
print(horario_str)#resultado: 15:15:30 (string)
