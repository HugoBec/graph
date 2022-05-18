import collections
import sys

from graphviz import Digraph
from graphviz import Graph as Graphviz

import edge
import vertex

# Atributo para indicar si un grafo es dirigido 
DIRECTED = "DIRECTED"

# Atributo para renderizar las imagens de graphviz
RENDER = False

# Indicador si un nodo ha sido descubierto
DISCOVERED = "DISCOVERED"


class Graph:
    def __init__(self, vertices=None, edges=None, attr={}):
        """
           Inicia la clase Grafo, esta almacena llos vertices y las aristas
           param vertices: Diccionario con nodos 
           param edges:    Diccionario con aristas
           param attr:     Propiedades del grafo
        """
        if vertices is None:
            vertices = {}
        self.vertices = vertices

        if edges is None:
            edges = {}
        self.edges = edges

        self.attr = attr

    def add_vertex(self, vertex):
        """ 
            Añade un nodo al grafo, si no existe algún
            otro con el mismo identificador (id) 
            param vertex: Nodo que se añade al grafo
        """
        if vertex.id not in self.vertices.keys():
            self.vertices[vertex.id] = vertex

    def get_vertices(self):
        return self.vertices

    def get_vertex(self, id):
        if id in self.vertices.keys():
            return self.vertices[id]
        else:
            return None

    def add_edge(self, edge, directed=False, auto=False):
        """
            Añade una arista al grafo, si no hay otra
            con la misma fuente y mismo destino
            :param edge: Arista que se va a insertar
            :param directed: Indicador si la arista es dirigida o no
            :param auto: Permite loops
        """
        (v1, v2) = edge.get_id()
        if v1 in self.vertices.keys() and v2 in self.vertices.keys():
            if directed:
                if auto:
                    self.edges[edge.get_id()] = edge
                else:
                    if v1 != v2:
                        self.edges[edge.get_id()] = edge
            else:
                if self.edges.get((v2, v1)) is None:
                    if auto:
                        self.edges[edge.get_id()] = edge
                    else:
                        if v1 != v2:
                            self.edges[edge.get_id()] = edge

    def get_edges(self):
        """
            Las aristas crean aristas en el grafo
        """
        edges = []
        for (key, target) in self.edges.keys():
            edges.append((key, target))
        return edges

    def get_edge(self, id, directed=False):
        """
        Obtiene el nodo por si identificador (id)
        param id: Tupla que identifica a la arista
        param directed: atributo que permite identificar mas rápido a la arista
        """
        (u, v) = id
        for (source, target) in self.edges.keys():
            if directed:
                if (source, target) == (u, v):
                    return self.edges[(source, target)]
            else:
                if (source, target) == (u, v) or (source, target) == (v, u):
                    return self.edges[(source, target)]
        return None

    def get_adjacent_vertices_by_vertex(self, id, type=None):
        """
        Obtiene el nodo adyacente de un nodo especifico
        param id: identificador del nodo en el grafo
        param type: Filter
            None - Todos los vertices adyacentes
            +    - Salida adyacente de los vertices
            -    - Entrada adyacente de los vertices
        """
        vertex = []
        for (source, target) in self.edges.keys():
            if type is None:
                if source == id:
                    vertex.append(target)
                elif target == id:
                    vertex.append(source)
            elif type == '+':
                if source == id:
                    vertex.append(target)
            elif type == '-':
                if target == id:
                    vertex.append(source)

        return vertex

    def get_edges_by_vertex(self, id, type=0):
        """
        Encuentra las artistas que inciden en un nodo con el
        identificador ( id )
        param id: Identificador del nodo en el grafo
        param type: Filtro de salida de las artistas
            1 - Aristas de salida
            2 - Aristas de entrada
            other - Todas las aristas
        return: Una lista de aristas
        """
        edges = []
        for (source, target) in self.edges.keys():
            if type == 1:
                if source == id:
                    edges.append((source, target))
            elif type == 2:
                if target == id:
                    edges.append((source, target))
            else:
                if source == id or target == id:
                    edges.append((source, target))
        return edges

    def clone(self):
        """
        Clona un grafo
        return: El clon de un grafo
        """
        g = Graph(attr=self.attr.copy(), vertices=self.vertices.copy(),
                  edges=self.edges.copy())
        return g


    def create_graphviz(self, file_name, attr_label_vertex=None, source=None,
                        attr_label_edge=None):
        dot = Graphviz()

        # Revisa si el grafo es dirigido
        if DIRECTED in self.attr:
            if self.attr[DIRECTED]:
                dot = Digraph()
            else:
                dot = Graphviz()
        if attr_label_vertex is None:
            # Mapea el grafo en una estructura de graphviz
            for n in list(self.vertices.keys()):
                dot.node(str(n), str(n))
        else:
            # Mapea el grafo a una estructura de graphviz y añade los atribudos de nos nodos
            for n in list(self.vertices.keys()):
                label = "Node: " + str(n)
                source_label = "Node source: " + str(
                    source) if source is not None else ""
                label = label + "\n" + source_label
                label = label + "\n" + attr_label_vertex + " (" + str(
                    self.vertices[n].attributes[attr_label_vertex]) + ")"
                dot.node(str(n), label)

        if attr_label_edge is None:
            for e in self.get_edges():
                (s, t) = e
                dot.edge(str(s), str(t))
        else:
            for e in self.get_edges():
                (s, t) = e
                label_edge = self.edges[(s, t)].attr["WEIGHT"]
                dot.edge(str(s), str(t), label=str(label_edge))

        file = open("./gv/" + file_name + ".gv", "w")
        file.write(dot.source)
        file.close()
        return dot

    ##### Segunda parte

    def bfs(self, s):
        """
        bfs Breadth-First Search es un algoritmo
        para recorrer o buscar estructuras de datos de grafos.
        Comienza en el nodo s
        y explora todos los nodos vecinos a la profundidad actual
        profundidad antes de pasar a los nodos del siguiente nivel de profundidad.
        :param s: nodo raíz para atravesar
        :return g gráfico generado según BFS
        """
        g = Graph(attr={DIRECTED: True})
        root = self.get_vertex(s)
        root.attributes[DISCOVERED] = True
        q = collections.deque()
        adjacent_type = '+' if DIRECTED in self.attr and self.attr[
            DIRECTED] else None
        # Inserta el nodo raiz en el grafo y en la cola de espera
        g.add_vertex(root)
        q.append(s)

        while (len(q) > 0):
            v = q.popleft()
            for e in self.get_adjacent_vertices_by_vertex(v, adjacent_type):
                w = self.get_vertex(e)
                if DISCOVERED not in w.attributes or w.attributes[
                    DISCOVERED] is False:
                    w.attributes[DISCOVERED] = True
                    q.append(w.id)
                    g.add_vertex(w)
                    g.add_edge(edge.Edge(v, e), True)

        # Para poder implementar otro Algoritmo de busqueda en el mismo grafo
        # Se pone los atribudos de los nodos como no recorridos
        for key in self.vertices:
            self.vertices[key].attributes[DISCOVERED] = False

        return g

    def dfs(self, s):
        """
        dfs Depth-First Search (DFS) es un algoritmo para recorrer o buscar estructuras de datos en forma de árbol o grafo.
        El algoritmo comienza en el nodo raíz y explora todo lo posible a lo largo de cada rama antes de retroceder.
        :param s: nodo raíz a recorrer
        :return g gráfico generado según DFS
        """
        g = Graph(attr={DIRECTED: True})
        adjacent_type = '+' if DIRECTED in self.attr and self.attr[
            DIRECTED] else None
        # Insert s root node in stack 
        stack = collections.deque()
        # Initial node does not have origin, it is represented by # 
        stack.append(('#', s))

        while (len(stack) > 0):
            (source, target) = stack.pop()
            w = self.get_vertex(target)
            if DISCOVERED not in w.attributes or w.attributes[
                DISCOVERED] is False:
                w.attributes[DISCOVERED] = True
                g.add_vertex(w)
                if (source != '#'):
                    g.add_edge(edge.Edge(source, w.id), True)
                for e in self.get_adjacent_vertices_by_vertex(w.id,
                                                              adjacent_type):
                    stack.append((w.id, e))

        # Para poder implementar otro Algoritmo de busqueda en el mismo grafo
        # Se pone los atribudos de los nodos como no recorridos
        for key in self.vertices:
            self.vertices[key].attributes[DISCOVERED] = False

        return g

    def dfs_r(self, s):
        """
        dfs_r Depth-First Search (DFSr) recursivo  es un algoritmo para recorrer o buscar estructuras de datos en forma de árbol
        o estructuras de datos de grafos.
        El algoritmo comienza en el nodo raíz y explora todo lo posible a lo largo de cada rama
        antes de retroceder.
        :param s: nodo raíz a recorrer
        :return g gráfico generado según DFS
        """
        g = Graph(attr={DIRECTED: True})

        # Para poder implementar otro Algoritmo de busqueda en el mismo grafo
        # Se pone los atribudos de los nodos como no recorridos
        for key in self.vertices:
            self.vertices[key].attributes[DISCOVERED] = False

        return self.dfs_rec(g, ('#', s))


    def dfs_rec(self, g, s):
        adjacent_type = '+' if DIRECTED in self.attr and self.attr[
            DIRECTED] else None
        (source, target) = s
        w = self.get_vertex(target)
        if DISCOVERED not in w.attributes or w.attributes[DISCOVERED] is False:
            w.attributes[DISCOVERED] = True
            g.add_vertex(w)
            if (source != '#'):
                g.add_edge(edge.Edge(source, w.id), True)
            for e in self.get_adjacent_vertices_by_vertex(w.id, adjacent_type):
                self.dfs_rec(g, (w.id, e))

        return g

    def dijkstra(self, s, t):
        """
        Dijkstra es un algoritmo que busca el camino mas corto entre dos nodos en un grafo
        :param s: node fuente
        :param t: node destino
        :return grafo generado con el camino mas corto entre los nodos
        """
        l = []
        dist = {}
        prev = {}
        discovered = {}
        for v in self.get_vertices():
            dist[v] = float('inf')
            prev[v] = None
            discovered[v] = False
        dist[s] = 0
        l.append((s, dist[s]))
        while len(l) != 0:
            u = min(l, key=lambda x: x[1])
            l.remove(u)
            u = u[0]
            discovered[u] = True
            if u == t:
                break
            for v in self.get_adjacent_vertices_by_vertex(u):
                if not discovered[v]:
                    alt = dist[u] + self.get_edge((u, v)).attr["WEIGHT"]
                    if alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u
                        l.append((v, dist[v]))
        # Crea un grafo de acuerdo a los nodos visitados, almacenados en el arreglo anterior
        u = t
        g = Graph(attr={DIRECTED: True})
        while u is not None:
            g.add_vertex(vertex.Vertex(u, {"WEIGHT": dist[u]}))
            if prev[u] is not None:
                g.add_vertex(vertex.Vertex(prev[u], {"WEIGHT": dist[prev[u]]}))
                g.add_edge(edge.Edge(prev[u], u))
                u = prev[u]
            else:
                break
        return g

    def dijkstra_tree(self, s):
        """
        El árbol de dijkstra es un algoritmo para encontrar el árbol de costos
        de cada nodo de acuerdo al algoritmo de dijkstra;
        :param s: node fuente
        :param t: nodo objetivo
        :return g graph generated with the shortest path from source to target
        """
        l = []
        dist = {}
        prev = {}
        discovered = {}
        g = Graph(attr={DIRECTED: True})
        g.add_vertex(vertex.Vertex(s, {"WEIGHT": 0}))
        for v in self.get_vertices():
            dist[v] = float('inf')
            prev[v] = None
            discovered[v] = False
        dist[s] = 0
        l.append((s, dist[s]))
        while len(l) != 0:
            u = min(l, key=lambda x: x[1])
            l.remove(u)
            u = u[0]
            discovered[u] = True
            for v in self.get_adjacent_vertices_by_vertex(u):
                if not discovered[v]:
                    alt = dist[u] + self.get_edge((u, v)).attr["WEIGHT"]
                    if alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u
                        l.append((v, dist[v]))
                        g.add_vertex(vertex.Vertex(v, {"WEIGHT": dist[v]}))
                        g.add_edge(edge.Edge(u, v, {"WEIGHT": dist[v]}))

        return
