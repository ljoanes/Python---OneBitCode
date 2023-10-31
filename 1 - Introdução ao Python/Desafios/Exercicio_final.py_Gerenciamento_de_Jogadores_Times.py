teams = {}
done = False

# Funcao para listar times


def print_teams():
    print("Times listados: ")
    for index, team in enumerate(teams.values()):
        player_count = len(team["players"])
        print(f"{index + 1}.{team['name']}({player_count} jogadores)")


# Função para listar jogadores de um time
def print_players(team_name):
    print(f"Jogadores de {team_name}: ")
    for index, player in enumerate(teams[team_name]["players"]):
        print(f"{index + 1}.{player}")


def printer():
    # print options
    print("O que você deseja fazer?")
    print("1. Adicionar um time")
    print("2. Remover um time")
    print("3. Listar times")
    print("4. Adicionar jogador em um time")
    print("5. Remover jogador em um time")
    print("6. Listar jogadores de um time")
    print("7. Sair")


printer()

choice = input(">")
if choice == "1":
    team_name = input("Digite o nome do time:\n")
    teams[team_name] = {"name": team_name, "players": []}
    print(f"Time {team_name} adicionado!")
    printer()
elif choice == "2":
    print_teams()
    team_num = int(input("Informe o número do time que deseja remover"))
    if team_num <= len(teams):
        del teams[teams.keys()[team_num - 1]]
        print(f"Time {teams.keys()[team_num - 1]} removido!")
        printer()
    else:
        print("Número do time inválido!")
elif choice == "3":
    print_teams()
    printer()
elif choice == "4":
    print_players()
    team_num = int(input("Informe o número do time que pretende adicionar o jogador\n"))
    if team_num <= len(teams):
        team_name = [teams.keys()[team_num - 1]]
        player = input("Digite o nome do novo jogador\n")
        teams["players"].append(player)
        print(f"Jogador {player} adicionado ao time {team_name}!")
        printer()
    else:
        print("Número do time inválido!")
elif choice == "5":
    print_teams()
    team_num = int(input("Informe o número do time que pretende remover o jogador\n"))
    if team_num <= len(teams):
        team_name = list([teams.keys()[team_num - 1]])
        player = input("Digite o nome do jogador que deseja remover\n")
        teams["players"].remove(player)
        print(f"Jogador {player} removido do time {team_name}!")
        printer()
    else:
        print("Número do time inválido!")
elif choice == "6":
    team_num = int(input("Informe o número do time que pretende adicionar o jogador\n"))
    if team_num <= len(teams):
        team_name = list([teams.keys()[team_num - 1]])
        print_players(teams[team_name])
    else:
        print("Número do time inválido!")
elif choice == "7":
    done = True
else:
    print("Opção inválida")
