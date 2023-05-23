import tkinter as tk
import conexao

# Função para deletar o registro
def deletar():
    del_1 = entrada.get()
    meu_cursor = conexao.con.cursor()

    sql = "DELETE FROM cliente WHERE id_cliente = %s"
    val = (del_1,)
    meu_cursor.execute(sql, val)
    conexao.con.commit()

    # Exibir uma mensagem após a exclusão
    resultado_label.config(text="Registro deletado com sucesso!")
    

# Criar uma tela Tkinter
tela = tk.Tk()
tela.title("Exemplo de Deletar Registro")

# Configurar os elementos da tela
label = tk.Label(tela, text="ID do Registro:")
label.place(x=10, y=10)

entrada = tk.Entry(tela)
entrada.place(x=10, y=30)

botao = tk.Button(tela, text="Deletar", command=deletar)
botao.place(x=10, y=60)

resultado_label = tk.Label(tela, text="")
resultado_label.place(x=10, y=90)

# Iniciar o loop principal da tela
tela.mainloop()
