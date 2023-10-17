gameName = "Fifa 23"
gameDescription = """
Fifa 23 é um jogo de futebol desenvolvido pela EA Sports
e que possibilita jogar localmente ou online
"""

# String[inicio:fim:passo] - índice começa na posição zero | índice final -1

# 1 - Busque toda string a partir da primeira posição
print(gameName[0:])
print(gameName[2:])

# 2 - Busque toda string até a última posição
print(gameName[:5])
print(gameName[:-4])

# 3 - Busque toda string da terceira até a última posição
print(gameName[2:])

# 4 - Busque toda a string de 2 em 2 caracteres
print(gameName[::2])

# 5 - Busque toda a string nos índices ímpares
print(gameName[1::2])

# 6 - Inverter uma string de trás pra frente
print(gameName[::-1])
