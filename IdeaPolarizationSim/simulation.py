from random import random
from IdeaPolarizationSim.simulation_classes import SocialNetwork
from IdeaPolarizationSim.simulation_classes import Graph
from IdeaPolarizationSim.simulation_classes import User
from IdeaPolarizationSim.simulation_classes import NewsItem

import toy_graph


class Simulation:
    def __init__(self, users, news_items, update_rate=0.1):
        self.users = users
        self.news_items = news_items
        self.update_rate = update_rate
        self.time = 1
        self.social_network = SocialNetwork(toy_graph.graph, news_items, update_rate)

    def update_simulation(self):

        for news_item in self.social_network.news_items:

            print(f'Nodes that can spread news item: {[user.user_id for user in news_item.infectious_users]}')
            print(f'Nodes that have been infected by news item: {[user.user_id for user in news_item.inoculated_users]}')

            for user in news_item.infectious_users:
                try:
                    self.social_network.share_news_item(user, news_item)
                except Exception as e:
                    print(e)

            self.social_network.graph.get_graph_image(self.time)  # Is this violating Law of Demeter?
            self.time += 1
            print(f'Number of users infected with story: {len(news_item.inoculated_users)}')
            print(f'Users infected with story: {[inoculated_user.user_id for inoculated_user in news_item.inoculated_users]}')
            print(f'Simulation time: {self.time}')




