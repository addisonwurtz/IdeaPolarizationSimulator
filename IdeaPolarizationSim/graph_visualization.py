from math import ceil

import pygraphviz as pgv


def get_visual_graph(graph_data):
    visual_graph = VisualGraph()
    for node in graph_data.nodes:
        visual_graph.set_node_attributes(node)

    for edge in graph_data.edge_weights:
        visual_graph.graph.add_edge(edge)
        visual_graph.graph.add_edges_from(graph_data.edge_weights)

    return visual_graph


class VisualGraph:
    def __init__(self):
        self.graph = pgv.AGraph(directed=False, center='True', bgcolor='transparent',
                                background='transparent', start=1, K=1)
        self.graph.node_attr['shape'] = 'circle'
        self.graph.node_attr['style'] = 'filled'

    def set_graph_attributes(self, graph_data):
        pass

    def read_graph_data(self, graph_data):
        pass

    def set_node_attributes(self, node):
        self.graph.add_node(node.user_id, fillcolor=self.get_node_color(node.opinion_score))

    def set_edge_attributes(self, edge):
        pass

    @staticmethod
    def get_node_color(opinion_score):
        color_code = str(hex(ceil(abs(opinion_score) * 255)))[2:]
        if opinion_score >= 0:
            # score of 1 is yellow, 0 is bright green
            return '#' + color_code + 'ff00'
        else:
            # score of -1 is aqua blue
            return '#00ff' + color_code


