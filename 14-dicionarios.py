gameFifa = {
    "name": "Fifa 23",
    "yearLaunch": 2022,
    "gamePrice": 90.50,
    "classification": 8.5,
    "genre": ["esporte", "família"],
}

print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# 1 - Recuperar um elemento do dicionario

print(gameFifa["genre"])
print(gameFifa["name"])
print(gameFifa["classification"])

# 2 - Buscar as chaves

print(gameFifa.keys())

# 3 - Buscar os valores

print(gameFifa.values())

# 4 - Buscar itens do dicionario com chave e valor

print(gameFifa.items())

# 5 - Adicionar items no dicionário

gameFifa["players"] = 2

print(gameFifa["players"])

# 6 - Atualizar meu dicionário

gameFifa.update({"players": 5})
print(gameFifa["players"])

# 7 - Remover items do dicionário

gameFifa.pop("players")
print(gameFifa)
