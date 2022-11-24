import random

from IdeaPolarizationSim.simulation_classes import GraphData, User


class GraphBuilder:
    def __init__(self, graph_data, filename):
        self.graph = graph_data
        self.filename = filename

    def build_graph(self):
        i = 0
        with open('C:/Users/addis/IdeaPolarizationSimulator/Data/' + self.filename) as file:
            for line in file.readlines():
                node1, node2 = self.get_nodes_from_line(line)
                user1, user2 = self.get_users(node1, node2)
                user1.add_connections([user2])
                user2.add_connections([user1])
                self.graph.add_nodes([user1, user2])
                self.graph.add_edge(self.graph.get_edge(user1, user2), self.assign_edge_weight())

                if i > 200:
                    break
                else:
                    i += 1

    @staticmethod
    def get_nodes_from_line(line):
        line = line.strip('\n')
        nodes = line.split(' ')
        return nodes

    def get_users(self, node1, node2):
        user1 = self.graph.get_node(node1)
        user2 = self.graph.get_node(node2)
        if user1 is None:
            user1 = User(node1, self.assign_opinion_score(), [])
        if user2 is None:
            user2 = User(node2, self.assign_opinion_score(), [])
        return user1, user2

    @staticmethod
    def assign_opinion_score():
        return random.randint(-10, 10) / 10.0

    @staticmethod
    def assign_edge_weight():
        return random.randint(1, 5) / 10.0


