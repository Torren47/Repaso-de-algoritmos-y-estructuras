# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Declaraci�n de variables
	i = int()
	n = int()
	suma = int()
	numeros = int()
	# Leer la cantidad de elementos del arreglo
	print("Ingrese la cantidad de n�meros: ")
	n = int(input())
	# Leer los elementos del arreglo
	for i in range(1,n+1):
		print("Ingrese el n�mero ",i,": ")
		numeros = int(input())
	# Inicializar la suma a 0
	suma = 0
	# Sumar cada elemento del arreglo
	for i in range(1,n+1):
		suma = suma+numeros
	# Mostrar la suma total
	print("La suma de todos los n�meros es: ",suma)

