import tkinter as tk
from tkinter import messagebox

def cadastrar_estudante():
    nome = entry_nome.get()
    matricula = entry_matricula.get()

    if nome and matricula:
        with open("estudantes.dat", "a") as file:
            file.write(f"{matricula},{nome}\n")
        messagebox.showinfo("Sucesso", f"Aluno {nome} cadastrado com sucesso!")
        entry_nome.delete(0, tk.END)
        entry_matricula.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

def consultar_estudantes():
    try:
        with open("estudantes.dat", "r") as file:
            alunos = file.readlines()
    except FileNotFoundError:
        alunos = []

    if alunos:
        resultado = "\n".join([f"Matrícula: {linha.split(',')[0]} - Nome: {linha.split(',')[1].strip()}" for linha in alunos])
    else:
        resultado = "Nenhum aluno cadastrado."

    messagebox.showinfo("Consulta de Alunos", resultado)

def sair():
    root.destroy()

root = tk.Tk()
root.title("Sistema de Cadastro de Alunos")

tk.Label(root, text="Nome do Aluno:").pack(pady=5)
entry_nome = tk.Entry(root)
entry_nome.pack(pady=5)

tk.Label(root, text="Matrícula do Aluno:").pack(pady=5)
entry_matricula = tk.Entry(root)
entry_matricula.pack(pady=5)

tk.Button(root, text="Cadastrar Aluno", command=cadastrar_estudante).pack(pady=10)
tk.Button(root, text="Consultar Alunos", command=consultar_estudantes).pack(pady=10)
tk.Button(root, text="Sair", command=sair).pack(pady=10)

root.mainloop()
