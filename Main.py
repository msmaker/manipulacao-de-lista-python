def calculo(matrix):
    custo = []

    for i in range(len(matrix)):
        custo.append(matrix[i][1] * matrix[i][2])

    idx = custo.index((max(custo)))
    quantidade = matrix[idx][1]
    codigo = matrix[idx][0]
    valor = round(float(custo[idx]),2)

    print("Item mais caro")
    print("Codigo:", codigo)
    print("Quantidade:", quantidade)
    print("Custo:", "{:.2f}".format(valor))

lista = []
listaFinal = []
flag = 1

while not(flag == 0):
    lista = input().split(" ")

    if (lista[0] == '0'):
        break

    lista[0] = int(lista[0])
    lista[1] = int(lista[1])
    lista[2] = float(lista[2])

    listaFinal.append(lista)

    flag = lista[0]

if (lista[0] == '0' and len(lista) == 3 and len(listaFinal) < 1 ):
    print("nao tem compras")

else:
    calculo(listaFinal)
