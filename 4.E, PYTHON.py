# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Definir variables
	tamano = int()
	contadorpares = int()
	i = int()
	arreglo = int()
	# Solicitar al usuario el tamaño del arreglo
	print("Ingrese el tamaño del arreglo:")
	tamano = int(input())
	# Leer los elementos del arreglo
	arreglo = [int() for ind0 in range(tamano)]
	contadorpares = 0
	for i in range(1,tamano+1):
		print("Ingrese el elemento ",i," del arreglo:")
		arreglo[i-1] = int(input())
		if arreglo[i-1]%2==0:
			# Incrementa el contador si el elemento es par
			contadorpares = contadorpares+1
	# Mostrar la cantidad de elementos pares
	print("La cantidad de elementos pares en el arreglo es: ",contadorpares)

