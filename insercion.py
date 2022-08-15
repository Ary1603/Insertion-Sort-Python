import os
arreglo = []
def mostrarL(lista, x):
	listaordenada = ""
	for i in range(0,x):
		listaordenada += str(lista[i]) + " "
	print(listaordenada)   

while True:	
    os.system("cls")
    
    x = int(input("Num: "))
    arreglo.append(x)

    opc = int(input("Otro:\n1. Si \n2. No\nOpc: "))

    if opc == 2:
        break

for i in range(1,len(arreglo)):
	clave = arreglo[i]
	j = i-1 #Aqui compara el valor seleccionado con todos los valores anteriores
	
	while (j>=0 and arreglo[j] > clave):
		#Insertar el valor donde corresponda
		arreglo[j+1] = arreglo[j]
		j = j-1
	arreglo[j+1] = clave
	mostrarL(arreglo, len(arreglo))
#mostrarL(arreglo, len(arreglo))    