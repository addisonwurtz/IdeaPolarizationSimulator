import random

from IdeaPolarizationSim.simulation_classes import GraphData, User


class GraphBuilder:
    def __init__(self, graph_data, filename):
        self.graph = graph_data
        self.filename = filename

    def build_graph(self):
        with open('C:/Users/addis/IdeaPolarizationSimulator/Data/' + self.filename) as file:
            for line in file.readlines():
                pass
            # TODO Finish this!

    def parse_edge(self):
        with open('C:/Users/addis/IdeaPolarizationSimulator/Data/' + self.filename) as file:
            line = file.readline()
            print(line)
        # read edge
            line = line.strip('\n')
            nodes = line.split(' ')
        # check if each node needs to be added
        # create new users as necessary (assign opinion scores and connection strength)
            user0 = self.graph.get_node(nodes[0])
            user1 = self.graph.get_node(nodes[1])
            if user0 is None:
                user0 = User(nodes[0], self.assign_opinion_score(), [])
                self.graph.add_node(user0)
            if user1 is None:
                user1 = User(nodes[1], self.assign_opinion_score(), [])
                self.graph.add_node(user1)
        # add connections to users
            user0.add_connections(user1)
            user1.add_connections(user0)
        # add edge weight to graph data
            self.graph.add_edge(self.graph.get_edge(user0, user1), self.assign_edge_weight())

    @staticmethod
    def assign_opinion_score():
        return random.randint(-10, 10) / 10.0

    @staticmethod
    def assign_edge_weight():
        return random.randint(1, 5) / 10.0


parser = GraphBuilder(GraphData([User(236, 1.0, [])], {}), '0.edges')
parser.parse_edge()
