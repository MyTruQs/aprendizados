# Lancamento do foguete
# import winsound
# x = 10
# while x >= 0:
#     print(x)
#     x -= 1
# winsound.Beep(1000, 500)


# Tabuada de um número
number = int(input("Tabuada de: \n"))
begin = int(input("De: \n"))
end = int(input("Até: \n"))

x = begin

while x <= end:
    print(f"Tabuada de {number} x {x} = {number * x}")
    x = x + 1