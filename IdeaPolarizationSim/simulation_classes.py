import os
from random import random
import pygraphviz as pgv

from IdeaPolarizationSim.graph_visualization import get_visual_graph


class SocialNetwork:
    def __init__(self, graph, news_items: [], update_rate):
        self.graph_data = graph
        self.users = graph.nodes
        self.news_items = news_items
        self.update_rate = update_rate

    def probability_of_infection(self, user, neighbor, news_item):
        edge_weight = self.graph_data.get_edge_weight(user, neighbor)
        selective_exposure = (1 - edge_weight) * (1 - abs(news_item.opinion_score - neighbor.opinion_score))
        return (edge_weight ** 2) + selective_exposure

    def share_news_item(self, user, news_item):
        if user not in news_item.infectious_users:
            raise UserNotInfectiousError(f'user {user.user_id} is not in the infectious user list for news item '
                                         f'{news_item.item_id}')
        for connection in user.connections:
            if connection not in news_item.inoculated_users:
                if random() < self.probability_of_infection(user, connection, news_item):
                    news_item.infect_user(connection)
                    connection.update_opinion(news_item.opinion_score)
                    self.graph_data.increase_connection_strength(user, connection)
                else:
                    self.graph_data.decrease_connection_strength(user, connection)
        news_item.remove_user_from_infectious_list(user)


class GraphData:
    def __init__(self, nodes: [], edge_weights: {}, update_rate):
        self.nodes = nodes
        self.edge_weights = edge_weights
        self.update_rate = update_rate
        # self.m_value = self.calculate_m_value()
        self.edge_homogeneity = self.calculate_edge_homogeneity()

    def add_nodes(self, node):
        self.nodes += node

    def add_edge(self, edge, weight):
        self.edge_weights[edge] = weight

    def get_node(self, node_name):
        for node in self.nodes:
            if node.user_id == int(node_name):
                return node
        return None

    def increase_connection_strength(self, sender, receiver):
        edge = self.get_edge(sender, receiver)
        edge_weight = self.edge_weights[edge]
        self.edge_weights[edge] = edge_weight + self.update_rate

    def decrease_connection_strength(self, sender, receiver):
        edge = self.get_edge(sender, receiver)
        edge_weight = self.edge_weights[edge]
        self.edge_weights[edge] = edge_weight - self.update_rate

    def get_graph_image(self, time):
        visual_graph = get_visual_graph(self, time)
        file_name = 'Graph_Images/graph' + str(time) + '.png'
        visual_graph.graph.draw(file_name, prog='neato')
        # visual_graph.graph.draw(file_name, prog='sfdp')

    @staticmethod
    def get_edge(user1, user2):
        if user1.user_id < user2.user_id:
            edge = (user1.user_id, user2.user_id)
        elif user1.user_id > user2.user_id:
            edge = (user2.user_id, user1.user_id)
        else:
            raise ValueError('Node cannot share edge with itself.')
        return edge

    def get_edge_weight(self, user1, user2):
        try:
            edge = self.get_edge(user1, user2)
            return self.edge_weights[edge]
        except ValueError as e:
            raise e
        except KeyError:
            raise KeyError(f'Error: Edge between user {user1.user_id} and user {user2.user_id} does not exist.')

    def calculate_m_value(self):
        pass

    def calculate_edge_homogeneity(self):
        sum_of_edge_weights = 0
        sum_of_product_of_opinion_weights = 0

        for node in self.nodes:
            for connection in node.connections:
                sum_of_edge_weights += self.get_edge_weight(node, connection)
                sum_of_product_of_opinion_weights += self.get_edge_weight(node, connection) * node.opinion_score * connection.opinion_score
        if sum_of_edge_weights == 0:
            return 0
        self.edge_homogeneity = sum_of_product_of_opinion_weights / sum_of_edge_weights
        return self.edge_homogeneity


class User:
    def __init__(self, user_id: int, opinion_score: float, connections, update_rate=0.1):
        self.user_id: int = user_id
        self.opinion_score: float = opinion_score
        self.connections: [User] = []
        self.connections += connections
        self.update_rate: float = update_rate

    def get_connections(self):
        return self.connections

    def add_connections(self, new_connections):
        self.connections += new_connections

    def update_opinion(self, news_opinion_score):
        if news_opinion_score > self.opinion_score != 1:
            self.opinion_score += abs(self.update_rate * news_opinion_score)
            if self.opinion_score > 1:
                self.opinion_score = 1
        elif news_opinion_score < self.opinion_score != -1:
            self.opinion_score -= abs(self.update_rate * news_opinion_score)
            if self.opinion_score < -1:
                self.opinion_score = -1


class NewsItem:
    def __init__(self, item_id: int, opinion_score: float, initial_spreader_nodes: [User]):
        self.item_id = item_id
        self.opinion_score: float = opinion_score
        self.initial_spreader_nodes: [User] = initial_spreader_nodes
        self.infectious_users: [User] = []
        self.infectious_users += initial_spreader_nodes
        self.inoculated_users: [User] = []
        self.inoculated_users += initial_spreader_nodes

    def infect_user(self, neighbor: User):
        if neighbor not in self.inoculated_users and neighbor not in self.infectious_users:
            self.infectious_users.append(neighbor)
            self.inoculated_users.append(neighbor)

    def remove_user_from_infectious_list(self, user: User):
        if user in self.infectious_users:
            self.infectious_users.remove(user)


class UserNotInfectiousError(Exception):
    pass
