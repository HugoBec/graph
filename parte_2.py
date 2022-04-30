import time
from graph import DIRECTED
import models

#Mesh
print( '.....................')
print( 'Algoritmo de Malla')
print( 'Generando el grafo 30' )

g    = models.mesh( 15, 2 )
dot  = g.create_graphviz('Mesh_30')

print( 'Iniciando los algoritmos de busqueda' )

g_bfs   = g.bfs(0)
dot_bfs = g_bfs.create_graphviz('Mesh_30_bfs')

print('...')

g_dfs   = g.dfs(0)
dot_dfs = g_dfs.create_graphviz('Mesh_30_bfs')

print('...')

g_dfs_r   = g.dfs_r(0)
dot_dfs_r = g_dfs_r.create_graphviz('Mesh_30_bfs_r')

print( 'Generando el grafo 100' )

g    = models.mesh( 10, 10 )
dot  = g.create_graphviz('Mesh_100')

print( 'Iniciando los algoritmos de busqueda' )

g_bfs   = g.bfs(0)
dot_bfs = g_bfs.create_graphviz('Mesh_100_bfs')

print('...')

g_dfs   = g.dfs(0)
dot_dfs = g_dfs.create_graphviz('Mesh_100_bfs')

print('...')

g_dfs_r   = g.dfs_r(0)
dot_dfs_r = g_dfs_r.create_graphviz('Mesh_100_bfs_rec')

print( 'Generando el grafo 500' )

g    = models.mesh( 25, 20 )
dot  = g.create_graphviz('Mesh_500')

print( 'Iniciando los algoritmos de busqueda' )

g_bfs   = g.bfs(0)
dot_bfs = g_bfs.create_graphviz('Mesh_500_bfs')

print('...')

g_dfs   = g.dfs(0)
dot_dfs = g_dfs.create_graphviz('Mesh_500_bfs')

print('...')

g_dfs_r   = g.dfs_r(0)
dot_dfs_r = g_dfs_r.create_graphviz('Mesh_500_bfs_rec')

print('Grafos de Malla completado')
print('..........................')

#ERdos Rengy
print( 'Algoritmo de Erdos-Rengy')
print( 'Generando el grafo 30' )

g    = models.erdos_rengy( 30, 45 )
dot  = g.create_graphviz('Erdos_Rengy_30')

print( 'Iniciando los algoritmos de busqueda' )

g_bfs   = g.bfs(0)
dot_bfs = g_bfs.create_graphviz('Erdos_Rengy_bfs_30')

print('...')

g_dfs   = g.dfs(0)
dot_dfs = g_dfs.create_graphviz('Erdos_Rengy_dfs_30')

print('...')

g_dfs_r   = g.dfs_r(0)
dot_dfs_r = g_dfs_r.create_graphviz('Erdos_Rengy_dfs_r_30')

print( 'Generando el grafo 100' )

g    = models.erdos_rengy( 100, 250 )
dot  = g.create_graphviz('Erdos_Rengy_100')

print( 'Iniciando los algoritmos de busqueda' )

g_bfs   = g.bfs(0)
dot_bfs = g_bfs.create_graphviz('Erdos_Rengy_100_bfs')

print('...')

g_dfs   = g.dfs(0)
dot_dfs = g_dfs.create_graphviz('Erdos_Rengy_100_dfs')

print('...')

g_dfs_r   = g.dfs_r(0)
dot_dfs_r = g_dfs_r.create_graphviz('Erdos_Rengy_100_dfs_rec')

print( 'Generando el grafo 500' )

g    = models.erdos_rengy( 500, 750 )
dot  = g.create_graphviz('Erdos_Rengy_500')

print( 'Iniciando los algoritmos de busqueda' )

g_bfs   = g.bfs(0)
dot_bfs = g_bfs.create_graphviz('Erdos_Rengy_500_bfs')

print('...')

g_dfs   = g.dfs(0)
dot_dfs = g_dfs.create_graphviz('Erdos_Rengy_500_dfs')

print('...')

g_dfs_r   = g.dfs_r(0)
dot_dfs_r = g_dfs_r.create_graphviz('Erdos_Rengy_500_dfs_rec')

print('Grafos de Erdos Rengy completado')
print('..........................')


#Gilbert
print( 'Algoritmo de Gilbert')
print( 'Generando el grafo 30' )

g    = models.gilbert( 30, .3 )
dot  = g.create_graphviz('Gilbert_30')

print( 'Iniciando los algoritmos de busqueda' )

g_bfs   = g.bfs(0)
dot_bfs = g_bfs.create_graphviz('Gilbert_30_bfs')

print('...')

g_dfs   = g.dfs(0)
dot_dfs = g_dfs.create_graphviz('Gilbert_30_dfs')

print('...')

g_dfs_r   = g.dfs_r(0)
dot_dfs_r = g_dfs_r.create_graphviz('Gilbert_30_dfs_rec')

print( 'Generando el grafo 100' )

g    = models.gilbert( 100, .3 )
dot  = g.create_graphviz('Gilbert_100')

print( 'Iniciando los algoritmos de busqueda' )

g_bfs   = g.bfs(0)
dot_bfs = g_bfs.create_graphviz('Gilbert_100_bfs')

print('...')

g_dfs   = g.dfs(0)
dot_dfs = g_dfs.create_graphviz('Gilbert_100_dfs')

print('...')

g_dfs_r   = g.dfs_r(0)
dot_dfs_r = g_dfs_r.create_graphviz('Gilbert_100_dfs_rec')

print( 'Generando el grafo 500' )

g    = models.gilbert( 500, .2 )
dot  = g.create_graphviz('Gilbert_500')

print( 'Iniciando los algoritmos de busqueda' )

g_bfs   = g.bfs(0)
dot_bfs = g_bfs.create_graphviz('Gilbert_500_bfs')

print('...')

g_dfs   = g.dfs(0)
dot_dfs = g_dfs.create_graphviz('Gilbert_500_dfs')

print('...')

g_dfs_r   = g.dfs_r(0)
dot_dfs_r = g_dfs_r.create_graphviz('Gilbert_500_dfs_rec')

print('Grafos de Gilbert completado')
print('..........................')

#Geo simple
print( 'Algoritmo Geográfico simple')
print( 'Generando el grafo 30' )

g    = models.geo_simple( 30, .3 )
dot  = g.create_graphviz('Geo_30')

print( 'Iniciando los algoritmos de busqueda' )

g_bfs   = g.bfs(0)
dot_bfs = g_bfs.create_graphviz('Geo_30_bfs')

print('...')

g_dfs   = g.dfs(0)
dot_dfs = g_dfs.create_graphviz('Geo_30_dfs')

print('...')

g_dfs_r   = g.dfs_r(0)
dot_dfs_r = g_dfs_r.create_graphviz('Geo_30_dfs_rec')

print( 'Generando el grafo 100' )

g    = models.geo_simple( 100, .3 )
dot  = g.create_graphviz('Geo_100')

print( 'Iniciando los algoritmos de busqueda' )

g_bfs   = g.bfs(0)
dot_bfs = g_bfs.create_graphviz('Geo_100_bfs')

print('...')

g_dfs   = g.dfs(0)
dot_dfs = g_dfs.create_graphviz('Geo_100_dfs')

print('...')

g_dfs_r   = g.dfs_r(0)
dot_dfs_r = g_dfs_r.create_graphviz('Geo_100_dfs_rec')

print( 'Generando el grafo 500' )

g    = models.geo_simple( 500, .2 )
dot  = g.create_graphviz('Geo_500')

print( 'Iniciando los algoritmos de busqueda' )

g_bfs   = g.bfs(0)
dot_bfs = g_bfs.create_graphviz('Geo_500_bfs')

print('...')

g_dfs   = g.dfs(0)
dot_dfs = g_dfs.create_graphviz('Geo_500_dfs')

print('...')

g_dfs_r   = g.dfs_r(0)
dot_dfs_r = g_dfs_r.create_graphviz('Geo_500_dfs_rec')

print('Grafos de Geográfico simple completado')
print('..........................')

#Barabasi
print( 'Algoritmo Barabasi')
print( 'Generando el grafo 30' )

g    = models.barabasi( 30, 15 )
dot  = g.create_graphviz('Barabasi_30')

print( 'Iniciando los algoritmos de busqueda' )

g_bfs   = g.bfs(0)
dot_bfs = g_bfs.create_graphviz('Barabasi_30_bfs')

print('...')

g_dfs   = g.dfs(0)
dot_dfs = g_dfs.create_graphviz('Barabasi_30_dfs')

print('...')

g_dfs_r   = g.dfs_r(0)
dot_dfs_r = g_dfs_r.create_graphviz('Barabasi_30_dfs_rec')

print( 'Generando el grafo 100' )

g    = models.barabasi( 100, 68 )
dot  = g.create_graphviz('Barabasi_100')

print( 'Iniciando los algoritmos de busqueda' )

g_bfs   = g.bfs(0)
dot_bfs = g_bfs.create_graphviz('Barabasi_100_bfs')

print('...')

g_dfs   = g.dfs(0)
dot_dfs = g_dfs.create_graphviz('Barabasi_100_dfs')

print('...')

g_dfs_r   = g.dfs_r(0)
dot_dfs_r = g_dfs_r.create_graphviz('Barabasi_100_dfs_rec')

print( 'Generando el grafo 500' )

g    = models.barabasi( 500, 15 )
dot  = g.create_graphviz('Barabasi_500')

print( 'Iniciando los algoritmos de busqueda' )

g_bfs   = g.bfs(0)
dot_bfs = g_bfs.create_graphviz('Barabasi_500_bfs')

print('...')

g_dfs   = g.dfs(0)
dot_dfs = g_dfs.create_graphviz('Barabasi_500_dfs')

print('...')

g_dfs_r   = g.dfs_r(0)
dot_dfs_r = g_dfs_r.create_graphviz('Barabasi_500_dfs_rec')

print('Grafos de Barabasi simple completado')
print('..........................')

#Dorogovtsev_Mendes
print( 'Algoritmo Dorogovtsev Mendes')
print( 'Generando el grafo 30' )

g    = models.dorogovtsev_mendes( 30 )
dot  = g.create_graphviz('Dorogovtsev_Mendes_30')

print( 'Iniciando los algoritmos de busqueda' )

g_bfs   = g.bfs(0)
dot_bfs = g_bfs.create_graphviz('Dorogovtsev_Mendes_30_bfs')

print('...')

g_dfs   = g.dfs(0)
dot_dfs = g_dfs.create_graphviz('Dorogovtsev_Mendes_30_dfs')

print('...')

g_dfs_r   = g.dfs_r(0)
dot_dfs_r = g_dfs_r.create_graphviz('Dorogovtsev_Mendes_30_dfs_rec')

print( 'Generando el grafo 100' )

g    = models.dorogovtsev_mendes( 100 )
dot  = g.create_graphviz('Dorogovtsev_Mendes_100')

print( 'Iniciando los algoritmos de busqueda' )

g_bfs   = g.bfs(0)
dot_bfs = g_bfs.create_graphviz('Dorogovtsev_Mendes_100_bfs')

print('...')

g_dfs   = g.dfs(0)
dot_dfs = g_dfs.create_graphviz('Dorogovtsev_Mendes_100_dfs')

print('...')

g_dfs_r   = g.dfs_r(0)
dot_dfs_r = g_dfs_r.create_graphviz('Dorogovtsev_Mendes_100_dfs_rec')

print( 'Generando el grafo 500' )

g    = models.dorogovtsev_mendes( 500 )
dot  = g.create_graphviz('Dorogovtsev_Mendes_500')

print( 'Iniciando los algoritmos de busqueda' )

g_bfs   = g.bfs(0)
dot_bfs = g_bfs.create_graphviz('Dorogovtsev_Mendes_500_bfs')

print('...')

g_dfs   = g.dfs(0)
dot_dfs = g_dfs.create_graphviz('Dorogovtsev_Mendes_500_dfs')

print('...')

g_dfs_r   = g.dfs_r(0)
dot_dfs_r = g_dfs_r.create_graphviz('Dorogovtsev_Mendes_500_dfs')

print('Grafos de Dorogovtsev Mendes simple completado')
print('..........................')
print('Test 2 completado')
