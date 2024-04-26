from tkinter import *
from tkinter import messagebox
from time import sleep 
import sqlite3 as sql
banco = sql.connect("banco_usuarios.db")
cursor = banco.cursor()

login = {}
usuarios = []
def verifuser():
    nome= userinput.get()
    senha   = senhainput.get()
    cursor.execute(f"SELECT usuario,senha FROM usuarios")
    usuario= cursor.fetchall()
    
    print(usuario)
    
    for x in usuario:
        if x[0] == nome: 
            print("Usuario localizado")
            if x[1] == senha:
                print("Login efetuado com sucesso")
                messagebox.showinfo('usuario',"Login efetuado com sucesso")
                break
            else:
                print("Senha incorreta")
                break
        else:
            print("Usuario não localizado")
        print("Proximo usuario")
    
                

   
    userinput.delete(0,END)
    senhainput.delete(0,END)
    emailinput.delete(0,END)
    cpfinput.delete(0,END)
    numeroinput.delete(0,END)

    
            
    
def cadastro():
    usuario = userinput.get()
    senha = senhainput.get()
    email= emailinput.get()
    cpf = cpfinput.get()   
    numero_telefone= numeroinput.get()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(usuario TEXT,senha TEXT,email TEXT , cpf TEXT ,numero_telefone TEXT)")
    # cursor.execute(f"INSERT INTO usuarios VALUES('{usuario},{senha},{email},{cpf},{numero_telefone}')")
    cursor.execute(f"INSERT INTO usuarios VALUES ('{usuario}','{senha}','{email}',{cpf},{numero_telefone})")
    banco.commit()
    
    
    messagebox.showinfo('Usuario','Usuario cadastrado com sucesso!')
    userinput.delete(0,END)
    senhainput.delete(0,END)
    emailinput.delete(0,END)
    cpfinput.delete(0,END)
    numeroinput.delete(0,END)


def listar():
    print('Atenção , visualização permitida somente para administradores')
    user = str(input('Digite seu usuario de admin:'))
    senha = str(input('Digite sua senha de admin:'))
    if user == 'gabriel123master' and senha == 'senha123':
        # print('\033[32mAcesso liberado\033[m]')
        messagebox.showinfo('Usuario','Acesso liberado[m')
        sleep(3)
        for i in usuarios:
            for c,v in i.items():
                print(f'{c}:{v}')
            print('=-'*15)
    else:
        print('\033[31mUsuario e/ou senha incorreto(s)')
        print('\033[31mPermissão negada\033[m')
        
janela = Tk()
janela.geometry('1000x520+550+300')
janela.title('Tela de Login')
titulolabel = Label(
    master=janela,
    text='Cadastro', 
    font=('System',20)  
)
titulolabel.pack(padx=20,pady=50)

frame_login = Frame(
    master=janela
)
frame_login.pack()

userlabel = Label(
    master=frame_login,
    text='User:'
)
userlabel.grid(column=0,row=0)

userinput = Entry(
    master=frame_login,
    width=20
)
userinput.grid(column=1,row=0)

senhalabel = Label(
    master=frame_login,
    text='Senha'
)
senhalabel.grid(column=0,row=1)

senhainput = Entry(
    master=frame_login,
    width=20,
    show='*'
)
senhainput.grid(column=1,row=1)

emaillabel = Label(
    master=frame_login,
    text='Email:'
    
)
emaillabel.grid(column=0,row=2)

emailinput = Entry(
    master=frame_login,
    width=20
)
emailinput.grid(column=1,row=2)

cpflabel = Label(
    master=frame_login,
    text='CPF:'
)
cpflabel.grid(column=0,row=3)

cpfinput = Entry(
    master=frame_login,
    width=20
)
cpfinput.grid(column=1,row=3)

numerolabel = Label(
    master=frame_login,
    text='numero de telefone:'
    
)
numerolabel.grid(column=0,row=4)

numeroinput = Entry(
    master=frame_login,
    width=20
)
numeroinput.grid(column=1,row=4)




botao = Button(
    master=frame_login,
    text='Entrar',
    command=verifuser
)
botao.grid(column=1,row=8)

cad = Button(
    master=frame_login,
    text='CADASTRAR',
    command=cadastro
)
cad.grid(column=2,row=8)

mostrar = Button(
    master=frame_login,
    text='Listar usuarios',
    command=listar
)
mostrar.grid(column=3,row=8)

janela.mainloop()