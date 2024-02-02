import pygame

from Este import Este
from Raketti import Raketti


class Game:
    def __init__(self):

        pygame.init()
        self.start_time = 0
        self.player_score = 0
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.score_update_delay = 100
        self.font = pygame.font.Font("fontti/Super Disco Personal Use.ttf", 50)
        self.background = pygame.image.load("kuvat/tausta.png").convert()
        self.background_rects = [self.background.get_rect(topleft=(0, 0)),
                                 self.background.get_rect(topleft=(0, -self.screen_height))]
        self.lower_text_effect = 0
        self.fade_speed = 100 / 30
        self.fade = True
        self.running = True
        self.game_elements()

    def game_elements(self):

        self.raketti = Raketti("kuvat/raketti.png", (550, 630))
        self.tahti = Este("kuvat/tahti.png", self.screen_width, self.screen_height)
        self.meteoriitti = Este("kuvat/kivi.png", self.screen_width, self.screen_height)
        self.score_update = pygame.time.get_ticks()
        self.game_on = False
        # Load texts and logo
        self.font = pygame.font.Font("fontti/Super Disco Personal Use.ttf", 60)
        self.logo = pygame.image.load("kuvat/logo.png")
        self.logo_rect = self.logo.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        self.upper_text = self.font.render("Avaruuskilpa", True, (4, 11, 209))
        self.lower_text = self.font.render("Aloita peli painamalla Spacebaria", True, (4, 11, 209))
        self.upper_text_rect = self.upper_text.get_rect(center=(self.screen_width // 2, self.screen_height - 700))
        self.lower_text_rect = self.lower_text.get_rect(center=(self.screen_width // 2, self.screen_height - 100))

    # Liikkuva tausta
    def move_background(self):
        for rect in self.background_rects:
            rect.y += 2
            if rect.top >= self.screen_height:
                rect.y = -self.screen_height

    def update_player_score(self):
        self.current_time = pygame.time.get_ticks() - self.start_time
        if self.current_time - self.score_update > self.score_update_delay:
            self.player_score += 1
            self.score_update = self.current_time
        self.player_score_surf = self.font.render(f"Pisteet: {self.player_score}", False, (4, 11, 209))
        self.points_rect = self.player_score_surf.get_rect(center=(600, 50))

    def reset_game(self):
        self.player_score = 0
        self.move_left = 0
        self.move_right = 0
        self.raketti.rect.topleft = (550, 630)
        self.tahti.reset_position()
        self.meteoriitti.reset_position()
        self.game_on = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if not self.game_on:
                            self.reset_game()

                    if self.game_on:
                        if event.key == pygame.K_LEFT:
                            self.move_left = -5
                        elif event.key == pygame.K_RIGHT:
                            self.move_right = 5

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.move_left = 0
                    elif event.key == pygame.K_RIGHT:
                        self.move_right = 0

            self.move_background()
            self.screen.blit(self.background, self.background_rects[0])
            self.screen.blit(self.background, self.background_rects[1])

            if self.game_on:
                # print("käynnissä")
                self.raketti.update(self.move_left, self.move_right, self.screen_width)
                self.tahti.update()
                self.meteoriitti.update()
                self.update_player_score()

                if self.raketti.rect.colliderect(self.tahti.rect):
                    # Collision occurred, handle it here
                    self.player_score += 10  # Increase the score or do any other action
                    self.tahti.reset_position()  # Reset the position of tahti

                if self.raketti.rect.colliderect(self.meteoriitti.rect):
                    # Collision occurred, handle it here
                    self.game_on = False
                    self.player_score = 0
                    self.move_left = 0
                    self.move_right = 0
                    # Reset the position of tahti

                self.screen.blit(self.raketti.image, self.raketti.rect)
                self.screen.blit(self.tahti.image, self.tahti.rect)
                self.screen.blit(self.meteoriitti.image, self.meteoriitti.rect)
                self.screen.blit(self.player_score_surf, self.points_rect)







            else:
                # Render starting screen elements if the game is not running.
                if self.fade:
                    if self.lower_text_effect < 255:
                        self.lower_text_effect += self.fade_speed
                    else:
                        self.lower_text_effect = 255
                        self.fade = False
                else:
                    if self.lower_text_effect > 0:
                        self.lower_text_effect -= self.fade_speed
                    else:
                        self.lower_text_effect = 0
                        self.fade = True
                #
                self.lower_text.set_alpha(self.lower_text_effect)
                self.screen.blit(self.logo, self.logo_rect)
                self.screen.blit(self.upper_text, self.upper_text_rect)
                self.screen.blit(self.lower_text, self.lower_text_rect)

            self.clock.tick(60)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
