# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Definir las opciones del juego
	opciones = str()
	opciones = "piedra papel tijeras"
	# Generar una elecci�n aleatoria para el programa
	e = ALEATORIO(1,3)
	eleccionprograma = opciones[(e-1)*7:7]
	# Solicitar al usuario que ingrese su elecci�n
	print("Elige piedra, papel o tijeras:")
	eleccionusuario = input()
	# Convertir la elecci�n del usuario a min�sculas para facilitar la comparaci�n
	eleccionusuario = str.lower(eleccionusuario)
	# Verificar si la elecci�n del usuario es v�lida
	if eleccionusuario=="piedra" or eleccionusuario=="papel" or eleccionusuario=="tijeras":
		# Determinar qui�n gana la partida
		if eleccionusuario==eleccionprograma:
			print("�Es un empate!")
		else:
			if (eleccionusuario=="piedra" and eleccionprograma=="tijeras") or (eleccionusuario=="papel" and eleccionprograma=="piedra") or (eleccionusuario=="tijeras" and eleccionprograma=="papel"):
				print("�Felicidades! Has ganado.")
			else:
				print("�Lo siento! Has perdido.")
	else:
		print("La elecci�n ingresada no es v�lida. Por favor, elige piedra, papel o tijeras.")

