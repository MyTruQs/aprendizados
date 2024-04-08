num1 = float(input("Digite o primeiro número:\n"))
num2 = float(input("Digite o segundo número\n"))
operation = input("Digite a operação a realizar (+ - * /)\n")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Operação inválida")
    result = 0
    
print(f"Resultado é: {result:.2f}")