gameName = "fifa 23"
gameDescription = '''
Fifa 23 é um jogo de futebol, desenvolvido pela EA Sports,
e que possibilita jogar localmente ou online.
'''

print(gameName.upper()) # Retornar string em maiúsculo
print(gameName.lower()) # Retornar string em minúsculo
print(gameName.capitalize()) # Apenas a primeira letra em maiúsculo
print(gameName.title()) # Apenas a primeira letra em maiúsculo
print(gameName.center(11, '-')) # Retornar string centralizada com o caractere de preenchimennto
print(gameName.find("f")) # Retorna a posição de um determinado caractere
print(gameDescription.count("f")) # Conta caracteres
print(gameDescription.count("a")) # Conta caracteres
print(gameDescription.replace("Fifa", "Pes")) # Altera um elemento por outro
print(gameDescription.split(","))