from tkinter import *
from tkinter import ttk
from classes import *
import json
import io
import os
import requests
from PIL import ImageTk, Image
import webbrowser

economiaVetor = []
saudeVetor = []
esportesVetor = []

def criarNoticias():
    economia = requests.get('https://newsapi.org/v2/top-headlines?country=br&category=business&apiKey=67c6c15161354ee48a57778d5714b6f0').json()
    esportes = requests.get('https://newsapi.org/v2/top-headlines?country=br&category=sports&apiKey=67c6c15161354ee48a57778d5714b6f0').json()
    saude = requests.get('https://newsapi.org/v2/top-headlines?country=br&category=health&apiKey=67c6c15161354ee48a57778d5714b6f0').json()

    for i in range(20):
        economia = open("noticias/economia.txt", 'r')
        economia = json.load(economia)
        autor = economia['articles'][i]['author']
        conteudo = economia['articles'][i]['description']
        titulo = economia['articles'][i]['title']
        data = economia['articles'][i]['publishedAt']
        assunto = economia['articles'][i]['description']
        url = economia['articles'][i]['url']
        noticia1 = Noticias(titulo, data, assunto, 'economia', conteudo, url, autor)
        economiaVetor.append(noticia1)

        esportes = open("noticias/esportes.txt", 'r')
        esportes = json.load(esportes)
        autor = esportes['articles'][i]['author']
        conteudo = esportes['articles'][i]['description']
        titulo = esportes['articles'][i]['title']
        data = esportes['articles'][i]['publishedAt']
        assunto = esportes['articles'][i]['description']
        url = esportes['articles'][i]['url']
        noticia1 = Noticias(titulo, data, assunto, 'esportes', conteudo, url, autor)
        esportesVetor.append(noticia1)

        saude = open("noticias/saude.txt", 'r')
        saude = json.load(saude)
        autor = saude['articles'][i]['author']
        conteudo = saude['articles'][i]['description']
        titulo = saude['articles'][i]['title']
        data = saude['articles'][i]['publishedAt']
        assunto = saude['articles'][i]['description']
        url = saude['articles'][i]['url']
        noticia1 = Noticias(titulo, data, assunto, 'saude', conteudo, url, autor)
        saudeVetor.append(noticia1)

def config_janela(janela, titulo, resolucao):
    janela.title(titulo)
    janela.configure(background= 'grey')
    janela.geometry(resolucao)
    janela.resizable(False, False)

criarNoticias()

print(economiaVetor[1].get_data())

def menuNoticias(janelaLogin):
    ordemNoticias = []
    
    def sairNoticias():
        janelaMenu.destroy()
        main()
    
    def filtro(event):
        ordemNoticias = []
        if filtros.get() == "Economia":
            adicionarLista("Economia")

        elif filtros.get() == "Saúde":
            adicionarLista("Saúde")

        elif filtros.get() == "Esportes":
            adicionarLista("Esportes")

        elif filtros.get() == "Filtrar":
            adicionarLista(0)

    def adicionarLista(valor):
        if valor == "Economia":
            lista.delete(0,END)
            for noticias in economiaVetor:
                ordemNoticias.append(noticias)
                lista.insert(END, noticias.get_titulo())

        if valor == "Esportes":
            lista.delete(0,END)
            for noticias in esportesVetor:
                ordemNoticias.append(noticias)
                lista.insert(END, noticias.get_titulo())

        if valor == "Saúde":
            lista.delete(0,END)
            for noticias in saudeVetor:
                ordemNoticias.append(noticias)
                lista.insert(END, noticias.get_titulo())

        if valor == 0:
            lista.delete(0,END)
            for noticias in economiaVetor:
                ordemNoticias.append(noticias)
                lista.insert(END, noticias.get_titulo())
            for noticias in esportesVetor:
                ordemNoticias.append(noticias)
                lista.insert(END, noticias.get_titulo())
            for noticias in saudeVetor:
                ordemNoticias.append(noticias)
                lista.insert(END, noticias.get_titulo())
    
    def openURL():
        index = lista.curselection()
        webbrowser.open(ordemNoticias[index[0]].get_url())

    def listaSelecionada():
        selecionar = lista.curselection()
        index = selecionar[0]
        if selecionar:
            noticiaTexto.configure(state='normal')
            noticiaTexto.delete('1.0', END)
            noticiaTexto.insert(END, ordemNoticias[index].get_conteudo())
            noticiaTexto.configure(state='disabled')
            labelTitulo = Label(janelaMenu, text = ordemNoticias[index].get_titulo())
            labelData = Label(janelaMenu, text = 'Data: ' + ordemNoticias[index].get_data())

            if ordemNoticias[index].get_autor() != None:
                labelAutor = Label(janelaMenu, text ='Autor(a): ' + ordemNoticias[index].get_autor())
        
            else:
                labelAutor = Label(janelaMenu, text ='Autor desconhecido')

            labelTitulo.place(x=100, y=250, height=50, width=800)
            labelAutor.place(x=300, y=380, height=30, width=200)
            labelData.place(x=555, y=380, height=30, width=150)

    def print_callback(event):
        listaSelecionada()

    janelaLogin.destroy()
    janelaMenu = Tk()
    config_janela(janelaMenu, 'Central de noticias', '1000x1000')
    image1 = Image.open("news.jpg")
    img = ImageTk.PhotoImage(image1)
    label02 = Label(janelaMenu,image=img, width=1000, height=1000)
    label02.place(x = 0, y = 0, width=1000, height=1000)
    label03 = Label(janelaMenu, text= 'Selecione uma notícia: ')
    label03.place(x= 100, y = 720, width=150, height=30) 
    label02.place(x = 0, y = 0, width=1000, height=1000)
    opcoes1 = ["Economia", "Saúde", "Esportes"]
    opcoes2 = ["Mais recente", "Menos recente"]
    filtros = ttk.Combobox(janelaMenu, values= opcoes1)
    filtros.set("Filtrar")
    filtros.place(x= 25, y=750, width= 70)
    scroll_bar = Scrollbar(janelaMenu)
    scroll_bar.place( x=900, y=750, height = 200)
    fonte = 1
    noticiaTexto = Text(janelaMenu, bg='white',height = 10, width = 50)
    noticiaTexto.configure(state='disabled')

    lerMais = Button(text= "Ler mais", command =openURL)
    lerMais.config(bg = 'white')
    lerMais.place(x=425, y=600,height = 30, width = 150)

    sair = Button(text= "Sair", command =sairNoticias)
    sair.config(bg = 'white')
    sair.place(x=425, y=640,height = 30, width = 150)

    noticiaTexto.place(x=300, y=430)
    lista = Listbox(janelaMenu, yscrollcommand = scroll_bar.set, font=("Helvetica", 10), selectmode="SINGLE")
    lista.place(x=100, y=750, height = 200, width = 800)
    scroll_bar.config(command = lista.yview())
    lista.bind("<<ListboxSelect>>", print_callback)
    filtros.bind("<<ComboboxSelected>>", filtro)
    adicionarLista(0)
    janelaMenu.mainloop()


def main():
    caminho = r'C:\Users\zackb\OneDrive\Área de Trabalho\Prova II\dados_login'
    arquivos = os.listdir(caminho)

    def sairLogin():
        janelaLogin.destroy()

    def entrarLogin():
        nome = user.get() + '.txt'
        for arquivo in arquivos:
            if nome == arquivo:
                login = open("dados_login/" + nome, 'r')
                senhaLogin = json.load(login)
                login.close()

                if senha.get() == senhaLogin:
                    invalid = Label(janelaLogin, text='') 
                    invalid.config(bg= 'white')
                    invalid.place(x=125, y=275,height = 30, width = 150)
                    menuNoticias(janelaLogin)
                else:
                    invalid = Label(janelaLogin, text='Senha inválida!') 
                    invalid.config(bg= 'white')
                    invalid.place(x=125, y=275,height = 30, width = 150)

        if nome not in arquivos:
            invalid = Label(janelaLogin, text='Usuário não cadastrado!')
            invalid.config(bg= 'white')
            invalid.place(x=125, y=275,height = 30, width = 150)

    def cadastroUsuario():
        def sairCadastro():
            janelaCadastro.destroy()
            main()

        def cadastro():
            caminho = r'C:\Users\zackb\OneDrive\Área de Trabalho\Prova II\dados_login'
            arquivos =  os.listdir(caminho)
            nome = user.get() + '.txt'

            def salvarLogin():
                userJ = user.get() 
                senhaJ = senha.get()

                criarArquivo = open(f'dados_login\{userJ}.txt', 'x')
                criarArquivo.close()
                
                arquivo = open(f'dados_login\{userJ}.txt', 'w')
                json.dump(senhaJ, arquivo)
                arquivo.close()

            if user.get() == "":
                userInv = Label(janelaCadastro, text='Usuário inválido!')   
                userInv.place(x=340, y=110, height = 30, width = 200)
                cadSucess = Label(janelaCadastro, text='')
                senhaInv = Label(janelaCadastro, text='')
                senhaInv.config(bg= 'lightblue') 
                cadSucess.config(bg= 'lightblue') 
                senhaInv.place(x=340, y=210, height = 30, width = 210)
                cadSucess.place(x=225, y=260, height = 30, width = 150)

            if nome in arquivos:
                userInv = Label(janelaCadastro, text='Usuário indisponível! Tente novamente.')   
                userInv.place(x=340, y=110, height = 30, width = 210)
                cadSucess = Label(janelaCadastro, text='')
                cadSucess.config(bg= 'lightblue') 
                cadSucess.place(x=225, y=260, height = 30, width = 150)
            
            elif nome not in arquivos and user.get() != "":
                userInv = Label(janelaCadastro, text='')
                userInv.config(bg= 'lightblue') 
                userInv.place(x=340, y=110, height = 30, width = 210)          

            if senha.get() == "" and nome not in arquivos and user.get() != "":
                senhaInv = Label(janelaCadastro, text='Senha inválida!')   
                senhaInv.place(x=340, y=210, height = 30, width = 210)
                cadSucess = Label(janelaCadastro, text='')
                cadSucess.config(bg= 'lightblue') 
                cadSucess.place(x=225, y=260, height = 30, width = 150)

            if senha2.get() != senha.get() and nome not in arquivos and user.get() != "":
                senhaInv = Label(janelaCadastro, text='As senhas não coincidem!')   
                senhaInv.place(x=340, y=210, height = 30, width = 210)
                cadSucess = Label(janelaCadastro, text='')
                cadSucess.config(bg= 'lightblue') 
                cadSucess.place(x=225, y=260, height = 30, width = 150)

            elif senha2.get() == senha.get() and nome not in arquivos and user.get() != "" and senha2.get() != "":
                salvarLogin()
                senhaInv = Label(janelaCadastro, text='')
                cadSucess = Label(janelaCadastro, text='Usuário cadastrado!')
                cadSucess.config(bg= 'lightblue') 
                senhaInv.config(bg= 'lightblue') 
                senhaInv.place(x=340, y=210, height = 30, width = 210)
                cadSucess.place(x=225, y=260, height = 30, width = 150)
            
        janelaLogin.destroy()
        janelaCadastro = Tk()
        config_janela(janelaCadastro, 'Cadastro', '580x470')
        janelaCadastro.config(bg = 'lightblue')
        userL = Label(janelaCadastro, text='Usuário:')
        senhaL = Label(janelaCadastro, text='Senha:')
        senhaL2 = Label(janelaCadastro, text='Repita a senha:')

        userL.config(bg = 'lightblue')
        senhaL.config(bg = 'lightblue')
        senhaL2.config(bg = 'lightblue')
        userL.place(x=20, y=110, height = 30, width = 150)
        senhaL.place(x=20, y=160, height = 30, width = 150)
        senhaL2.place(x=20, y=210, height = 30, width = 150)

        user = Entry(janelaCadastro)
        senha = Entry(janelaCadastro)
        senha2 = Entry(janelaCadastro)
        user.place(x=160, y=110, height = 30, width = 150)
        senha.place(x=160, y=160, height = 30, width = 150)
        senha2.place(x=160, y=210, height = 30, width = 150)

        cadastrar = Button(text= "Cadastrar", command =cadastro)
        sair = Button(text= "Sair", command =sairCadastro)
        cadastrar.place(x=225, y=350,height = 30, width = 150)
        sair.place(x=225, y=400,height = 30, width = 150)

    janelaLogin = Tk()
    config_janela(janelaLogin, 'Login', '400x500')

    image1 = Image.open("login.png")
    img = ImageTk.PhotoImage(image1)
    label02 = Label(janelaLogin,image=img)
    label02.place(x = 0, y = 0)

    userL = Label(janelaLogin, text='Usuário')
    senhaL = Label(janelaLogin, text='Senha')


    userL.config(bg = 'white')
    senhaL.config(bg = 'white')
    userL.place(x=125, y=105, height = 30, width = 150)
    senhaL.place(x=125, y=185, height = 30, width = 150)

    user = Entry(janelaLogin)
    senha = Entry(janelaLogin, show="*")
    entrar = Button(text= "Entrar", command =entrarLogin)
    sair = Button(text= "Sair", command =sairLogin)
    cadastrar = Button(text= "Cadastrar novo usuário", command =cadastroUsuario)

    entrar.config(bg = 'white')
    sair.config(bg = 'white')
    cadastrar.config(bg = 'white')

    user.place(x=125, y=140, height = 30, width = 150)
    senha.place(x=125, y=220, height = 30, width = 150)
    entrar.place(x=125, y=330,height = 30, width = 150)
    sair.place(x=125, y=410,height = 30, width = 150)
    cadastrar.place(x=125, y=370,height = 30, width = 150)
    janelaLogin.mainloop()

main()