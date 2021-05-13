#Aprenda a utilizar informações de data,
# horário e relacionar datas diferentes
#Data
from datetime import date

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
print(data_atual_str)#resultado: Thursday May 2021
print(type(data_atual_str))#resultado: <class 'str'>
