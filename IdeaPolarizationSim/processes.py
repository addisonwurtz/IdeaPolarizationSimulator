import simpy

user_connection_graph = {int: list[int]}  # adjacency list representation of graph
user_opinions = {int: float}  # maps user to opinion value between -1 and 1
user_connection_strengths = {tuple, float}  # maps edges to connection strength value between 0 and 1
news_item_opinion_scores = {int, float}  # maps news item to opinion value between -1 nd 1
initial_spreader_nodes = {int: list[int]}
update_rate = 0.1  # update rate for opinion and connection strength


class Person:
    def __init__(self, env: simpy.Environment, node_name: int, opinion: float):
        self.env = env
        self.node = node_name
        self.opinion = opinion


class NewsItem:
    def __init__(self, env: simpy.Environment, opinion: float):
        self.env = env
        self.opinion = opinion

