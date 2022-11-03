
class SocialNetwork:
    def __init__(self, graph, users: [], news_items: [], update_rate):
        self.graph = graph
        self.users = users
        self.news_items = news_items
        self.update_rate = update_rate


class Graph:
    def __init__(self, nodes: [], edge_weights: {}, update_rate):
        self.nodes = nodes
        self.edge_weights = edge_weights
        self.update_rate = update_rate

    def share_news_item(self, user):
        pass

    def increase_connection_strength(self, sender, receiver):
        edge = self.get_edge(sender, receiver)
        self.edge_weights[edge] += self.update_rate

    def decrease_connection_strength(self, sender, receiver):
        edge = self.get_edge(sender, receiver)
        self.edge_weights[edge] -= self.update_rate

    def get_edge(self, node1, node2):
        edge_string = ''
        if node1.name < node2.name:
            edge_string = [node1.name, node2.name].join('-')
        elif node1.name > node2.name:
            edge_string = [node2.name, node1.name].join('-')

        if node1.name == node2.name:
            if node1 is node2:
                raise ValueError('Error: get_edge_string() node1 is the same as node2')
            else:
                raise ValueError('Error: Two nodes cannot have the same name')

        return self.edge_weights[edge_string]


class User:
    def __init__(self, name: int, opinion_score: float, connections: list, update_rate=0.1):
        self.node = name
        self.opinion_score = opinion_score
        self.connections = connections
        self.update_rate = update_rate

    def add_connections(self, connections):
        self.connections.append(connections)


class NewsItem:
    def __init__(self, opinion_score: float, initial_spreader_nodes: []):
        self.opinion_score = opinion_score
        self.initial_spreader_nodes = initial_spreader_nodes
        self.inoculated_nodes = initial_spreader_nodes


