# 1 - Contas letras minusculas e maiusculas:


def check_char(text):
    type = {"Uppercase": 0, "Lowercase": 0}
    for char in text:
        if char.isupper():
            type["Uppercase"] += 1
        elif char.islower():
            type["Lowercase"] += 1
    print("Texto original: ", text)
    print("Número de letras maiúsculas: ", type["Uppercase"])
    print("Número de letras minúsculas: ", type["Lowercase"])


# string_test('The quick Brown Fox')
check_char("A melhor forma de prever o futuro é Criá-Lo")

# 2 - Verifica se o número é par ou ímpar:


def check_numbers(numbers):
    pairs = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            pairs.append(number)
        else:
            odd.append(number)
    return pairs, odd


print(check_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
