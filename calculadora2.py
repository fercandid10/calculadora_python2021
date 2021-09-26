def calculadora(n1,sinal,n2):

    aux = 0
    if sinal == '+':
        aux = n1 + n2

    if sinal == '-':
        aux = n1 - n2

    if sinal == '*':
        aux = n1 * n2

    if sinal == '/':
        aux = n1 / n2

    if sinal == '%':
        aux = n1 * n2 / 100

    aux2 = str(input("Continuar ? S/N"))
    if aux2 == 'N' or aux2 == 'n':
        return aux
        exit()
    else:
        op = str(input("Digite o sinal: "))
        value = int(input("valor: "))
        novo = calculadora(aux,op,value)
        return novo

calculo = calculadora(10,'%',10)
print(calculo)

