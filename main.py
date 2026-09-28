import tkinter as tk
from interface import criar_interface


janela = tk.Tk()

janela.title("TaskManager")
janela.geometry("1000x650")
janela.minsize(800, 500)

criar_interface(janela)

janela.mainloop()