
import sys
import random

import pygame

pygame.init()


ROZLISENI_X = 1500
ROZLISENI_Y = 600
FPS = 60
CERNA_BARVA = (0, 0, 0)
BILA_BARVA = (255, 255, 255)

velikost = 50
pozice_x = (ROZLISENI_X - velikost) / -2
pozice_y = (ROZLISENI_Y - velikost) / 6
rychlost = 2 
position_x = (ROZLISENI_X - velikost) / 4 
position_y = (ROZLISENI_Y - velikost) / 4 
hodiny = pygame.time.Clock()



okno = pygame.display.set_mode((ROZLISENI_X, ROZLISENI_Y))
pygame.display.set_caption('Závod')


while True:
    
    for udalost in pygame.event.get():
        
        if udalost.type == pygame.QUIT:
           
            pygame.quit()
            
            sys.exit()

    
    klavesy = pygame.key.get_pressed()
    
    if klavesy[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    if klavesy[pygame.K_RIGHT]:
        pozice_x += rychlost
    if klavesy[pygame.K_LEFT]:
        position_x += rychlost
    
    
    
    if pozice_x > ROZLISENI_X - velikost:
        pozice_x = ROZLISENI_X - velikost
    if pozice_y > ROZLISENI_Y - velikost:
        pozice_y = ROZLISENI_Y - velikost
    if pozice_x < 0:
        pozice_x = 0
    if pozice_y < 0:
        pozice_y = 0
    
    
    okno.fill(BILA_BARVA)
    
    
    
    obrazek = pygame.image.load('C:/Users/PC/OneDrive/Plocha/Pandulak .png')
    
    obrazek = pygame.transform.scale(obrazek, (velikost, velikost))
    
    okno.blit(obrazek, (pozice_x, pozice_y))
    
    pygame.display.update()
    
    hodiny.tick(FPS)

