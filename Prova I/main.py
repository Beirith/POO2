class Produto():
    def __init__(self, codigo, sessao):
        self.codigo = codigo
        self.sessao = sessao

    def get_codigo(self):
        return self.codigo

    def get_sessao(self):
        return self.sessao

    def set_codigo(self, codigo):
        self.codigo = codigo

    def set_sessao(self, sessao):
        self.sessao = sessao

class Livro(Produto):
    def __init__(self, codigo, sessao, autor, titulo, ano):
        super().__init__(codigo, sessao)
        self.autor = autor
        self.titulo = titulo
        self.ano = ano
        

    def get_autor(self):
        return self.autor

    def get_titulo(self):
        return self.titulo

    def get_ano(self):
        return self.ano

    def set_autor(self, autor):
        self.autor = autor

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_ano(self, ano):
        self.ano = ano

def menuINICIAL(): #Esse é o primeiro menu. Nele é possível logar no sistema como administrador ou usuário.
    print()
    print("-------- MENU --------")
    print()
    print("1 - Administrador")
    print("2 - Visualizar catálogo como usuário ")
    print("0 - Sair ")
    print()
    print("----------------------")
    print()

def menuADM():
    print()
    print("-------- MENU DE ADMINISTRADOR --------")
    print()
    print("1 - Adicionar livro ao catálogo")
    print("2 - Remover livro do catálogo")
    print("3 - Alterar atributos de livro")
    print("0 - Sair")
    print()
    print("---------------------------------------")
    print()

def menuALTERA():
    print("--------------- MENU DE ALTERAÇÃO ---------------")
    print()
    print("1 - Alterar código")
    print("2 - Alterar autor")
    print("3 - Alterar ano")
    print("4 - Alterar título")
    print("5 - Alterar sessao")
    print("0 - Sair")
    print()


livro1 = Livro('00','CD','Rick Ryan','O cego','1990')  #Adicionei dois livros para o banco de dados da bilioteca
livro2 = Livro('01','AB','David Anderson','A lua','2001')

x = True
livros = [livro1, livro2]
codigos = ['01', '00']
while True: #Loop inicial, onde é inicializado o primeiro menu.
    menuINICIAL()
    valid_op = ['1','2','0']
    fechar = False

    if x == True:
        entry = input("Selecione uma opção: ")
        if entry not in valid_op:
            x = False
    else: 
        entry = input("Opção inválida. Tente novamente: ")

    if entry == '0': #Caso a entrada seja '0', o aplicativo é finalizado.
        print("Sessão finalizada!")
        break
    
    if entry == '2':  #Catálogo visualizado pelo usuário.
        print('------------------- CATÁLOGO -------------------')
        print()
        for i in range(len(livros)):
            indice = i + 1
            codigo1 = livros[i].get_codigo()
            sessao1 = livros[i].get_sessao()
            titulo1 = livros[i].get_titulo()
            autor1 = livros[i].get_autor()
            ano1 = livros[i].get_ano()
            print('%s - Código: %s, Sessão: %s, Título: %s, Autor: %s, Ano: %s' % (indice ,codigo1, sessao1, titulo1, autor1, ano1))
            print()

    if entry == '1': #Se a entrada for 1, então o usuário entra como administador.
        x = True
        while True:
            if fechar == True:
                break
            print()
            print("Digite '0000' para sair.")
            print()
            senhas = ['123']
            if x == True:
                entry = input("Digite sua senha: ")  #Se ele possuir a senha, ele pode entrar como administrador.
            else:
                entry = input("Senha inválida. Tente novamente: ")
            if entry not in senhas:
                x = False
            if entry == '0000':
                x = True
                break
            
            if entry in senhas:
                x = True
                while True:
                    menuADM()
                    valid_op = ['1','2','3','4','0']
                    entry = input("Selecione uma opção: ")

                    if entry == '0': #Caso a entrada seja '0', o menu de administrador é fechado e o sistema volta para o menu inicial.
                        fechar = True
                        break
                        
                    if entry == '1': #Menu de cadastro de livro
                        x = True
                        print("----------- CADASTRO DE LIVRO ----------")
                        print()
                        while True:
                            x = True
                            print()
                            print('Digite "0000" para voltar')
                            print()
                            while True:
                                if x == True:
                                    codigo = input("Digite o código do produto: ")
                                    x = False
                                else:
                                    codigo = input("Código já cadastrado. Digite outro: ")
                                
                                if codigo in codigos:
                                    x = False
                                
                                if codigo == '0000':
                                    break 

                                if codigo not in codigos:
                                    break
                            x = True           
                            codigos.append(codigo)
                            
                            titulo = input("Informe o titulo do livro: ")
                            autor = input("Informe o autor do livro: ")
                            sessao = input("Informe a sessao onde o livro está: ")
                            ano = input("Informe o ano do livro: ")

                            livroX = Livro('','','','','')
                            livroX.set_codigo(codigo)
                            livroX.set_autor(autor)
                            livroX.set_sessao(sessao)
                            livroX.set_ano(ano)
                            livroX.set_titulo(titulo)
                            livros.append(livroX)

                            print()
                            print("Livro cadastrado com sucesso!")
                            print()
                            x = True
                            break

                    if entry == '2':
                            x = True
                            while True:
                                if x == True:
                                    print()
                                    print("Digite '0000' para voltar")
                                    print()
                                    entry = input("Digite o código do livro que será removido: ")
                                    print()
                                
                                else:
                                    print()
                                    print("Digite '0000' para voltar")
                                    print()
                                    entry = input("Livro não cadastrado no sistema. Tente novamente: ")
                                    print()
                                
                                if entry == '0000':
                                    break

                                if entry not in codigos:
                                    x = False
                                
                                if entry in codigos:
                                    codigos.remove(entry)
                                    break

                    for i in range(len(livros)):
                        if entry == livros[i].get_codigo():
                            livros.remove(livros[i])
                            print()
                            print("Livro removido com sucesso!")
                            print()
                            break     

                    if entry == '3':
                        x = True
                        while True:
                            if x == True:
                                codig = input('Digite o código do livro a ser alterado: ')

                            elif x == False:
                                codig = input('Livro não cadastrado no sistema. Tente novamente: ')

                            if codig not in codigos:
                                x = False
                            
                            else:
                                codigo_produto = codig
                                break
                        
                        valid_op = ['0', '1', '2', '3', '0']
                        x = True
                        while True:
                            menuALTERA()

                            if x == True:
                                entry = input('Selecione uma operação: ')
                        
                            elif x == False:
                                entry = input('Operação inválida. Tente novamente: ')
                            
                            if entry not in valid_op:
                                x = False
                            
                            if entry == '0':
                                break

                            if entry == '1':
                                x = True
                                for i in range(len(livros)):
                                    if codigo_produto == livros[i].get_codigo():
                                        while True:
                                            if x == True:
                                                novo_codigo = input('Digite o novo código do livro: ')
                                            else:
                                                novo_codigo = input('Código já cadastrado. Digite outro código: ')

                                            if novo_codigo in codigos:
                                                x = False
                                                
                                            else:
                                                livros[i].set_codigo(novo_codigo)
                                                codigos.append(novo_codigo)
                                                codigos.remove(codigo_produto)
                                                print()
                                                print('Código alterado com sucesso!')
                                                print()
                                                x = True
                                                break    

                            if entry == '2':
                                for i in range(len(livros)):
                                    if codigo_produto == livros[i].get_codigo():
                                        novo_autor = input('Digite o novo autor do livro: ')
                                        livros[i].set_autor(novo_autor)
                                        print()
                                        print('Autor alterado com sucesso!')
                                        print()
                                break

                            if entry == '3':
                                for i in range(len(livros)):
                                    if codigo_produto == livros[i].get_codigo():
                                        novo_ano = input('Digite o novo ano do livro: ')
                                        livros[i].set_ano(novo_ano)
                                        print()
                                        print('Ano alterada com sucesso!')
                                        print()
                                break

                            if entry == '4':
                                for i in range(len(livros)):
                                    if codigo_produto == livros[i].get_codigo():
                                        novo_titulo = input('Digite o novo título do livro: ')
                                        livros[i].set_titulo(novo_titulo)
                                        print()
                                        print('Título alterado com sucesso!')
                                        print()
                                break

                            if entry == '5':
                                for i in range(len(livros)):
                                    if codigo_produto == livros[i].get_codigo():
                                        nova_sessao = input('Digite a nova sessao do livro: ')
                                        livros[i].set_quantidade(nova_sessao)
                                        print()
                                        print('Sessão alterada com sucesso!')
                                        print()
                                break