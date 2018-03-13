
numero1=int(input("Insira um número:"))
numero2=int(input("Insira outro nr:"))

pergunta=input("Qual dos seguintes operadores deseja? + - * / :")

if pergunta == "+":
    print(numero1 + numero2)
elif pergunta == "-":
    print(numero1 - numero2)
elif pergunta == "*":
    print(numero1 * numero2)
elif pergunta == "/":
    print(numero1 / numero2)
else: 
    print("ERRO")
