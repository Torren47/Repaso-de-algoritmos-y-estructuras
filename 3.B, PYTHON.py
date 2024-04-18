# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Declaración de variables
	cadena = str()
	letra = str()
	i = int()
	contador = int()
	# Lectura de la cadena
	cadena = input()
	# Leer la letra a buscar
	letra = input()
	# Inicializar el contador
	contador = 0
	# Recorrer la cadena caracter por caracter
	for i in range(1,len(cadena)+1):
		# Si el caracter actual es igual a la letra, aumentar el contador
		if cadena[i-1:1]==letra:
			contador = contador+1
	# Mostrar el número de apariciones
	print("La letra ",letra," aparece ",contador," veces en la cadena.")

