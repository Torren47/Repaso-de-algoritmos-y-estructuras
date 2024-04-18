# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Definir las opciones del juego
	opciones = str()
	opciones = "piedra papel tijeras"
	# Generar una elección aleatoria para el programa
	e = ALEATORIO(1,3)
	eleccionprograma = opciones[(e-1)*7:7]
	# Solicitar al usuario que ingrese su elección
	print("Elige piedra, papel o tijeras:")
	eleccionusuario = input()
	# Convertir la elección del usuario a minúsculas para facilitar la comparación
	eleccionusuario = str.lower(eleccionusuario)
	# Verificar si la elección del usuario es válida
	if eleccionusuario=="piedra" or eleccionusuario=="papel" or eleccionusuario=="tijeras":
		# Determinar quién gana la partida
		if eleccionusuario==eleccionprograma:
			print("¡Es un empate!")
		else:
			if (eleccionusuario=="piedra" and eleccionprograma=="tijeras") or (eleccionusuario=="papel" and eleccionprograma=="piedra") or (eleccionusuario=="tijeras" and eleccionprograma=="papel"):
				print("¡Felicidades! Has ganado.")
			else:
				print("¡Lo siento! Has perdido.")
	else:
		print("La elección ingresada no es válida. Por favor, elige piedra, papel o tijeras.")

