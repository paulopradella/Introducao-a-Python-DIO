from datetime import datetime
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
