notaA=float(input("informe a nota1: "))
notaB=float(input("informe a nota1: "))

#calcular media
mediafinal =(notaA + notaB) / 2

#verifição
if mediafinal >=7.0:
    print("A media: %.1f - Aprovado" % mediafinal)
else:
    print("A Media: %1f - Reprovado " % mediafinal)
