import pygame


class Raketti:

    def __init__(self, naytto, naytto_leveys, naytto_korkeus):
        self.naytto = naytto
        self.raketti = pygame.image.load("raketti.png")
        self.raketti_width, self.raketti_height = self.raketti.get_size()
        self.x = (naytto_leveys - self.raketti_width) // 2
        self.y = (naytto_korkeus - self.raketti_height) // 0.7
        self.nopeus = 5

    def luoRaketti(self):
        self.naytto.blit(self.raketti, (self.x, self.y))

    def liikutaRaketti(self, x, y):
        self.x += x
        self.y += y
