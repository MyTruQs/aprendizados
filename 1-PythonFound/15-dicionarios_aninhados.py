import pprint

gamesDict = {
    "resident evil 4":{
        "yearLauch": 2023,
        "classificarion": 9.8,
        "genre": ["ação", "aventura"]
    },
    "mario odyssey":{
        "yearLauch": 2017,
        "classificarion": 10.0,
        "genre": ["aventura", "3d"]
    },
    "donkey kong country":{
        "yearLauch": 1995,
        "classificarion": 9.5,
        "genre": ["aventura", "plataforma"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)


# 1 - Buscar informações dentro de um dicionário aninhado
print(gamesDict["mario odyssey"]["genre"])

# 2 - Adicionar novo item 
gamesDict["mario odyssey"]["players"] = 1
print(gamesDict["mario odyssey"])

# 3 - Excluir um dicionário
del gamesDict["resident evil 4"]
pp.pprint(gamesDict)