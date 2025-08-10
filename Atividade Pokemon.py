while True:
    #Inicio
    print ("Seja bem vindo a Batalha Pokemon")
    print("Para iniciarmos, escolha seu pokemon")
    print("pokemons disponiveis:")
    print("1 - Charmander")
    print("2 - Squirtle")
    print("3 - Bulbasaur")

    #Escolha Pokemon
    escolha = int(input("Escolha um pokemon: "))
    print("")
    if escolha == 1:
        print("Você escolheu o Chamander")
        danoj = 20
        defj = 5
    elif escolha == 2:
        print("Você escolheu o Squirtle")
        danoj = 15
        defj = 7
    else  :
        print("Você escolheu o Bulbasaur")
        danoj = 17
        defj = 10
    print("")

    #Inimigo Pokemon
    import random
    my_list = ["Chamander", "Squirtle", "Bulbasaur"]
    inimigo = random.choice(my_list)
    if inimigo == 1:
        print("Inimigo sorteado: Chamander")
        danoi = 20
        defi = 6

    elif inimigo == 2:
        print("Inimigo sorteado: Squirtle")
        danoi = 18
        defi = 4
    else :
        print("Inimigo sorteado: Bulbasaur")
        danoi = 16
        defi = 8
    print("")

    #Inicio de batalha
    print("--- Batalha Iniciada ---")

    vida = 100
    vida_inimigo = 100
    print("Sua vida:",vida, "| Vida do inimigo:",vida_inimigo)
    print("1 - Atacar")
    print("2 - Defender")
    print("2 - Fugir")

    #Escolha de ataque/defesa/fugir
    batalha = int(input("Escolha uma opção: "))
    print("")

    #Ações 
    while vida_inimigo >=0 and vida >=0:
        if batalha == 1:
            dano = danoj - defi
            vida_inimigo = (vida_inimigo - dano)
            print("Você atacou o",inimigo,"causando",dano,"de dano!")
            print("Sua vida:",vida, "| Vida do inimigo:",vida_inimigo)
        
        elif batalha == 2:
            dano = vida - danoi / 2
            vida = int(dano)
            resto = (danoi / 2)
            print(inimigo,"atacou causando",resto,"de dano")
            print("Sua vida:",vida, "| Vida do inimigo:",vida_inimigo)
        else :
            print("Você fugiu!")
            vida_inimigo == 0
            break
        
        batalha = int(input("Escolha uma opção: "))
        if vida_inimigo >= 0:
            print ("Você perdeu!")
        else: 
            print("Você ganhou!")
    print("")
    jogar = input("Quer jogar de novo? (sim/não): ")
    if jogar != 'sim':
        break

