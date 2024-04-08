# # Cálculo de Distância:
# distancia = float(input("Digite a distância em Km a ser percorrida no trajeto:\n"))

# if distancia > 200:
#     total = distancia * 0.35
# else:
#     total = distancia * 0.50

# print(f"O preço da passagem é: {total}")

# Aumento salário funcionário:

salario = float(input("Digite o salário do funcionário para calcular o aumento:\n"))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

print(f"O aumento é de: {aumento:.2f}\nValor do salário atualizado: {salario + aumento}")