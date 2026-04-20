import pygame
import random
pygame.init()
def genereaza_grila_culori():
    """Creeaza o matrice de 10x10 cu culori generate aleatoriu."""
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
            for _ in range(10)] for _ in range(10)]
latime_fereastra = 500
inaltime_fereastra = 500
ecran = pygame.display.set_mode((latime_fereastra, inaltime_fereastra))
pygame.display.set_caption("Grila de Culori - Regenerare la 5 secunde")
grila_culori = genereaza_grila_culori()
ruleaza = True
REGENEREAZA_EVENIMENT = pygame.USEREVENT + 1
pygame.time.set_timer(REGENEREAZA_EVENIMENT, 5000)

while ruleaza:
    ecran.fill((0, 0, 0))
    for y in range(10):
        for x in range(10):
            culoare_patrat = grila_culori[y][x]
            pygame.draw.rect(ecran, culoare_patrat, (x * 50, y * 50, 50, 50))
    pygame.display.flip()
    for eveniment in pygame.event.get():
        if eveniment.type == pygame.QUIT:
            ruleaza = False
        elif eveniment.type == REGENEREAZA_EVENIMENT:
            grila_culori = genereaza_grila_culori()
            print("Grila a fost regenerata automat!")
        elif eveniment.type == pygame.KEYDOWN:
            if eveniment.key == pygame.K_SPACE:
                grila_culori = genereaza_grila_culori()
pygame.quit()