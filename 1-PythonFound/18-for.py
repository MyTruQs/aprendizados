gameList = ["Fifa", "God of War", "Red Dead 2", "Uncharted", 90.50]

# 1 - Interando valores de uma lista
for game in gameList:
    print(game)
    
# 2 - Quando a condição for atendida, o loop será encerrado
for game in gameList:
    if game == "Red Dead 2":
        break
    print(game)
    
# 3 - Quando a condição for atendida, o loop vai para a próxima iteração
for game in gameList:
    if game == "Red Dead 2":
        continue
    print(game)
    
# 4 - Avaliação do Jogo
gameName = input("Digite o nome do jogo\n")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo\n"))

sum = 0
for i in range(gameRating):
    note = float(input("Digite a nota para o jogo\n"))
    sum += note
print(f"Média de avaliação do jogo {gameName} é {sum/gameRating :.2f}")