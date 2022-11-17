from random import random
from IdeaPolarizationSim.simulation_classes import SocialNetwork
from IdeaPolarizationSim.simulation_classes import GraphData
from IdeaPolarizationSim.simulation_classes import User
from IdeaPolarizationSim.simulation_classes import NewsItem

import toy_graph


class Simulation:
    def __init__(self, social_network):
        self.social_network = social_network
        self.time = 0
        self.news_iterator = iter(self.social_network.news_items)
        self.current_news_item = next(self.news_iterator)

    def update_simulation(self):

        self.time += 1

        # for news_item in self.social_network.news_items:
        if self.current_news_item is not None:
            # print(f'Nodes that can spread news item: {[user.user_id for user in self.current_news_item.infectious_users]}')
            # print(f'Nodes that have been infected by news item: {[user.user_id for user in self.current_news_item.inoculated_users]}')

            for user in self.current_news_item.infectious_users:
                try:
                    self.social_network.share_news_item(user, self.current_news_item)
                except Exception as e:
                    print(e)

            # print(f'Number of users infected with story: {len(self.current_news_item.inoculated_users)}')
            # print(f'Users infected with story: '
            #      f'{[inoculated_user.user_id for inoculated_user in self.current_news_item.inoculated_users]}')
            print(f'\nSimulation time: {self.time}\n')

            for user in self.social_network.graph_data.nodes:
                print(f'User {user.user_id}\tOpinion Score: {user.opinion_score}')

            self.social_network.graph_data.get_graph_image(self.time)  # Is this violating Law of Demeter?
            try:
                self.current_news_item = next(self.news_iterator)
            except StopIteration:
                if self.time < 50:
                    self.news_iterator = iter(self.social_network.news_items)
                    self.current_news_item = next(self.news_iterator)
                else:
                    self.current_news_item = None

            return self.time




