import pygame

class timer:
    def __init__(self, duration, func = None, repeat = None, autostart = False):
        self.duration = duration # duration is in ms(miliseconds)
        self.start_time = 0
        self.active = False
        self.func = func
        self.repeat = repeat
        
        if autostart == True:
            self.start()
    
    def __bool__(self):
        return self.active
    
    def start(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()

    def stop(self):
        self.active = False
        self.start_time = 0

        if self.repeat == True:
            self.start()
    
    def update(self):
        if pygame.time.get_ticks() - self.start_time >= self.duration:
            if self.func and self.start_time != 0:
                self.func()
            self.stop()
