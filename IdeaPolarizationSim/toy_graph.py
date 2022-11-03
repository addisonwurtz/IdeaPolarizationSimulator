from IdeaPolarizationSim.simulation_classes import User

nodes = []
edge_weights = {}

user_1 = User(1, 1, [])
user_2 = User(2, 0.9, [])
user_3 = User(3, 0.6, [])
user_4 = User(4, -0.2, [])
user_5 = User(5, -0.65, [])
user_6 = User(6, -1, [])

user_1.add_connections([user_2, user_3])
edge_weights['1-2'] = 0.8
edge_weights['1-3'] = 0.9
user_2.add_connections([user_1, user_2, user_5])
edge_weights['2-3'] = 0.7
edge_weights['2-5'] = 0.2
user_3.add_connections([user_1, user_2, user_4])
edge_weights['3-4'] = 0.3
user_4.add_connections([user_3, user_5, user_6])
edge_weights['4-5'] = 0.5
edge_weights['4-6'] = 0.7
user_5.add_connections([user_2, user_4, user_6])
edge_weights['5-6'] = 0.8
user_6.add_connections([user_4, user_5])

nodes = [user_1, user_2, user_3, user_4, user_5, user_6]