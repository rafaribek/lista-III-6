qtde = int(input("informe a quantidade comprada: "))
valorunit = float(input("informe o valor unitario: "))
desconto = float(input("informe o desconto:"))

totalsemdesconto = qtde * valorunit
totalcomdesconto = totalsemdesconto - (totalsemdesconto * desconto/100)
print(f"o total sem desconto será R$ {totalsemdesconto:.2f}")
print(f"o valor com desconto será R$ {totalcomdesconto:.2f}")

