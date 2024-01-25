import pygame

from raketti import Raketti

#Näyön määritys
naytto_leveys = 1200
naytto_korkeus = 900
naytto = pygame.display.set_mode((naytto_leveys, naytto_korkeus))

#Logon ja taustan määritys
logo = pygame.image.load("logo.png").convert()
tausta = pygame.image.load("tausta.png").convert()

def main():
    pygame.init()




    pygame.display.set_icon(logo)
    pygame.display.set_caption("Avaruuskilpa")

    kello = pygame.time.Clock()
    raketti = Raketti(naytto, naytto_leveys, naytto_korkeus)

    run = True
    liikuta_vasen = False
    liikuta_oikea = False
    liikuta_ylos = False
    liikuta_alas = False

    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    liikuta_vasen = True
                elif event.key == pygame.K_RIGHT:
                    liikuta_oikea = True
                elif event.key == pygame.K_UP:
                    liikuta_ylos = True
                elif event.key == pygame.K_DOWN:
                    liikuta_alas = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    liikuta_vasen = False
                elif event.key == pygame.K_RIGHT:
                    liikuta_oikea = False
                elif event.key == pygame.K_UP:
                    liikuta_ylos = False
                elif event.key == pygame.K_DOWN:
                    liikuta_alas = False

        if liikuta_vasen:
            raketti.liikutaRaketti(-raketti.nopeus, 0)
        if liikuta_oikea:
            raketti.liikutaRaketti(raketti.nopeus, 0)
        if liikuta_ylos:
            raketti.liikutaRaketti(0, -raketti.nopeus)
        if liikuta_alas:
            raketti.liikutaRaketti(0, raketti.nopeus)

        naytto.blit(tausta, [0, 0])
        raketti.luoRaketti()
        pygame.display.update()
        kello.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
