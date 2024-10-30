from .settings import *

class component:
    def __init__(self):
        pass

class movementComponent(pygame.Vector2):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)

class keyboardComponent(component):
    def __init__(self):
        super().__init__()

    def is_down(self, KEY):
        input = pygame.key.get_pressed()
        if input[KEY]:
            return True
        else:
            return False
    
    def is_pressed(self, KEY):
        input = pygame.key.get_just_pressed()
        if input[KEY]:
            return True
        else:
            return False
    
    def is_released(self, KEY):
        input = pygame.key.get_just_released()
        if input[KEY]:
            return True
        else:
            return False

class collisionComponent(component):
    def __init__(self):
        super().__init__()
    
    def check_collision(self, rect, colliding_group, motion_vector, direction= 'horizontal'):  
        for sprite in colliding_group:
            if sprite.rect.colliderect(rect):
                if direction == 'horizontal':
                    if motion_vector.x > 0: rect.right = sprite.rect.left
                    if motion_vector.x < 0: rect.left = sprite.rect.right
                    motion_vector.x = 0
                if direction == 'vertical':
                    if motion_vector.y > 0: rect.bottom = sprite.rect.top
                    if motion_vector.y < 0: rect.top = sprite.rect.bottom
                    motion_vector.y = 0