
coordenadax=int(input("Insira a coordenada x:"))
coordenaday=int(input("Insira a coordenada y:"))

if coordenadax < 0 and coordenaday < 0:   # - -
    print("O ponto encontra-se no terceiro quadrante.")
elif coordenadax < 0 and coordenaday > 0:  # - +
    print("O ponto encontra-se no segundo quadrante.")
elif coordenadax > 0 and coordenaday < 0:  # + -
    print("O ponto encontra-se no quarto quadrante.")
elif coordenadax > 0 and coordenaday > 0: # + +
    print("O ponto encontra-se no primeiro quadrante.")
elif coordenadax == 0 and coordenaday < 0:  # 0 -
    print("O ponto encontra-se sobre o eixo y, no lado negativo de y.")
elif coordenadax <0 and coordenaday == 0:  # - 0
    print("O ponto encontra-se sobre o eixo x, no lado negativo de x.")
elif coordenadax == 0 and coordenaday == 0: # 0 0
    print("O ponto encontra-se na origem.")
elif coordenadax > 0 and coordenaday ==0:
    print("O ponto encontra-se sobre o eixo x, no seu lado positivo.")
else: 
    print("O ponto encontra-se sobre o eixo y, no seu lado positivo.")