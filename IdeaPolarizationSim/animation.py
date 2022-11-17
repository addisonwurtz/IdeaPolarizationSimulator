import os
import sys

import pygame
from pygame import image
from pygame.locals import *
from IdeaPolarizationSim import toy_graph
from IdeaPolarizationSim.simulation import Simulation
from IdeaPolarizationSim.simulation_classes import NewsItem, SocialNetwork


class Animation:
    def __init__(self, simulation):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.size = self.width, self.height = 800, 600
        self.simulation = simulation
        self.time = 0

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.simulation.social_network.graph_data.get_graph_image(0)
        self._image_surf = pygame.image.load('Graph_Images/graph0.png').convert()
        self.simulation.social_network.graph_data.get_graph_image(time=0)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            sys.exit()

    def on_loop(self):
        if self.simulation.current_news_item is not None and self.simulation.time < self.simulation.max_time:
            self.time = self.simulation.update_simulation()
            image_name = 'Graph_Images/graph' + str(self.time) + '.png'
            self._image_surf = pygame.image.load(image_name)
            self._image_surf.get_rect()
        else:
            pygame.QUIT

    def on_render(self):
        self._display_surf.fill('white')
        self._display_surf.blit(self._image_surf, (100, 50))
        pygame.display.flip()
        # pygame.time.delay(100)

    def on_cleanup(self):
        pygame.quit()
        self.delete_graph_images()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def delete_graph_images(self):
        file_name = ''
        for time in range(1, self.simulation.time):
            file_name = 'Graph_Images/graph' + str(time) + '.png'
            os.remove(file_name)


if __name__ == "__main__":
    update_rate = 0.1

    news_items = [NewsItem(1, -1, [toy_graph.user_5, toy_graph.user_6]),
                  NewsItem(2, -1, [toy_graph.user_5, toy_graph.user_6]),
                  NewsItem(3, -1, [toy_graph.user_5, toy_graph.user_6]),
                  NewsItem(4, -1, [toy_graph.user_5, toy_graph.user_6]),
                  NewsItem(5, -1, [toy_graph.user_5, toy_graph.user_6]),
                  NewsItem(6, -1, [toy_graph.user_5, toy_graph.user_6]),
                  NewsItem(7, 1, [toy_graph.user_1, toy_graph.user_2]),
                  NewsItem(8, 1, [toy_graph.user_1, toy_graph.user_2]),
                  NewsItem(9, 1, [toy_graph.user_1, toy_graph.user_2]),
                  NewsItem(10, 1, [toy_graph.user_1, toy_graph.user_2]),
                  NewsItem(11, 1, [toy_graph.user_1, toy_graph.user_2]),
                  NewsItem(12, 1, [toy_graph.user_1, toy_graph.user_2])
                  ]

    social_network = SocialNetwork(toy_graph.graph, news_items, update_rate)

    my_simulation = Simulation(social_network, 60)

    animation = Animation(my_simulation)
    animation.on_execute()
