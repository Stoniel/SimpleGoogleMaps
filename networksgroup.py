from heapq import heappush, heappop
from typing import List
import networkx as nx
import matplotlib.pyplot as plt
import sys


def dijkstra(start):
    G.nodes[start]['d'] = 0
    G.nodes[start]['pi'] = start
    my_heap = [start]
    visited = []
    while my_heap:
        current = heappop(my_heap)
        if current not in visited:
            visited.append(current)
            for n in G.neighbors(current):
                weight = G[current][n]['weight']
                if n not in visited:
                    if weight + G.nodes[current]['d'] < G.nodes[n]['d']:
                        G.nodes[n]['d'] = weight + G.nodes[current]['d']
                        G.nodes[n]['pi'] = current
                    heappush(my_heap, n)





#graph initialization from geeksforgeeks code for dijkstras from my brain

G = nx.Graph()
edges = [
        ("A", "B", 3),
        ("A", "D", 6),
        ("B", "C", 1),
        ("B", "D", 3),
        ("B", "E", 5),
        ("C", "E", 6),
        ("D", "E", 5),
        ("D", "F", 9),
        ("E", "F", 1),
        ("E", "G", 1),
        ("F", "G", 2)
]
for (e1, e2, w) in edges:
    G.add_node(e1, color='r', pi=None, d=sys.maxsize)
    G.add_node(e2, color='r', pi=None, d=sys.maxsize)
    G.add_edge(e1, e2, weight=w, color='r')

start = 'A'
dijkstra('A')
for e in G.nodes(data=True):
    print(e)
path_to_finish = []
end = 'G'
path_to_finish.append(end)
while start != end:
    path_to_finish.append(G.nodes[end]['pi'])
    end = G.nodes[end]['pi']
path_to_finish.reverse()
print(path_to_finish)

