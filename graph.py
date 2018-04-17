import networkx as nx
import matplotlib.pyplot as plt
import sys


def display(G):
    pos = nx.spring_layout(G)
    node_colors = []
    for (u, c) in G.nodes(data='color'):
        node_colors.append(c)
    nx.draw_networkx_nodes(G, pos, node_color = node_colors)
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

    plt.show()


def recolor(mst):
    for (u, v) in G.edges():
        G[u][v]['color'] = 'r'
        G.node[u]['color'] = 'r'
        G.node[v]['color'] = 'r'

    for (u, v, d) in G.edges(data='weight'):
        if (u, v, d) in mst:
            G[u][v]['color'] = 'b'
            G.node[u]['color'] = 'b'
            G.node[v]['color'] = 'b'


visited = []
parent = []

def dfs(mst, edge):
    visited[edge] = True
    for i in G.neighbors(edge):
        if i in mst and not visited[i]:
            parent[i] = edge
            dfs(i)


def find_cycle(mst,edge):
    visited = [False]*len(G.nodes())
    dfs(mst, edge)




def update_mst(min_tree, edge1, edge2, change):
    if (edge1, edge2) in min_tree and change > 0:  #In MST and increased
        print('present')
    elif not((edge1, edge2) in min_tree) and change < 0:  #Not in MST and decreased
        min_tree.append((edge1, edge2, G[edge1][edge2]['weight']))
        #min_tree = sorted(min_tree, key=lambda x: x[2])
        print(min_tree)
        del min_tree[len(min_tree)-1]
        recolor(min_tree)
    else:
        print('No changes need to be made.')
        return


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


def krusk(G):
    edge_index = 0
    mst_index = 0
    sorted_edges = sorted(G.edges(data='weight'), key=lambda x:x[2])
    result = []
    for (node, pi) in G.nodes(data='pi'):
        G.node[node]['pi'] = node
    while mst_index < len(G.nodes())-1:
        u, v, weight = sorted_edges[edge_index]
        edge_index += 1
        parent_u = find(u)
        parent_v = find(v)
        if parent_u != parent_v:
            mst_index += 1
            result.append((u, v, weight))
            # G[u][v]['color'] = 'b'
            # G.node[u]['color'] = 'b'
            # G.node[v]['color'] = 'b'
            union(parent_u, parent_v)
    return result


G = nx.Graph()
G.add_node('a', rank=0, pi=None, color='r')
G.add_node('b', rank=0, pi=None, color='r')
G.add_node('c', rank=0, pi=None, color='r')
G.add_node('d', rank=0, pi=None, color='r')
G.add_node('e', rank=0, pi=None, color='r')

G.add_edge('a', 'b', weight=4, color='r')
G.add_edge('a', 'c', weight=3, color='r')
G.add_edge('a', 'd', weight=2, color='r')
G.add_edge('c', 'd', weight=5, color='r')
G.add_edge('b', 'c', weight=2, color='r')
G.add_edge('b', 'e', weight=9, color='r')

MST = krusk(G)
print(MST)
recolor(MST)
display(G)
new_weight = 1
diff = new_weight - G['a']['b']['weight']
G['a']['b']['weight'] = new_weight
update_mst(MST, 'a', 'b', diff)

display(G)
