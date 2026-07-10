

#--------------------------------------------------------------
class EstadoSelecao(EstadoFerramenta):
    def clicar(self, ctrl, x, y):
        # Encontra o objeto mais próximo do clique do mouse
        itens = ctrl.visao.tela.find_closest(x,y)
        
        # Remove a borda de destaque do objeto anteriormente selecionado (se houver)
        if ctrl.modelo.figura_selecionada:
            ctrl.visao.tela.itemconfig(ctrl.modelo.figura_selecionada, dash=())

        if itens:
            # Seleciona o item do topo da pilha sob o clique
            ctrl.modelo.figura_selecionada = itens[0]
            # Adiciona um efeito tracejado temporário indicando seleção
            ctrl.visao.tela.itemconfig(ctrl.modelo.figura_selecionada, dash=(8, 8))
            
            # Salva a posição inicial do clique para calcular o deslocamento (delta)
            ctrl.modelo.ultimo_x = x
            ctrl.modelo.ultimo_y = y
        else:
            ctrl.modelo.figura_selecionada = None

    def arrastar(self, ctrl, x, y):
        if ctrl.modelo.figura_selecionada and ctrl.modelo.ultimo_x is not None:
            # Calcula a distância movida
            dx = x - ctrl.modelo.ultimo_x
            dy = y - ctrl.modelo.ultimo_y
            
            # Move o objeto selecionado
            ctrl.visao.tela.move(ctrl.modelo.figura_selecionada, dx, dy)
            
            # Atualiza o último rastro do mouse
            ctrl.modelo.ultimo_x = x
            ctrl.modelo.ultimo_y = y

    def soltar(self, ctrl, e):
        ctrl.modelo.ultimo_x = None
        ctrl.modelo.ultimo_y = None
 Mateus Gusmão
#-------------------------------------------------------

# Controlador: --> CONTEXTO DO PADRÃO STATE

class Controlador:
    def __init__(self, modelo, visao):  
        self.modelo = modelo
        self.visao = visao
        
        # Define o estado inicial da aplicação
        self.estado_atual = EstadoPincel()

        # Vinculação dos botões passando instâncias das classes de estado
        visao.botao_selecionar.config(command=lambda: self.definir_estado(EstadoSelecao()))
        visao.botao_pincel.config(command=lambda: self.definir_estado(EstadoPincel()))
        visao.botao_linha.config(command=lambda: self.definir_estado(EstadoLinha()))
        visao.botao_retangulo.config(command=lambda: self.definir_estado(EstadoRetangulo()))
        visao.botao_oval.config(command=lambda: self.definir_estado(EstadoOval()))
        visao.botao_circulo.config(command=lambda: self.definir_estado(EstadoCirculo()))
        visao.botao_poligono.config(command=lambda: self.definir_estado(EstadoPoligono()))

        visao.botao_cor_borda.config(command=self.cor_borda)
        visao.botao_cor_preenchimento.config(command=self.cor_preenchimento)

        visao.escala_tamanho.config(command=lambda x: setattr(self.modelo, "tamanho", int(x)))

        # Eventos do Mouse
        visao.tela.bind("<Button-1>", self.clicar)
        visao.tela.bind("<B1-Motion>", self.arrastar)
        visao.tela.bind("<ButtonRelease-1>", self.soltar)
        visao.tela.bind("<Double-Button-1>", self.fechar)

        # Eventos de Teclado (Vinculados à janela principal ou ao canvas focado)
        visao.janela.bind("<Delete>", self.apagar_figura)
        visao.janela.bind("<Right>", self.frente_uma_posicao)
        visao.janela.bind("<Left>", self.atras_uma_posicao)
        visao.janela.bind("<Up>", self.frente_topo)
        visao.janela.bind("<Down>", self.fundo_total)
        
        # Atalhos de Copiar e Colar (Tratando maiúsculas/minúsculas nativas do Tkinter)
        visao.janela.bind("<Control-c>", self.copiar_figura)
        visao.janela.bind("<Control-v>", self.colar_figura)
        visao.janela.bind("<Control-C>", self.copiar_figura)
        visao.janela.bind("<Control-V>", self.colar_figura)
Arthut Maciel
#-------------------------------------------------------------------------------------
    def definir_estado(self, novo_estado):
        # Remove tracejado de destaque se sair do modo seleção
        if not isinstance(novo_estado, EstadoSelecao) and self.modelo.figura_selecionada:
            try:
                self.visao.tela.itemconfig(self.modelo.figura_selecionada, dash=())
            except:
                pass
            self.modelo.figura_selecionada = None

        # Limpa os dados residuais de polígonos inacabados ao trocar de ferramenta
        if self.modelo.pontos_poligono:
            for l in self.modelo.linhas_guia:
                self.visao.tela.delete(l)
            self.modelo.linhas_guia.clear()
            self.modelo.pontos_poligono.clear()
            
        self.estado_atual = novo_estado

  

    # --- Operações de Teclado sobre a Figura Selecionada ---
    def apagar_figura(self, e):
        if self.modelo.figura_selecionada:
            self.visao.tela.delete(self.modelo.figura_selecionada)
            self.modelo.figura_selecionada = None

    def frente_uma_posicao(self, e):
        if self.modelo.figura_selecionada:
            # No Tkinter Canvas, tag_raise acima do próximo vizinho joga uma posição para a frente
            alvo = self.visao.tela.find_above(self.modelo.figura_selecionada)
            if alvo:
                self.visao.tela.tag_raise(self.modelo.figura_selecionada, alvo)

    def atras_uma_posicao(self, e):
        if self.modelo.figura_selecionada:
            # tag_lower abaixo do próximo vizinho joga uma posição para trás
            alvo = self.visao.tela.find_below(self.modelo.figura_selecionada)
            if alvo:
                self.visao.tela.tag_lower(self.modelo.figura_selecionada, alvo)

    def frente_topo(self, e):
        if self.modelo.figura_selecionada:
            # Sem segundo argumento, joga diretamente para o topo visual
            self.visao.tela.tag_raise(self.modelo.figura_selecionada)

    def fundo_total(self, e):
        if self.modelo.figura_selecionada:
            # Sem segundo argumento, joga diretamente para o fundo do canvas
            self.visao.tela.tag_lower(self.modelo.figura_selecionada)

    def copiar_figura(self, e):
        if self.modelo.figura_selecionada:
            # Extrai os dados necessários para duplicar o objeto
            tipo = self.visao.tela.type(self.modelo.figura_selecionada)
            coords = self.visao.tela.coords(self.modelo.figura_selecionada)
            cfg = {}
            for opcao in ["fill", "outline", "width"]:
                try:
                    cfg[opcao] = self.visao.tela.itemcget(self.modelo.figura_selecionada, opcao)
                except tk.TclError:
                    pass # Algumas propriedades podem não existir dependendo do tipo da figura
            
            # Salva no buffer do modelo
            self.modelo.buffer_copia = {"tipo": tipo, "coords": coords, "cfg": cfg}

    def colar_figura(self, e):
        if self.modelo.buffer_copia:
            dados = self.modelo.buffer_copia
            tipo = dados["tipo"]
            # Desloca as coordenadas ligeiramente (+20 pixels) para não colar exatamente em cima da original
            novas_coords = [coord + 20 for coord in dados["coords"]]
            
            # Remove a propriedade de tracejado gerada na cópia se houver
            dados["cfg"].pop("dash", None)

            # Recria o objeto baseado no tipo armazenado
            novo_id = None
            if tipo == "line":
                novo_id = self.visao.tela.create_line(novas_coords, **dados["cfg"])
            elif tipo == "rectangle":
                novo_id = self.visao.tela.create_rectangle(novas_coords, **dados["cfg"])
            elif tipo == "oval":
                novo_id = self.visao.tela.create_oval(novas_coords, **dados["cfg"])
            elif tipo == "polygon":
                novo_id = self.visao.tela.create_polygon(novas_coords, **dados["cfg"])

            if novo_id:
                # Seleciona automaticamente o novo objeto clonado
                if self.modelo.figura_selecionada:
                    self.visao.tela.itemconfig(self.modelo.figura_selecionada, dash=())
                self.modelo.figura_selecionada = novo_id
                self.visao.tela.itemconfig(self.modelo.figura_selecionada, dash=(4, 4))

  Vinicius Levi 
#------------------------------------------------------------------------------------------
