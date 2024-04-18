# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	numero = float()
	print("ingresa un numero")
	numero = float(input())
	if numero==0:
		print("el numero ",numero," es neutro ")
	else:
		if numero>0:
			print("el numero es positivo")
		else:
			print("el numero es negativo")

