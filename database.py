import sqlite3
from pathlib import Path


class Database:

    def __init__(self):

        Path("database").mkdir(exist_ok=True)

        self.conn = sqlite3.connect("database/sesmt.db")

        self.conn.row_factory = sqlite3.Row

        self.cursor = self.conn.cursor()

        self.create_tables()

        self.insert_default_items()


    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS estoque(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            nome TEXT UNIQUE,

            unidade TEXT,

            quantidade INTEGER

        )

        """)


        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS setores(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            nome TEXT UNIQUE

        )

        """)


        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS entregas(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            data TEXT,

            setor TEXT,

            responsavel TEXT

        )

        """)


        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS itens_entrega(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            entrega_id INTEGER,

            insumo TEXT,

            unidade TEXT,

            quantidade INTEGER

        )

        """)

        self.conn.commit()


    def insert_default_items(self):

        itens = [

            ("Compressa Estéril","Unidade",100),

            ("Curativo Adesivo","Caixa",40),

            ("Luva de Látex","Caixa",60),

            ("Esparadrapo","Rolo",30),

            ("Atadura","Unidade",80),

            ("Água Boricada","Frasco",25),

            ("Spray Antisséptico","Frasco",18),

            ("Algodão","Pacote",50),

            ("Tesoura para Vestes","Unidade",15),

            ("Manta Térmica","Unidade",20),

            ("Luva Cirúrgica","Par",90),

            ("Máscara RCP","Unidade",12),

            ("Ressuscitador Cardiopulmonar","Unidade",6)

        ]

        for item in itens:

            self.cursor.execute("""

            INSERT OR IGNORE INTO estoque

            (nome,unidade,quantidade)

            VALUES(?,?,?)

            """, item)


        setores = [

            ("Portaria",),

            ("Recepção",),

            ("Produção",),

            ("Almoxarifado",),

            ("Administrativo",)

        ]

        for setor in setores:

            self.cursor.execute("""

            INSERT OR IGNORE INTO setores(nome)

            VALUES(?)

            """, setor)

        self.conn.commit()


    def listar_estoque(self):

        self.cursor.execute("""

        SELECT *

        FROM estoque

        ORDER BY nome

        """)

        return self.cursor.fetchall()


    def atualizar_estoque(self,id_item,nova_qtd):

        self.cursor.execute("""

        UPDATE estoque

        SET quantidade=?

        WHERE id=?

        """,(nova_qtd,id_item))

        self.conn.commit()


    def listar_setores(self):

        self.cursor.execute("""

        SELECT *

        FROM setores

        ORDER BY nome

        """)

        return self.cursor.fetchall()


    def salvar_entrega(self,data,setor,responsavel,itens):

        self.cursor.execute("""

        INSERT INTO entregas

        (data,setor,responsavel)

        VALUES(?,?,?)

        """,(data,setor,responsavel))

        entrega_id=self.cursor.lastrowid

        for item in itens:

            self.cursor.execute("""

            INSERT INTO itens_entrega

            (entrega_id,insumo,unidade,quantidade)

            VALUES(?,?,?,?)

            """,(

                entrega_id,

                item["nome"],

                item["unidade"],

                item["quantidade"]

            ))

        self.conn.commit()
