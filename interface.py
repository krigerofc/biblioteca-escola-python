import customtkinter


class Tela:
    def __init__(self, titulo="EEPFV", dimensao="800x600"):
        self.tela = customtkinter.CTk(fg_color="grey11")
        self.tela.geometry(dimensao)
        self.tela.title(titulo)
        self.tela.iconbitmap("log2.ico")
        
    def tela2(self):
        f1 = customtkinter.CTkFrame(master=self.tela)
        f1.configure(fg_color="grey11")
        f1.pack(pady=0 ,padx=0 ,fill="both", expand=True)
        


    def login(self, log, sen):
        if log.get().strip() == "22" and sen.get().strip() == '22':
            self.tela2()
        else:
            customtkinter.CTkLabel(self.tela, text="Login Invalido", text_color="Red").place(x=360, y=270)

    def inicial(self):
        customtkinter.CTkLabel(self.tela, text="Login").place(x=380, y=180)
        log = customtkinter.CTkEntry(self.tela, placeholder_text="User")
        log.place(x=330, y=230)
        sen = customtkinter.CTkEntry(self.tela, placeholder_text="Senha", show="*")
        sen.place(x=330, y=310)
        customtkinter.CTkButton(self.tela, fg_color="purple", text='Logar', command=lambda: self.login(log, sen)).place(x=330, y=380)
        self.tela.mainloop()
    pass


jogo = Tela(titulo='Biblioteca José Venâncio', dimensao="800x600")
jogo.inicial()

