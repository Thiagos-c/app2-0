import customtkinter as ctk

from screens.dashboard import Dashboard


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class SESMTManager(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("SESMT Manager")

        self.geometry("1400x850")

        self.minsize(1200, 700)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=220)

        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.content = ctk.CTkFrame(self)

        self.content.grid(row=0, column=1, sticky="nsew")

        self.create_sidebar()

        self.show_dashboard()


    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()


    def create_sidebar(self):

        titulo = ctk.CTkLabel(

            self.sidebar,

            text="SESMT\nManager",

            font=("Segoe UI",26,"bold")

        )

        titulo.pack(pady=30)

        botoes = [

            ("🏠 Dashboard", self.show_dashboard),

            ("📦 Estoque", self.not_ready),

            ("📝 Nova Entrega", self.not_ready),

            ("📜 Histórico", self.not_ready),

            ("📊 Relatórios", self.not_ready),

            ("⚙ Configurações", self.not_ready),

        ]

        for texto, comando in botoes:

            btn = ctk.CTkButton(

                self.sidebar,

                text=texto,

                command=comando,

                height=45

            )

            btn.pack(fill="x", padx=15, pady=8)


    def show_dashboard(self):

        self.clear_content()

        Dashboard(self.content).pack(fill="both", expand=True)


    def not_ready(self):

        self.clear_content()

        frame = ctk.CTkFrame(self.content)

        frame.pack(expand=True)

        ctk.CTkLabel(

            frame,

            text="🚧 Em desenvolvimento",

            font=("Segoe UI",28,"bold")

        ).pack(pady=40)


if __name__ == "__main__":

    app = SESMTManager()

    app.mainloop()
