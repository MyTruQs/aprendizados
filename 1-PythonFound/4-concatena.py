name = input("Digite o nome do jogo\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo\n"))
gamePrice = float(input("Digite o preço do jogo\n"))
planIncluded = bool(input("Esta incluso no serviço mensal?\n"))


print("###########Dados do Jogo##############")
print("======================================")
print("Nome do Jogo: ", name)

# F String
print(f"Nome do jogo: {name} \nAno Lançamento: {yearLaunch} \nPreço do jogo: {gamePrice} \nEstá incluso no serviço? {planIncluded}")