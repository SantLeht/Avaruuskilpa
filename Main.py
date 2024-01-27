import random

import pygame

def pisteet():
    aika = pygame.time.get_ticks() - aloita_aika
    pisteet = fontti_alateksti.render(f"{aika}",False,(0,0,255))
    pisteet_rect = pisteet.get_rect(center = (600,50))
    naytto.blit(pisteet,pisteet_rect)

pygame.init()

# Näyön määritys
naytto_leveys = 1200
naytto_korkeus = 800
naytto = pygame.display.set_mode((naytto_leveys, naytto_korkeus))

# Logon ja taustan määritys
logo = pygame.image.load("kuvat/logo.png").convert()
logo_aloitusnaytto = pygame.image.load("kuvat/logo.png")
tausta = pygame.image.load("kuvat/tausta.png").convert()
raketti = pygame.image.load("kuvat/raketti.png").convert_alpha()
tahti = pygame.image.load("kuvat/tahti.png").convert_alpha()
meteoriitti = pygame.image.load("kuvat/kivi.png").convert_alpha()

logo_muokattu = pygame.transform.scale(logo_aloitusnaytto, (300, 300))

pygame.display.set_icon(logo)
pygame.display.set_caption("Avaruuskilpa")

fontti_ylateksti = pygame.font.Font("fontti/Super Disco Personal Use.ttf", 100)
yla_teksti = fontti_ylateksti.render("Avaruuskilpa", True, (0, 0, 255))
fontti_alateksti = pygame.font.Font("fontti/Super Disco Personal Use.ttf", 50)
ala_teksti = fontti_alateksti.render("Aloita peli painamalla Spacebaria", True, (0, 0, 255))


tausta1_rect = tausta.get_rect(topleft=(0, 0))
tausta2_rect = tausta.get_rect(topleft=(0, -naytto_korkeus))

kello = pygame.time.Clock()

raketti_rect = raketti.get_rect(topleft=(250, 400))
raketti_x = 550
raketti_y = 630

tahti_rect = tahti.get_rect(topleft=(0, -300))
meteoriitti_rect = meteoriitti.get_rect(topleft=(400, -500))

teksti_alpha = 0
fade_nopeus = 100 / 30

liikuta_vasen = 0
liikuta_oikea = 0
liikuta_ylos = False
liikuta_alas = False
fade = True

peli_kaynnissa = False
#aloita_aika = 0
pelaaja_pisteet = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if not peli_kaynnissa and event.key == pygame.K_SPACE:
                peli_kaynnissa = True
                aloita_aika = pygame.time.get_ticks()

                meteoriitti_rect.top = 10
            if event.key == pygame.K_LEFT:
                liikuta_vasen = - 5

            elif event.key == pygame.K_RIGHT:
                liikuta_oikea = +5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                liikuta_vasen = 0
            if event.key == pygame.K_RIGHT:
                liikuta_oikea = 0

        if fade:
            if teksti_alpha < 255:
                teksti_alpha += fade_nopeus
            else:
                teksti_alpha = 255
                fade = False
        else:
            if teksti_alpha > 0:
                teksti_alpha -= fade_nopeus
            else:
                teksti_alpha = 0
                fade = True



    tausta1_rect.y += 1
    tausta2_rect.y += 1

    if tausta1_rect.top >= naytto_korkeus:
        tausta1_rect.y = -naytto_korkeus

    if tausta2_rect.top >= naytto_korkeus:
        tausta2_rect.y = -naytto_korkeus

    ala_teksti.set_alpha(teksti_alpha)

    if peli_kaynnissa:

        naytto.blit(tausta, tausta1_rect)
        naytto.blit(tausta, tausta2_rect)

        pisteet_teksti = fontti_alateksti.render(f"Pisteet: {pelaaja_pisteet}", False, (0, 0, 255))

        naytto.blit(pisteet_teksti, (10, 10))



        naytto.blit(raketti, raketti_rect)
        raketti_x += liikuta_vasen + liikuta_oikea
        raketti_rect.topleft = (raketti_x, raketti_y)

        if raketti_rect.x <0:
            raketti_rect.x = 1125

        if raketti_rect.x > 1200:
            raketti_rect.x = 0

        tahti_rect.y += 6
        if tahti_rect.top > naytto_korkeus:
            tahti_rect.x = random.randint(0, naytto_leveys - tahti.get_width())
            tahti_rect.y = -tahti.get_height()

        meteoriitti_rect.y += 6
        if meteoriitti_rect.top > naytto_korkeus:
            meteoriitti_rect.x = random.randint(0, naytto_leveys - meteoriitti.get_width())
            meteoriitti_rect.y = -meteoriitti.get_height()

        if meteoriitti_rect.colliderect(raketti_rect):
            peli_kaynnissa = False

        if tahti_rect.colliderect(raketti_rect):
            pelaaja_pisteet +=100
            tahti_rect.x = random.randint(0, naytto_leveys- tahti.get_width())
            tahti_rect.y =-tahti.get_height()



        naytto.blit(meteoriitti, meteoriitti_rect)

        naytto.blit(tahti, tahti_rect)

        naytto.blit(meteoriitti, meteoriitti_rect)



    else:
        pelaaja_pisteet =0
        naytto.blit(tausta, tausta1_rect)
        naytto.blit(tausta, tausta2_rect)
        naytto.blit(yla_teksti, (300, 100))
        naytto.blit(ala_teksti, (200, 600))
        naytto.blit(logo_muokattu, (440, 250))

    kello.tick(120)
    pygame.display.update()

