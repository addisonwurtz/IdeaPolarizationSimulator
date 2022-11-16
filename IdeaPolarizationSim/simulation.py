from random import random
from IdeaPolarizationSim.simulation_classes import SocialNetwork
from IdeaPolarizationSim.simulation_classes import Graph_Data
from IdeaPolarizationSim.simulation_classes import User
from IdeaPolarizationSim.simulation_classes import NewsItem

import toy_graph


class Simulation:
    def __init__(self, users, news_items, update_rate=0.1):
        self.users = users
        self.news_items = news_items
        self.update_rate = update_rate
        self.time = 0
        self.social_network = SocialNetwork(toy_graph.graph, news_items, update_rate)
        self.current_news_item = news_items[0]

    def update_simulation(self):

        self.time += 1

        # for news_item in self.social_network.news_items:
        if self.current_news_item is not None:
            print(f'Nodes that can spread news item: {[user.user_id for user in self.current_news_item.infectious_users]}')
            print(f'Nodes that have been infected by news item: {[user.user_id for user in self.current_news_item.inoculated_users]}')

            for user in self.current_news_item.infectious_users:
                try:
                    self.social_network.share_news_item(user, self.current_news_item)
                except Exception as e:
                    print(e)

            print(f'Number of users infected with story: {len(self.current_news_item.inoculated_users)}')
            print(f'Users infected with story: '
                  f'{[inoculated_user.user_id for inoculated_user in self.current_news_item.inoculated_users]}')
            print(f'Simulation time: {self.time}\n')

            self.social_network.graph.get_graph_image(self.time)  # Is this violating Law of Demeter?
            return self.time




