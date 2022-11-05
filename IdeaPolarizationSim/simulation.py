from random import random
from IdeaPolarizationSim.simulation_classes import SocialNetwork
from IdeaPolarizationSim.simulation_classes import Graph
from IdeaPolarizationSim.simulation_classes import User
from IdeaPolarizationSim.simulation_classes import NewsItem


import toy_graph

update_rate = 0.1
users: [User] = toy_graph.nodes
news_items: [NewsItem] = [NewsItem(0, [toy_graph.user_1, toy_graph.user_6])]

social_network = SocialNetwork(toy_graph.graph, users, news_items, update_rate)

for news_item in social_network.news_items:

    time = 1
    print(f'Nodes that can spread news item: {news_item.infectious_users}')
    print(f'Nodes that have been infected by news item: {news_item.inoculated_users}')

    for user in news_item.infectious_users:
        social_network.share_news_item(user, news_item)

    time += 1

for news_item in social_network.news_items:
    print(f'Users infected with story: {len(news_item.inoculated_users)}')





