import pygame
from BoxEngine.settings import *

class sprite(pygame.sprite.Sprite):
    def __init__(self, pos, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

    def load(self, path):
        self.image = pygame.image.load(path).convert_alpha() #surface
        self.rect = self.image.get_rect(topleft = self.image.get_rect().topleft)

    def blit(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))
    
    def tint(self, tint=(0,0,0,0)):
        self.image.fill(tint, special_flags = pygame.BLEND_ADD)

class animatedSprite(sprite):
    def __init__(self, pos, frames, groups):
        self.frames, self.frame_index, self.anim_spd = frames, 0, 10
        super().__init__(pos, groups, self.frames[self.frame_index])

    def animate(self, dt):
        self.frame_index += self.anim_spd * dt
        self.image = self.frames[int(self.frame_index) % len(self.frames)]

# old code ----------------------
    # def __init__(self, pos, f_w, f_h, groups):
    #     super().__init__(pos,groups)
    #     self.frame_index = 0
    #     self.frame_size = (f_w, f_h)
    #     self.image = None
    #     self.rect = pygame.Rect(pos[0], pos[1], f_w, f_h)  # Set rect size
    #     self.sprite_sheet = None  # To hold the loaded sprite sheet
    #     self.frame_count = 0  # Initialize frame count

    # def load(self, path):
    #     # Load the sprite sheet
    #     self.sprite_sheet = pygame.image.load(path).convert_alpha()
    #     self.frame_count = self.sprite_sheet.get_width() // self.frame_size[0]

    # def get_frame(self):
    #     # Calculate the position of the frame on the sprite sheet
    #     frame_x = int(self.frame_index) * self.frame_size[0]
    #     frame_rect = pygame.Rect(frame_x, 0, self.frame_size[0], self.frame_size[1])
        
    #     # Extract the frame from the sprite sheet
    #     frame = pygame.Surface(self.frame_size, pygame.SRCALPHA).convert_alpha()
    #     frame.blit(self.sprite_sheet, (0, 0), frame_rect)
    #     return frame

    # def animate(self, speed=0.15):
    #     # Update the frame index
    #     self.frame_index += speed
    #     if self.frame_index >= self.frame_count:
    #         self.frame_index = 0  # Reset to the first frame

    #     # Get the current frame
    #     self.image = self.get_frame()
    #     self.rect.topleft = self.rect.topleft  # Keep rect position updated

    # def blit(self, display):
    #     # Draw the sprite on the display
    #     display.blit(self.image, self.rect.topleft)
