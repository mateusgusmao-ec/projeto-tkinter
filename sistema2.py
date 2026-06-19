import tkinter as tk

janela = tk.Tk()
janela.title("Desenho com Scroll e Paleta")
janela.geometry("900x600")

janela.grid_columnconfigure(0, weight=1)
janela.grid_rowconfigure(0, weight=1)

cor_atual = "black"

v = tk.Scrollbar(janela, orient=tk.VERTICAL)
h = tk.Scrollbar(janela, orient=tk.HORIZONTAL)

canvas = tk.Canvas(janela, scrollregion=(0, 0, 1000, 1000),
                   yscrollcommand=v.set, xscrollcommand=h.set, bg="white")

h['command'] = canvas.xview
v['command'] = canvas.yview

canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
h.grid(column=0, row=1, sticky=(tk.W, tk.E))
v.grid(column=1, row=0, sticky=(tk.N, tk.S))

lastx, lasty = 0, 0

def xy(event):
    global lastx, lasty
    lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)

def addLine(event):
    global lastx, lasty
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    canvas.create_line((lastx, lasty, x, y), fill=cor_atual, width=5, tags='currentline')
    lastx, lasty = x, y

def fim_desenho(event):
    canvas.itemconfigure('currentline', width=1)

def setColor(nova_cor):
    global cor_atual
    cor_atual = nova_cor
    canvas.itemconfigure('palette', outline='white')
    tag_selecionada = f'palette{nova_cor}'
    canvas.itemconfigure(tag_selecionada, outline='#999999', width=2)

canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
canvas.bind("<ButtonRelease-1>", fim_desenho)

id_red = canvas.create_rectangle((10, 10, 40, 40), fill='red', tags=('palette', 'palettered'))
canvas.tag_bind(id_red, "<Button-1>", lambda x: setColor('red'))

id_blue = canvas.create_rectangle((10, 50, 40, 80), fill='blue', tags=('palette', 'paletteblue'))
canvas.tag_bind(id_blue, "<Button-1>", lambda x: setColor('blue'))

id_black = canvas.create_rectangle((10, 90, 40, 120), fill='black', tags=('palette', 'paletteblack'))
canvas.tag_bind(id_black, "<Button-1>", lambda x: setColor('black'))

setColor('black')
canvas.itemconfigure('palette', width=1)

janela.mainloop()   