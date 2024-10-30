
from .settings import * 

class cameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.Vector2()

    def draw(self, display, target_pos):
        self.offset.x = -(target_pos[0] - display.get_width() / (2 * (WIDTH / display.get_width())))
        self.offset.y = -(target_pos[1] - display.get_height() / (2 * (HEIGHT / display.get_height())))

        for sprite in self:
            #sprite.rect.topleft = sprite.rect.topleft + self.offset
            display.blit(sprite.image, sprite.rect.topleft + self.offset)
