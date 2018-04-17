from typing import List

import networkx as nx
import matplotlib.pyplot as plt
import sys


def recolor(fin):
    for (u, v) in G.edges():
        G[u][v]['color'] = 'r'
        G.nodes[u]['color'] = 'r'
        G.nodes[v]['color'] = 'r'

    #PATH TO GREEN TODO
    #path = [(node, attrs['pi']) for node, attrs in G.nodes.data()]
    finish = fin
    path = []

    while finish != G.nodes[finish]['pi']:
        path.append((finish, G.nodes[finish]['pi']))
        finish = G.nodes[finish]['pi']
    print("path = ", path)
    nx.draw_networkx_edges(G, pos, edgelist=path, edge_color='green')


def display():
    node_colors = []
    node_labels = []
    for (u, c) in G.nodes(data='color'):
        node_colors.append(c)
        node_labels.append(u)
    nx.draw_networkx_nodes(G, pos, node_color=node_colors)
    nx.draw_networkx_labels(G, pos)
    edge_colors = []
    for (u, v, d) in G.edges(data='color'):
        edge_colors.append(d)
    weights = []
    for (u, v, d) in G.edges(data='weight'):
        weights.append(d)

    labels = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)


def dijkstra(start):
    for i in G.nodes():
        G.nodes[i]['pi'] = None
        G.nodes[i]['d'] = sys.maxsize

    q = set(G.nodes)
    G.node[start]['d'] = 0
    G.node[start]['pi'] = start

    while q:
        u = min(q, key=lambda x: G.nodes[x]['d'])
        q.remove(u)
        for v in G.neighbors(u):
            alt = G.node[u]['d'] + G[u][v]['weight']
            if alt < G.node[v]['d']:
                G.node[v]['d'] = alt
                G.node[v]['pi'] = u


G = nx.Graph()
G.add_node('a', d=sys.maxsize, pi=None, color='r', visited=True)
G.add_node('b', d=sys.maxsize, pi=None, color='r', visited=True)
G.add_node('c', d=sys.maxsize, pi=None, color='r', visited=True)
G.add_node('d', d=sys.maxsize, pi=None, color='r', visited=True)
G.add_node('e', d=sys.maxsize, pi=None, color='r', visited=True)

G.add_edge('a', 'b', weight=4, color='r')
G.add_edge('a', 'c', weight=3, color='r')
G.add_edge('a', 'd', weight=2, color='r')
G.add_edge('c', 'd', weight=5, color='r')
G.add_edge('b', 'c', weight=2, color='r')
G.add_edge('b', 'e', weight=9, color='r')
pos = nx.spring_layout(G)
start = 'e'
end = 'd'
dijkstra(start)
path_to_finish = []
path_to_finish.append(end)
while start != end:
    path_to_finish.append(G.nodes[end]['pi'])
    end = G.nodes[end]['pi']
path_to_finish.reverse()
print(path_to_finish)

end = 'd'
while start != end and path_to_finish:
    start = path_to_finish[0]
    del path_to_finish[0]
    dijkstra(start)
    display()
    recolor(end)
    plt.show()
