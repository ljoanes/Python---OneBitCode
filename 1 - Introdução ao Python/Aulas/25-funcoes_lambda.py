# 1 - Função de potencia de número

power = lambda num: num**2

# 2 - Verificação se é par
pair = lambda x: x % 2 == 0

# 3 - Divisão de um numero pelo outro
divNum = lambda x, y: x / y

# 4 - Inversão de string
reverse = lambda s: s[::-1]

print(power(5))
print(power(9))
print(pair(27))
print(pair(30))
print(divNum(10, 2))
print(divNum(7, 2))
print(reverse("Função"))
print(reverse("Tecnologia"))
