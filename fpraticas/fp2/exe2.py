
#ler dois valores numericos e ordena-los do maior pro menor

numero1=int(input("Insira um valor:"))
numero2=int(input("insira outro:"))

if numero1 > numero2:
    print(numero1 , numero2)
elif numero2 > numero1:
    print(numero2 , numero1 )
elif numero1 == numero2:
    print("Os numeros são iguais")

