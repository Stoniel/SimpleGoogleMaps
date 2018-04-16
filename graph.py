import networkx as nx
import matplotlib.pyplot as plt
import sys


def display(G):
    pos = nx.spring_layout(G)
    node_colors = []
    for (u, c) in G.nodes(data='color'):
        node_colors.append(c)
    nx.draw_networkx_nodes(G, pos,node_color = node_colors)
    nx.draw_networkx_labels(G, pos)
    edge_colors = []
    print(G.edges(data='color'))
    for (u, v, d) in G.edges(data='color'):
        edge_colors.append(d)
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors)
    nx.draw_networkx_edge_labels(G, pos)
    plt.show()


def find(node):
    if G.node[node]['pi'] == node:
        return node
    return find(G.node[node]['pi'])


def union(node, node1):
    root = find(node)
    root1 = find(node1)
    rank_root = G.node[root]['rank']
    rank_root1 = G.node[root1]['rank']
    if rank_root < rank_root1:
        G.node[root]['pi'] = root1
    elif rank_root > rank_root1:
        G.node[root1]['pi'] = root
    else:
        G.node[root1]['pi'] = root
        G.node[root]['rank'] += 1


def getKey(item):
    return item[2]


def krusk(G):
    edge_index = 0
    mst_index = 0
    sorted_edges = sorted(G.edges(data='weight'), key=getKey)
    result = []
    for (node, pi) in G.nodes(data='pi'):
        G.node[node]['pi'] = node
    print(G.node[node]['pi'])
    while mst_index < len(G.nodes())-1:
        u, v, weight = sorted_edges[edge_index]
        edge_index += 1
        parent_u = find(u)
        parent_v = find(v)
        if parent_u != parent_v:
            mst_index += 1
            result.append([u,v,weight])
            G[u][v]['color'] = 'b'
            G.node[u]['color'] = 'b'
            G.node[v]['color'] = 'b'
            union(parent_u, parent_v)




G = nx.Graph()

G.add_node('a', rank=0, pi=None, color='r')
G.add_node('b', rank=0, pi=None, color='r')
G.add_node('c', rank=0, pi=None, color='r')

G.add_edge('a', 'b', weight=4, color='r')
G.add_edge('a', 'c', weight=3, color='r')
G.add_edge('b', 'c', weight=2, color='r')

krusk(G)
display(G)
