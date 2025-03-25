def somar(numero1, numero2):
    print(numero1 + numero2)


def subtrair(numero1, numero2):
    print(numero1 - numero2)


def imprime_parametros(**kwargs):
    for key, value in kwargs.items():
        print("%s = %s" % (key, value))


somar(12, 30)
subtrair(10, 5)

imprime_parametros(nome="Ana", sobrenome="Maria")
imprime_parametros(nome="Felicity", sobrenome="Smoke", idade=37, apelido="FS", dataNasciemnto="10/08/1988")
