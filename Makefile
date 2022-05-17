COMPILER = python3

help:
	@echo "Esta es una biblioteca orientada a objetos para la generacion de grafos "
	@echo "-> make help: "
	@echo " 	  Mostrara los comandos disponibles de la versión mas reciente del proyecto "
	@echo "-> make clean: "
	@echo " 	  Elimina todos los archivos .gv generados por el test "
	@echo "-> make test_1: "
	@echo " 	  Corre el archivo Parte_1.py que da lugar a los archivos .gv de la parte 1 del proyecto "
	@echo "-> make test_2: "
	@echo " 	  Corre el archivo Parte_2.py que da lugar a los archivos .gv de la parte 2 del proyecto "
	@echo "-> make test_4: "
	@echo " 	  Corre el archivo Parte_3.py que da lugar a los archivos .gv de la parte 3 del proyecto "

clean:
	@echo " Eliminando archivos .gv "
	rm -rf gv/
	@echo " Archivos .gv "

test_1: 
	@echo " Parte_1 "
	@echo " Ejecuntando algoritmos de creación "
	@echo " Ejecutando el test... "
	${COMPILER} parte_1.py

test_2: 
	@echo " Parte_2 "
	@echo " Algoritmos de busqueda "
	@echo " Ejecutando el test... "
	${COMPILER} parte_2.py

test_3: 
	@echo " Parte_3 "
	@echo " Algoritmos de Dijkstra "
	@echo " Ejecutando el test... "
	${COMPILER} parte_3.py
