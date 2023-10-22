"""## Substituindo caractere repetido

Escreva um programa Python para obter uma string de uma determinada
string em que
todas as ocorrências de seu primeiro caractere foram alteradas para '$',
exceto o próprio primeiro caractere
    """

# 1 - Exercício Primeiro
name = input("Digite o nome do jogo\n")

character = name[0].lower()
print(character)
new1 = name.replace(character, "$")
print(new1)
new2 = character + new1[1:]
print(new2)
new3 = new1.replace("F", character)
print(new3)

# 2 - Exercício Segundo

st1 = input("Digite 3 letras \n")
st2 = input("Digite 3 letras\n")

new_st1 = st2[:2] + st1[2:]
new_st2 = st1[:2] + st2[2:]

print(f"{new_st1}")
print(f"{new_st2}")

print(f"{new_st1} {new_st2}")
