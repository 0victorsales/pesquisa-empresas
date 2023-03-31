from project import automacao
import tkinter as tk
from tkinter import filedialog, messagebox
import os


#criando janela
janela = tk.Tk()
janela.geometry("300x300")
janela.config(background="#9932CC")

#criando a função para fazer upload do arquivo
def open_file():
    file_path = filedialog.askopenfilename()
    
    #extraindo extensão do arquivo
    _,ext = os.path.splitext(file_path)
    
    #verificando se o aquivo é um excel
    if ext == ".xlsx":
        automacao(file_path)
        messagebox.showinfo(title='Noticação', message='Arquivo enviado com sucesso!')
    else:
        messagebox.showerror(title='Erro de arquivo',message='Esse arquivo não é um excel!' )


#criando botão
open_button = tk.Button(janela, text="Abrir arquivo", command=open_file,width=30, height=3)


#adicionando botão na tele principal
open_button.place(relx=0.5, rely=0.5, anchor='center')

janela.mainloop()