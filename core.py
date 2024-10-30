import pygame, sys
from BoxEngine.settings import *


class Engine:
    def __init__(self, w, h, title, fps = 60):
        pygame.init()

        self.screen_width = w
        self.screen_height = h
        self.framerate = fps
        self.is_running = True

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(title)
        
        self.clock = pygame.time.Clock()
        self.delta = 0


    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

        pygame.display.update()
        self.clock.tick(self.framerate)
        self.delta = self.clock.tick(self.framerate) / 1000
        self.input = pygame.key.get_pressed()
    
