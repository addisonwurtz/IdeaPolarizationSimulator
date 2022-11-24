import sys

import pygame


class AnimateGraphImages:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.size = self.width, self.height = 1200, 900
        self.count = 0

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._display_surf.fill('white')
        pygame.display.update()
        self._image_surf = pygame.image.load('Graph_Images/graph0.png').convert()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            sys.exit()

    def on_loop(self):
        if self.count < 10000:
            image_name = 'Graph_Images/graph' + str(self.count) + '.png'
            self._image_surf = pygame.image.load(image_name)
            self._image_surf.get_rect()
            self.count += 100
        else:
            pygame.QUIT

    def on_render(self):
        self._display_surf.fill('white')
        self._display_surf.blit(self._image_surf, (200, 50))
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
    animation = AnimateGraphImages()
    animation.on_execute()
