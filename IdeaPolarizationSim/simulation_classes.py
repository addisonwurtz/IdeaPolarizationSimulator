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
        connections: [User] = user.get_connections()
        for connection in connections:
            if connection not in news_item.inoculated_users:
                if random() < self.probability_of_infection(user, connection, news_item):
                    news_item.infect_user(connection)
                    connection.update_opinion(news_item.opinion_score)
                    self.graph.increase_connection_strength(user, connection)
                else:
                    self.graph.decrease_connection_strength(user, connection)
        news_item.remove_user_from_infectious_list(user)


class Graph:
    def __init__(self, nodes: [], edge_weights: {}, update_rate):
        self.nodes = nodes
        self.edge_weights = edge_weights
        self.update_rate = update_rate

    def increase_connection_strength(self, sender, receiver):
        edge_string = self.get_edge_string(sender, receiver)
        edge_weight = self.edge_weights[edge_string]
        self.edge_weights[edge_string] = edge_weight + self.update_rate

    def decrease_connection_strength(self, sender, receiver):
        edge_string = self.get_edge_string(sender, receiver)
        edge_weight = self.edge_weights[edge_string]
        self.edge_weights[edge_string] = edge_weight - self.update_rate

    def get_edge_string(self, user1, user2):
        edge_string = ''
        if user1.user_id < user2.user_id:
            edge_string = str(user1.user_id) + '-' + str(user2.user_id)
        elif user1.user_id > user2.user_id:
            edge_string = str(user2.user_id) + '-' + str(user1.user_id)
        if user1.user_id == user2.user_id:
            if user1 is user2:
                raise ValueError('Error: get_edge_string() user1 is the same as user2')
            else:
                raise ValueError('Error: Two nodes cannot have the same name')
        return edge_string

    def get_edge_weight(self, user1, user2):
        edge_string = self.get_edge_string(user1, user2)
        return self.edge_weights[edge_string]


class User:
    def __init__(self, user_id: int, opinion_score: float, connections, update_rate=0.1):
        self.user_id: int = user_id
        self.opinion_score: float = opinion_score
        self.connections: [User] = connections
        self.update_rate: float = update_rate

    def get_connections(self):
        return self.connections

    def add_connections(self, new_connections):
        self.connections += new_connections

    def update_opinion(self, news_opinion_score):
        if news_opinion_score > self.opinion_score:
            self.opinion_score += self.update_rate * news_opinion_score
        elif news_opinion_score < self.opinion_score:
            self.opinion_score -= self.update_rate * news_opinion_score


class NewsItem:
    def __init__(self, opinion_score: float, initial_spreader_nodes: [User]):
        self.opinion_score: float = opinion_score
        self.initial_spreader_nodes: [User] = initial_spreader_nodes
        self.infectious_users: [User] = initial_spreader_nodes
        self.inoculated_users: [User] = initial_spreader_nodes

    def infect_user(self, neighbor: User):
        if neighbor not in self.inoculated_users:
            self.infectious_users.append(neighbor)
            self.inoculated_users.append(neighbor)

    def remove_user_from_infectious_list(self, user: User):
        if user in self.infectious_users:
            self.infectious_users.remove(user)

    def update_inoculated_nodes(self):
        for node in self.infectious_users:
            if node not in self.inoculated_users:
                self.inoculated_users.append(node)


