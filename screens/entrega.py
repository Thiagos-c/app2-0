import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime


class NovaEntrega(ctk.CTkFrame):

    def __init__(self, master, db):

        super().__init__(master)

        self.db = db
        self.inputs = []

        titulo = ctk.CTkLabel(
            self,
            text="Nova Entrega de Insumos",
            font=("Segoe UI", 28, "bold")
        )

        titulo.pack(pady=15)

        topo = ctk.CTkFrame(self)
        topo.pack(fill="x", padx=20)

        ctk.CTkLabel(topo, text="Setor").grid(row=0, column=0, padx=10, pady=10)

        setores = [s["nome"] for s in self.db.listar_setores()]

        self.setor = ctk.CTkComboBox(
            topo,
            values=setores,
            width=220
        )

        self.setor.grid(row=0, column=1)

        ctk.CTkLabel(topo, text="Responsável").grid(row=0, column=2)

        self.responsavel = ctk.CTkEntry(
            topo,
            width=250
        )

        self.responsavel.grid(row=0, column=3, padx=10)

        tabela = ctk.CTkScrollableFrame(
            self,
            height=450
        )

        tabela.pack(fill="both", expand=True, padx=20, pady=20)

        cab = ctk.CTkFrame(tabela)

        cab.pack(fill="x")

        ctk.CTkLabel(cab, text="Insumo", width=280).grid(row=0, column=0)
        ctk.CTkLabel(cab, text="Estoque", width=80).grid(row=0, column=1)
        ctk.CTkLabel(cab, text="Quantidade", width=120).grid(row=0, column=2)

        for item in self.db.listar_estoque():

            linha = ctk.CTkFrame(tabela)
            linha.pack(fill="x", pady=2)

            ctk.CTkLabel(
                linha,
                text=item["nome"],
                width=280,
                anchor="w"
            ).grid(row=0, column=0)

            cor = "green"

            if item["quantidade"] < 10:
                cor = "red"

            elif item["quantidade"] < 30:
                cor = "orange"

            ctk.CTkLabel(
                linha,
                text=str(item["quantidade"]),
                width=80,
                text_color=cor
            ).grid(row=0, column=1)

            entrada = ctk.CTkEntry(
                linha,
                width=100,
                placeholder_text="0"
            )

            entrada.grid(row=0, column=2)

            self.inputs.append((item, entrada))

        ctk.CTkButton(
            self,
            text="Salvar Entrega",
            height=45,
            command=self.salvar
        ).pack(pady=15)

    def salvar(self):

        if self.setor.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Selecione um setor."
            )
            return

        if self.responsavel.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Informe o responsável."
            )
            return

        itens = []

        for item, campo in self.inputs:

            valor = campo.get().strip()

            if valor == "":
                continue

            qtd = int(valor)

            if qtd <= 0:
                continue

            if qtd > item["quantidade"]:

                messagebox.showerror(
                    "Erro",
                    f"Estoque insuficiente para {item['nome']}"
                )

                return

            itens.append({

                "id": item["id"],

                "nome": item["nome"],

                "unidade": item["unidade"],

                "quantidade": qtd

            })

        if len(itens) == 0:

            messagebox.showwarning(
                "Aviso",
                "Nenhum item informado."
            )

            return

        data = datetime.now().strftime("%d/%m/%Y %H:%M")

        self.db.salvar_entrega(

            data,

            self.setor.get(),

            self.responsavel.get(),

            itens

        )

        for item in itens:

            saldo = next(

                x["quantidade"]

                for x in self.db.listar_estoque()

                if x["id"] == item["id"]

            )

            self.db.atualizar_estoque(

                item["id"],

                saldo - item["quantidade"]

            )

        messagebox.showinfo(

            "Sucesso",

            "Entrega registrada."

        )

        self.master.master.show_dashboard()
