#escrever 2 numeros inteiros e ler o maior

numero1=int(input("Insira um número:"))
numero2=int(input("Insira outro:"))

if numero1 < numero2:
    print(numero2)
elif numero1 > numero2:
    print (numero1)
elif numero1 == numero2:
    print("São iguais infelizmente")