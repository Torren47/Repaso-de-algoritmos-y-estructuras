# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Declaración de variables
	distanciacarrera = int()
	metroscorredor1 = int()
	metroscorredor2 = int()
	velocidadcorredor1 = float()
	velocidadcorredor2 = float()
	# Definir la distancia de la carrera
	distanciacarrera = 100
	# Inicializar variables a 0 (including velocities)
	metroscorredor1 = 0
	metroscorredor2 = 0
	tiempocarrera = 0
	# Ejemplo: velocidad del Corredor 1 en metros por segundo
	velocidadcorredor1 = 8
	# Ejemplo: velocidad del Corredor 2 en metros por segundo
	velocidadcorredor2 = 100
	# Bucle para simular la carrera
	while (tiempocarrera<=1):
		# Generar metros aleatorios para cada corredor
		metroscorredor1 = ALEATORIO(1,10)
		metroscorredor2 = ALEATORIO(1,10)
		# Sumar metros a la distancia total recorrida por cada corredor
		metroscorredor1 = metroscorredor1+metroscorredor1
		metroscorredor2 = metroscorredor2+metroscorredor2
		# Incrementar el tiempo de carrera en 0.1 segundos
		tiempocarrera = tiempocarrera+0.1
	# Calcular el tiempo de cada corredor
	tiempocorredor1 = tiempocarrera/velocidadcorredor1
	tiempocorredor2 = tiempocarrera/velocidadcorredor2
	# Mostrar el ganador
	if (tiempocorredor1<tiempocorredor2):
		print("El ganador es el Corredor 1 con un tiempo de ",tiempocorredor1," segundos")
	else:
		print("El ganador es el Corredor 2 con un tiempo de ",tiempocorredor2," segundos")

