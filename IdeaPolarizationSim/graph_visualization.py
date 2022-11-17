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
        self.graph = pgv.AGraph(directed=False, center='True', bgcolor='white', label='Social Network',
                                background='transparent')
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
        match opinion_score:
            case -1:
                return'#960064'
            case -.9:
                return'#960c64'
            case -.8:
                return'#961864'
            case -.7:
                return'#962464'
            case -.6:
                return '#963064'
            case -.5:
                return '#963c64'
            case -.4:
                return '#964864'
            case -.3:
                return '#965464'
            case -.2:
                return '#966064'
            case -.1:
                return '#966c64'
            case 0:
                return '#967864'
            case .1:
                return '#968464'
            case .2:
                return '#969064'
            case .3:
                return '#969c64'
            case .4:
                return '#96a864'
            case .5:
                return '#96b464'
            case .5:
                return '#96c064'
            case .6:
                return '#96cc64'
            case .7:
                return '#96d864'
            case .8:
                return '#96e464'
            case .9:
                return '#96f064'
            case 1:
                return '#96ff64'
            case _:
                return '#f6f000'
