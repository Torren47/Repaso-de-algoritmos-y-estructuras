# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Declaración de variables
	numero = int()
	suma = int()
	# Inicialización de la resta
	# Inicialización de la suma
	suma = 0
	# Bucle para leer y sumar números
	while numero>=0:
		# Leer un número
		print(("Ingrese un número entero positivo (o un número negativo para terminar): "))
		numero = int(input())
		# Si el número es positivo, sumarlo
		if (numero>0):
			suma = suma+numero
	# Mostrar la suma total
	print("La suma total de los números ingresados es: ",suma)

