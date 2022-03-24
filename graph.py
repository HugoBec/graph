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

