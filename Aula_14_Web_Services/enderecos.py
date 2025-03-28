import sqlite3


class Endereco(object):

    def __init__(self):
        self.cep = None
        self.logradouro = None
        self.complemento = None
        self.bairro = None
        self.localidade = None
        self.uf = None
        self.unidade = None
        self.ibge = None
        self.gia = None

        def cria_tabela(self):
            conn = sqlite3.connect("enderecos.db")
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS endereco (
                    cep TEXT PRIMARY KEY,
                    logradouro TEXT,
                    complemento TEXT,
                    bairro TEXT,
                    localidade TEXT,
                    uf TEXT,
                    unidade TEXT,
                    ibge TEXT,
                    gia TEXT
                )
            """)

            conn.commit()
            conn.close()

        def salvar(self):
            self.cria_tabela()

            conn = sqlite3.connect("enderecos.db")
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO endereco VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (self.cep, self.logradouro, self.complemento, self.bairro,
                  self.localidade, self.uf, self.unidade, self.ibge, self.gia)
                           )

            conn.commit()

            print(f"Cep {self.cep} encontrado e salvo sucesso!")
