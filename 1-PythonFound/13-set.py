# Não possbilita recuperar valores via fariamento ou slice


gamesSet = {"Resident Evil 4", "Star Wars Jedi Survivor", "The Legend of Zelda", 
              "Red Dead", "Mario Odyssey"}
print(gamesSet)

# 1 - Buscar o tamanho do set
print(len(gamesSet))

# 2 - True e 1 são considerados o mesmo valor
exampleSet = {"Fifa 23", True, 1, 90.50}
print(exampleSet)

# 3 - Adicionar item de outro set
gamesSet.update(exampleSet)
print(gamesSet)

# 4 - Remover um item no set
gamesSet.remove(True)
gamesSet.remove(90.50)
print(gamesSet)