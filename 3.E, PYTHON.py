# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Inicializar el producto a 1
	producto = 1
	# Bucle para leer números y calcular el producto
	while (numero>=0):
		# Leer un número entero
		print(("Ingrese un número entero (negativo para finalizar): "))
		numero = float(input())
		# Si el número es positivo, multiplicarlo por el producto actual
		if (numero>0):
			producto = producto*numero
	# Mostrar el producto final
	if (producto>1):
		print("El producto de todos los números ingresados es: ",producto)
	else:
		print(("No se ha ingresado ningún número positivo."))

