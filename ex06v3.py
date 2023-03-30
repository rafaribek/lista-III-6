qtde = int(input("informe a quantidade comprada: "))
valorunit = float(input("informe o valor unitario: "))
desconto = float(input("informe o desconto:"))

totalcomdesconto = (qtde * valorunit) * (1 - desconto/100)

print(f"o valor com desconto será R$ {totalcomdesconto:.2f}")

