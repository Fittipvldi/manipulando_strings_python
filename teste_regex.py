import re

celular1 = '98289-0192'
celular2 = '90203-2034'
celular3 = '90928-0293'
celulares = '90928-0293 90928-0293 90928-0293'

padrao = '[9][0-9]{4}[-][0-9]{4}'

retorno = re.search(padrao, celular1)
print(retorno.group())

retorno = re.search(padrao, celular2)
print(retorno.group())

retorno = re.search(padrao, celular3)
print(retorno.group())

retorno = re.findall(padrao, celulares)  # acha mais de um padrão e retorna em uma lista
print(retorno)
