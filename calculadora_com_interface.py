import tkinter as tk

# Configurações da janela principal, tamanho, titulo, configurações
# das linha, e das colunas
janela_principal = tk.Tk()
janela_principal.geometry('250x200')
janela_principal.title('Calculadora')
janela_principal.rowconfigure([0, 1, 2], minsize=100)

frame_butao = tk.Frame(master=janela_principal, relief=tk.FLAT, borderwidth=2)

btn_1 = tk.Button(master=janela_principal, text='1', width=5)

btn_1.grid(row=1, column=0, ipady=5, padx=20)

janela_principal.mainloop()
