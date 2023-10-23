# 1 - Função para imprimir Hello World


def wellcome():
    print("Hello World!")


print(wellcome())

# 2 - Função para somar dois numeros


def sum():
    print(5 + 4)
    return 5 + 4


print(sum())


# 3 - Função para cadastrar um jogo
def createGame():
    name = input("Digite o nome do jogo?\n")
    yearLaunch = int(input("Qual o ano do jogo?\n"))
    gamePrice = float(input("Qual o preço do jogo\n"))
    noteRating = float(input("Digite a nota de avaliação do jogo\n"))
    print(f"{name} - R$ {gamePrice}")


createGame()
