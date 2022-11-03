from random import random

class SocialNetwork:
    def __init__(self, graph, users: [], news_items: [], update_rate):
        self.graph = graph
        self.users = users
        self.news_items = news_items
        self.update_rate = update_rate

    def probability_of_infection(self, user, neighbor, news_item):
        edge_weight = self.graph.get_edge_weight(user, neighbor)
        selective_exposure = (1 - edge_weight) * (1 - abs(news_item.opinion_score - neighbor.opinion_score))
        return (edge_weight ** 2) + selective_exposure

    def share_news_item(self, user, news_item):
        for neighbor in user.connections:
            if neighbor not in news_item.inoculated_users:
                if random() < self.probability_of_infection(user, neighbor, news_item):
                    news_item.infect_user(neighbor)
                    neighbor.update_opinion(news_item)
                    self.graph.increase_connection_strength(user, neighbor)
                else:
                    self.graph.decrease_connection_strength(user, neighbor)


class Graph:
    def __init__(self, nodes: [], edge_weights: {}, update_rate):
        self.nodes = nodes
        self.edge_weights = edge_weights
        self.update_rate = update_rate

    def increase_connection_strength(self, sender, receiver):
        edge = self.get_edge_weight(sender, receiver)
        self.edge_weights[edge] += self.update_rate

    def decrease_connection_strength(self, sender, receiver):
        edge = self.get_edge_weight(sender, receiver)
        self.edge_weights[edge] -= self.update_rate

    def get_edge_weight(self, node1, node2):
        edge_string = ''
        if node1.get_user_id() < node2.get_user_id():
            edge_string = [node1.user_id, node2.user_id].join('-')
        elif node1.user_id > node2.user_id:
            edge_string = [node2.user_id, node1.user_id].join('-')

        if node1.name == node2.name:
            if node1 is node2:
                raise ValueError('Error: get_edge_string() node1 is the same as node2')
            else:
                raise ValueError('Error: Two nodes cannot have the same name')

        return self.edge_weights[edge_string]


class User:
    def __init__(self, user_id: int, opinion_score: float, connections: list, update_rate=0.1):
        self.user_id = user_id
        self.opinion_score = opinion_score
        self.connections = connections
        self.update_rate = update_rate

    def get_user_id(self):
        return self.user_id

    def add_connections(self, connections):
        self.connections.append(connections)

    def update_opinion(self, news_opinion_score):
        if news_opinion_score > self.opinion_score:
            self.opinion_score += self.update_rate * news_opinion_score
        elif news_opinion_score < self.opinion_score:
            self.opinion_score -= self.update_rate * news_opinion_score


class NewsItem:
    def __init__(self, opinion_score: float, initial_spreader_nodes: []):
        self.opinion_score = opinion_score
        self.initial_spreader_nodes = [initial_spreader_nodes]
        self.infectious_users = [initial_spreader_nodes]
        self.inoculated_users = [initial_spreader_nodes]

    def infect_user(self, neighbor):
        self.infectious_users.append(neighbor)
        self.inoculated_users.append(neighbor)

    def update_inoculated_nodes(self):
        for node in self.infectious_users:
            if node not in self.inoculated_users:
                self.inoculated_users.append(node)


