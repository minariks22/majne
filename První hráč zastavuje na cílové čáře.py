     
import sys     
import random     
     
import pygame     
     
pygame.init()     
  
  
  
ROZLISENI_X = 1200     
ROZLISENI_Y = 600     
ROZLISENIX = 940     
ROZLISENIY = 600  
 
FPS = 60     
CERNA_BARVA = (0, 0, 0)     
BILA_BARVA = (255, 255, 255)     
pozadi_pozice = [10, 10]     
pozadi_obrazek = pygame.image.load('Dráha.png')    
obrazek = pygame.image.load("Panacek 2.png")     
jarda = pygame.image.load('Jarda2.png')    
score = 0  
medaile = pygame.image.load("Medaile 1.png")  
medaile2 = pygame.image.load('Medaile 2.png') 
 
velikost = 50    
vyska = 50     
velikost1 = 70  
pozice_x = (ROZLISENI_X - velikost) / 9.5     
pozice_y = (ROZLISENI_Y - velikost) / 1.2       
position_x = (ROZLISENI_X - vyska) / 9.5      
position_y = (ROZLISENI_Y - vyska) / 1.04     
pozicex = (ROZLISENI_X - velikost1) / 1.16  
pozicey = (ROZLISENI_Y - velikost1) / 20  
pozicex2 = (ROZLISENI_X - velikost1) / 1.01  
pozicey2 = (ROZLISENI_Y - velikost1) / 20 
 
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
    if position_x > ROZLISENI_X - vyska:  
        position_x = ROZLISENI_X - vyska  
    if position_y > ROZLISENI_Y - vyska:  
        position_y = ROZLISENI_Y - vyska  
    if position_x < 0:  
        position_x = 0   
    if position_y < 0:  
        position_y = 0 
    if position_x > ROZLISENIX - vyska: 
        position_x = ROZLISENIX - vyska 
    if position_y > ROZLISENIY - vyska: 
        position_y = ROZLISENIY- vyska 
    if position_x < 0:  
        position_x = 0   
    if position_y < 0:  
        position_y = 0
    if pozice_x > ROZLISENIX - vyska: 
        pozice_x = ROZLISENIX - vyska 
    if pozice_y > ROZLISENIY - vyska: 
        pozice_y = ROZLISENIY- vyska 
    if pozice_x < 0:  
        pozice_x = 0   
    if pozice_y < 0:  
        pozice_y = 0
     
        
          
      
      
      
      
    okno.fill(BILA_BARVA)     
         
         
         
    
        
    obrazek = pygame.transform.scale(obrazek, (velikost, velikost))     
      
    medaile = pygame.transform.scale(medaile, (velikost1, velikost1))  
     
    medaile_2 = pygame.transform.scale(medaile2, (velikost1, velikost1)) 
     
    jarda = pygame.transform.scale(jarda, (vyska, vyska))   
       
    okno.blit(pozadi_obrazek, pozadi_pozice)    
        
    okno.blit(obrazek, (pozice_x, pozice_y))    
        
    okno.blit(jarda, (position_x, position_y))    
      
    okno.blit(medaile, (pozicex, pozicey))  
     
    okno.blit(medaile_2, (pozicex2, pozicey2)) 
     
    pygame.display.update()     
         
    hodiny.tick(FPS)     
     
