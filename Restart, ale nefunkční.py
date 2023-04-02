      
import sys      
import random      
      
import pygame      
      
pygame.init()      
 
pygame.font.init() 
   
#Rozliseni 
ROZLISENI_X = 1200      
ROZLISENI_Y = 600      
ROZLISENIX = 940      
ROZLISENIY = 600  

#Definice
FPS = 20     
CERNA_BARVA = (0, 0, 0)      
CERVENA_BARVA = (255, 0, 0)
BILA_BARVA = (255, 255, 255)      
pozadi_pozice = [10, 10]      
pozadi_obrazek = pygame.image.load('Dráha.png')     
obrazek = pygame.image.load("Panacek 2.png")      
jarda = pygame.image.load('Jarda2.png')     
score1 = 0 
score2 = 0 
medaile = pygame.image.load("Medaile 1.png")   
medaile2 = pygame.image.load('Medaile 2.png')  
player1 = pygame.image.load('Hráč1.png') 
player2 = pygame.image.load('Hráč2.png') 


    
#Pozice a velikosti 
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
pozicex3 = (ROZLISENI_X - velikost) / 5.7 
pozicey3 = (ROZLISENI_Y - velikost) / 90 
pozicex4 = (ROZLISENI_X - velikost) / 3.1 
pozicey4 = (ROZLISENI_Y - velikost) / 90 
pozicex5 = (ROZLISENI_X - velikost) / 5 
pozicey5 = (ROZLISENI_Y - velikost) / 5 

rychlost = 8    
hodiny = pygame.time.Clock()      
      
  
      
okno = pygame.display.set_mode((ROZLISENI_X, ROZLISENI_Y))      
pygame.display.set_caption('Závod')      
      
      
while True:      
          
    for udalost in pygame.event.get():      
              
        if udalost.type == pygame.QUIT:      
                 
            pygame.quit()      
                  
            sys.exit()      
              
    #Klavesy      
    klavesy = pygame.key.get_pressed()      
          
    if klavesy[pygame.K_ESCAPE]:      
        pygame.quit()      
        sys.exit()      
      
    if klavesy[pygame.K_RIGHT]:      
        pozice_x += rychlost 
    if klavesy[pygame.K_RIGHT]:      
        score1 += 1      
    if klavesy[pygame.K_LCTRL]:      
        position_x += rychlost      
    if klavesy[pygame.K_LCTRL]:      
        score2 += 1      
    
        
          
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
    if score1 == 100: 
        score1 = 0 
    if score2 == 100: 
        score2 = 0
    
                             
         
     
 
        
     
    #Obrazky a skóre 
    okno.fill(BILA_BARVA)      
            
    obrazek = pygame.transform.scale(obrazek, (velikost, velikost))        
    
    medaile = pygame.transform.scale(medaile, (velikost1, velikost1))   
      
    medaile_2 = pygame.transform.scale(medaile2, (velikost1, velikost1))  
      
    jarda = pygame.transform.scale(jarda, (vyska, vyska))    
     
    player_1 = pygame.transform.scale(player1, (velikost, velikost)) 
     
    player_2 = pygame.transform.scale(player2, (velikost, velikost)) 
     
    okno.blit(pozadi_obrazek, pozadi_pozice)     
        
    okno.blit(obrazek, (pozice_x, pozice_y))     
         
    okno.blit(jarda, (position_x, position_y))     
       
    okno.blit(medaile, (pozicex, pozicey))   
      
    okno.blit(medaile_2, (pozicex2, pozicey2))  
     
    okno.blit(player_1, (pozicex3, pozicey3)) 
     
    okno.blit(player_2, (pozicex4, pozicey4))      

    font = pygame.font.Font(None, 74) 
     
    text = font.render(str(score1), 1, CERNA_BARVA) 
     
    okno.blit(text, (250,10)) 
    
    restart = font.render("Stiskni R pro restart", True, CERVENA_BARVA, CERNA_BARVA)
    
    if score1 == 95:
        okno.blit(restart, (300, 200))
        
    
    text = font.render(str(score2), 1, CERNA_BARVA)
    
    okno.blit(text, (420, 11))
     
    pygame.display.update()      
     
    pygame.display.flip() 
    
    
    hodiny.tick(FPS)      
     
     
