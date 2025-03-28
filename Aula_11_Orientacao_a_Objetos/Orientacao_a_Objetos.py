class Pessoa(object):
    nome = None

    def salvar(self, nome):
        self.nome = nome
        print('Salvando', self.nome)


class Carro(object):

    def __init__(self, caminho):
        self.caminho = caminho

    def andar(self):
        print('Andando pela', self.caminho)


class Fusca(Carro):

    def __init__(self, caminho):
        self.caminho = caminho

    def cvorrer(self):
        self.caminho = 'pista'
        super(Fusca, self).andar()


class Ferrari(Carro):

    def __init__(self, caminho):
        self.caminho = caminho

    def andar(self):
        print("Correndo muito")


p = Pessoa()

print(type(p))

p.nome = 'João'
p.salvar("Felicty")

print(p.nome)

c = Carro()
c.andar()
print(c.caminho)

c.caminho = 'Estrada'
print(c.caminho)
