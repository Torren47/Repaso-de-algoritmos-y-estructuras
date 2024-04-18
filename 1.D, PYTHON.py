# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Declaración de variables
	letra = str()
	# Lectura de datos
	letra = input()
	# Convertir la letra a minúscula
	letra = str.lower(letra)
	# Determinar si la letra es vocal
	if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
		print(("La letra "),letra,(" es una vocal."))
	else:
		print(("La letra "),letra,(" es una consonante."))

