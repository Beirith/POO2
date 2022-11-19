from tkinter import *
from produtos import Produtos

def config_janela(janela):
    janela.title("Supermercado")
    janela.configure(background= 'lightblue')
    janela.geometry("750x550")
    janela.resizable(False, False)

preco =[0]
produtos = []
carrinho = []
codigos = []

def menu_inicial():
    def funcionarioF():
        def visualizarProduto():
            def voltarVisualizar():
                janelaVisualizar.destroy()
                funcionarioF()

            def scroll_command(*args):
                codigosL.yview(*args)
                tiposL.yview(*args)
                marcasL.yview(*args)
                precosL.yview(*args)
                quantidadesL.yview(*args)

            janelaFuncionario.destroy()
            janelaVisualizar = Tk()
            config_janela(janelaVisualizar)
            label_codigo = Label(janelaVisualizar, text='CATÁLOGO')
            label_codigo.config(bg= 'lightblue')
            label_codigo.place(x=275, y=0, height = 30, width = 200)
            codigoT = Label(janelaVisualizar, text='Código')
            tipoT = Label(janelaVisualizar, text='Tipo')
            marcaT = Label(janelaVisualizar, text='Marca')
            precoT = Label(janelaVisualizar, text='Preço')
            quantidadeT = Label(janelaVisualizar, text='Quantidade')
            codigoT.place(x=100, y=90, height = 30, width = 100)
            tipoT.place(x=210, y=90, height = 30, width = 100)
            marcaT.place(x=320, y=90, height = 30, width = 100)
            precoT.place(x=430, y=90, height = 30, width = 100)
            quantidadeT.place(x=540, y=90, height = 30, width = 100)
            voltar = Button(text= "Voltar", command =voltarVisualizar)
            voltar.place(x=275, y=485,height = 30, width = 200)
            
            scroll_bar = Scrollbar(janelaVisualizar)
            scroll_bar.pack( side = RIGHT, fill = Y )

            codigosL = Listbox(janelaVisualizar, yscrollcommand = scroll_bar.set, font=("Helvetica", 10))
            codigosL.place(x=100, y=125, height = 350, width = 100)

            tiposL = Listbox(janelaVisualizar, yscrollcommand = scroll_bar.set, font=("Helvetica", 10) )
            tiposL.place(x=210, y=125, height = 350, width = 100)

            marcasL = Listbox(janelaVisualizar, yscrollcommand = scroll_bar.set, font=("Helvetica", 10) )
            marcasL.place(x=320, y=125, height = 350, width = 100)

            precosL = Listbox(janelaVisualizar, yscrollcommand = scroll_bar.set, font=("Helvetica", 10) )
            precosL.place(x=430, y=125, height = 350, width = 100)

            quantidadesL = Listbox(janelaVisualizar, yscrollcommand = scroll_bar.set, font=("Helvetica", 10) )
            quantidadesL.place(x=540, y=125, height = 350, width = 100)

            scroll_bar.config( command = scroll_command)
                    
            for i in range(len(produtos)):
                codigo = produtos[i].get_codigo()
                tipo = produtos[i].get_tipo()
                marca = produtos[i].get_marca()
                preco = produtos[i].get_preco()
                quantidade = produtos[i].get_quantidade()
                codigosL.insert(END, str(codigo))
                tiposL.insert(END, str(tipo))
                marcasL.insert(END, str(marca))
                precosL.insert(END, str(preco))
                quantidadesL.insert(END, str(quantidade))

        def atualizarF():
            def voltarAtualizar():
                janelaAtualizar.destroy()
                funcionarioF()

            def atualizarProduto():
                if codigoE.get() in codigos:
                    atualizarProduto2(codigoE.get())
                else:
                    label0 = Label(janelaAtualizar, text='Código não cadastrado. Digite um código válido')
                    label0.place(x=200, y=150, height = 30, width = 350)

            def atualizarProduto2(codigoE):
                def voltarAtualizar2():
                    janelaAtualizar2.destroy()
                    funcionarioF()

                def checkValidAtt():
                    for i in range(len(produtos)):
                        if codigoE == produtos[i].get_codigo():
                            if codigo.get() in codigos:      
                                label0 = Label(janelaAtualizar2, text='Código já cadastrado. Digite outro código')
                                label0.place(x=440, y=125, height = 30, width = 250)
                            if codigo.get() == "":
                                label1 = Label(janelaAtualizar2, text='')
                                label1.config(bg='lightblue')
                                label1.place(x=440, y=125, height = 30, width = 250)
                            if codigo.get() not in codigos and codigo.get() != "":
                                label0 = Label(janelaAtualizar2, text='Código alterado com sucesso')
                                label0.place(x=440, y=125, height = 30, width = 250)
                                codigos.remove(produto.get_codigo())
                                produtos[i].set_codigo(codigo.get())
                                codigos.append(codigo.get())
                            if tipo.get() != "":
                                label1 = Label(janelaAtualizar2, text='Tipo alterado com sucesso')
                                produtos[i].set_tipo(tipo.get())
                                label1.place(x=440, y=175, height = 30, width = 250)
                            else:
                                label1 = Label(janelaAtualizar2, text='')
                                label1.place(x=440, y=175, height = 30, width = 250)
                                label1.config(bg='lightblue')
                            if marca.get() != "":
                                label2 = Label(janelaAtualizar2, text='Marca alterada com sucesso')
                                produtos[i].set_marca(marca.get())
                                label2.place(x=440, y=225, height = 30, width = 250)
                            else:
                                label2 = Label(janelaAtualizar2, text='')
                                label2.place(x=440, y=225, height = 30, width = 250)
                                label2.config(bg='lightblue')
                            if quantidade.get() != "":
                                label3 = Label(janelaAtualizar2, text='Quantidade alterada com sucesso')
                                produtos[i].set_quantidade(int(quantidade.get()))
                                label3.place(x=440, y=275, height = 30, width = 250)
                            else:
                                label3 = Label(janelaAtualizar2, text='')
                                label3.place(x=440, y=275, height = 30, width = 250)
                                label3.config(bg='lightblue')
                            if  preco.get() != "":
                                label4 = Label(janelaAtualizar2, text='Preço alterado com sucesso')
                                label4.place(x=440, y=325, height = 30, width = 250)
                                produtos[i].set_preco(float(preco.get()))
                            else:
                                label3 = Label(janelaAtualizar2, text='')
                                label3.place(x=440, y=325, height = 30, width = 250)
                                label3.config(bg='lightblue')

                janelaAtualizar.destroy()
                janelaAtualizar2 = Tk()
                config_janela(janelaAtualizar2)
                for produto in produtos:
                    if produto.get_codigo() == codigoE:
                        codigo = Entry(janelaAtualizar2)
                        tipo = Entry(janelaAtualizar2)
                        marca = Entry(janelaAtualizar2)
                        quantidade = Entry(janelaAtualizar2)
                        preco = Entry(janelaAtualizar2)
                        label1 = Label(janelaAtualizar2, text='Novo código')
                        label2 = Label(janelaAtualizar2, text='Novo tipo')
                        label3 = Label(janelaAtualizar2, text='Nova marca')
                        label4 = Label(janelaAtualizar2, text='Nova quantidade')
                        label5 = Label(janelaAtualizar2, text='Novo preço')
                        label1.place(x=155, y=125, height = 30, width = 150)
                        label2.place(x=155, y=175, height = 30, width = 150)
                        label3.place(x=155, y=225, height = 30, width = 150)
                        label4.place(x=155, y=275, height = 30, width = 150)
                        label5.place(x=155, y=325, height = 30, width = 150)
                        label_codigo = Label(janelaAtualizar2, text='ALTERAÇÃO DE PRODUTO')
                        codigo.place(x=325, y=125,height = 30, width = 100)
                        tipo.place(x=325, y=175,height = 30, width = 100)
                        marca.place(x=325, y=225,height = 30, width = 100)
                        quantidade.place(x=325, y=275,height = 30, width = 100)
                        preco.place(x=325, y=325,height = 30, width = 100)
                        label_codigo.place(x=275, y=0, height = 30, width = 200)
                        atualizar = Button(text= "Alterar", command =checkValidAtt)
                        voltar = Button(text= "Voltar", command =voltarAtualizar2)
                        atualizar.place(x=325, y=375,height = 30, width = 100)
                        voltar.place(x=325, y=425,height = 30, width = 100)

            janelaFuncionario.destroy()
            janelaAtualizar = Tk()
            config_janela(janelaAtualizar)
            codigoE = Entry(janelaAtualizar)
            label = Label(janelaAtualizar, text='Digite o código do produto a ser alterado')
            label.place(x=200, y=100, height = 30, width = 350)
            codigoE.place(x=325, y=200,height = 30, width = 100)
            removerB = Button(text= "Selecionar", command =atualizarProduto)
            voltar = Button(text= "Voltar", command =voltarAtualizar)
            voltar.place(x=275, y=300,height = 30, width = 200)
            removerB.place(x=275, y=250,height = 30, width = 200)

        def removerF():
            def removerProduto():
                if codigo.get() in codigos:
                    codigos.remove(codigo.get())
                    for i in range(len(produtos)):
                        if codigo.get() == produtos[i].get_codigo():
                            label0 = Label(janelaRemover, text='')
                            label0.place(x=200, y=150, height = 30, width = 350)
                            label0.config(bg = 'lightblue')
                            produtos.remove(produtos[i])
                            labelR = Label(janelaRemover, text='Produto removido com sucesso!')
                            labelR.place(x=200, y=350, height = 30, width = 350)
                else:
                    label0 = Label(janelaRemover, text='Código não cadastrado. Digite um código válido')
                    label0.place(x=200, y=150, height = 30, width = 350)
                    labelR = Label(janelaRemover, text='')
                    labelR.place(x=200, y=350, height = 30, width = 350)
                    labelR.config(bg= 'lightblue')
        
            def voltarRemover():
                janelaRemover.destroy()
                funcionarioF()
            
            janelaFuncionario.destroy()
            janelaRemover = Tk()
            config_janela(janelaRemover)
            codigo = Entry(janelaRemover)
            label = Label(janelaRemover, text='Digite o código do produto a ser removido')
            label.place(x=200, y=100, height = 30, width = 350)
            codigo.place(x=325, y=200,height = 30, width = 100)
            label_codigo = Label(janelaRemover, text='REMOVER PRODUTO')
            label_codigo.place(x=300, y=0, height = 30, width = 150)
            removerB = Button(text= "Remover", command =removerProduto)
            voltar = Button(text= "Voltar", command =voltarRemover)
            voltar.place(x=275, y=300,height = 30, width = 200)
            removerB.place(x=275, y=250,height = 30, width = 200)

        def voltarFuncionario():
            janelaFuncionario.destroy()
            menu_inicial()

        def cadastroF():         
            def voltarCadastro():
                janelaCadastro.destroy()
                funcionarioF()

            def checkValid():
                if codigo.get() in codigos:
                    label0 = Label(janelaCadastro, text='Código já cadastrado. Digite outro código')
                    label0.place(x=440, y=125, height = 30, width = 250)
                    cod = False
                if codigo.get() == "":
                    label1 = Label(janelaCadastro, text='Digite um código válido')
                    label1.place(x=440, y=125, height = 30, width = 250)
                    cod = False
                elif codigo.get() != "" and codigo.get() not in codigos:
                    label1 = Label(janelaCadastro, text='')
                    label1.place(x=440, y=125, height = 30, width = 250)
                    label1.config(bg= 'lightblue')
                    cod = True
                if tipo.get() == "":
                    label2 = Label(janelaCadastro, text='Digite um tipo válido')
                    label2.place(x=440, y=175, height = 30, width = 250)
                    typ = False
                else:
                    label2 = Label(janelaCadastro, text='')
                    label2.place(x=440, y=175, height = 30, width = 250)
                    label2.config(bg= 'lightblue')
                    typ = True
                if marca.get() == "":
                    label3 = Label(janelaCadastro, text='Digite uma marca válida')
                    label3.place(x=440, y=225, height = 30, width = 250)
                    mar = False
                else:
                    label3 = Label(janelaCadastro, text='')
                    label3.place(x=440, y=225, height = 30, width = 250)
                    label3.config(bg= 'lightblue')
                    mar = True
                if quantidade.get() == "":
                    label4 = Label(janelaCadastro, text='Digite uma quantidade válida')
                    label4.place(x=440, y=275, height = 30, width = 250)
                    qua = False
                else:
                    label4 = Label(janelaCadastro, text='')
                    label4.place(x=440, y=275, height = 30, width = 250)
                    label4.config(bg= 'lightblue')
                    qua = True
                if preco.get() == "":
                    label5 = Label(janelaCadastro, text='Digite um preço válido')
                    label5.place(x=440, y=325, height = 30, width = 250)
                    pre = False
                else:
                    label5 = Label(janelaCadastro, text='')
                    label5.place(x=440, y=325, height = 30, width = 250)
                    label5.config(bg= 'lightblue')
                    pre = True
                if cod == False or typ == False or mar == False or qua == False or pre == False:
                    label6 = Label(janelaCadastro, text='')
                    label6.place(x=440, y=375, height = 30, width = 250)
                    label6.config(bg='lightblue')
                elif cod == True and typ == True and mar == True and qua == True and pre == True:
                    produto1 = Produtos('','','','','')
                    produto1.set_codigo(codigo.get())
                    produto1.set_tipo(tipo.get())
                    produto1.set_marca(marca.get())
                    produto1.set_preco(preco.get())
                    produto1.set_quantidade(quantidade.get())
                    codigos.append(codigo.get())
                    produtos.append(produto1)
                    label6 = Label(janelaCadastro, text='Produto cadastrado com sucesso!')
                    label6.place(x=440, y=375, height = 30, width = 250)

            janelaFuncionario.destroy()
            janelaCadastro = Tk()
            config_janela(janelaCadastro)
            codigo = Entry(janelaCadastro)
            tipo = Entry(janelaCadastro)
            marca = Entry(janelaCadastro)
            quantidade = Entry(janelaCadastro)
            preco = Entry(janelaCadastro)
            label1 = Label(janelaCadastro, text='Código')
            label2 = Label(janelaCadastro, text='Tipo')
            label3 = Label(janelaCadastro, text='Marca')
            label4 = Label(janelaCadastro, text='Quantidade')
            label5 = Label(janelaCadastro, text='Preço')
            label1.place(x=155, y=125, height = 30, width = 150)
            label2.place(x=155, y=175, height = 30, width = 150)
            label3.place(x=155, y=225, height = 30, width = 150)
            label4.place(x=155, y=275, height = 30, width = 150)
            label5.place(x=155, y=325, height = 30, width = 150)
            label_codigo = Label(janelaCadastro, text='CADASTRO DE PRODUTO')
            codigo.place(x=325, y=125,height = 30, width = 100)
            tipo.place(x=325, y=175,height = 30, width = 100)
            marca.place(x=325, y=225,height = 30, width = 100)
            quantidade.place(x=325, y=275,height = 30, width = 100)
            preco.place(x=325, y=325,height = 30, width = 100)
            label_codigo.place(x=300, y=0, height = 30, width = 150)
            cadastrar = Button(text= "Cadastrar", command =checkValid)
            voltar = Button(text= "Voltar", command =voltarCadastro)
            cadastrar.place(x=325, y=375,height = 30, width = 100)
            voltar.place(x=325, y=425,height = 30, width = 100)

        janelaFuncionario = Tk()
        config_janela(janelaFuncionario)
        cadastro = Button(text= "Cadastrar um produto", command =cadastroF)
        remover = Button(text= "Remover um produto", command =removerF)
        alterar = Button(text= "Alterar informações de um produto", command =atualizarF)
        visualizar = Button(text= "Visualizar catálogo", command =visualizarProduto)
        voltar = Button(text= "Voltar", command =voltarFuncionario)
        cadastro.place(x=275, y=125,height = 30, width = 200)
        remover.place(x=275, y=175,height = 30, width = 200)
        alterar.place(x=275, y=225,height = 30, width = 200)
        visualizar.place(x=275, y=275,height = 30, width = 200)
        voltar.place(x=275, y=325,height = 30, width = 200)

    def senha():
        def voltar():
            janelaSenha.destroy()
            menu_inicial()

        def senhaCorreta():
            senhas = ['123']
            if senha1.get() in senhas:
                janelaSenha.destroy()
                funcionarioF()
            else:
                label0 = Label(janelaSenha, text='Senha incorreta. Tente novamente')
                label0.place(x=275, y=200, height = 30, width = 200)

        janela.destroy()
        janelaSenha =  Tk()
        config_janela(janelaSenha)
        label = Label(janelaSenha, text='Digite sua senha')
        label.place(x=300, y=150, height = 30, width = 150)
        senha1 = Entry(janelaSenha,show='*')
        senha1.place(x=300, y=250, height = 30, width = 150)
        entrar = Button(text= "Entrar", command =senhaCorreta)
        entrar.place(x=325, y=300,height = 30, width = 100)
        voltar = Button(text= "Voltar", command =voltar)
        voltar.place(x=300, y=350, height = 30, width = 150)

    def clienteF():
        def realizarCompras():
            def adicionarCarrinho():
                if codigosAA.get() in codigos:
                    erro = Label(janelaCompras, text='')
                    erro.config(bg='lightblue')
                    erro.place(x=420, y=80, height = 30, width = 280)

                    for i in range(len(produtos)):
                        if produtos[i].get_codigo() == codigosAA.get():
                            if int(quantidade.get()) > int(produtos[i].get_quantidade()):
                                erro1 = Label(janelaCompras, text='Quantidade desejada indisponível. Há '+str(produtos[i].get_quantidade())+' itens em estoque.')
                                erro1.place(x=165, y=180, height = 30, width = 400)

                            elif int(quantidade.get()) <= int(produtos[i].get_quantidade()) and quantidade.get() != '':
                                preco[0] = preco[0] + (float(produtos[i].get_preco()) * int(quantidade.get()))
                                quantidade_autal = int(produtos[i].get_quantidade()) - int(quantidade.get())
                                produtos[i].set_quantidade(quantidade_autal)
                                erro1 = Label(janelaCompras, text='Produto adicionado ao carrinho!')
                                erro1.place(x=165, y=180, height = 30, width = 400)

                                erro1 = Label(janelaCompras, text='Preço total: R$ '+ str(preco[0]))
                                erro1.place(x=165, y=220, height = 30, width = 400)

                            if quantidade.get() == '':
                                erro1 = Label(janelaCompras, text='Digite uma quantidade válida.')
                                erro1.place(x=165, y=180, height = 30, width = 400)

                else:
                    erro = Label(janelaCompras, text='Código não cadastrado. Digite um código válido.')
                    erro.place(x=420, y=80, height = 30, width = 280)
                    erro1 = Label(janelaCompras, text='')
                    erro1.config(bg='lightblue')
                    erro1.place(x=165, y=180, height = 30, width = 400)
                
            def voltarCompras():
                janelaCompras.destroy()
                janelaVisualizar.destroy()
                menu_inicial()
                
            def catalogo():
                def fecharCatalogo():
                    janelaVisualizar.destroy()

                def scroll_command(*args):
                    codigosL.yview(*args)
                    tiposL.yview(*args)
                    marcasL.yview(*args)
                    precosL.yview(*args)
                    quantidadesL.yview(*args)

                label_codigo = Label(janelaVisualizar, text='CATÁLOGO')
                label_codigo.config(bg= 'lightblue')
                label_codigo.place(x=275, y=0, height = 30, width = 200)
                codigoT = Label(janelaVisualizar, text='Código')
                tipoT = Label(janelaVisualizar, text='Tipo')
                marcaT = Label(janelaVisualizar, text='Marca')
                precoT = Label(janelaVisualizar, text='Preço')
                quantidadeT = Label(janelaVisualizar, text='Quantidade')
                codigoT.place(x=100, y=90, height = 30, width = 100)
                tipoT.place(x=210, y=90, height = 30, width = 100)
                marcaT.place(x=320, y=90, height = 30, width = 100)
                precoT.place(x=430, y=90, height = 30, width = 100)
                quantidadeT.place(x=540, y=90, height = 30, width = 100)
                voltar = Button(janelaVisualizar,text= "Fechar", command =fecharCatalogo)
                voltar.place(x=275, y=485,height = 30, width = 200)
                scroll_bar = Scrollbar(janelaVisualizar)
                scroll_bar.pack( side = RIGHT, fill = Y )
                codigosL = Listbox(janelaVisualizar, yscrollcommand = scroll_bar.set, font=("Helvetica", 10))
                codigosL.place(x=100, y=125, height = 350, width = 100)
                tiposL = Listbox(janelaVisualizar, yscrollcommand = scroll_bar.set, font=("Helvetica", 10) )
                tiposL.place(x=210, y=125, height = 350, width = 100)
                marcasL = Listbox(janelaVisualizar, yscrollcommand = scroll_bar.set, font=("Helvetica", 10) )
                marcasL.place(x=320, y=125, height = 350, width = 100)
                precosL = Listbox(janelaVisualizar, yscrollcommand = scroll_bar.set, font=("Helvetica", 10) )
                precosL.place(x=430, y=125, height = 350, width = 100)
                quantidadesL = Listbox(janelaVisualizar, yscrollcommand = scroll_bar.set, font=("Helvetica", 10) )
                quantidadesL.place(x=540, y=125, height = 350, width = 100)
                scroll_bar.config( command = scroll_command)
                        
                for i in range(len(produtos)):
                    codigo = produtos[i].get_codigo()
                    tipo = produtos[i].get_tipo()
                    marca = produtos[i].get_marca()
                    preco = produtos[i].get_preco()
                    quantidade = produtos[i].get_quantidade()
                    codigosL.insert(END, str(codigo))
                    tiposL.insert(END, str(tipo))
                    marcasL.insert(END, str(marca))
                    precosL.insert(END, str(preco))
                    quantidadesL.insert(END, str(quantidade))

            janelaCliente.destroy()
            janelaCompras =  Tk()
            config_janela(janelaCompras)
            janelaVisualizar = Tk()
            config_janela(janelaVisualizar)
            catalogo()
            voltar = Button(janelaCompras,text= "Voltar", command =voltarCompras)
            voltar.place(x=275, y=485,height = 30, width = 200)
            digite = Label(janelaCompras, text='Digite o código do produto desejado')
            digite.place(x=100, y=80, height = 30, width = 200)
            digite2 = Label(janelaCompras, text='Digite a quantidade desejada')
            digite2.place(x=100, y=130, height = 30, width = 200)
            quantidade = Entry(janelaCompras)
            codigosAA = Entry(janelaCompras)
            quantidade.place(x=310, y=130,height = 30, width = 100)
            codigosAA.place(x=310, y=80,height = 30, width = 100)
            adicionar = Button(janelaCompras, text= "Adicionar ao carrinho", command =adicionarCarrinho)
            adicionar.place(x=275, y=260,height = 30, width = 200)

        def voltarCliente():
            janelaCliente.destroy()
            menu_inicial()

        janela.destroy()
        janelaCliente = Tk()
        config_janela(janelaCliente)
        compras = Button(text= "Realizar compras", command =realizarCompras)
        voltar = Button(text= "Voltar", command =voltarCliente)
        compras.place(x=300, y=180,height = 30, width = 150)
        voltar.place(x=300, y=250, height = 30, width = 150)

    def sairF():
        janela.destroy()

    janela = Tk()
    config_janela(janela)
    funcionarios = Button(text= "Entrar como funcionário", command =senha)
    clientes = Button(text= "Entrar como cliente", command =clienteF)
    sair = Button(text= "Sair", command =sairF)
    funcionarios.place(x=300, y=180,height = 30, width = 150)
    clientes.place(x=300, y=250, height = 30, width = 150)
    sair.place(x=325, y=320,height = 30, width = 100)
    label_codigo = Label(janela, text='MENU INICIAL')
    label_codigo.config(bg = 'lightblue')
    label_codigo.place(x=300, y=0, height = 30, width = 150)
    janela.mainloop()

menu_inicial()

# =======================================================================================================================================================================================

def Main_App():
    produtos = []
    carrinho = []
    codigos = []

    op1 = True

    while True:
        print()
        print('------------------- MENU -------------------')
        print()
        print('1 - Entrar como funcionário.')
        print('2 - Entrar como cliente.')
        print('0 - Sair.')
        print()
        print('--------------------------------------------')

        valid_op = ['0', '1', '2']

        if op1 == True:
            op = input('Selecione uma operação: ')

        if op1 == False:
            op = input('Operação inválida. Tente novamente: ')

        if op not in valid_op:
            op1 = False
            print()

        elif op == '0':
            break

        if op == '1':
            op1 = True
            op2 = True
            while True:
                senha = ['123']
                print()
                print('Digite "0000" para sair')
                if op2 == True:
                    op = input('Digite sua senha: ')
                    print()
                else:
                    op = input('Senha inválida. Tente novamente: ')
                    print()

                if op in senha:
                    break

                elif op not in senha:
                    op2 = False

                if op == '0000':
                    break

            op2 = True
            if op in senha:
                while True:
                    valid_op = ['0', '1', '2', '3', '4']
                    print('------------------- MENU -------------------')
                    print()
                    print('1 - Cadastrar um produto.')
                    print('2 - Remover um produto.')
                    print('3 - Alterar as informações de um produto.')
                    print('4 - Visualizar catálogo.')
                    print('0 - Voltar.')
                    print()
                    print('--------------------------------------------')

                    if op1 == True:
                        op = input('Selecione uma operação: ')

                    if op1 == False:
                        op = input('Operação inválida. Tente novamente: ')

                    if op not in valid_op:
                        op1 = False

                    if op == '0':
                        break
                    
                    if op == '1':
                        print('------------ CADASTRO DE PRODUTO -----------')
                        print()
                        op1 = True
                        while True:
                            if op1 == True:
                                print()
                                print('Digite "0000" para voltar')
                                print()
                                codigo = int(input('Digite o código do produto: '))
                            
                            else:
                                print()
                                print('Digite "0000" para voltar')
                                print()
                                codigo = int(input('Código já cadastrado. Digite outro código: '))

                            if codigo == 0000:
                                break

                            if codigo in codigos:
                                op1 = False
                                
                            if codigo not in codigos:
                                break

                        if codigo == 0000:
                            break

                        op1 = True           
                        codigos.append(codigo)

                        tipo = input('Informe o tipo de produto: ')
                        marca = input('Informe a marca do produto: ')
                        quantidade = int(input('Informe a quantidade em estoque: '))
                        preco = float(input('Informe o preço unitário: '))

                        produto1 = Produtos('','','','','')
                        produto1.set_codigo(codigo)
                        produto1.set_tipo(tipo)
                        produto1.set_marca(marca)
                        produto1.set_preco(preco)
                        produto1.set_quantidade(quantidade)

                        produtos.append(produto1)

                        print()
                        print('Produto cadastrado com sucesso!')
                        print()
                    
                    if op == '2':
                        op1 = True
                        while True:
                            if op1 == True:
                                print()
                                print('Digite "0000" para voltar')
                                print()
                                op = int(input('Digite o código do produto que será removido: '))
                                print()
                            
                            else:
                                print()
                                print('Digite "0000" para voltar')
                                print()
                                op = int(input('Produto não cadastrado no sistema. Tente novamente: '))
                                print()
                            
                            if op == 0000:
                                break

                            if op not in codigos:
                                op1 = False
                            
                            if op in codigos:
                                codigos.remove(op)
                                break

                        for i in range(len(produtos)):
                            if op == produtos[i].get_codigo():
                                produtos.remove(produtos[i])
                                print()
                                print('Produto removido com sucesso!')
                                print()
                                break
                            
                    if op == '3':
                        op1 = True
                        while True:
                            if op1 == True:
                                cod1 = int(input('Digite o código do produto a ser alterado: '))

                            elif op1 == False:
                                cod1 = int(input('Produto não cadastrado no sistema. Tente novamente: '))

                            if cod1 not in codigos:
                                op1 = False
                            
                            else:
                                codigo_produto = cod1
                                break
                        
                        valid_op = ['0', '1', '2', '3', '4', '5']
                        op1 = True

                        while True:
                            print('--------------- MENU DE ALTERAÇÃO ---------------')
                            print()
                            print('1 - Alterar código')
                            print('2 - Alterar tipo')
                            print('3 - Alterar marca')
                            print('4 - Alterar preço')
                            print('5 - Alterar quantidade')
                            print('0 - Voltar')
                            print()

                            if op1 == True:
                                op = input('Selecione uma operação: ')
                            
                            elif op1 == False:
                                op = input('Operação inválida. Tente novamente: ')
                            
                            if op not in valid_op:
                                op1 = False
                            
                            if op == '0':
                                break

                            if op == '1':
                                op1 = True
                                for i in range(len(produtos)):
                                    if codigo_produto == produtos[i].get_codigo():
                                        
                                        while True:
                                            if op1 == True:
                                                novo_codigo = int(input('Digite o novo código do produto: '))
                                            else:
                                                novo_codigo = int(input('Código já cadastrado. Digite outro código: '))

                                            if novo_codigo in codigos:
                                                op1 = False
                                                
                                            else:
                                                produtos[i].set_codigo(novo_codigo)
                                                codigos.append(novo_codigo)
                                                codigos.remove(codigo_produto)
                                                print()
                                                print('Código alterado com sucesso!')
                                                print()
                                                op1 = True
                                                break
                                            

                            if op == '2':
                                for i in range(len(produtos)):
                                    if codigo_produto == produtos[i].get_codigo():
                                        novo_tipo = input('Digite o novo tipo de produto: ')
                                        produtos[i].set_tipo(novo_tipo)
                                        print()
                                        print('Tipo alterado com sucesso!')
                                        print()
                                break

                            if op == '3':
                                for i in range(len(produtos)):
                                    if codigo_produto == produtos[i].get_codigo():
                                        nova_marca = input('Digite a nova marca do produto: ')
                                        produtos[i].set_marca(nova_marca)
                                        print()
                                        print('Marca alterada com sucesso!')
                                        print()
                                break

                            if op == '4':
                                for i in range(len(produtos)):
                                    if codigo_produto == produtos[i].get_codigo():
                                        novo_preco = float(input('Digite o novo preço do produto: '))
                                        produtos[i].set_preco(novo_preco)
                                        print()
                                        print('Preço alterado com sucesso!')
                                        print()
                                break

                            if op == '5':
                                for i in range(len(produtos)):
                                    if codigo_produto == produtos[i].get_codigo():
                                        nova_quant = int(input('Digite a nova quantidade do produto: '))
                                        produtos[i].set_quantidade(nova_quant)
                                        print()
                                        print('Quantidade alterada com sucesso!')
                                        print()
                                break

                    if op == '4':
                        print('------------------- CATÁLOGO -------------------')
                        print()
                        for i in range(len(produtos)):
                            indice = i + 1
                            codigo1 = produtos[i].get_codigo()
                            tipo1 = produtos[i].get_tipo()
                            marca1 = produtos[i].get_marca()
                            preco1 = produtos[i].get_preco()
                            quantidade1 = produtos[i].get_quantidade()
                            print('%d - Código: %d, Tipo: %s, Marca: %s, Preço: R$ %.2f, Quantidade: %d' % (indice ,codigo1, tipo1, marca1, preco1, quantidade1))
                            print()
                                
        if op == '2':
            valid_op = ['0', '1', '2']
            op1 = True
            while True:
                print('------------------- MENU -------------------')
                print()
                print('1 - Realizar compras.')
                print('0 - Voltar.')
                print()
                print('--------------------------------------------')

                if op1 == True:
                    op = input('Selecione uma operação: ')
                
                else:
                    op = input('Operação inválida. Tente novamente: ')

                if op not in valid_op:
                    op1 = False
                
                elif op in valid_op:
                    break
            
                if op == '0':
                    break

            if op == '1':
                valor_total = 0
                op1 = True
                while True:
                    print('------------------- CATÁLOGO -------------------')
                    print()
                    for i in range(len(produtos)):
                        indice = i + 1
                        codigo1 = produtos[i].get_codigo()
                        tipo1 = produtos[i].get_tipo()
                        marca1 = produtos[i].get_marca()
                        preco1 = produtos[i].get_preco()
                        quantidade1 = produtos[i].get_quantidade()
                        print('%d - Código: %d, Tipo: %s, Marca: %s, Preço: R$ %.2f, Quantidade: %d' % (indice ,codigo1, tipo1, marca1, preco1, quantidade1))
                        print()
                    
                    if op1 == True:
                        print('----------------------------------------------')
                        print('Digite "0000" para voltar')
                        print('Digite "9999" para finalizar a compra')
                        print()
                        prod = int(input('Selecione o código do produto para adicioná-lo ao carrinho: '))
                        print()
                    
                    if op1 == False:
                        print('Digite "0000" para voltar')
                        print('Digite "9999" para finalizar a compra')
                        print()
                        prod = int(input('Código inválido. Tente novamente: '))
                        print()

                    if prod == 9999:
                        print('Valor total do carrinho: R$ %.2f' % (valor_total))
                        print()
                        break

                    if prod == 0000:
                        break

                    if prod not in codigos:
                        op1 = False
                    
                    elif prod in codigos:
                        op1 = True
                        for i in range(len(produtos)):
                            if prod == produtos[i].get_codigo():
                                while True:
                                    if op1 == True:
                                        op = int(input('Digite a quantidade desejada: '))
                                        print()
                                    else:
                                        print('Quantidade desejada indisponível. Há %d itens em estoque.' % (produtos[i].get_quantidade()))
                                        op = int(input('Digite uma quantidade válida: '))
                                        print()

                                    if op > produtos[i].get_quantidade():
                                        op1 = False
                                    else:
                                        print('Produto(s) adicionados ao carrinho com sucesso!')
                                        print()
                                        n_quant = produtos[i].get_quantidade() - op
                                        produtos[i].set_quantidade(n_quant)
                                        valor_total += produtos[i].get_preco() * op
                                        break
