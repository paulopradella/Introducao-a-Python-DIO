#Aprenda a utilizar informações de data,
# horário e relacionar datas diferentes
#Data
from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    #importar a data atual
    data_atual = date.today()
    print(data_atual)

    #formatar a data, verificar na documentação do Python
    # as demais opções que tem de formatacãa.
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%y'))#resultado: 13/05/21
    print(data_atual.strftime('%d/%m/%Y'))#resultado: 13/05/2021
    print(data_atual.strftime('%A %B %Y'))#resultado: Thursday May 2021

    #outra opção
    data_atual = date.today()
    data_atual_str =data_atual.strftime('%A %B %Y')
    print(data_atual_str)#resultado: Thursday May 2021 (string)

def trabalhando_com_time():
    #criar com um horário pré determinado
    horario = time(hour=15, minute=18, second=30)
    print(horario)#resultado: 15:15:30
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)#resultado: 15:15:30 (string)

def trabalhando_com_datetime():
    #Data e hora atual
    data_atual2 = datetime.now()
    print(data_atual2)#resultado: 2021-05-13 11:24:20.864253
    data_atual2_str = data_atual2.strftime('%d/%m/%Y')
    print(data_atual2_str)#resultado:13/05/2021
    data_atual2_str2 = data_atual2.strftime('%H:%M:%S')
    print(data_atual2_str2)  # resultado:11:27:18
    data_atual2_str3 = data_atual2.strftime('%d/%m/%Y %H:%M:%S')
    print(data_atual2_str3)  # resultado:13/05/2021 11:27:58
    data_atual2_str4 = data_atual2.strftime('%c')
    print(data_atual2_str4)  # resultado:Thu May 13 11:29:08 2021
    data_atual2_str5 = data_atual2.day
    print(data_atual2_str5)  # resultado: 13 (dia atual)
    data_atual2_str6 = data_atual2.year
    print(data_atual2_str6)  # resultado:2021 (ano atual)
    data_atual2_str7 = data_atual2.hour
    print(data_atual2_str7)  # resultado:11 (hora tual
    data_atual2_str8 = data_atual2.minute
    print(data_atual2_str8)  # resultado:33 (minuto atual)
    data_atual2_str9 = data_atual2.second
    print(data_atual2_str9)  # resultado:13 (segundo atual)
    data_atual2_str10 = data_atual2.weekday()
    print(data_atual2_str10)  # resultado: 3 referente a quarta
    data_atual2_str11 = data_atual2.month
    print(data_atual2_str11)  # resultado: 5 refernte a maio
    data_atual2_str12 = data_atual2.weekday()
    tupla = ('Segunda','Terça','Quarta','Quinta','Sexta',
             'Sábado','Domingo')#forma para trazer traduzido
    print(tupla[data_atual2.weekday()])# resultado: Quinta
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)# 2018-06-20 15:30:20
    data_criada_str = data_criada.strftime('%c')
    print(data_criada_str)# resultado: Wed Jun 20 15:30:20 2018
    #converter string para datetime
    data_string = '01/01/2019'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida) # resultado: 2019-01-01 00:00:00 (pelos zeros da pra saber que converteu com sucesso)

    #Soma e subtração de datas
    nova_data = data_convertida - timedelta(days=365)#não tira year, preisa usar o days
    print(nova_data)# resultado:2018-01-01 00:00:00
    nova_data2 = data_convertida - timedelta(hours=2)
    print(nova_data2)  # resultado:2018-12-31 22:00:00
    nova_data3 = data_convertida - timedelta(minutes=15)
    print(nova_data3)  # resultado:2018-12-31 23:45:00

if __name__ == '__main__':
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()
