# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Declaraci�n de variables
	numero = int()
	suma = int()
	# Inicializaci�n de la resta
	# Inicializaci�n de la suma
	suma = 0
	# Bucle para leer y sumar n�meros
	while numero>=0:
		# Leer un n�mero
		print(("Ingrese un n�mero entero positivo (o un n�mero negativo para terminar): "))
		numero = int(input())
		# Si el n�mero es positivo, sumarlo
		if (numero>0):
			suma = suma+numero
	# Mostrar la suma total
	print("La suma total de los n�meros ingresados es: ",suma)

