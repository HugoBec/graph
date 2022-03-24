COMPILER = python3

help:
	@echo "Esta es una biblioteca orientada a objetos para la generacion de grafos "
	@echo "-> make help: "
	@echo " 	  Mostrara los comandos disponibles de la versión mas reciente del proyecto "
	@echo "-> make test: "
	@echo " 	  Corre el archivo main.py que da lugar a los archivo .gv "

test: 
	@echo " Ejecutando el test "
	${COMPILER} main.py
