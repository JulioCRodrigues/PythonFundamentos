#Exibe o nome do aplicativo
print("********** CALCULADORA DO JUCA **********")

#Exibe as opções do menu
print("Selecione o número da operação:  \n")

operacao = ['1 - Adicao', '2 - Subtracao', '3 - Divisao', '4 - Multiplicacao \n']

for i in operacao:
    print(i)

#Aguarda usuário escolher a operação 
opcao = float(input('\n Digite a sua operação: 1/2/3/4/: '))

#Definindo variaveis
n1 = float(input('\n Digite o primeiro número: '))
n2 = float(input('\n Digite o segundo número: '))


if opcao == 1:

    #Calcula operação soma
    result = n1 + n2
    print('\n')
    print('{} + {} = {}'.format(n1, n2, result))

elif opcao == 2:

    #Calcula subtração
    result = n1 - n2
    print('\n')
    print('{} - {} = {}'.format(n1, n2, result))

elif opcao == 3:

    #Calcula divisão
    result = n1 / n2
    print('\n')
    print('{} / {} = {}'.format(n1, n2, result)) 

elif opcao == 4:

    #Calcula multiplicação
    result = n1 * n2
    print('\n')
    print('{} * {} = {}'.format(n1, n2, result)) 

else:
    print('Opção inválida!')