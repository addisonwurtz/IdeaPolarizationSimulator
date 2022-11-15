import pygraphviz as pgv
import toy_graph

graph = pgv.AGraph(directed=False)

for edge in toy_graph.edge_weights:
    graph.add_edge(edge)
    graph.add_edges_from(toy_graph.edge_weights)

graph.draw('Graph_Images/graph.png', prog='fdp')
