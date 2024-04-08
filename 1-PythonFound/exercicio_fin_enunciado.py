verdadeiro = False
times = {}


# Função para listar time
def listTimes():
    print("Lista de times:")
    print("==========================") 
    for i, time in enumerate(times.values()):
        print(f"{i+1}. {time['nameTime']} - Jogadores: {len(time['jogadores'])}")
    print("==========================")

# Função para listar jogador
def listJogadores(timeName):
    print(f"Lista de jogador do time: {timeName['nameTime']}") 
    print("==========================")
    for i, jogador in enumerate(timeName['jogadores']):
        print(f"{i+1}. {jogador}")
    print("==========================")
        

while not verdadeiro:
    print("\n\nBem vindo ao gerenciamento de time!\n")
    print("1- Adicionar um time")
    print("2- Remover um time")
    print("3- Listar um time")
    print("4- Adicionar Jogador no time")
    print("5- Remover jogador do time")
    print("6- Listar jogador do time")
    print("7- Sair do programa")
    menu = input("Escolha um dos menus acima\n")

     
    
    if menu == "1":
        # Adicionar um time
        timeName = input("Digite o nome do time:\n")
        times[timeName] = {'nameTime' : timeName, 'jogadores' : []}
        print('O time foi adicionado.')

    elif menu == "2":
        # Remover time
        listTimes()
        timeR = int(input("Insira o numero do time que deseja remover:\n"))
        if timeR <= len(times):
            timeName = list(times.keys())[timeR-1]
        
            times.pop(timeName)
        
            print(f"O time: {timeName} foi removido.")
        
        else:
            print("Número invalido!")
        
    elif menu == "3":
        # Listar times
        listTimes()   
        
    elif menu == "4":
        # Adicionar Jogador no time
        listTimes()
        
        numeroTime = int(input("Insira o numero do time que deseja add o jogador:\n"))
        
        timeName = list(times.keys())[numeroTime-1]

        jogadorNome = input("Insira o nome do jogador:\n")
        
        times[timeName]['jogadores'].append(jogadorNome)
        
    elif menu == "5":
        # Remover jogador do time
        listTimes()
        numeroTime = int(input("Insira o numero do time que deseja remover o jogador:\n"))
        timeName = list(times.keys())[numeroTime-1]
        
        listJogadores(times[timeName])
        
        jogadorRem = int(input("Insira o numero do jogador que deseja remover:\n"))
        jogadorName = times[timeName]['jogadores'][jogadorRem-1]
         
        print(jogadorName)
        
        times[timeName]['jogadores'].remove(jogadorName)
        
        
    elif menu == "6":
        # Listar jogador do time
        listTimes()
        
        numeroTime = int(input("Insira o numero do time que deseja listar os jogadores:\n"))
        timeName = list(times.keys())[numeroTime-1]
        
        listJogadores(times[timeName])
        
    elif menu == "7":
        verdadeiro = True
        
    else:
        print("Opção inválida!")


