import tkinter as tk

janela_principal = tk.Tk()

for butao in range(1, 10):
    btn = tk.Button(text=f'{butao}')
    for linha in range(1, 4):
        for coluna in range(1, 4):
            btn.grid(row=linha, column=coluna)
janela_principal.mainloop()
