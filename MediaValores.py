qtd = 0
soma = 0
valor = float(input("digite um valor: "))

while(valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1 
    #entrada de valores
    valor = float(input("Digite um valor: "))

#caso digite um valor negativo o laço encerra
media = soma/qtd
print("\n total da soma: ",soma)
print("\n quantidade de valores digitais: ",qtd)
print("\n Media dos valores: ",media)