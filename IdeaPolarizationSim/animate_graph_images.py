#!/usr/bin/python
import sys
import pygame


class AnimateGraphImages:
    def __init__(self, directory, time_step):
        self.directory = directory
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.static_image = None
        self.size = self.width, self.height = 1900, 1100
        self.center = (950, 100)
        self.count = 0
        self.time_step = time_step

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._display_surf.fill('white')
        pygame.display.update()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            sys.exit()

    def on_loop(self):
        if self.count <= 10000:
            # image_name = 'Graph_Images/graph' + str(self.count) + '.png'
            image_name = str(self.directory) + 'graph' + str(self.count) + '.png'
            static_image_name = str(self.directory) + 'graph0.png'
            self._image_surf = pygame.image.load(image_name)
            self.static_image = pygame.image.load(static_image_name)
            self._image_surf.get_rect()
            self.count += self.time_step
        else:
            pygame.QUIT

    def on_render(self):
        self._display_surf.fill('white')
        self._display_surf.blit(self._image_surf, self.center)
        self._display_surf.blit(self.static_image, (50, 100))
        pygame.display.flip()
        pygame.time.delay(100)

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
    time_step = 50
    # time_step = 100

    graph_directory = sys.argv[1]
    animation = AnimateGraphImages(graph_directory, time_step)
    animation.on_execute()
