import pygame


class Raketti(pygame.sprite.Sprite):
    def __init__(self, image_path, initial_position):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=initial_position)

    def update(self, liikuta_vasen, liikuta_oikea, screen_width):
        self.rect.x += liikuta_vasen + liikuta_oikea
        # Estetään raketti karkaamasta näytön ulkopuolelle
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.left < 0:
            self.rect.left = 0