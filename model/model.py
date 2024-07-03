from datetime import datetime

import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._grafo = nx.Graph()

    def buildGraph(self, anno):
        self._countries = DAO.getAllCountries(anno)
        self._idMap = {}
        for country in self._countries:
            self._idMap[country.CCode] = country

        self._grafo.clear()
        borders = DAO.getCountryPairs(self._idMap, anno)
        self._grafo.add_nodes_from(self._countries)
        for b in borders:
            self._grafo.add_edge(b.c1, b.c2)

    def getNodes(self):
        return list(self._grafo.nodes)

    def getNumConfinanti(self, v):
        return len(list(self._grafo.neighbors(v)))

    def getNumCompConnesse(self):
        return nx.number_connected_components(self._grafo)

    def getRaggiungibiliBFS(self, n):
        tree = nx.bfs_tree(self._grafo, n)
        a = list(tree.nodes)
        a.remove(n)
        return a

    def getRaggiungibili(self, n):
        tic = datetime.now()
        a = self.getRaggiungibiliBFS(n)
        print(f"DFS: {datetime.now() - tic} - {len(a)}")
        return a




