# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	suma = int()
	numero = int()
	# Lectura del número
	numero = int(input())
	# Inicializar la suma
	suma = 0
	# Recorrer los números impares desde 1 hasta el número ingresado
	for i in range(1,numero+1,2):
		# Si el número es impar, sumarlo
		if i%2==1:
			suma = suma+i
	# Mostrar la suma
	print(("La suma de los números impares desde 1 hasta "),numero," es: ",suma)

