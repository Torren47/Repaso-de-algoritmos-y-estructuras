# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Inicializar el producto a 1
	producto = 1
	# Bucle para leer n�meros y calcular el producto
	while (numero>=0):
		# Leer un n�mero entero
		print(("Ingrese un n�mero entero (negativo para finalizar): "))
		numero = float(input())
		# Si el n�mero es positivo, multiplicarlo por el producto actual
		if (numero>0):
			producto = producto*numero
	# Mostrar el producto final
	if (producto>1):
		print("El producto de todos los n�meros ingresados es: ",producto)
	else:
		print(("No se ha ingresado ning�n n�mero positivo."))

