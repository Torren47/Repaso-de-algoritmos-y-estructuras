# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Generar un n�mero aleatorio entre 1 y 100
	numeroaleatorio = ALEATORIO(1,100)
	# Inicializar la variable para almacenar el n�mero ingresado por el usuario
	numeroingresado = 0
	# Mientras el n�mero ingresado por el usuario sea diferente al n�mero aleatorio
	while numeroingresado!=numeroaleatorio:
		# Solicitar al usuario que ingrese un n�mero
		print("Adivina el n�mero (entre 1 y 100):")
		numeroingresado = float(input())
		# Comparar el n�mero ingresado con el n�mero aleatorio y dar pistas al usuario
		if numeroingresado<numeroaleatorio:
			print("El n�mero ingresado es menor que el n�mero secreto.")
		else:
			if numeroingresado>numeroaleatorio:
				print("El n�mero ingresado es mayor que el n�mero secreto.")
	# Mostrar mensaje de felicitaciones al usuario por adivinar el n�mero
	print("�Felicidades! Has adivinado el n�mero secreto.")

