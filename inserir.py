from tkinter import *
import conexao


def  cadastrar(nome, cpf, email):
    meu_cursor = conexao.con.cursor()
    sql = 'INSERT INTO cliente (nome, cpf, email) VALUES (%s, %s, %s)'
    val = (nome, cpf, email)
    meu_cursor.execute(sql,val)
    conexao.con.commit()
    meu_cursor.close()  
    conexao.con.close()


tela = Tk()
tela.title('INSERT')
tela.geometry('500x300')
tela.configure(bg='#FFFACD')




#NOME
nome_aluno = Label(text='Nome Aluno')
nome_aluno.place(rely=0.01,relx=0.00)
nome_aluno.configure(background='#FFFACD')

nome_aluno_1 = Entry(tela)
nome_aluno_1.place(rely=0.01,relx=0.17)

#CPF
cpf_aluno = Label(text='CPF Aluno')
cpf_aluno.place(rely=0.10,relx=0.0)
cpf_aluno.configure(background='#FFFACD')

cpf_aluno_1 = Entry(tela)
cpf_aluno_1.place(rely=0.10,relx=0.17)

#E-MAIL
email_aluno = Label(text='E-mail Aluno')
email_aluno.place(rely=0.18,relx=0.00)
email_aluno.configure(background='#FFFACD')

email_aluno_1 = Entry(tela)
email_aluno_1.place(rely=0.18,relx=0.17)

def cad_aluno():
    nome = nome_aluno_1.get()
    cpf = cpf_aluno_1.get()
    email = email_aluno_1.get()
    cadastrar(nome,cpf,email)
    tela.destroy()




#BOTÃO CADASTRO
enviar = Button(tela, text='Cadastrar')
enviar.place(rely=0.28,relx=0.20)
enviar.config(command=cad_aluno)





tela.mainloop()