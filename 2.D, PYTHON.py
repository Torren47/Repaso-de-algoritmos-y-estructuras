# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	print("ingrese una palabra")
	palabra = input()
	tamanodepalabra = len(palabra)
	posicion = 1
	while True:# no hay 'repetir' en python
		letra = palabra[posicion-1:posicion]
		print(letra)
		posicion = posicion+1
		if posicion>tamanodepalabra: break

