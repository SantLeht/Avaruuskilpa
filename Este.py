import pygame
import random


class Este(pygame.sprite.Sprite):
    def __init__(self, image_path, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(
            topleft=(random.randint(0, screen_width - self.image.get_width()), -self.image.get_height()))
        self.screen_height = screen_height

    def reset_position(self):
        self.rect.x = random.randint(0, self.screen_width - self.rect.width)
        self.rect.y = random.randint(-self.screen_height, -self.rect.height)

    def update(self):
        self.rect.y += 6
        if self.rect.top > self.screen_height:
            self.rect.x = random.randint(0, self.screen_width - self.image.get_width())
            self.rect.y = -self.image.get_height()



