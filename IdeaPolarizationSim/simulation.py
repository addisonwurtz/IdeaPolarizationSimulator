from random import random
from IdeaPolarizationSim.simulation_classes import SocialNetwork
from IdeaPolarizationSim.simulation_classes import Graph
from IdeaPolarizationSim.simulation_classes import User
from IdeaPolarizationSim.simulation_classes import NewsItem


import toy_graph

update_rate = 0.1
users: [User] = toy_graph.nodes
news_items: [NewsItem] = [NewsItem(1, 0, [toy_graph.user_1, toy_graph.user_6])]

social_network = SocialNetwork(toy_graph.graph, news_items, update_rate)

time = 1

for news_item in social_network.news_items:

    print(f'Nodes that can spread news item: {[user.user_id for user in news_item.infectious_users]}')
    print(f'Nodes that have been infected by news item: {[user.user_id for user in news_item.inoculated_users]}')

    for user in news_item.infectious_users:
        try:
            social_network.share_news_item(user, news_item)
        except Exception as e:
            print(e)

    time += 1

for news_item in social_network.news_items:
    print(f'Number of users infected with story: {len(news_item.inoculated_users)}')
    print(f'Users infected with story: {[inoculated_user.user_id for inoculated_user in news_item.inoculated_users]}')
    print(f'Simulation time: {time}')




