from tkinter import *
from tkinter import messagebox
import conexao

def buscar_informacoes():
    # Obter o valor do campo id_1 como uma string
    n = id_1.get()

    # Verificar se o campo está vazio
    if not n:
        messagebox.showinfo("Informações do Banco de Dados", "Por favor, insira uma matrícula.")
        return None

    try:
        # Converter o valor para um número inteiro
        n_int = int(n)
    except ValueError:
        messagebox.showinfo("Informações do Banco de Dados", "A matrícula deve ser um número inteiro.")
        return None    
    
    cursor = conexao.con.cursor()

    # Executar a consulta para obter as informações do banco
    cursor.execute("SELECT nome, cpf, email FROM cliente WHERE id_cliente = %s", (n_int,))
    resultado = cursor.fetchall()

    # Fechar a conexão com o banco de dados
    cursor.close()

    # Retornar as informações encontradas
    return resultado


def exibir_informacoes():
    informacoes = buscar_informacoes()
    
    if informacoes:
        mensagem = ""
        for info in informacoes:
            nome, cpf, email = info
            mensagem += f"Nome: {nome}\nCPF: {cpf}\nE-mail: {email}\n\n"
            
        messagebox.showinfo("Informações do Banco de Dados", mensagem)
        tela.destroy()
    else:
        messagebox.showinfo("Informações do Banco de Dados", "Nenhuma informação encontrada.")

# Criar a janela principal
tela = Tk()
tela.geometry('300x300')

id_label = Label(tela, text='Matricula')
id_label.place(relx='0.00', rely='0.00')

id_1 = Entry(tela)
id_1.place(relx='0.20', rely='0.00')

# Criar um botão para exibir as informações do banco de dados
botao_exibir = Button(tela, text="Exibir Informações", command=exibir_informacoes)
botao_exibir.place(relx='0.22', rely='0.09')

# Iniciar o loop principal da janela
tela.mainloop()
