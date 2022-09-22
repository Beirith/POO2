from classes import *
import random

cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
naipe = ['Copas', 'Espadas', 'Ouro', 'Paus']
baralho = []
decks_jogadores = []

for i in range(len(naipe)):
    for x in range(len(cartas)):
        carta_x = cartas[x] + ' de ' + naipe[i]
        baralho.append(carta_x)

    def Menu():
        print(''' 
1 - Ver baralho
2 - Embaralhar
3 - Distribuir cartas
4 - Recolher cartas
0 - Sair
        ''')

vl = True
while True:

    valid_ent = ['1', '2', '3', '4', '0']
    Menu()

    if vl == True:
        ent = input("Selecione uma opção: " )
    
    else:
        ent = input("Opção inválida. Tente novamente: " )
    
    if ent not in valid_ent:
        vl = False

    if ent == '0':
        break

    if ent == '1':
        v1 = True
        if len(baralho) == 0:
            print()
            print("Baralho vazio!")

        for i in range(len(baralho)):
            print(baralho[i])
    
    if ent == '2':
        if len(baralho) == 0:
            print()
            print("Baralho vazio!")
        
        else:
            v1 = True
            random.shuffle(baralho)
            print()
            print('Baralho embaralhado!')
    
    if ent == '3':
        v1 = True
        while True:
            if len(baralho) == 0:
                print()
                print("Não há cartas para serem distribuidas.")
                break

            for i in range(10):
                deck1 = Decks('')
                cartas_deck = []

                for h in range(len(baralho)):
                    if i < 7 and baralho[h] != '0':
                        cartas_deck.append(baralho[h])
                        baralho[h]= '0'
                        if len(cartas_deck) == 6:
                            deck1.set_deck(cartas_deck)
                            decks_jogadores.append(deck1)
                            break

                    if i > 7 and baralho[h] != '0':
                        cartas_deck.append(baralho[h])
                        baralho[h]= '0'
                        if len(cartas_deck) == 5:
                            deck1.set_deck(cartas_deck)
                            decks_jogadores.append(deck1)
                            break
            print()           
            for i in range(len(decks_jogadores)):
                deck_print = decks_jogadores[i].get_deck()
                nj = i + 1
                print("JOGADOR %d" % nj)
                print(deck_print)
                print()

            baralho.clear()
            break

    if ent == '4':
        v1 = True
        if len(baralho) != 0:
            print()
            print("Não há cartas para serem recolhidas.")
        else:
            print()
            print("Cartas recolhidas!")

        for n in range(len(decks_jogadores)):
            remover_deck = decks_jogadores[n].get_deck()
            for k in range(len(remover_deck)):
                baralho.append(remover_deck[k])

        decks_jogadores.clear()
