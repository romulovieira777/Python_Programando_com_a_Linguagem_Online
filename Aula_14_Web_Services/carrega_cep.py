import requests
import json
from enderecos import Endereco

r = requests.get("http://www.impacta.com.br")
print(r)
print(r.sttus_code)
print(r.headers)
print(r.headers.get("Server"))
print(r.text)


cep = input("Digite o CEP: ")
url = f"https://viacep.com.br/ws/{cep}/json/"
r = requests.get(url)

if r.status_code == requests.codes.ok:
    j = json.loads(r.text)

    endereco = Endereco()
    endereco.cep = j['cep']
    endereco.logradouro = j['logradouro']
    endereco.complemento = j['complemento']
    endereco.bairro = j['bairro']
    endereco.localidade = j['localidade']
    endereco.uf = j['uf']
    endereco.unidade = j['unidade']
    endereco.ibge = j['ibge']
    endereco.gia = j['gia']

    endereco.salvar()
else:
    print("CEP não encontrado")
    print(r.status_code)
    print(r.text)
    exit(1)
