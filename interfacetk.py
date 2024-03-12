from customtkinter import *#phind ia para retorno de fontes 
from tkinter import messagebox

# from PIL import image 
#PLACEHOLDER_TEXT E AQUELE TEXTO FANTASMA QUE FICA NO CAMPO ANTES DA GENTE DIGITAR 
#pra criar uma nova janela e destruir a anterior podemos usar o destro()
usuario = {}
usuarios = []
def cadastro():
    global inputuser,inputsenha
    try:
        usuario['username'] = inputuser.get()
        usuario['password'] = inputsenha.get()
    except:
        print('Digite valores validos')    
    else:
        messagebox.showinfo('Usuario','Usuario Cadastrado com sucesso!')
        usuarios.append(usuario.copy())
    
    
    
def login():
    global inputuser,inputsenha
    try:
        if inputuser.get() in usuarios and inputsenha.get() in usuarios:
            pass
    except:
        print('Usuario nao cadastrado')
        
def listar():
    for i in usuarios:
        print(usuarios[i])
        
    
#appearenc conf
Font = 'Nirmala UI'
Size_title = 26
DEFAUT_SIZE = 16


set_appearance_mode("dark")#seleciona o tema dark para nossa janela , colocamos 'System' como atributo pegamos o tema da maquina
set_default_color_theme("dark-blue")

#app config
app = CTk()
app.title('Login')
app.geometry('450x450+780+520')
app.resizable(False,False)

# logo_image = image.open('')
# logo_image = CTkImage(logo_image,size=(72,45))

label_title_login = CTkLabel(
    master=app,
    text='Login',
    font=(Font,Size_title)
    
)
label_title_login.place(relx=0.5,rely=0.1)

labeluser = CTkLabel(
    master=app,
    text='Usuario',
)
labeluser.place(relx=0.1,rely=0.2)

# labelimage = CTkLabel(
#     master=app,
#     image=''
# )

inputuser = CTkEntry(
    master=app,
    width=150,
    placeholder_text='usuario123',
    
)
inputuser.place(relx=0.3,rely=0.2)

labelsenha = CTkLabel(
    master=app,
    text='Senha',
    
)
labelsenha.place(relx=0.1,rely=0.3)

inputsenha = CTkEntry(
    master=app,
    width=150,
    placeholder_text='senha',
    show='*'
)
inputsenha.place(relx=0.3,rely=0.3)


Botao_login = CTkButton(
    master=app,
    text='Login',
    command=login
)
Botao_login.place(relx=0.3,rely=0.5)

Botao_cadastrar = CTkButton(
    master=app,
    text='Cadastrar',
    command=cadastro
)
Botao_cadastrar.place(relx=0.3,rely=0.6)

Botao_listar = CTkButton(
    master=app,
    text='Listar',
    command=listar
)
Botao_listar.place(relx=0.3,rely=0.7)

app.mainloop()