import simpy


class Network:
    def __init__(self, env: simpy.Environment, nodes: [], edge_weights: {}):
        self.env = env
        self.nodes = nodes
        self.edge_weights = edge_weights


class Person:
    def __init__(self, env: simpy.Environment, name: int, opinion: float, connections: list, update_rate=0.1):
        self.env = env
        self.node = name
        self.opinion = opinion
        self.connections = connections
        self.update_rate = update_rate

    def add_connections(self, connections):
        self.connections.append(connections)
        # TODO should probably update edge_weights anytime connection is added?

    def share_news_item(self):
        pass

    def update_connection_strength(self):
        pass


class NewsItem:
    def __init__(self, env: simpy.Environment, opinion_score: float, initial_spreader_nodes: []):
        self.env = env
        self.opinion_score = opinion_score
        self.initial_spreader_nodes = initial_spreader_nodes


