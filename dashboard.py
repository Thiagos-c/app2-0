import customtkinter as ctk


class Dashboard(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        titulo = ctk.CTkLabel(

            self,

            text="Dashboard",

            font=("Segoe UI",30,"bold")

        )

        titulo.pack(pady=20)


        cards = ctk.CTkFrame(self)

        cards.pack(fill="x", padx=20)


        dados = [

            ("📦 Estoque", "245"),

            ("📋 Entregas Hoje", "12"),

            ("⚠ Estoque Baixo", "4"),

            ("👷 Setores", "18")

        ]


        for texto, valor in dados:

            card = ctk.CTkFrame(cards, width=220, height=120)

            card.pack(side="left", padx=15, pady=20)

            card.pack_propagate(False)

            ctk.CTkLabel(

                card,

                text=texto,

                font=("Segoe UI",18)

            ).pack(pady=(20,5))

            ctk.CTkLabel(

                card,

                text=valor,

                font=("Segoe UI",34,"bold")

            ).pack()
