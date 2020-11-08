import networkx as nx
import matplotlib.pyplot as plt


class RoadNet:
    def __init__(self, edges):
        self.G = nx.Graph()
        self.G.add_edges_from(edges)

    def show(self):
        plt.figure("GraphVisual")
        nx.draw(self.G, with_labels=True)
        plt.show()
