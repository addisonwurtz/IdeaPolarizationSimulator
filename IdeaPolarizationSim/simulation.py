from random import random
from IdeaPolarizationSim.simulation_classes import SocialNetwork
from IdeaPolarizationSim.simulation_classes import GraphData
from IdeaPolarizationSim.simulation_classes import User
from IdeaPolarizationSim.simulation_classes import NewsItem

import toy_graph


class Simulation:
    def __init__(self, social_network, max_time, time_step):
        self.social_network = social_network
        self.max_time = max_time
        self.time_step = time_step
        self.time = 0
        self.news_iterator = iter(self.social_network.news_items)
        self.current_news_item = next(self.news_iterator)

    def update_simulation(self):

        # for news_item in self.social_network.news_items:
        if self.current_news_item is not None:

            for user in self.current_news_item.infectious_users:
                try:
                    self.social_network.share_news_item(user, self.current_news_item)
                except Exception as e:
                    print(e)


            # for user in self.social_network.graph_data.nodes:
            #    print(f'User {user.user_id}\tOpinion Score: {user.opinion_score}')
            if self.time % self.time_step == 0:
                print(f'\nSimulation time: {self.time}\n')
                self.social_network.graph_data.calculate_edge_homogeneity()
                self.social_network.graph_data.get_graph_image(self.time)
            try:
                self.current_news_item = next(self.news_iterator)
            except StopIteration:
                if self.time <= self.max_time:
                    self.news_iterator = iter(self.social_network.news_items)
                    self.current_news_item = next(self.news_iterator)
                else:
                    self.current_news_item = None

        self.time += 1

        return self.time




