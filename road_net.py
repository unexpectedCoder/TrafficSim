import networkx as nx


class RoadNet:
    def __init__(self, crossroads):
        self.G = nx.Graph()
        self.G.add_nodes_from(crossroads)
