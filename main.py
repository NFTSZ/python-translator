from tkinter import ttk, Text
from ttkthemes import ThemedTk
from googletrans import Translator

translator = Translator()

def traduzir(evento=None):
    texto = entrada.get('1.0', 'end')
    src = combo_entrada.get()
    dest = combo_saida.get()
    resultado = translator.translate(text=texto, src=src, dest=dest)
    
    saida.configure(state='normal')
    saida.delete('1.0', 'end')
    saida.insert('1.0', resultado.text)
    saida.configure(state='disabled')
  # print(resultado.text)
    
janela = ThemedTk(theme='yaru')

frame_geral = ttk.Frame()
frame_geral.pack()
janela.title('Tradutor')

values = ['pt', 'en', 'es', 'it', 'ja', 'la']

# entradas
entrada_frame = ttk.Frame(frame_geral)

label_entrada = ttk.Label(entrada_frame, text='Entrada', font=('Monospace', 10))
combo_entrada = ttk.Combobox(entrada_frame, values=values, font=('Monospace', 10))
combo_entrada.set('pt')


label_entrada.grid(row=0, column=0, padx=10, pady=10)
combo_entrada.grid(row=0, column=1, padx=10, pady=10)
entrada_frame.pack()

entrada = Text(frame_geral, height=10, width=50)
entrada.pack(padx=10, pady='10', fill='both', expand='yes')

# Saidas
saida_frame = ttk.Frame(frame_geral)

label_saida = ttk.Label(saida_frame, text='Saida', font=('Monospace', 10))
combo_saida= ttk.Combobox(saida_frame, values=values, font=('Monospace', 10))
combo_saida.set('en')


label_saida.grid(row=0, column=0, padx=10, pady=10)
combo_saida.grid(row=0, column=1, padx=10, pady=10)
saida_frame.pack()

saida = Text(frame_geral, height=10, width=50, state='disabled')
saida.pack(padx=10, pady='10', fill='both', expand='yes')


# botao
botao = ttk.Button(frame_geral, text='Traduzir', command=traduzir)
botao.pack(fill='both')

janela.bind('<Return>', traduzir)

janela.mainloop()