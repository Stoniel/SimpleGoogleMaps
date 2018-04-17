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
    nodes = []
    while finish != G.nodes[finish]['pi']:
        path.append((finish, G.nodes[finish]['pi']))
        nodes.append((finish))
        finish = G.nodes[finish]['pi']
    #print("path = ", path)
    nx.draw_networkx_edges(G, pos, edgelist=path, edge_color='green')
    nx.draw_networkx_nodes(G, pos, nodelist = nodes, node_color='green')


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
    G.add_node(e1, d=sys.maxsize, pi=None, color='r', visited=True)
    G.add_node(e2, d=sys.maxsize, pi=None, color='r', visited=True)
    G.add_edge(e1, e2, weight=w, color='r')

pos = nx.spring_layout(G)
start = input('Please enter start node')
end = input('Please enter finish node')
temp = end
dijkstra(start)

def get_path(begin, dest):
    path = []
    path.append(end)
    while begin != dest:
        path.append(G.nodes[dest]['pi'])
        dest = G.nodes[dest]['pi']
    path.reverse()
    return path


# path_to_finish = []
# path_to_finish.append(end)
# while start != temp:
#     path_to_finish.append(G.nodes[temp]['pi'])
#     temp = G.nodes[temp]['pi']
# path_to_finish.reverse()
# print(path_to_finish, G.nodes[end]['d'])

path_to_finish = get_path(start, end)
while start != end and path_to_finish:
    start = path_to_finish[0]
    del path_to_finish[0]
    G.nodes[start]['color'] = 'blue'
    to_change = input('Change an edge?')
    if(to_change == 'yes'):
        edge1 = input('Input edge1: ')
        edge2 = input('Input edge2: ')
        w = input('Input Updated weight:')
        G[edge1][edge2]['weight'] = int(w)
        path_to_finish = get_path(start, end)
    dijkstra(start)
    display()
    recolor(end)
    plt.show()
