import tkinter as tk
import mysql.connector
from tkinter import messagebox
import bcrypt
import re

def validar_email(email):
    # Padrão de regex para validar email
    padrao = r'^\S+@\S+.\S+$'
    return re.match(padrao, email) is not None



def cadastrar_usuario():

    email = email_entry.get()
    senha = senha_entry.get()


    if not validar_email(email):
        messagebox.showerror("Erro", "Email inválido!")
        return

    hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    conexao = mysql.connector.connect(
        host="localhost",
        user="root", 
        password="",
        database="bancodogolfinho"
    )

    cursor = conexao.cursor()


    inserir_sql = "INSERT INTO usuario (email, senha) VALUES (%s, %s)"
    valores = (email, hashed_senha)

    try:
        cursor.execute(inserir_sql, valores)
        conexao.commit()


        email_entry.delete(0, 'end')
        senha_entry.delete(0, 'end')


        messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")

    except mysql.connector.Error as err:

        messagebox.showerror("Erro", f"Erro ao cadastrar: {err}")

    finally:
        conexao.close()



root = tk.Tk()
root.title('Golfinho')
root.geometry('219x190+830+255')


email_label = tk.Label(root, text="Email:", pady=10)
email_entry = tk.Entry(root)


senha_label = tk.Label(root, text="Senha:", pady=10)
senha_entry = tk.Entry(root, show="*")


cadastro_button = tk.Button(root, text="Cadastrar", command=cadastrar_usuario, pady=10)


email_label.pack()
email_entry.pack()
senha_label.pack()
senha_entry.pack()
cadastro_button.pack()


root.mainloop()