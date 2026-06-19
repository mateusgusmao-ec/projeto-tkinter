import tkinter as tk
from tkinter import colorchooser

class AplicativoDesenho:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Desenho Livre e Formas com Rolagem")
        self.janela.geometry('800x600')
        
        # Configuração do Grid da janela principal
        self.janela.grid_columnconfigure(0, weight=1)
        self.janela.grid_rowconfigure(0, weight=1)
        
        # Atributos de estado (antigas variáveis globais)
        self.forma_atual = "pincel"
        self.cor_preenchimento = "black"
        self.cor_borda = "black"
        self.tamanho_pincel = 2
        
        self.inicio_x = 0
        self.inicio_y = 0
        self.objeto_atual = None
        self.ultimo_x_pincel = None
        self.ultimo_y_pincel = None
        
        # Inicialização dos componentes da interface
        self.criar_widgets()
        self.configurar_eventos()
       
        
        # Estado inicial da paleta
        self.definir_cor_preenchimento('black')
        self.tela.itemconfigure('paleta', width=1)

    def criar_widgets(self):
        # Barras de rolagem
        self.barra_rolagem_vert = tk.Scrollbar(self.janela, orient=tk.VERTICAL)
        self.barra_rolagem_horiz = tk.Scrollbar(self.janela, orient=tk.HORIZONTAL)
        
        # Canvas (Tela)
        self.tela = tk.Canvas(
            self.janela, 
            scrollregion=(0, 0, 1000, 1000),
            yscrollcommand=self.barra_rolagem_vert.set, 
            xscrollcommand=self.barra_rolagem_horiz.set, 
            bg="white"
        )
        
        self.barra_rolagem_horiz['command'] = self.tela.xview
        self.barra_rolagem_vert['command'] = self.tela.yview
        
        # Posicionamento no Grid
        self.tela.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.barra_rolagem_horiz.grid(column=0, row=1, sticky=(tk.W, tk.E))
        self.barra_rolagem_vert.grid(column=1, row=0, sticky=(tk.N, tk.S))
        
        # Quadro de controles (Botões inferiores)
        self.quadro_controles = tk.Frame(self.janela)
        self.quadro_controles.grid(column=0, row=2, sticky=(tk.W, tk.E), pady=5)
        
        # Botões de formas
        tk.Button(self.quadro_controles, text="Pincel Livre", command=lambda: self.definir_forma("pincel")).pack(side=tk.LEFT, padx=2)
        tk.Button(self.quadro_controles, text="Linha", command=lambda: self.definir_forma("linha")).pack(side=tk.LEFT, padx=2)
        tk.Button(self.quadro_controles, text="Retângulo", command=lambda: self.definir_forma("retangulo")).pack(side=tk.LEFT, padx=2)
        tk.Button(self.quadro_controles, text="Oval", command=lambda: self.definir_forma("oval")).pack(side=tk.LEFT, padx=2)
        tk.Button(self.quadro_controles, text="Círculo", command=lambda: self.definir_forma("circulo")).pack(side=tk.LEFT, padx=2)
        
        # Controle de tamanho
        tk.Label(self.quadro_controles, text="Tamanho:").pack(side=tk.LEFT, padx=(10, 2))
        self.escala_tamanho = tk.Scale(self.quadro_controles, from_=1, to=20, orient=tk.HORIZONTAL, command=self.definir_tamanho_pincel)
        self.escala_tamanho.set(2)
        self.escala_tamanho.pack(side=tk.LEFT, padx=2)
        
        # Botões de cores
        tk.Button(self.quadro_controles, text="Cor Borda/Pincel", command=self.escolher_cor_borda).pack(side=tk.LEFT, padx=10)
        tk.Button(self.quadro_controles, text="Cor Preenchimento", command=self.escolher_cor_preenchimento_geral).pack(side=tk.LEFT, padx=2)

    def configurar_eventos(self):
        self.tela.bind("<Button-1>", self.capturar_posicao)
        self.tela.bind("<B1-Motion>", self.desenhar)
        self.tela.bind("<ButtonRelease-1>", self.finalizar_desenho)

    def capturar_posicao(self, evento):
        self.inicio_x, self.inicio_y = self.tela.canvasx(evento.x), self.tela.canvasy(evento.y)
        
        if self.forma_atual == "pincel":
            self.ultimo_x_pincel, self.ultimo_y_pincel = self.inicio_x, self.inicio_y
        else:
            self.ultimo_x_pincel, self.ultimo_y_pincel = None, None

    def desenhar(self, evento):
        x, y = self.tela.canvasx(evento.x), self.tela.canvasy(evento.y)
        
        if self.forma_atual == "pincel":
            if self.ultimo_x_pincel is not None and self.ultimo_y_pincel is not None:
                self.tela.create_line(
                    self.ultimo_x_pincel, self.ultimo_y_pincel, x, y, 
                    fill=self.cor_borda, width=self.tamanho_pincel, capstyle=tk.ROUND, smooth=True
                )
            self.ultimo_x_pincel, self.ultimo_y_pincel = x, y
            
        else:
            if self.objeto_atual:
                self.tela.coords(self.objeto_atual, self.inicio_x, self.inicio_y, x, y)
            else:
                if self.forma_atual == "linha":
                    self.objeto_atual = self.tela.create_line(self.inicio_x, self.inicio_y, x, y, fill=self.cor_borda, width=self.tamanho_pincel)
                elif self.forma_atual == "retangulo":
                    self.objeto_atual = self.tela.create_rectangle(self.inicio_x, self.inicio_y, x, y, outline=self.cor_borda, fill=self.cor_preenchimento, width=2)
                elif self.forma_atual == "oval":
                    self.objeto_atual = self.tela.create_oval(self.inicio_x, self.inicio_y, x, y, outline=self.cor_borda, fill=self.cor_preenchimento, width=2)
                elif self.forma_atual == "circulo":
                    self.objeto_atual = self.tela.create_oval(self.inicio_x, self.inicio_y, x, y, outline=self.cor_borda, fill=self.cor_preenchimento, width=2)

    def finalizar_desenho(self, evento):
        self.objeto_atual = None
        self.ultimo_x_pincel, self.ultimo_y_pincel = None, None

    def definir_forma(self, nova_forma):
        self.forma_atual = nova_forma

    def definir_tamanho_pincel(self, valor):
        self.tamanho_pincel = int(valor)

    def definir_cor_preenchimento(self, nova_cor):
        self.cor_preenchimento = nova_cor
        self.tela.itemconfigure('paleta', outline='white')
        tag_selecionada = f'paleta{nova_cor}'
        if self.tela.find_withtag(tag_selecionada):
            self.tela.itemconfigure(tag_selecionada, outline='#999999', width=2)

    def escolher_cor_borda(self):
        codigo_cor = colorchooser.askcolor(title="Escolha a cor do pincel/borda")[1]
        if codigo_cor:
            self.cor_borda = codigo_cor

    def escolher_cor_preenchimento_geral(self):
        codigo_cor = colorchooser.askcolor(title="Escolha a cor de preenchimento")[1]
        if codigo_cor:
            self.definir_cor_preenchimento(codigo_cor)

if __name__ == "__main__":
    janela = tk.Tk()
    app = AplicativoDesenho(janela)
    janela.mainloop() 
