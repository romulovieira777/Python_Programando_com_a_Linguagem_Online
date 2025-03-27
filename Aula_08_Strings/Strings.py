print("Marcos")
print('Antonio')

'''
Texto multilinha
para teste
na aula de python
'''

print("Texto para ser fatiado."[0:6])
print("Texto para ser fatiado."[0:10])
print("Texto para ser fatiado."[3:10])
print("Texto para ser fatiado."[:10])
print("Texto para ser fatiado."[0:])
print("Texto para ser fatiado."[0:10:3])

print("Fatiamento com o valor negativo."[3:-4])
print("Fatiamento com o valor negativo."[::-1])

nome = 'ana'
print(nome == nome[::-1])

nome = 'arara'
print(nome == nome[::-1])

nome = 'Marcos'
print(nome[0])

nome = 'B' + nome[1:]
print(nome)

print(nome.startswith('B'))
print(nome.startswith('b'))

print(nome.endswith('r'))

print(nome.replace('r', '3'))

nome = nome.replace('r', '3')
print(nome)

texto = "Testando split no pytohn"

s = texto.split()
print(s)

texto = "Testando;novos;delimitadores"
s = texto.split(';')
print(s)

data = ['18', '05', '1979']
print('/'.join(data))
