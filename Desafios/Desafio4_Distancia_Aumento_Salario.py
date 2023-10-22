# 1 - Calculo de distancia

distancia = int(input("Qual a distância a ser percorrida?\n"))

if distancia <= 200:
    taxa = 0.5
    result = distancia * 0.5
else:
    taxa = 0.35
    result = distancia * 0.35

print(
    f"A distancia a ser percorrida é de {distancia} e e o valor gasto com ela será de {result} valendo {taxa} centavos o km"
)


# 2 - Aumento salário funcionário

salario = float(input("Qual o salário que você recebe?\n"))

if salario > 1250.00:
    taxa = 0.10
    result = salario * taxa
else:
    taxa = 0.15
    result = salario * taxa

print(f"O aumento será de {result:.2f} num percentual de {int(taxa * 100)}%")

##############################################################################
salary = float(input("Digite seu salário: "))
perc_increase = 0.15
if salary > 1250:
    perc_increase = 0.10
incresase = salary * perc_increase
print(f"Seu aumento será de: R$ {incresase:.2f}")
