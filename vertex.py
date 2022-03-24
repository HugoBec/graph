class Vertex:
    """
    Inicia a un nodo del grafo
    :param id: identificador unico del nodo 
    :param attr: Propiedades del nodo
    """

    def __init__(self, id, attributes=None):
        self.id = id
        if attributes is None:
            self.attributes = {}
        else:
            self.attributes = attributes
