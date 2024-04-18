# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Declaración de variables
	numero = int()
	# Lectura de datos
	numero = int(input())
	# Validar el número
	if numero<1 or numero>7:
		print(("El número ingresado no es válido."))
	else:
		print("")
	if numero==1:
		print("lunes")
	elif numero==2:
		print("martes")
	elif numero==3:
		print("miercoles")
	elif numero==4:
		print("jueves")
	elif numero==5:
		print("viernes")
	elif numero==6:
		print("sabado")
	elif numero==7:
		print("domingo")

