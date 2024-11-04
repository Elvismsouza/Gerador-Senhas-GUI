import tkinter as tk
from tkinter import messagebox
import random
import string

# Função para gerar a senha
def gerar_senha():
    comprimento = int(entry_comprimento.get())
    incluir_maiusculas = var_maiusculas.get()
    incluir_minusculas = var_minusculas.get()
    incluir_numeros = var_numeros.get()
    incluir_simbolos = var_simbolos.get()

    # Define o conjunto de caracteres baseado nas escolhas do usuário
    caracteres = ""
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    # Verifica se pelo menos um tipo de caractere foi selecionado
    if not caracteres:
        messagebox.showwarning("Aviso", "Selecione pelo menos um tipo de caractere.")
        return

    # Gera a senha aleatória
    senha = "".join(random.choice(caracteres) for _ in range(comprimento))
    entry_senha.delete(0, tk.END)
    entry_senha.insert(0, senha)

# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Gerador de Senhas Aleatórias")
janela.geometry("400x300")
janela.resizable(False, False)

# Label e campo para comprimento da senha
label_comprimento = tk.Label(janela, text="Comprimento da senha:")
label_comprimento.pack(pady=5)
entry_comprimento = tk.Entry(janela)
entry_comprimento.insert(0, "8")  # Comprimento padrão
entry_comprimento.pack()

# Opções para componentes da senha
var_maiusculas = tk.BooleanVar()
check_maiusculas = tk.Checkbutton(janela, text="Incluir Letras Maiúsculas", variable=var_maiusculas)
check_maiusculas.pack()

var_minusculas = tk.BooleanVar()
check_minusculas = tk.Checkbutton(janela, text="Incluir Letras Minúsculas", variable=var_minusculas)
check_minusculas.pack()

var_numeros = tk.BooleanVar()
check_numeros = tk.Checkbutton(janela, text="Incluir Números", variable=var_numeros)
check_numeros.pack()

var_simbolos = tk.BooleanVar()
check_simbolos = tk.Checkbutton(janela, text="Incluir Símbolos", variable=var_simbolos)
check_simbolos.pack()

# Botão para gerar a senha
botao_gerar = tk.Button(janela, text="Gerar Senha", command=gerar_senha)
botao_gerar.pack(pady=10)

# Campo para exibir a senha gerada
label_senha = tk.Label(janela, text="Senha Gerada:")
label_senha.pack(pady=5)
entry_senha = tk.Entry(janela, width=30)
entry_senha.pack()

# Função para copiar a senha
def copiar_senha():
    senha = entry_senha.get()
    janela.clipboard_clear()
    janela.clipboard_append(senha)
    messagebox.showinfo("Informação", "Senha copiada para a área de transferência.")

# Botão para copiar a senha
botao_copiar = tk.Button(janela, text="Copiar Senha", command=copiar_senha)
botao_copiar.pack(pady=10)

# Inicia a interface
janela.mainloop()
