gameName = "Fifa 23"
gameDescription = """
Fifa 23 é um jogo de futebol, desenvolvido pela EA Sports,
e que possibilita jogar localmente ou online
"""

# 1 - Alguns métodos com string
print(gameName.upper())  # Retorna string em maiúsculo
print(gameName.lower())  # Retorna string em maiúsculo
print(gameName.title())  # Apenas a primeira letra em maiúsculo
print(gameName.capitalize())  # Apenas a primeira letra em maiúsculo
print(gameName.center(9, "-"))
# Retorna a string centralizada com caractere de preenchimento
print(gameDescription.find("a"))
# Retorna a posição de um determinado caractere
print(gameDescription.count("f"))  # Conta caracteres
print(gameDescription.replace("Fifa", "PES"))  # Altera um elemento por outro
print(gameDescription.split(","))
