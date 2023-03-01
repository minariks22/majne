  
import sys  
import random  
  
import pygame  
  
pygame.init()  
  
  
ROZLISENI_X = 1200  
ROZLISENI_Y = 600  
FPS = 60  
CERNA_BARVA = (0, 0, 0)  
BILA_BARVA = (255, 255, 255)  
pozadi_pozice = [10, 10]  
pozadi_obrazek = pygame.image.load('Dráha.png') 
obrazek = pygame.image.load('Panacek 2.png')  
jarda = pygame.image.load('Jarda2.png') 

velikost = 50 
vyska = 50  
pozice_x = (ROZLISENI_X - velikost) / 9.5  
pozice_y = (ROZLISENI_Y - velikost) / 1.2    
position_x = (ROZLISENI_X - vyska) / 9.5   
position_y = (ROZLISENI_Y - vyska) / 1.04  
rychlost = 2 
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
    if klavesy[pygame.K_LCTRL]:  
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
      
      
      
 
     
    obrazek = pygame.transform.scale(obrazek, (velikost, velikost))  
    
    jarda = pygame.transform.scale(jarda, (vyska, vyska))
    
    okno.blit(pozadi_obrazek, pozadi_pozice) 
     
    okno.blit(obrazek, (pozice_x, pozice_y)) 
     
    okno.blit(jarda, (position_x, position_y)) 
     
    pygame.display.update()  
      
    hodiny.tick(FPS)  
  
