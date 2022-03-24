class Edge:
    """
    Inicializa una arista desde un punto fuente a otro
    :param source: punto de origen
    :param target: punto al que se dirige
    """

    def __init__(self, source, target, attr=None):
        self.source = source
        self.targer = target
        self.edge = (source, target)
        if attr is None:
            self.attr = {}
        else:
            self.attr = attr

    def get_id(self):
        """
        Devuelve la tupla (source, target) que identifica a la arista
        """
        return self.edge
