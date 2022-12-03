from math import ceil

import pygraphviz as pgv


def get_visual_graph(graph_data, time):
    visual_graph = VisualGraph()
    visual_graph.set_graph_attributes(time)
    for node in graph_data.nodes:
        visual_graph.set_node_attributes(node)

    for edge in graph_data.edge_weights:
        visual_graph.graph.add_edge(edge)

    return visual_graph


class VisualGraph:
    def __init__(self):
        self.graph = pgv.AGraph(directed=False, center='True', bgcolor='transparent',
                                background='transparent', dim=3, ratio='1:3', size='22,8', start=1, K=10)
        # self.graph.graph_attr['overlap'] = False
        # self.graph.graph_attr['sep'] = '-0.3'
        # self.graph.graph_attr['beautify'] = True

        self.graph.node_attr['shape'] = 'circle'
        self.graph.node_attr['style'] = 'filled'
        self.graph.node_attr['fontcolor'] = 'white'
        self.graph.node_attr['fixedsize'] = True
        self.graph.node_attr['width'] = 0.5
        self.graph.node_attr['height'] = 0.5

        self.graph.edge_attr['penwidth'] = 0.25

    def set_graph_attributes(self, time):
        # self.graph.graph_attr['label'] = 'Edge Homogeneity: ' + str(edge_homogeneity)
        self.graph.graph_attr['label'] = 'Time: ' + str(time)
        self.graph.graph_attr['fontsize'] = 34.0

    def read_graph_data(self, graph_data):
        pass

    def set_node_attributes(self, node):
        # self.graph.add_node(node.user_id, fillcolor=self.get_node_color(node.opinion_score))
        self.graph.add_node(node.user_id, label=round(node.opinion_score, 1), fillcolor=self.get_node_color(node.opinion_score))

    def set_edge_attributes(self, edge):
        pass

    @staticmethod
    def get_node_color(opinion_score):
        color_code = str(hex(ceil(abs(opinion_score) * 255)))[2:]
        if opinion_score >= 0:
            # score of 1 is yellow, 0 is bright green
            #return '#' + color_code + 'A000'
            #return '#' + color_code + 'ff00'
            return '#' + color_code + '0000'
        else:
            # score of -1 is aqua blue
            #return '#00A0' + color_code
            #return '#00ff' + color_code
            return '#0000' + color_code


