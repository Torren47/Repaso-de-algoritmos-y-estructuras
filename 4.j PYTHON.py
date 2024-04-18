# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	x = int()
	n = int()
	a = int()
	error = int()
	letra = str()
	secreta = str()
	vector1 = str()
	vector2 = str()
	print("Ingresa la palabra secreta")
	secreta = input()
	n = len(secreta)
	vector1 = [str() for ind0 in range(n)]
	vector2 = [str() for ind0 in range(n)]
	for x in range(1,n+1):
		vector1[x-1] = secreta[x-1:x]
		vector2[x-1] = "_"
	a = 0
	while a<5:
		for x in range(1,n+1):
			print(vector2[x-1], end="")
		print("")
		print("Ingresa una letra")
		letra = input()
		error = 1
		for x in range(1,n+1):
			if letra==vector1[x-1]:
				if vector2[x-1]=="_":
					vector2[x-1] = letra
					error = 0
					c = c+1
		if c==n:
			print("Felicidades has ganado el juego")
			a = 6
		else:
			if error==1:
				a = a+1
			if a==1:
				print(".")
				print(".")
				print(".")
				print(".")
				print("Te quedan 4 intentos")
			if a==2:
				print(".....")
				print(".")
				print(".")
				print(".")
				print("Te quedan 3 intentos")
			if a==3:
				print(".....")
				print(".   o")
				print(".")
				print(".")
				print("Te quedan 2 intentos")
			if a==4:
				print(".....")
				print(".   o")
				print(".   ^")
				print(".")
				print("Te queda 1 intento")
			if a==5:
				print(".....")
				print(".   o")
				print(".   ^")
				print(".   ^")
				print("AHORCADO")

