import tkinter as tk

class SistemaPontuacao:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema de Pontuação de Taekwondo")

        # Configuração da geometria relativa para ocupar toda a tela
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        self.janela.geometry(f"{largura_tela}x{altura_tela}")

        # Dividindo a tela em duas partes: parte azul e parte vermelha
        self.frame_azul = tk.Frame(janela, bg="blue")
        self.frame_azul.grid(row=0, column=0, sticky="nsew")
        self.frame_vermelha = tk.Frame(janela, bg="red")
        self.frame_vermelha.grid(row=0, column=1, sticky="nsew")

        # Configuração do tamanho dos quadros
        self.frame_azul.config(width=largura_tela // 2)
        self.frame_vermelha.config(width=largura_tela // 2)

        # Ajustando as proporções das colunas e linhas
        self.janela.grid_columnconfigure(0, weight=1)
        self.janela.grid_columnconfigure(1, weight=1)
        self.janela.grid_rowconfigure(0, weight=5)
        self.janela.grid_rowconfigure(1, weight=1)

        # Rótulos para exibir pontuações e faltas
        self.pontuacao_azul = 0
        self.pontuacao_vermelha = 0
        self.faltas_azul = 0
        self.faltas_vermelha = 0

        self.lbl_pont_azul = tk.Label(self.frame_azul, text=self.pontuacao_azul, fg="white", bg="blue", font=("Arial", int(altura_tela / 4), "bold"))
        self.lbl_pont_azul.pack(expand=True, fill="both")
        self.lbl_faltas_azul = tk.Label(self.frame_azul, text=f"Faltas: {self.faltas_azul}", fg="white", bg="blue", font=("Arial", int(altura_tela / 18)))
        self.lbl_faltas_azul.pack(expand=True)

        self.lbl_pont_vermelha = tk.Label(self.frame_vermelha, text=self.pontuacao_vermelha, fg="white", bg="red", font=("Arial", int(altura_tela / 4), "bold"))
        self.lbl_pont_vermelha.pack(expand=True, fill="both")
        self.lbl_faltas_vermelha = tk.Label(self.frame_vermelha, text=f"Faltas: {self.faltas_vermelha}", fg="white", bg="red", font=("Arial", int(altura_tela / 18)))
        self.lbl_faltas_vermelha.pack(expand=True)

        # Botões de controle de pontuação e faltas
        self.btn_add_ponto_azul = tk.Button(self.frame_azul, text="+ Ponto", command=lambda: self.alterar_pontuacao("azul", 2), width=8, height=2)
        self.btn_add_ponto_azul.pack(side="left")
        self.btn_add_ponto_azul_1 = tk.Button(self.frame_azul, text="+1 SOCO", command=lambda: self.alterar_pontuacao("azul", 1), width=8, height=2)
        self.btn_add_ponto_azul_1.pack(side="left")
        self.btn_add_ponto_azul_3 = tk.Button(self.frame_azul, text="+3 PONTOS", command=lambda: self.alterar_pontuacao("azul", 3), width=8, height=2)
        self.btn_add_ponto_azul_3.pack(side="left")
        self.btn_add_ponto_azul_4 = tk.Button(self.frame_azul, text="+4 PONTOS", command=lambda: self.alterar_pontuacao("azul", 4), width=8, height=2)
        self.btn_add_ponto_azul_4.pack(side="left")
        self.btn_add_ponto_azul_5 = tk.Button(self.frame_azul, text="+5 PONTOS", command=lambda: self.alterar_pontuacao("azul", 5), width=8, height=2)
        self.btn_add_ponto_azul_5.pack(side="left")
        self.btn_dim_ponto_azul = tk.Button(self.frame_azul, text="- Ponto", command=lambda: self.alterar_pontuacao("azul", -1), width=8, height=2)
        self.btn_dim_ponto_azul.pack(side="left")
        self.btn_add_falta_azul = tk.Button(self.frame_azul, text="+ Falta", command=lambda: self.alterar_faltas("azul", 1), width=8, height=2)
        self.btn_add_falta_azul.pack(side="left")
        self.btn_dim_falta_azul = tk.Button(self.frame_azul, text="- Falta", command=lambda: self.alterar_faltas("azul", -1), width=8, height=2)
        self.btn_dim_falta_azul.pack(side="left")

        self.btn_add_ponto_vermelho = tk.Button(self.frame_vermelha, text="+ Ponto", command=lambda: self.alterar_pontuacao("vermelho", 2), width=8, height=2)
        self.btn_add_ponto_vermelho.pack(side="right")
        self.btn_add_ponto_vermelho_1 = tk.Button(self.frame_vermelha, text="+1 SOCO", command=lambda: self.alterar_pontuacao("vermelho", 1), width=8, height=2)
        self.btn_add_ponto_vermelho_1.pack(side="right")
        self.btn_add_ponto_vermelho_3 = tk.Button(self.frame_vermelha, text="+3 PONTOS", command=lambda: self.alterar_pontuacao("vermelho", 3), width=8, height=2)
        self.btn_add_ponto_vermelho_3.pack(side="right")
        self.btn_add_ponto_vermelho_4 = tk.Button(self.frame_vermelha, text="+4 PONTOS", command=lambda: self.alterar_pontuacao("vermelho", 4), width=8, height=2)
        self.btn_add_ponto_vermelho_4.pack(side="right")
        self.btn_add_ponto_vermelho_5 = tk.Button(self.frame_vermelha, text="+5 PONTOS", command=lambda: self.alterar_pontuacao("vermelho", 5), width=8, height=2)
        self.btn_add_ponto_vermelho_5.pack(side="right")
        self.btn_dim_ponto_vermelho = tk.Button(self.frame_vermelha, text="- Ponto", command=lambda: self.alterar_pontuacao("vermelho", -1), width=8, height=2)
        self.btn_dim_ponto_vermelho.pack(side="right")
        self.btn_add_falta_vermelho = tk.Button(self.frame_vermelha, text="+ Falta", command=lambda: self.alterar_faltas("vermelho", 1), width=8, height=2)
        self.btn_add_falta_vermelho.pack(side="right")
        self.btn_dim_falta_vermelho = tk.Button(self.frame_vermelha, text="- Falta", command=lambda: self.alterar_faltas("vermelho", -1), width=8, height=2)
        self.btn_dim_falta_vermelho.pack(side="right")

        # Campo de entrada e botões para controle de tempo
        self.frame_inferior = tk.Frame(self.janela)
        self.frame_inferior.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.frame_inferior.grid_columnconfigure(0, weight=1)
        self.frame_inferior.grid_columnconfigure(1, weight=1)
        self.frame_inferior.grid_columnconfigure(2, weight=1)
        self.frame_inferior.grid_columnconfigure(3, weight=1)
        self.frame_inferior.grid_columnconfigure(4, weight=1)
        self.frame_inferior.grid_columnconfigure(5, weight=1)
        self.frame_inferior.grid_columnconfigure(6, weight=1)

        self.lbl_tempo = tk.Label(self.frame_inferior, text="--:--", font=("Arial", 50))
        self.lbl_tempo.grid(row=0, column=3)

        self.btn_iniciar = tk.Button(self.frame_inferior, text="Iniciar", command=self.iniciar_contagem)
        self.btn_iniciar.grid(row=0, column=2)

        self.btn_parar = tk.Button(self.frame_inferior, text="Parar", command=self.parar_contagem)
        self.btn_parar.grid(row=0, column=4)

        self.btn_zerar = tk.Button(self.frame_inferior, text="Zerar Pontos", command=self.zerar_pontuacao_faltas, font=("Arial", 10))
        self.btn_zerar.grid(row=0, column=0)

        self.tempo_restante = 120  # Tempo em segundos(Altera o tempo)
        self.timer_id = None

        # Configuração para detectar teclas pressionadas
        self.janela.bind("<Key>", self.tecla_pressionada)
    def zerar_pontuacao_faltas(self):
        self.pontuacao_azul = 0
        self.pontuacao_vermelha = 0
        self.faltas_azul = 0
        self.faltas_vermelha = 0
        self.lbl_pont_azul.config(text=self.pontuacao_azul)
        self.lbl_pont_vermelha.config(text=self.pontuacao_vermelha)
        self.lbl_faltas_azul.config(text=f"Faltas: {self.faltas_azul}")
        self.lbl_faltas_vermelha.config(text=f"Faltas: {self.faltas_vermelha}")

    def iniciar_contagem(self):
        self.contar_tempo()

    def parar_contagem(self):
        if self.timer_id:
            self.janela.after_cancel(self.timer_id)
            self.timer_id = None

    def contar_tempo(self):
        if self.tempo_restante > 0:
            minutos = self.tempo_restante // 60
            segundos = self.tempo_restante % 60
            self.lbl_tempo.config(text=f"{minutos:02d}:{segundos:02d}")
            self.tempo_restante -= 1
            self.timer_id = self.janela.after(1000, self.contar_tempo)

    def alterar_pontuacao(self, cor, pontos):
        if cor == "azul":
            self.pontuacao_azul += pontos
            if self.pontuacao_azul < 0:
                self.pontuacao_azul = 0
            self.lbl_pont_azul.config(text=self.pontuacao_azul)
        elif cor == "vermelho":
            self.pontuacao_vermelha += pontos
            if self.pontuacao_vermelha < 0:
                self.pontuacao_vermelha = 0
            self.lbl_pont_vermelha.config(text=self.pontuacao_vermelha)

    def alterar_faltas(self, cor, faltas):
        if cor == "azul":
            self.faltas_azul += faltas
            if self.faltas_azul < 0:
                self.faltas_azul = 0
            self.lbl_faltas_azul.config(text=f"Faltas: {self.faltas_azul}")
            if faltas > 0:  # Fault added
                self.pontuacao_vermelha += 1
                self.lbl_pont_vermelha.config(text=self.pontuacao_vermelha)
            elif faltas < 0:  # Fault removed
                self.pontuacao_vermelha -= 1
                if self.pontuacao_vermelha < 0:  # Prevent score from going negative
                    self.pontuacao_vermelha = 0
                self.lbl_pont_vermelha.config(text=self.pontuacao_vermelha)
        elif cor == "vermelho":
            self.faltas_vermelha += faltas
            if self.faltas_vermelha < 0:
                self.faltas_vermelha = 0
            self.lbl_faltas_vermelha.config(text=f"Faltas: {self.faltas_vermelha}")
            if faltas > 0:  # Fault added
                self.pontuacao_azul += 1
                self.lbl_pont_azul.config(text=self.pontuacao_azul)
            elif faltas < 0:  # Fault removed
                self.pontuacao_azul -= 1
                if self.pontuacao_azul < 0:  # Prevent score from going negative
                    self.pontuacao_azul = 0
                self.lbl_pont_azul.config(text=self.pontuacao_azul)

    def tecla_pressionada(self, evento):
        tecla = evento.keysym.lower()
        if tecla == "a":
            self.tecla_cor = "azul"
        elif tecla == "v":
            self.tecla_cor = "vermelho"
        elif tecla.isdigit():
            pontos = int(tecla)
            if self.tecla_cor == "azul":
                self.alterar_pontuacao("azul", pontos)
            elif self.tecla_cor == "vermelho":
                self.alterar_pontuacao("vermelho", pontos)


# Inicializando o sistema
janela = tk.Tk()
sistema_pontuacao = SistemaPontuacao(janela)
janela.mainloop()
