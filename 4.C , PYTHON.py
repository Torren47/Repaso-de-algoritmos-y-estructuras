# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Definir variables
	tamano = int()
	minimo = int()
	i = int()
	arreglo = int()
	# Solicitar al usuario el tama�o del arreglo
	print("Ingrese el tama�o del arreglo:")
	tamano = int(input())
	# Leer los elementos del arreglo
	arreglo = [int() for ind0 in range(tamano)]
	for i in range(1,tamano+1):
		print("Ingrese el elemento ",i," del arreglo:")
		arreglo[i-1] = int(input())
	# Encontrar el m�nimo del arreglo
	# Asigna el primer elemento del arreglo como el m�nimo inicialmente
	minimo = arreglo[0]
	for i in range(2,tamano+1):
		if arreglo[i-1]<minimo:
			# Actualiza el m�nimo si el elemento actual es menor
			minimo = arreglo[i-1]
	# Mostrar el m�nimo
	print("El m�nimo elemento del arreglo es: ",minimo)

