# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Definir variables
	tamano = int()
	suma = int()
	i = int()
	arreglo = int()
	media = float()
	# Solicitar al usuario el tamaño del arreglo
	print("Ingrese el tamaño del arreglo:")
	tamano = int(input())
	# Leer los elementos del arreglo
	arreglo = [int() for ind0 in range(tamano)]
	suma = 0
	for i in range(1,tamano+1):
		print("Ingrese el elemento ",i," del arreglo:")
		arreglo[i-1] = int(input())
		# Sumar cada elemento para calcular la suma total
		suma = suma+arreglo[i-1]
	# Calcular la media
	media = suma/tamano
	# Mostrar la media
	print("La media de los elementos del arreglo es: ",media)

