# Graph

from collections import defaultdict

graph = defaultdict(list)


def add_Edges(graph, u, v):
    graph[u].append(v)


def gen_graph(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges


add_Edges(graph, 'a', 'c')
add_Edges(graph,'b','c')

print(gen_graph(graph))