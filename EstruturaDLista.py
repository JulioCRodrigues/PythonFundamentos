#Aprendendo sobre listas - básico
frutas = ['Goiaba', 'Manga', 'Uva']
print(frutas)

#Altera/substitui valor na lista
frutas[1] = "Banana"
print(frutas)

#Deleta item da lista
del frutas[1]
print(frutas)

#Lista aninhada
listas = [[1,2,3], [4,5,6], [7.5, 8.0, 6.3]]
print(listas)

#Retornar tamanho da lista
print(len(frutas))

#Adicionar elemento no final da lista
frutas.append('Maracujá')
print(frutas)
print(len(frutas))

#Mostrar lista invertida
frutas.reverse()
print(frutas)

#Ordenar lista
numeros = [4, 3, 2, 1]
numeros.sort()
print(numeros)