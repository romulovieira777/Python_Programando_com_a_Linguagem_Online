import sqlite3

conn = sqlite3.connect('galeria.db')
cursor = conn.cursor()


# Criação da tabela
def criar_tabela():
    sql = """
    CREATE TABLE IF NOT EXISTS albums (
    titulo text, artista text, data_lancamento text, data_publicacao text, midia text
    )
    """

    cursor.execute(sql)
    conn.commit()


# Inserção de dados
def grava_album(titulo, artista, data_lancamento, data_publicacao, midia):
    sql = """
    INSERT INTO albums VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(sql, (titulo, artista, data_lancamento, data_publicacao, midia))
    conn.commit()


def grava_muitos():
    sql = """
    INSERT INTO albums VALUES (?, ?, ?, ?, ?)
    """
    dados = [
        ('Céu', 'Aline barros', '2024/07/2012', '2023-10-21', 'CD'),
        ('A Sky Full of Stars', 'Coldplay', '2024/07/2012', '2023-10-21', 'MP3'),
        ('The Sound of Silence', 'Simon & Garfunkel', '2024/07/2012', '2023-10-21', 'CD')
    ]
    cursor.executemany(sql, dados)
    conn.commit()


def atualiza():
    sql = """
    UPDATE albums SET data_publicacao = ? WHERE titulo = ?
    """
    cursor.execute(sql, ('2023/10/21', 'Glow'))
    conn.commit()


def excluir():
    sql = """
    DELETE FROM albums WHERE titulo = ?
    """
    cursor.execute(sql, ('Glow',))
    conn.commit()


def listar():
    sql = """
    SELECT * FROM albums ORDER BY artista
    """
    cursor.execute(sql)
    for linha in cursor.fetchall():
        print(linha)


criar_tabela()
grava_album('Glow', 'Andy Hunter', '2024/07/2012', '2023-10-21', 'MP3')
grava_muitos()
atualiza()
excluir()
listar()
