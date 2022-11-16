import pygraphviz as pgv


def set_graph_attributes(graph):
    graph.graph_attr['label'] = 'Social Network'
    graph.graph_attr['center'] = 'True'
    graph.graph_attr['bgcolor'] = 'lightblue'
    # graph.graph_attr['colorscheme'] = ''

    graph.node_attr['shape'] = 'circle'
    graph.node_attr['style'] = 'filled'


class GraphVisualization:
    def __init__(self):
        self.graph = pgv.AGraph(directed=False, label='Social Network', background='transparent')

    def read_graph_date(graph_data):
        pass

    def set_node_attributes(graph):
        pass
