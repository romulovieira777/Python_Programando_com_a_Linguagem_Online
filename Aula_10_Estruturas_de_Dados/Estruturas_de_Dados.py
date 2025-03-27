lista = [1, 2, 3, 4, 5]
print(lista)
print(lista[1])

for x in lista:
    print(x)

lista1 = [1, 'Felicty', 3.14, 'Arrow', True]

for item in lista1:
    print(item)

print(lista1[2])

lista1.append('Novo valor')
print(lista1)

lista1[2] = 'PI'
print(lista1)

lista1.pop()
print(lista1)

lista1.remove('Arrow')
print(lista1)

lista1.insert(2, 'Insert')
print(lista1)

lista1.insert(0, 'Inicio')
print(lista1)

lista1.reverse()
print(lista1)

lista2 = ['Felicty', 'Arrow']
lista2.sort()
print(lista2)

lista2.sort(reverse=True)
print(lista2)

tuplas = (3, 4, 'Nome')
print(tuplas)

tupla2 = 3, 5, 'Nome', 'Sobrenome'
print(tupla2)

s = set()
print(s)

s.add(1)
print(s)

s.add(12)
print(s)

s.add(13)
s.add(14)
print(s)

s.pop()
print(s)

s.remove(13)
print(s)

d = {}
print(d)
print(type(d))

d['nome'] = "Felicty"
d['sobrenome'] = 'Smoke'
print(d)

d['data_nascimento'] = '18/05/1979'
d['telefone'] = '1199998533'
print(d)

d.pop('telefone')
print(d)

print(d.popitem())
print(d.values())
print(d.keys())
