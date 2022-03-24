import time
from graph import DIRECTED
import models

init = time.time()

print( "Iniciando tests" )

#mesh
g    = models.mesh( 30, 30 )
dot  = g.create_graphviz('Mesh_30x30')

g    = models.mesh( 100, 10 )
dot  = g.create_graphviz('Mesh_100x10')

g    = models.mesh( 500, 150 )
dot  = g.create_graphviz('Mesh_500x150')

#erdos_rengy
g   = models.erdos_rengy( 30, 30)
dot = g.create_graphviz( 'Erdos_Rengy_30x30' )

g    = models.erdos_rengy( 100, 100 )
dot  = g.create_graphviz('Erdos_Rengy_100x100')

g    = models.erdos_rengy( 500, 500 )
dot  = g.create_graphviz('Erdos_Rengy_500x500')

#gilbert
g   = models.gilbert( 30, .5 )
dot = g.create_graphviz( 'Gilbert_30x.5' )

g    = models.gilbert( 100, .5 )
dot  = g.create_graphviz('Gilbert_100x.5')

g    = models.gilbert( 500, .5 )
dot  = g.create_graphviz('Gilbert_500x.5')

#geo
g   = models.geo_simple( 30, .5 )
dot = g.create_graphviz( 'Geo_Simple_30x.5' )

g    = models.geo_simple( 100, .5 )
dot  = g.create_graphviz('Geo_Simple_100x.5')

g    = models.geo_simple( 500, .5 )
dot  = g.create_graphviz('Geo_Simple_500x.5')

#barabasi
g   = models.barabasi( 30, 15 )
dot = g.create_graphviz( 'barabasi_30x15' )

g    = models.barabasi( 100, 52 )
dot  = g.create_graphviz('barabasi_100x52')

g    = models.barabasi( 500, 100 )
dot  = g.create_graphviz('barabasi_500x100')

#dorogovtsev_mendes()
g   = models.dorogovtsev_mendes( 30, True )
dot = g.create_graphviz( 'dorogovtsev_mendes_30_T' )

g    = models.dorogovtsev_mendes( 100, True )
dot  = g.create_graphviz('dorogovtsev_mendes_100_T')

g    = models.dorogovtsev_mendes( 500, True )
dot  = g.create_graphviz('dorogovtsev_mendes_500_T')

end = time.time()

print("Tests finalizados, segundos transcurrido: ")
print( end - init )
