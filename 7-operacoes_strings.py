gameDescription = """
Fifa 23 é um jogo de futebol desenvolvido pela EA Sports
e que possibilita jogar localmente ou online
"""

gameName = "Fifa "
gameVersion = "23"

# 1 - Operação de Concatenação de Strings
gameFullName = gameName + gameVersion
print(gameFullName)

# 2 - Operação de multiplicação de strings
line = "="
print(line * 25)

# 3 - Procura palavra dentro de um texto
print("Fifa" in gameDescription)
print("fifa" in gameDescription)
print("Futebol" in gameDescription)
print("futebol" in gameDescription)
