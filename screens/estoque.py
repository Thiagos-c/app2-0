import customtkinter as ctk


class Estoque(ctk.CTkFrame):

    def __init__(self, master, db):

        super().__init__(master)

        self.db=db

        titulo=ctk.CTkLabel(

            self,

            text="Controle de Estoque",

            font=("Segoe UI",28,"bold")

        )

        titulo.pack(pady=20)


        tabela=ctk.CTkScrollableFrame(

            self,

            width=900,

            height=500

        )

        tabela.pack(fill="both",expand=True,padx=20,pady=20)


        cabecalho=ctk.CTkFrame(tabela)

        cabecalho.pack(fill="x")

        ctk.CTkLabel(cabecalho,text="Insumo",width=300).grid(row=0,column=0)

        ctk.CTkLabel(cabecalho,text="Unidade",width=120).grid(row=0,column=1)

        ctk.CTkLabel(cabecalho,text="Quantidade",width=120).grid(row=0,column=2)


        for item in self.db.listar_estoque():

            linha=ctk.CTkFrame(tabela)

            linha.pack(fill="x",pady=2)

            ctk.CTkLabel(

                linha,

                text=item["nome"],

                width=300,

                anchor="w"

            ).grid(row=0,column=0,padx=5)

            ctk.CTkLabel(

                linha,

                text=item["unidade"],

                width=120

            ).grid(row=0,column=1)

            cor="green"

            if item["quantidade"]<10:

                cor="red"

            elif item["quantidade"]<30:

                cor="orange"

            ctk.CTkLabel(

                linha,

                text=str(item["quantidade"]),

                width=120,

                text_color=cor

            ).grid(row=0,column=2)
