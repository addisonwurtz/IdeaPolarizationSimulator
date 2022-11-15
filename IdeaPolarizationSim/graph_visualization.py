import pygraphviz as pgv
import toy_graph

graph = pgv.AGraph(directed=False)
graph.add_nodes_from(toy_graph.nodes)
