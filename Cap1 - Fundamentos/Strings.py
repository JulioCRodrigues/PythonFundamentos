#Manipulando strings
#Indexação começa por 0
nome = "Julio"
print(nome)
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[4])

# UPPER
print(nome.upper())

#lower
print(nome.lower())

#Quebra de linha  \n = faz função da tecla 'enter'
print("Testando \n Strings \n em \n 'Python'")

#Indexação em python
s = "Estou aprendendo Python"
print(s)
print(s[0])
print(s[1])

#Fatiamento - retorna todos os elementos da string começando pela posição
print(s[1:])

#Retorna tudo até determinada posição
print(s[:3])

#Excluir até a determiada posição
print(s[:-6])

print(s.upper())
print(s.lower())

#Dividir separando por espaço em branco
print(s.split())

#Dividir separando por parametro
print(s.split('o'))

#Contar quantas vezes o caractere aparece
print(s.count('a'))