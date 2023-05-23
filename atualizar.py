from tkinter import *
import conexao




def atualiza_cadastro(nome, cpf, email,id_cliente):
    meu_cursor = conexao.con.cursor()
    sql = "UPDATE cliente SET nome = %s, cpf = %s, email = %s  WHERE  id_cliente = %s"
    val = (nome, cpf, email,id_cliente)
    meu_cursor.execute(sql, val)
    conexao.con.commit()
    meu_cursor.close()   
    conexao.con.close() 


tela = Tk()
tela.title('UPdate')
tela.geometry('500x300')
tela.configure(bg='#FFFACD')




#NOME
nome_aluno = Label(text='Nome ')
nome_aluno.place(rely=0.01,relx=0.00)
nome_aluno.configure(background='#FFFACD')

nome_aluno_1 = Entry(tela)
nome_aluno_1.place(rely=0.01,relx=0.17)

#CPF
cpf_aluno = Label(text='CPF')
cpf_aluno.place(rely=0.10,relx=0.0)
cpf_aluno.configure(background='#FFFACD')

cpf_aluno_1 = Entry(tela)
cpf_aluno_1.place(rely=0.10,relx=0.17)

#E-MAIL
email_aluno = Label(text='E-mail ')
email_aluno.place(rely=0.18,relx=0.00)
email_aluno.configure(background='#FFFACD')

email_aluno_1 = Entry(tela)
email_aluno_1.place(rely=0.18,relx=0.17)

#ID_CLIENTE

id_aluno = Label(text='ID')
id_aluno.place(rely=0.25,relx=0.00)
id_aluno.configure(background='#FFFACD')

id_aluno_1 = Entry(tela)
id_aluno_1.place(rely=0.25,relx=0.17)


def atualizar_cad():
    nome = nome_aluno_1.get()
    cpf = cpf_aluno_1.get()
    email = email_aluno_1.get()
    id = id_aluno_1.get()
    atualiza_cadastro(nome,cpf,email,id)
    tela.destroy()




#BOTÃO CADASTRO
enviar = Button(tela, text='Salvar Atualização')
enviar.place(rely=0.33,relx=0.20)
enviar.config(command=atualizar_cad)





tela.mainloop()