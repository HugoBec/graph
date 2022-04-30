COMPILER = python3

help:
	@echo "Esta es una biblioteca orientada a objetos para la generacion de grafos "
	@echo "-> make help: "
	@echo " 	  Mostrara los comandos disponibles de la versión mas reciente del proyecto "
	@echo "-> make test: "
	@echo " 	  Corre el archivo main.py que da lugar a los archivo .gv "

test_1: 
	@echo " Parte_1 "
	@echo " Algoritmos generadores "
	@echo " Ejecutando el test... "
	${COMPILER} parte_1.py
test_2: 
	@echo " Parte_2 "
	@echo " Algoritmos de busqueda "
	@echo " Ejecutando el test... "
	${COMPILER} parte_2.py
