import tkinter as tk
from tkinter import colorchooser
from abc import ABC, abstractmethod
import math
from tkinter import messagebox


# ---> função que calcula a distância
def distancia(x1, y1, x2, y2, px, py):

    dx = x2 - x1
    dy = y2 - y1

    ab_len_sq = dx**2 + dy**2

    if ab_len_sq == 0:
        return math.sqrt((px - x1)**2 + (py - y1)**2)

    ap_x = px - x1
    ap_y = py - y1

    t = (ap_x * dx + ap_y * dy) / ab_len_sq

    t = max(0.0, min(1.0, t))

    ponto_proximo_x = x1 + t * dx
    ponto_proximo_y = y1 + t * dy

    return math.sqrt((px - ponto_proximo_x)**2 + (py - ponto_proximo_y)**2)


class Modelo:
    def __init__(self):
        self.cor_borda = "black"
        self.cor_preenchimento = "black"
        self.tamanho = 2
        self.inicio_x = 0
        self.inicio_y = 0
        self.ultimo_x = None
        self.ultimo_y = None
        self.objeto = None
        self.pontos_poligono = []
        self.linhas_guia = []

        # ---- seleção múltipla ----
        self.figuras_selecionadas = set()   # conjunto com os ids das figuras selecionadas
        self.buffer_copia = None            # lista de figuras copiadas (Ctrl+C / Ctrl+V)
        self.retangulo_selecao = None       # id do retângulo de seleção "com laço"
        self.modo_arraste = None            # "mover" ou "retangulo", usado pelo EstadoSelecao
        self.grupo_contador = 0             # contador para gerar tags de figuras compostas


class Visao:
    def __init__(self, janela):
        self.janela = janela
        janela.title("Paint - MVC com State Pattern")
        janela.geometry("1000x1000")
        janela.grid_columnconfigure(0, weight=1)
        janela.grid_rowconfigure(0, weight=1)

        self.barra_vertical = tk.Scrollbar(janela, orient=tk.VERTICAL)
        self.barra_horizontal = tk.Scrollbar(janela, orient=tk.HORIZONTAL)

        self.tela = tk.Canvas(janela, bg="white", scrollregion=(0, 0, 2000, 2000),
                            yscrollcommand=self.barra_vertical.set,
                            xscrollcommand=self.barra_horizontal.set)

        self.barra_vertical.config(command=self.tela.yview)
        self.barra_horizontal.config(command=self.tela.xview)

        self.tela.grid(row=0, column=0, sticky="nsew")
        self.barra_vertical.grid(row=0, column=1, sticky="ns")
        self.barra_horizontal.grid(row=1, column=0, sticky="ew")

        self.quadro = tk.Frame(janela)
        self.quadro.grid(row=2, column=0, sticky="ew")

        self.quadro2 = tk.Frame(janela)
        self.quadro2.grid(row=3, column=0, sticky="ew")

        def botao(txt, quadro=None):
            b = tk.Button(quadro if quadro is not None else self.quadro, text=txt)
            b.pack(side=tk.LEFT, padx=2)
            return b

        self.botao_selecionar = botao("Selecionar")
        self.botao_pincel = botao("Pincel")
        self.botao_linha = botao("Linha")
        self.botao_retangulo = botao("Retângulo")
        self.botao_oval = botao("Oval")
        self.botao_circulo = botao("Círculo")
        self.botao_poligono = botao("Polígono")
        self.botao_poligono_regular = botao("Polígono Regular")
        self.botao_distancia = botao("Distância dos pontos")

        tk.Label(self.quadro, text="Tamanho").pack(side=tk.LEFT, padx=5)
        self.escala_tamanho = tk.Scale(self.quadro, from_=1, to=20, orient=tk.HORIZONTAL)
        self.escala_tamanho.set(2)
        self.escala_tamanho.pack(side=tk.LEFT)

        tk.Label(self.quadro, text="Lados").pack(side=tk.LEFT, padx=5)
        self.spin_lados = tk.Spinbox(self.quadro, from_=3, to=12, width=3)
        self.spin_lados.delete(0, "end")
        self.spin_lados.insert(0, "5")
        self.spin_lados.pack(side=tk.LEFT)

        self.botao_cor_borda = botao("Cor Borda")
        self.botao_cor_preenchimento = botao("Cor Preenchimento")

        # ---- segunda linha: operações de seleção múltipla / figuras compostas ----
        self.botao_agrupar = botao("Agrupar (figura composta)", self.quadro2)
        self.botao_desagrupar = botao("Desagrupar", self.quadro2)
        self.botao_selecionar_tudo = botao("Selecionar Tudo", self.quadro2)


class EstadoFerramenta(ABC):
    @abstractmethod
    def clicar(self, ctrl, x, y, ctrl_pressionado=False):
        pass

    @abstractmethod
    def arrastar(self, ctrl, x, y, ctrl_pressionado=False):
        pass

    def soltar(self, ctrl, e):
        ctrl.modelo.objeto = None

    def fechar(self, ctrl, x, y):
        pass


class EstadoSelecao(EstadoFerramenta):
    """
    Suporta seleção múltipla de duas formas:
      1) clique simples seleciona uma figura; CTRL+clique adiciona/retira
         outras figuras do conjunto selecionado;
      2) clique e arraste em área vazia desenha um retângulo (fundo
         transparente) e, ao soltar o botão, seleciona todas as figuras
         que ficarem totalmente dentro dele.
    Também move/opera sobre todo o conjunto selecionado de uma vez.
    """

    def clicar(self, ctrl, x, y, ctrl_pressionado=False):
        alvo = self._figura_no_ponto(ctrl, x, y)

        if alvo is not None:
            if ctrl_pressionado:
                # alterna a figura (ou o grupo dela) dentro/fora da seleção
                if alvo in ctrl.modelo.figuras_selecionadas:
                    ctrl.desselecionar_figura(alvo)
                else:
                    ctrl.selecionar_figura(alvo)
            else:
                # clique simples: se a figura já não fizer parte da seleção
                # atual, troca a seleção inteira por ela (ou pelo seu grupo)
                if alvo not in ctrl.modelo.figuras_selecionadas:
                    ctrl.limpar_selecao()
                    ctrl.selecionar_figura(alvo)
                # se já estava selecionada, mantém o conjunto (permite
                # arrastar várias figuras juntas)

            ctrl.modelo.ultimo_x = x
            ctrl.modelo.ultimo_y = y
            ctrl.modelo.modo_arraste = "mover"
        else:
            # clicou em área vazia -> inicia seleção por retângulo (laço)
            if not ctrl_pressionado:
                ctrl.limpar_selecao()
            ctrl.modelo.inicio_x = x
            ctrl.modelo.inicio_y = y
            ctrl.modelo.modo_arraste = "retangulo"

    def arrastar(self, ctrl, x, y, ctrl_pressionado=False):
        if ctrl.modelo.modo_arraste == "mover" and ctrl.modelo.figuras_selecionadas:
            dx = x - ctrl.modelo.ultimo_x
            dy = y - ctrl.modelo.ultimo_y
            for fig in ctrl.modelo.figuras_selecionadas:
                ctrl.visao.tela.move(fig, dx, dy)
            ctrl.modelo.ultimo_x = x
            ctrl.modelo.ultimo_y = y

        elif ctrl.modelo.modo_arraste == "retangulo":
            if ctrl.modelo.retangulo_selecao:
                ctrl.visao.tela.coords(
                    ctrl.modelo.retangulo_selecao,
                    ctrl.modelo.inicio_x, ctrl.modelo.inicio_y, x, y
                )
            else:
                # fundo transparente: sem "fill", apenas contorno tracejado
                ctrl.modelo.retangulo_selecao = ctrl.visao.tela.create_rectangle(
                    ctrl.modelo.inicio_x, ctrl.modelo.inicio_y, x, y,
                    outline="blue", dash=(4, 2), fill=""
                )

    def soltar(self, ctrl, e):
        if ctrl.modelo.modo_arraste == "retangulo" and ctrl.modelo.retangulo_selecao:
            x1, y1, x2, y2 = ctrl.visao.tela.coords(ctrl.modelo.retangulo_selecao)
            xmin, xmax = sorted((x1, x2))
            ymin, ymax = sorted((y1, y2))

            # find_enclosed -> apenas as figuras TOTALMENTE dentro do retângulo
            itens = ctrl.visao.tela.find_enclosed(xmin, ymin, xmax, ymax)
            for item in itens:
                if item != ctrl.modelo.retangulo_selecao:
                    ctrl.selecionar_figura(item)

            ctrl.visao.tela.delete(ctrl.modelo.retangulo_selecao)
            ctrl.modelo.retangulo_selecao = None

        ctrl.modelo.modo_arraste = None
        ctrl.modelo.ultimo_x = None
        ctrl.modelo.ultimo_y = None

    @staticmethod
    def _figura_no_ponto(ctrl, x, y):
        """Retorna a figura mais próxima do ponto, só se o ponto estiver
        realmente sobre (ou bem perto d)ela — evita selecionar qualquer
        coisa ao clicar em área totalmente vazia."""
        candidatos = ctrl.visao.tela.find_closest(x, y)
        if not candidatos:
            return None
        item = candidatos[0]
        if item == ctrl.modelo.retangulo_selecao:
            return None
        bbox = ctrl.visao.tela.bbox(item)
        if not bbox:
            return None
        margem = 4
        if (bbox[0] - margem <= x <= bbox[2] + margem and
                bbox[1] - margem <= y <= bbox[3] + margem):
            return item
        return None


class EstadoPincel(EstadoFerramenta):
    def clicar(self, ctrl, x, y, ctrl_pressionado=False):
        ctrl.modelo.ultimo_x = x
        ctrl.modelo.ultimo_y = y

    def arrastar(self, ctrl, x, y, ctrl_pressionado=False):
        ctrl.visao.tela.create_line(
            ctrl.modelo.ultimo_x, ctrl.modelo.ultimo_y, x, y,
            fill=ctrl.modelo.cor_borda,
            width=ctrl.modelo.tamanho,
            smooth=True
        )
        ctrl.modelo.ultimo_x = x
        ctrl.modelo.ultimo_y = y


class EstadoLinha(EstadoFerramenta):
    def clicar(self, ctrl, x, y, ctrl_pressionado=False):
        ctrl.modelo.inicio_x = x
        ctrl.modelo.inicio_y = y

    def arrastar(self, ctrl, x, y, ctrl_pressionado=False):
        if ctrl.modelo.objeto:
            ctrl.visao.tela.coords(ctrl.modelo.objeto, ctrl.modelo.inicio_x, ctrl.modelo.inicio_y, x, y)
        else:
            ctrl.modelo.objeto = ctrl.visao.tela.create_line(
                ctrl.modelo.inicio_x, ctrl.modelo.inicio_y, x, y,
                fill=ctrl.modelo.cor_borda,
                width=ctrl.modelo.tamanho
            )


class EstadoRetangulo(EstadoFerramenta):
    def clicar(self, ctrl, x, y, ctrl_pressionado=False):
        ctrl.modelo.inicio_x = x
        ctrl.modelo.inicio_y = y

    def arrastar(self, ctrl, x, y, ctrl_pressionado=False):
        if ctrl.modelo.objeto:
            ctrl.visao.tela.coords(ctrl.modelo.objeto, ctrl.modelo.inicio_x, ctrl.modelo.inicio_y, x, y)
        else:
            ctrl.modelo.objeto = ctrl.visao.tela.create_rectangle(
                ctrl.modelo.inicio_x, ctrl.modelo.inicio_y, x, y,
                outline=ctrl.modelo.cor_borda,
                fill=ctrl.modelo.cor_preenchimento,
                width=ctrl.modelo.tamanho
            )


class EstadoOval(EstadoFerramenta):
    def clicar(self, ctrl, x, y, ctrl_pressionado=False):
        ctrl.modelo.inicio_x = x
        ctrl.modelo.inicio_y = y

    def arrastar(self, ctrl, x, y, ctrl_pressionado=False):
        if ctrl.modelo.objeto:
            ctrl.visao.tela.coords(ctrl.modelo.objeto, ctrl.modelo.inicio_x, ctrl.modelo.inicio_y, x, y)
        else:
            ctrl.modelo.objeto = ctrl.visao.tela.create_oval(
                ctrl.modelo.inicio_x, ctrl.modelo.inicio_y, x, y,
                outline=ctrl.modelo.cor_borda,
                fill=ctrl.modelo.cor_preenchimento,
                width=ctrl.modelo.tamanho
            )


class EstadoCirculo(EstadoFerramenta):
    def clicar(self, ctrl, x, y, ctrl_pressionado=False):
        ctrl.modelo.inicio_x = x
        ctrl.modelo.inicio_y = y

    def arrastar(self, ctrl, x, y, ctrl_pressionado=False):
        lado = min(abs(x - ctrl.modelo.inicio_x), abs(y - ctrl.modelo.inicio_y))
        x_fim = ctrl.modelo.inicio_x + lado if x >= ctrl.modelo.inicio_x else ctrl.modelo.inicio_x - lado
        y_fim = ctrl.modelo.inicio_y + lado if y >= ctrl.modelo.inicio_y else ctrl.modelo.inicio_y - lado

        if ctrl.modelo.objeto:
            ctrl.visao.tela.coords(ctrl.modelo.objeto, ctrl.modelo.inicio_x, ctrl.modelo.inicio_y, x_fim, y_fim)
        else:
            ctrl.modelo.objeto = ctrl.visao.tela.create_oval(
                ctrl.modelo.inicio_x, ctrl.modelo.inicio_y, x_fim, y_fim,
                outline=ctrl.modelo.cor_borda,
                fill=ctrl.modelo.cor_preenchimento,
                width=ctrl.modelo.tamanho
            )


class EstadoPoligono(EstadoFerramenta):
    def clicar(self, ctrl, x, y, ctrl_pressionado=False):
        ctrl.modelo.pontos_poligono.extend([x, y])
        if len(ctrl.modelo.pontos_poligono) >= 4:
            x1, y1 = ctrl.modelo.pontos_poligono[-4], ctrl.modelo.pontos_poligono[-3]
            l = ctrl.visao.tela.create_line(
                x1, y1, x, y,
                fill=ctrl.modelo.cor_borda,
                width=ctrl.modelo.tamanho
            )
            ctrl.modelo.linhas_guia.append(l)

    def arrastar(self, ctrl, x, y, ctrl_pressionado=False):
        pass

    def fechar(self, ctrl, x, y):
        if len(ctrl.modelo.pontos_poligono) >= 6:
            for l in ctrl.modelo.linhas_guia:
                ctrl.visao.tela.delete(l)
            ctrl.modelo.linhas_guia.clear()

            ctrl.visao.tela.create_polygon(
                ctrl.modelo.pontos_poligono,
                outline=ctrl.modelo.cor_borda,
                fill=ctrl.modelo.cor_preenchimento,
                width=ctrl.modelo.tamanho
            )
            ctrl.modelo.pontos_poligono.clear()


class EstadoPoligonoRegular(EstadoFerramenta):
    

    def clicar(self, ctrl, x, y, ctrl_pressionado=False):
        ctrl.modelo.inicio_x = x
        ctrl.modelo.inicio_y = y

    def arrastar(self, ctrl, x, y, ctrl_pressionado=False):
        cx, cy = ctrl.modelo.inicio_x, ctrl.modelo.inicio_y
        raio = math.hypot(x - cx, y - cy)
        if raio < 1:
            return

        try:
            lados = max(3, int(ctrl.visao.spin_lados.get()))
        except (ValueError, tk.TclError):
            lados = 5

        pontos = []
        for i in range(lados):
            angulo = -math.pi / 2 + (2 * math.pi * i / lados)
            px = cx + raio * math.cos(angulo)
            py = cy + raio * math.sin(angulo)
            pontos.extend([px, py])

        if ctrl.modelo.objeto:
            ctrl.visao.tela.coords(ctrl.modelo.objeto, *pontos)
        else:
            ctrl.modelo.objeto = ctrl.visao.tela.create_polygon(
                pontos,
                outline=ctrl.modelo.cor_borda,
                fill=ctrl.modelo.cor_preenchimento,
                width=ctrl.modelo.tamanho
            )


class EstadoDistancia(EstadoFerramenta):

    def clicar(self, ctrl, x, y, ctrl_pressionado=False):
        itens = ctrl.visao.tela.find_closest(x, y)

        if not itens:
            return

        item = itens[0]

        if ctrl.visao.tela.type(item) != "line":
            messagebox.showwarning(
                "Aviso",
                "Selecione uma linha."
            )
            return

        coords = ctrl.visao.tela.coords(item)

        if len(coords) != 4:
            messagebox.showwarning(
                "Aviso",
                "O objeto deve ser um segmento de reta."
            )
            return

        x1, y1, x2, y2 = coords

        d = distancia(x1, y1, x2, y2, x, y)

        messagebox.showinfo(
            "Distância",
            f"Distância = {d:.2f} pixels"
        )

    def arrastar(self, ctrl, x, y, ctrl_pressionado=False):
        pass


class Controlador:
    def __init__(self, modelo, visao):
        self.modelo = modelo
        self.visao = visao

        self.estado_atual = EstadoPincel()

        visao.botao_selecionar.config(command=lambda: self.definir_estado(EstadoSelecao()))
        visao.botao_pincel.config(command=lambda: self.definir_estado(EstadoPincel()))
        visao.botao_linha.config(command=lambda: self.definir_estado(EstadoLinha()))
        visao.botao_retangulo.config(command=lambda: self.definir_estado(EstadoRetangulo()))
        visao.botao_oval.config(command=lambda: self.definir_estado(EstadoOval()))
        visao.botao_circulo.config(command=lambda: self.definir_estado(EstadoCirculo()))
        visao.botao_poligono.config(command=lambda: self.definir_estado(EstadoPoligono()))
        visao.botao_poligono_regular.config(command=lambda: self.definir_estado(EstadoPoligonoRegular()))
        visao.botao_distancia.config(command=lambda: self.definir_estado(EstadoDistancia()))

        visao.botao_cor_borda.config(command=self.cor_borda)
        visao.botao_cor_preenchimento.config(command=self.cor_preenchimento)

        visao.botao_agrupar.config(command=self.agrupar_figuras)
        visao.botao_desagrupar.config(command=self.desagrupar_figuras)
        visao.botao_selecionar_tudo.config(command=self.selecionar_tudo)

        visao.escala_tamanho.config(command=lambda x: setattr(self.modelo, "tamanho", int(x)))

        visao.tela.bind("<Button-1>", self.clicar)
        visao.tela.bind("<B1-Motion>", self.arrastar)
        visao.tela.bind("<ButtonRelease-1>", self.soltar)
        visao.tela.bind("<Double-Button-1>", self.fechar)

        visao.janela.bind("<BackSpace>", self.apagar_figura)
        visao.janela.bind("<Delete>", self.apagar_figura)

        # navegação de camadas (evita conflito com as setas, usadas para mover)
        visao.janela.bind("<Prior>", self.frente_uma_posicao)   # Page Up
        visao.janela.bind("<Next>", self.atras_uma_posicao)     # Page Down
        visao.janela.bind("<Home>", self.frente_topo)
        visao.janela.bind("<End>", self.fundo_total)

        visao.janela.bind("<Control-c>", self.copiar_figura)
        visao.janela.bind("<Control-v>", self.colar_figura)
        visao.janela.bind("<Control-C>", self.copiar_figura)
        visao.janela.bind("<Control-V>", self.colar_figura)

        visao.janela.bind("<Control-g>", self.agrupar_figuras)
        visao.janela.bind("<Control-G>", self.agrupar_figuras)
        visao.janela.bind("<Control-a>", lambda e: self.selecionar_tudo())
        visao.janela.bind("<Control-A>", lambda e: self.selecionar_tudo())

        # setas movem a(s) figura(s) selecionada(s) 5px na direção indicada
        visao.janela.bind("<Left>", lambda e: self.mover_por_teclado(-5, 0))
        visao.janela.bind("<Right>", lambda e: self.mover_por_teclado(5, 0))
        visao.janela.bind("<Up>", lambda e: self.mover_por_teclado(0, -5))
        visao.janela.bind("<Down>", lambda e: self.mover_por_teclado(0, 5))

    # ------------------------------------------------------------------
    # Seleção múltipla / figuras compostas
    # ------------------------------------------------------------------
    def obter_grupo(self, item):
        """Retorna a tag de grupo ('grupo_N') do item, se ele pertencer a
        uma figura composta, ou None caso contrário."""
        for tag in self.visao.tela.gettags(item):
            if tag.startswith("grupo_"):
                return tag
        return None

    def selecionar_figura(self, item):
        """Seleciona a figura; se ela pertencer a um grupo (figura
        composta), seleciona todas as figuras desse grupo junto."""
        grupo = self.obter_grupo(item)
        alvos = self.visao.tela.find_withtag(grupo) if grupo else (item,)
        for alvo in alvos:
            if alvo not in self.modelo.figuras_selecionadas:
                self.modelo.figuras_selecionadas.add(alvo)
                try:
                    self.visao.tela.itemconfig(alvo, dash=(6, 4))
                except tk.TclError:
                    pass

    def desselecionar_figura(self, item):
        grupo = self.obter_grupo(item)
        alvos = self.visao.tela.find_withtag(grupo) if grupo else (item,)
        for alvo in alvos:
            if alvo in self.modelo.figuras_selecionadas:
                self.modelo.figuras_selecionadas.discard(alvo)
                try:
                    self.visao.tela.itemconfig(alvo, dash=())
                except tk.TclError:
                    pass

    def limpar_selecao(self):
        for item in list(self.modelo.figuras_selecionadas):
            try:
                self.visao.tela.itemconfig(item, dash=())
            except tk.TclError:
                pass
        self.modelo.figuras_selecionadas.clear()

    def selecionar_tudo(self):
        self.definir_estado(EstadoSelecao())
        self.limpar_selecao()
        for item in self.visao.tela.find_all():
            if item != self.modelo.retangulo_selecao:
                self.selecionar_figura(item)

    def agrupar_figuras(self, e=None):
        """Transforma o conjunto selecionado em uma figura composta: elas
        passam a ser selecionadas, movidas e apagadas sempre juntas."""
        if len(self.modelo.figuras_selecionadas) < 2:
            return
        self.modelo.grupo_contador += 1
        tag = f"grupo_{self.modelo.grupo_contador}"
        for item in self.modelo.figuras_selecionadas:
            self.visao.tela.addtag_withtag(tag, item)

    def desagrupar_figuras(self, e=None):
        """Desfaz a figura composta das figuras atualmente selecionadas."""
        for item in list(self.modelo.figuras_selecionadas):
            grupo = self.obter_grupo(item)
            if grupo:
                self.visao.tela.dtag(item, grupo)

    def mover_por_teclado(self, dx, dy):
        if isinstance(self.estado_atual, EstadoSelecao) and self.modelo.figuras_selecionadas:
            for item in self.modelo.figuras_selecionadas:
                self.visao.tela.move(item, dx, dy)

    def definir_estado(self, novo_estado):
        if not isinstance(novo_estado, EstadoSelecao) and self.modelo.figuras_selecionadas:
            self.limpar_selecao()

        if self.modelo.pontos_poligono:
            for l in self.modelo.linhas_guia:
                self.visao.tela.delete(l)
            self.modelo.linhas_guia.clear()
            self.modelo.pontos_poligono.clear()

        if self.modelo.retangulo_selecao:
            self.visao.tela.delete(self.modelo.retangulo_selecao)
            self.modelo.retangulo_selecao = None

        self.modelo.objeto = None
        self.estado_atual = novo_estado

    # ------------------------------------------------------------------
    # Cores (aplicadas a toda a seleção)
    # ------------------------------------------------------------------
    def cor_borda(self):
        c = colorchooser.askcolor()[1]
        if c:
            self.modelo.cor_borda = c
            for item in self.modelo.figuras_selecionadas:
                tipo = self.visao.tela.type(item)
                opcao = "fill" if tipo == "line" else "outline"
                self.visao.tela.itemconfig(item, **{opcao: c})

    def cor_preenchimento(self):
        c = colorchooser.askcolor()[1]
        if c:
            self.modelo.cor_preenchimento = c
            for item in self.modelo.figuras_selecionadas:
                tipo = self.visao.tela.type(item)
                if tipo != "line":
                    self.visao.tela.itemconfig(item, fill=c)

    # ------------------------------------------------------------------
    # Apagar / reordenar camadas (aplicados a toda a seleção)
    # ------------------------------------------------------------------
    def apagar_figura(self, e):
        for item in list(self.modelo.figuras_selecionadas):
            self.visao.tela.delete(item)
        self.modelo.figuras_selecionadas.clear()

    def frente_uma_posicao(self, e):
        for item in self.modelo.figuras_selecionadas:
            alvo = self.visao.tela.find_above(item)
            if alvo:
                self.visao.tela.tag_raise(item, alvo)

    def atras_uma_posicao(self, e):
        for item in self.modelo.figuras_selecionadas:
            alvo = self.visao.tela.find_below(item)
            if alvo:
                self.visao.tela.tag_lower(item, alvo)

    def frente_topo(self, e):
        for item in self.modelo.figuras_selecionadas:
            self.visao.tela.tag_raise(item)

    def fundo_total(self, e):
        for item in self.modelo.figuras_selecionadas:
            self.visao.tela.tag_lower(item)

    # ------------------------------------------------------------------
    # Copiar / colar (toda a seleção, preservando o agrupamento)
    # ------------------------------------------------------------------
    def copiar_figura(self, e=None):
        if not self.modelo.figuras_selecionadas:
            return

        copiados = []
        for item in self.modelo.figuras_selecionadas:
            tipo = self.visao.tela.type(item)
            coords = self.visao.tela.coords(item)
            cfg = {}
            for opcao in ["fill", "outline", "width"]:
                try:
                    cfg[opcao] = self.visao.tela.itemcget(item, opcao)
                except tk.TclError:
                    pass
            copiados.append({"tipo": tipo, "coords": coords, "cfg": cfg})

        self.modelo.buffer_copia = copiados

    def colar_figura(self, e=None):
        if not self.modelo.buffer_copia:
            return

        self.limpar_selecao()
        novos_ids = []

        for dados in self.modelo.buffer_copia:
            tipo = dados["tipo"]
            novas_coords = [coord + 20 for coord in dados["coords"]]
            cfg = dict(dados["cfg"])
            cfg.pop("dash", None)

            novo_id = None
            if tipo == "line":
                novo_id = self.visao.tela.create_line(novas_coords, **cfg)
            elif tipo == "rectangle":
                novo_id = self.visao.tela.create_rectangle(novas_coords, **cfg)
            elif tipo == "oval":
                novo_id = self.visao.tela.create_oval(novas_coords, **cfg)
            elif tipo == "polygon":
                novo_id = self.visao.tela.create_polygon(novas_coords, **cfg)

            if novo_id:
                novos_ids.append(novo_id)

        # se mais de uma figura foi colada, elas viram uma figura composta
        if len(novos_ids) > 1:
            self.modelo.grupo_contador += 1
            tag = f"grupo_{self.modelo.grupo_contador}"
            for nid in novos_ids:
                self.visao.tela.addtag_withtag(tag, nid)

        for nid in novos_ids:
            self.selecionar_figura(nid)

    # ------------------------------------------------------------------
    # Eventos de mouse
    # ------------------------------------------------------------------
    def clicar(self, e):
        self.visao.tela.focus_set()
        x = self.visao.tela.canvasx(e.x)
        y = self.visao.tela.canvasy(e.y)
        ctrl_pressionado = bool(e.state & 0x0004)
        self.estado_atual.clicar(self, x, y, ctrl_pressionado)

    def arrastar(self, e):
        x = self.visao.tela.canvasx(e.x)
        y = self.visao.tela.canvasy(e.y)
        ctrl_pressionado = bool(e.state & 0x0004)
        self.estado_atual.arrastar(self, x, y, ctrl_pressionado)

    def soltar(self, e):
        self.estado_atual.soltar(self, e)

    def fechar(self, e):
        x = self.visao.tela.canvasx(e.x)
        y = self.visao.tela.canvasy(e.y)
        self.estado_atual.fechar(self, x, y)


if __name__ == "__main__":
    janela = tk.Tk()
    modelo = Modelo()
    visao = Visao(janela)
    Controlador(modelo, visao)
    janela.mainloop()
