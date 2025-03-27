import random
import string


print(dir(random))

print(random.random())
print(random.random())
print(random.random())
print(random.random())

print(random.randint(10, 20))
print(random.randint(10, 20))
print(random.randint(10, 20))
print(random.randint(10, 20))

print(help(random.choice))

x = ['gol', 'astra', 'fusca', 'palio', 'uno']

print(random.choice(x))
print(random.choice(x))
print(random.choice(x))
print(random.choice(x))

print(x)

print(random.shuffle(x))

print(string.punctuation)
print(string.digits)
print(string.hexdigits)
print(string.capwords('teste de capitalize no curso de python'))
