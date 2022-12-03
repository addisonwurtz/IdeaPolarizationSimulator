from IdeaPolarizationSim.simulation_classes import User, GraphData, NewsItem

nodes = []
edge_weights = {}

user_1 = User(1, 1, [])
user_2 = User(2, -0.9, [])
user_3 = User(3, 0.6, [])
user_4 = User(4, -0.2, [])
user_5 = User(5, -0.6, [])
user_6 = User(6, -1, [])
user_7 = User(7, 0.5, [])
user_8 = User(8, -0.5, [])
user_9 = User(9, 0.75, [])
user_10 = User(10, -0.75, [])

user_1.add_connections([user_2, user_3, user_7, user_9, user_10])
edge_weights[(1, 2)] = 0.4
edge_weights[(1, 3)] = 0.5
edge_weights[(1, 7)] = 0.5
edge_weights[(1, 9)] = 0.3
edge_weights[(1, 10)] = 0.2
user_2.add_connections([user_1, user_8, user_10])
edge_weights[(2, 3)] = 0.3
edge_weights[(2, 8)] = 0.4
edge_weights[(2, 10)] = 0.2
user_3.add_connections([user_1, user_2, user_8, user_9, user_10])
edge_weights[(3, 8)] = 0.5
edge_weights[(3, 9)] = 0.4
edge_weights[(3, 10)] = 0.1
user_4.add_connections([user_5, user_6, user_7, user_10])
edge_weights[(4, 5)] = 0.1
edge_weights[(4, 6)] = 0.3
edge_weights[(4, 7)] = 0.5
edge_weights[(4, 10)] = 0.2
user_5.add_connections([user_4, user_6, user_8, user_9, user_10])
edge_weights[(5, 6)] = 0.4
edge_weights[(5, 8)] = 0.5
edge_weights[(5, 9)] = 0.3
edge_weights[(5, 10)] = 0.2
user_6.add_connections([user_4, user_5, user_7])
edge_weights[(6, 7)] = 0.5
user_7.add_connections([user_1, user_4, user_6, user_8, user_9])
edge_weights[(7, 8)] = 0.5
edge_weights[(7, 9)] = 0.3
user_8.add_connections([user_2, user_3, user_5, user_7, user_10])
edge_weights[(8, 10)] = 0.2


nodes = [user_1, user_2, user_3, user_4, user_5, user_6, user_7, user_8, user_9, user_10]

graph = GraphData(nodes, edge_weights, 0.1)

news_items = [NewsItem(1, -1, [user_5, user_6]),
              NewsItem(2, -1, [user_5, user_6]),
              NewsItem(3, -1, [user_5, user_6]),
              NewsItem(4, -1, [user_5, user_6]),
              NewsItem(5, -1, [user_5, user_6]),
              NewsItem(6, -1, [user_5, user_6]),
              NewsItem(7, 1, [user_1, user_2]),
              NewsItem(8, 1, [user_1, user_2]),
              NewsItem(9, 1, [user_1, user_2]),
              NewsItem(10, 1, [user_1, user_2]),
              NewsItem(11, 1, [user_1, user_2]),
              NewsItem(12, 1, [user_1, user_2])
              ]
