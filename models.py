import math
import random
from random import randint
from random import random

import graph
import edge
import vertex

# Cordenadas 
COORDINATE_X = "x"
COORDINATE_Y = "y"


def mesh(m, n, directed=False):
    """
    Crea un grado con el metodo de malla de m x m
    :param m: Numero de columnas debe ser mayor a 1
    :param n: Numero de filas debe ser mayor a 1
    :param directed: indica si el grafo es dirigido
    :return: El grafo ya generado
    """
    # Valida los parametros 
    if m <= 1 or n <= 1:
        raise ValueError("m,n parameters must to be > 1")

    g = graph.Graph()
    # Añade el atributo "Dirigido" 
    g.attr[graph.DIRECTED] = directed

    for i in range(m * n):
        v = vertex.Vertex(i)
        g.add_vertex(v)
    index = 0
    for i in range(m):
        for j in range(n):
            if i != (m - 1):
                g.add_edge(edge.Edge(index, (index + n)), directed)
            if j != (n - 1):
                g.add_edge(edge.Edge(index, (index + 1)), directed)
            index = index + 1
    return g


def erdos_rengy(n, m, directed=False, auto=False):
    """
    Cread un grtafo de n nodos con el modelo de Erdos Rengy
    :param n: Numero de nodos debe ser mayor a 1
    :param m: Numero de aristas deben ser mayores a n - 1
    :param directed: Indica si el grafo es dirigido
    :param auto: Permite bucles
    :return: El grafo construido
    """
    # Valida los parametros 
    if n <= 0:
        raise ValueError("n parameter must to be > 0 ")
    if m < n - 1:
        raise ValueError("m parameter must to be >= n-1 ")

    g = graph.Graph()
    # Añada el atributo de dirigido al grafo
    g.attr[graph.DIRECTED] = directed

    for i in range(n):
        g.add_vertex(vertex.Vertex(i))
    edges = {}
    while len(g.edges) != m:
        # Cread un un numer m de diferentes aristas aleatorias 
        source = randint(0, m - 1)
        target = randint(0, m - 1)
        e = (source, target)
        if e not in edges:
            edges[e] = e
            g.add_edge(edge.Edge(source, target), directed, auto)
    return g


def gilbert(n, p, directed=False, auto=False):
    """
    Crea un grafo de n nodos con el modelo de Gilbert
    :param n: Numero de nodos debe ser mayour a 0
    :param p: Probabilidad de crear una arista entre 1 y 0
    :param directed: Establece si el grafo es dirigido
    :param auto: Permite bucles
    :return: El grafo construido
    """
    # Valida los parametros
    if n <= 0:
        raise ValueError("n parameter must to be > 0 ")
    if p <= 0 or p >= 1:
        raise ValueError("p parameter must to be in range (0,1)")

    g = graph.Graph()
    # Añade el atributo de dirigido en el grafo
    g.attr[graph.DIRECTED] = directed

    for i in range(n):
        g.add_vertex(vertex.Vertex(i))
    for i in range(n):
        for j in range(n):
            # Crea una artista con la probabilidad indicada
            if random() <= p:
                g.add_edge(edge.Edge(i, j), directed, auto)

    return g


def geo_simple(n, r, directed=False, auto=False):
    """
    Crea un grafo aleatorio con el modelo geografico simple
    :param n: Numero de nodos mayor a 0
    :param r: Distancia maxima para generar los nodos entre 1 y 0
    :param directed: Indica si el grafo es dirigido
    :param auto: Permite bucles  
    :return: Grafo ya generado
    """
    # Valida los parametros
    if n <= 0:
        raise ValueError("n parameter must to be > 0 ")
    if r <= 0 or r >= 1:
        raise ValueError("r parameter must to be in range (0,1)")

    g = graph.Graph()
    # Añade el atributo de  dirigido al grafo
    g.attr[graph.DIRECTED] = directed

    # Crea n nodos con las coordenadas uniformes 
    for i in range(n):
        g.add_vertex(
            vertex.Vertex(i, {COORDINATE_X: random(), COORDINATE_Y: random()}))

    # Crea una arista entre dos nodos si la distancia es menor a r
    for i in range(n):
        for j in range(n):
            # Calcula la distancia entre dos puntos
            p1 = (g.get_vertex(i).attributes[COORDINATE_X],
                  g.get_vertex(i).attributes[COORDINATE_Y])
            p2 = (g.get_vertex(j).attributes[COORDINATE_X],
                  g.get_vertex(j).attributes[COORDINATE_Y])
            d = calculate_distance(p1, p2)
            if d <= r:
                g.add_edge(edge.Edge(i, j), directed, auto)
    return g


def barabasi(n, d, directed=False, auto=False):
    """
    Crea un grafo Barabasi-Albert
    :param n: Numer ode nodos mayor a 0
    :param d: Numero maximo de aristas en los nodos, de be ser mayor a 1
    :param directed: Indica si el grafo es dirigido
    :param auto: Permite bucle
    return: Grafo generado
    """
    #Valida los parametros
    if n <= 0:
        raise ValueError("n parameter must to be > 0 ")
    if d <= 1:
        raise ValueError("d parameter must to be > 1")

    g = graph.Graph()
    # Añade el atributo de dirigido al grafo
    g.attr[graph.DIRECTED] = directed

    # Los primeros d nodos son creados con aristas para relacionarlos con los demas 
    for i in range(d):
        g.add_vertex(vertex.Vertex(i))
    for i in range(d):
        for j in range(d):
            if len(g.get_edges_by_vertex(i)) < d and len(
                    g.get_edges_by_vertex(j)) < d:
                g.add_edge(edge.Edge(i, j), directed, auto)

    for i in range(d, n):
        g.add_vertex(vertex.Vertex(i))
        for j in range(i):
            # La probalidad p de que un nuevo nodo i sea conectado al nodo j
            # es el grado de de nodos j dividido entre el numero de aristas de grafo
            p = len(g.get_edges_by_vertex(j)) / len(g.get_edges())
            if len(g.get_edges_by_vertex(i)) < d and len(
                    g.get_edges_by_vertex(j)) < d and p >= random():
                g.add_edge(edge.Edge(i, j), directed, auto)
    return g


def dorogovtsev_mendes(n, directed=False):
    """
    Crea un grafo Dorogovtsev-Mendes
    :param n: numero de nodos
    :param directed: Indica si el grafo es dirigido
    :return: graph created
    """
    # Valida los parametros
    if n < 3:
        raise ValueError("n parameter must to be >= 3 ")

    g = graph.Graph()
    # Añade el atributo de dirigido al grafo
    g.attr[graph.DIRECTED] = directed

    # Crea 3 nodos y 3 arista para formar un triangulo
    for i in range(3):
        g.add_vertex(vertex.Vertex(i))
    for i in range(3):
        j = i + 1 if i < 2 else 0
        g.add_edge(edge.Edge(i, j), directed)

    # Para añadir los nodos siguiente uno a uno, se elige de manera aleatoria una arista del grafo
    # y crea las aristas entre un nuevo nodo y da origen a la fuente de la arista seleccionada
    for i in range(3, n):
        g.add_vertex(vertex.Vertex(i))
        # Selecciona una arista al azar
        id_edge = randint(0, len(g.get_edges()) - 1)
        edge_selected = g.get_edges()[id_edge]
        (source, target) = edge_selected
        # Crea aristas entre un nuevo nodo y da origen a la fuente de la arista seleccionada
        g.add_edge(edge.Edge(i, source), directed)
        g.add_edge(edge.Edge(i, target), directed)

    return g


def calculate_distance(p1, p2):
    """
    Calcula la distavnia entre 2 nodos
    param p1: tupla de cordenadas x,y del nodo 1
    param p2: tupla de cordenadas x,y del nodo 2
    return: Distancia entre los nodos
    """
    x1, y1 = p1
    x2, y2 = p2
    d = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    return d
