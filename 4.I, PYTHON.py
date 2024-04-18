# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from time import sleep

if __name__ == '__main__':
	# Definir el tamaño del arreglo
	arreglo = [int() for ind0 in range(10)]
	# Generar números aleatorios y llenar el arreglo
	for i in range(1,11):
		arreglo[i-1] = ALEATORIO(0,9)
	# Mostrar el arreglo por unos segundos
	print("Memoriza estos números:")
	for i in range(1,11):
		print(arreglo[i-1])
	# Esperar 3 segundos (3000 milisegundos)
	sleep(3)
	# Ocultar los números
	print("") # no hay forma directa de borrar la pantalla con Python estandar
	# Pedir al usuario que ingrese los números en el mismo orden
	print("Ingresa los números en el mismo orden:")
	for i in range(1,11):
		print("Número ",i,":")
		numeroingresado = input()
		# Verificar si el número ingresado coincide con el número en el arreglo
		if numeroingresado!=arreglo[i-1]:
			print("¡Has perdido! Los números no coinciden.")
	# Si el usuario llega aquí, ha ingresado todos los números correctamente
	print("¡Felicidades! Has ganado.")

