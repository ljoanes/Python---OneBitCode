# 1 - Contagem regressiva
import winsound

timer = 10

while timer >= 0:
    print(timer)
    timer -= 1
winsound.Beep(2500, 500)

# 2 - Tabuada
number = int(input("Tabuada de: "))
begin = int(input("De: "))
end = int(input("Até: "))
x = begin
while x <= end:
    print(f"{number} x {x} = {number * x}")
    x = x + 1
