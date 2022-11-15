import pygame
from pygame import image
from pygame.locals import *
from IdeaPolarizationSim import toy_graph
from IdeaPolarizationSim.simulation import Simulation
from IdeaPolarizationSim.simulation_classes import NewsItem


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.size = self.width, self.height = 640, 480
        self.simulation = Simulation(toy_graph.nodes, [NewsItem(1, 0, [toy_graph.user_1, toy_graph.user_6])])

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._image_surf = pygame.image.load('Graph_Images/graph0.png').convert()
        self.simulation.social_network.graph.get_graph_image(time=0)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        if self.simulation.time > 10:
            pygame.QUIT
        else:
            self.simulation.update_simulation()

    def on_render(self):
        self._display_surf.blit(self._image_surf, (0, 0))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
