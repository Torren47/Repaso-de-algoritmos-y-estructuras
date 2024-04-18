# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Generar un número aleatorio entre 1 y 100
	numeroaleatorio = ALEATORIO(1,100)
	# Inicializar la variable para almacenar el número ingresado por el usuario
	numeroingresado = 0
	# Mientras el número ingresado por el usuario sea diferente al número aleatorio
	while numeroingresado!=numeroaleatorio:
		# Solicitar al usuario que ingrese un número
		print("Adivina el número (entre 1 y 100):")
		numeroingresado = float(input())
		# Comparar el número ingresado con el número aleatorio y dar pistas al usuario
		if numeroingresado<numeroaleatorio:
			print("El número ingresado es menor que el número secreto.")
		else:
			if numeroingresado>numeroaleatorio:
				print("El número ingresado es mayor que el número secreto.")
	# Mostrar mensaje de felicitaciones al usuario por adivinar el número
	print("¡Felicidades! Has adivinado el número secreto.")

