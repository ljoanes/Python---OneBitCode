import pprint

gamesDict = {
    "resident evil 4": {"yearLaunch": 2023, "classification": 9.8, "genre": ["acao", "aventura"]},
    "mario odyssey": {"yearLaunch": 2017, "classification": 10, "genre": ["aventura", "3d"]},
    "donkey kong country": {"yearLaunch": 1995, "classification": 9.5, "genre": ["aventura", "plataforma"]},
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

# 1 - Buscar Informações dentro de um dicionário aninhado

print(gamesDict["mario odyssey"]["genre"])

# 2 - Adicionar novo item
gamesDict["mario odyssey"]["players"] = 1
print(gamesDict["mario odyssey"])

# 3 - Excluir um dicionário
del gamesDict("resident evil 4")
print(gamesDict)
