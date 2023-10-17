gameList = ["Resident Evil 4", "Star Wars: Jedi Survivor", "The Legend of Zelda", "Red Dead 2", "Mario Odyssey"]

# 1 - Tamanho da lista

print(len(gameList))

# 2 - Recuperar um item da lista pelo índice

print(gameList.index("Mario Odyssey"))
print(gameList[4])

# 3 - Adicionar um item ao final da lista

gameList.append("GTA V")
print(gameList)

# 4 - Ordenar a lista
gameList.sort()
print(gameList)

# 5 - Copiar os itens de uma lista
gameReset = gameList.copy()
gameReset.remove("Star Wars: Jedi Survivor")
print(gameReset)

# 6 - Remove todos os itens da lista
gameList.clear()
print(gameList)
