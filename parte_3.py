
import time
from graph import DIRECTED
import models
from random import randint

init = time.time()

print( '.....................')
print( 'Algoritmo de Malla')
print( 'Generando el grafo 30' )

g    = models.mesh( 15, 2 )

for i in g.edges.values():
    i.attr["WEIGHT"] = randint( 1, 10 )

dot = g.create_graphviz( 'Mesh_30', attr_label_edge="WEIGHT" )

print( 'Iniciando algoritmo de Dijkstra' )

g_d  = g.dijkstra( 0, 29 )
dot_d = g_d.create_graphviz( 'Mesh_30_Dijkstra',"WEIGHT", 0)

print( 'Generando el grafo 500' )

g    = models.mesh( 25, 20 )

for i in g.edges.values():
    i.attr["WEIGHT"] = randint( 1, 10 )

dot  = g.create_graphviz('Mesh_500')

print( 'Iniciando algoritmo de Dijkstra' )

g_d   = g.dijkstra( 0, 499 )
dot_d = g_d.create_graphviz( 'Mesh_500_Dijkstra',"WEIGHT", 0)


print('Grafos de Malla completado')
print('..........................')

#ERdos Rengy
print( 'Algoritmo de Erdos-Rengy')
print( 'Generando el grafo de 30' )

g = models.erdos_rengy( 30 , 29 )

for i in g.edges.values():
    i.attr["WEIGHT"] = randint( 1, 10 )

dot = g.create_graphviz( 'Erdos_Rengy_30' )

g_d   = g.dijkstra( 0, 29 )
dot_d = g_d.create_graphviz( 'Erdos_Rengy_30_Dijkstra',"WEIGHT", 0)

print( 'Generando el grafo de 500' )

g = models.erdos_rengy( 500 , 499 )

for i in g.edges.values():
    i.attr["WEIGHT"] = randint( 1, 10 )

dot = g.create_graphviz( 'Erdos_Rengy_500' )

g_d   = g.dijkstra( 0, 499 )
dot_d = g_d.create_graphviz( 'Erdos_Rengy_500_Dijkstra',"WEIGHT", 0)

print('Grafos de Erdos Rengy completado')
print('..........................')

#Gilbert
print( 'Algoritmo de Gilbert')
print( 'Generando el grafo 30' )

g = models.gilbert( 30, 0.3 )

for i in g.edges.values():
    i.attr["WEIGHT"] = randint( 1, 10 )

dot = g.create_graphviz( 'Gilbert_30' )

g_d   = g.dijkstra( 0, 29 )
dot_d = g_d.create_graphviz( 'Gilbert_30_Dijkstra',"WEIGHT", 0)

print( 'Generando el grafo de 500' )

g = models.gilbert( 500, 0.2 )

for i in g.edges.values():
    i.attr["WEIGHT"] = randint( 1, 10 )

dot = g.create_graphviz( 'Gilbert_500' )

g_d   = g.dijkstra( 0, 499 )
dot_d = g_d.create_graphviz( 'Gilbert_500_Dijkstra',"WEIGHT", 0)

print('Grafos de Gilbert completado')
print('..........................')

# #Geo simple
print( 'Algoritmo Geográfico simple')
print( 'Generando el grafo 30' )

g = models.geo_simple( 30, 0.4 )

for i in g.edges.values():
    i.attr["WEIGHT"] = randint( 1, 10 )

dot = g.create_graphviz( 'Geo_Simple_30' )

g_d   = g.dijkstra( 0, 29 )
dot_d = g_d.create_graphviz( 'Geo_Simple_30_Dijkstra',"WEIGHT", 0)

print( 'Generando el grafo de 500' )

g = models.geo_simple( 500, 0.2 )

for i in g.edges.values():
    i.attr["WEIGHT"] = randint( 1, 10 )

dot = g.create_graphviz( 'Geo_Simple_500' )

g_d   = g.dijkstra( 0, 499 )
dot_d = g_d.create_graphviz( 'Geo_Simple_500_Dijkstra',"WEIGHT", 0)

print('Grafos de Geográfico simple completado')
print('..........................')

# #Barabasi
print( 'Algoritmo Barabasi')
print( 'Generando el grafo 30' )

g = models.barabasi( 30, 7 )

for i in g.edges.values():
    i.attr["WEIGHT"] = randint( 1, 10 )

dot = g.create_graphviz( 'Barabasi_30' )

g_d   = g.dijkstra( 0, 29 )
dot_d = g_d.create_graphviz( 'Barabasi_30_Dijkstra',"WEIGHT", 0)

print( 'Generando el grafo de 500' )

g = models.barabasi( 500, 30 )

for i in g.edges.values():
    i.attr["WEIGHT"] = randint( 1, 10 )

dot = g.create_graphviz( 'Barabasi_500' )

g_d   = g.dijkstra( 0, 499 )
dot_d = g_d.create_graphviz( 'Barabasi_500_Dijkstra',"WEIGHT", 0)

print('Grafos de Barabasi simple completado')
print('..........................')

#Dorogovtsev_Mendes
print( 'Algoritmo Dorogovtsev Mendes')
print( 'Generando el grafo de 30' )

g = models.dorogovtsev_mendes( 30 )

for i in g.edges.values():
    i.attr["WEIGHT"] = randint( 1, 10 )

dot = g.create_graphviz( 'Dorogovtsev_Mendes_30' )

g_d   = g.dijkstra( 0, 29 )
dot_d = g_d.create_graphviz( 'Dorogovtsev_Mendes_30_Dijkstra',"WEIGHT", 0)

print( 'Generando el grafo de 500' )

g = models.dorogovtsev_mendes( 500 )

for i in g.edges.values():
    i.attr["WEIGHT"] = randint( 1, 10 )

dot = g.create_graphviz( 'Dorogovtsev_Mendes_500' )

g_d   = g.dijkstra( 0, 499 )
dot_d = g_d.create_graphviz( 'Dorogovtsev_Mendes_500_Dijkstra',"WEIGHT", 0)

print('Grafos de Dorogovtsev Mendes simple completado')
print('..........................')
print('Test 3 completado')
