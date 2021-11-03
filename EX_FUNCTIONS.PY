# Faça um programa para imprimir:

#    1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n

# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

print()
alcance = int(input('Você deseja contar a pirâmide até qual valor? '))
alcance = alcance + 1

def cont_pir():
    for i in range(alcance):
        print(str(i)*i)

cont_pir()
print()

# Faça um programa para imprimir:

#    1
#    1   2
#    1   2   3
#    .....
#    1   2   3   ...  n

# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

alcance = int(input('Deseja contar a pirâmide até qual valor? '))
alcance = alcance+1

def count_pir():
    for i in range(alcance):
        for j in range(i):
            j = j+1
            print(j, end = ' ') # Clausula END = ' ', para não pular linha do print dentro do laço FOR
        print()

count_pir()
print()

# Faça um programa com uma função chamada somaImposto. 
# A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. 
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

# Sem parâmetros de entrada, inserção de dados dentro da função INPUT

def soma_imposto():
    custo = float(input('Qual o valor do item? '))
    taxa_imposto = int(input('Qual a taxa de imposto? '))
    taxa_imposto = (taxa_imposto/100)
    soma_imp = custo+(taxa_imposto*100)
    return soma_imp

print()
print(f'VALOR TOTAL: {soma_imposto()}')

# Com parâmetros de entrada no Hard Code:

print()
custo = float(input('Qual o valor do item? '))
taxa_imposto = int(input('Qual a taxa de imposto? '))


def soma_imposto(custo, taxa_imposto):
    taxa_imposto = (taxa_imposto/100)
    soma_imp = custo+(taxa_imposto*100)
    return soma_imp

print()
print(f'VALOR TOTAL: {soma_imposto(custo, taxa_imposto)}')
print()

# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. 
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. 
# O programa deverá então exibir o valor a ser pago na tela. 
# Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. 
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. 
# O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. 
# Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

presta = []
Dias = []

def valor_pagamento():
    multa = 0.031
    while True:
        print()
        prest = int(input('Informe o valor da Prestação: '))
        if prest == 0:
            print()
            print('Bye')
            break
        prest = str(prest)
        presta.append(prest)
        print()
        dias = int(input('Informe os dias de atraso: '))
        prest = int(prest)
        dias = prest + (dias*multa)
        dias = str(dias)
        Dias.append(dias)

    float_Dias = list(map(float,Dias))    

    print()
    print(f'''
_______________________________    
RELATORIO GERAL:
_______________________________  
    QTD. PREST.: {len(presta)}
_______________________________
    TOTAL: {sum(float_Dias)}
_______________________________    
    ''')

valor_pagamento()
print()