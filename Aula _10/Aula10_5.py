from datetime import timedelta, datetime
data_string = '01/01/2019'
data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
print(data_convertida) # resultado: 2019-01-01 00:00:00 (pelos zeros da pra saber que converteu com sucesso)

#Subtração e soma de datas,
#mesmo príncipio, bas alterar o sinal.
nova_data = data_convertida - timedelta(days=365)#não tira year, preisa usar o days
print(nova_data)# resultado:2018-01-01 00:00:00
nova_data2 = data_convertida - timedelta(hours=2)
print(nova_data2)  # resultado:2018-12-31 22:00:00
nova_data3 = data_convertida - timedelta(minutes=15)
print(nova_data3)  # resultado:2018-12-31 23:45:00

