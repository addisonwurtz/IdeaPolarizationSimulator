import os

import pygame
from pygame import image
from pygame.locals import *
from IdeaPolarizationSim import toy_graph
from IdeaPolarizationSim.simulation import Simulation
from IdeaPolarizationSim.simulation_classes import NewsItem


class App:
    def __init__(self, simulation):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.size = self.width, self.height = 640, 480
        self.simulation = simulation
        self.time = 0

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.simulation.social_network.graph.get_graph_image(0)
        self._image_surf = pygame.image.load('Graph_Images/graph0.png').convert()
        self.simulation.social_network.graph.get_graph_image(time=0)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        if self.simulation.time > 10:
            pygame.QUIT
        else:
            self.time = self.simulation.update_simulation()
            image_name = 'Graph_Images/graph' + str(self.time) + '.png'
            self._image_surf = pygame.image.load(image_name)

    def on_render(self):
        self._display_surf.blit(self._image_surf, (200, 100))
        pygame.display.flip()
        pygame.time.delay(300)

    def on_cleanup(self):
        pygame.quit()
        # self.delete_graph_images()

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
        for time in range(0, self.simulation.time):
            file_name = 'Graph_Images/graph' + str(time) + '.png'
        os.remove(file_name)


if __name__ == "__main__":
    news_items =[NewsItem(1, 0, [toy_graph.user_1, toy_graph.user_6])]
    simulation = Simulation(toy_graph.nodes, news_items)
    theApp = App(simulation)
    theApp.on_execute()
