from tkinter import *
from tkinter import messagebox
from time import sleep 
login = {}
usuarios = []
def verifuser():
    login['usuario'] = userinput.get()
    login['senha']   = senhainput.get()
    for i in usuarios:
        if i['usuario'] == login['usuario']:
            if i['senha'] == login['senha']:
                print('\033[32mLogin realizado com sucesso!\033[m')
            else:
                print('\033[31msenha incorreta\033[m')
        else:
            print('usuario não cadastrado')
    userinput.delete(0,END)
    senhainput.delete(0,END)
    emailinput.delete(0,END)
    cpfinput.delete(0,END)
    numeroinput.delete(0,END)
            
    
def cadastro():
    login['usuario'] = userinput.get()
    login['senha'] = senhainput.get()
    login['email'] = emailinput.get()
    login['cpf'] = cpfinput.get()
    try:
        while len(login['cpf']) != 11:
            print('Atenção digite um valor valido para o seu cpf:')
            login['cpf'] = cpfinput.get()
    except(ValueError,TypeError):
        print('Erro de tipo: digite um valor valido ')
    login['numero de telefone'] = numeroinput.get()
    usuarios.append(login.copy())
    # print('Usuario cadastrado com sucesso!')
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