import tkinter as tk

# Configurações da janela principal, tamanho, titulo, configurações
# das linha, e das colunas
janela_principal = tk.Tk()
janela_principal.title('Calculadora')
janela_principal.columnconfigure([0, 1, 2, 3], minsize=1)
janela_principal.rowconfigure([0, 1, 2, 3], minsize=40)

# Botões numéricos
btn_0 = tk.Button(text='0', width=5, relief=tk.GROOVE, borderwidth=2, bg='white')
btn_1 = tk.Button(text='1', width=5, relief=tk.GROOVE, borderwidth=2, bg='white')
btn_2 = tk.Button(text='2', width=5, relief=tk.GROOVE, borderwidth=2, bg='white')
btn_3 = tk.Button(text='3', width=5, relief=tk.GROOVE, borderwidth=2, bg='white')
btn_4 = tk.Button(text='4', width=5, relief=tk.GROOVE, borderwidth=2, bg='white')
btn_5 = tk.Button(text='5', width=5, relief=tk.GROOVE, borderwidth=2, bg='white')
btn_6 = tk.Button(text='6', width=5, relief=tk.GROOVE, borderwidth=2, bg='white')
btn_7 = tk.Button(text='7', width=5, relief=tk.GROOVE, borderwidth=2, bg='white')
btn_8 = tk.Button(text='8', width=5, relief=tk.GROOVE, borderwidth=2, bg='white')
btn_9 = tk.Button(text='9', width=5, relief=tk.GROOVE, borderwidth=2, bg='white')

# Botões de operação
# (x - multiplacação)
# (s - subtração -)
# (a - adição +)
# (i - igual =)
btn_x = tk.Button(text='x', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA')
btn_s = tk.Button(text='-', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA')
btn_a = tk.Button(text='+', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA')
btn_i = tk.Button(text='=', width=5, relief=tk.GROOVE, borderwidth=2, bg='#66C4F2')

# Outros Botões
# (n - positvo ou negativo)
# (v - vígula)
btn_n = tk.Button(text='+/-', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA')
btn_v = tk.Button(text=',', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA')

# Botões numéricos posicionados
btn_0.grid(row=3, column=1, ipady=5, padx=2)
btn_1.grid(row=2, column=0, ipady=5, padx=2)
btn_2.grid(row=2, column=1, ipady=5, padx=2)
btn_3.grid(row=2, column=2, ipady=5, padx=2)
btn_4.grid(row=1, column=0, ipady=5, padx=2)
btn_5.grid(row=1, column=1, ipady=5, padx=2)
btn_6.grid(row=1, column=2, ipady=5, padx=2)
btn_7.grid(row=0, column=0, ipady=5, padx=2)
btn_8.grid(row=0, column=1, ipady=5, padx=2)
btn_9.grid(row=0, column=2, ipady=5, padx=2)

# Botões de operação posicionados
btn_x.grid(row=0, column=3, ipady=5, padx=2)
btn_s.grid(row=1, column=3, ipady=5, padx=2)
btn_a.grid(row=2, column=3, ipady=5, padx=2)
btn_i.grid(row=3, column=3, ipady=5, padx=2)

# Outros Botões posicionados
btn_n.grid(row=3, column=0, ipady=5, padx=2)
btn_v.grid(row=3, column=2, ipady=5, padx=2)

janela_principal.mainloop()
