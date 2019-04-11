#imports
import pygame
from pygame.locals import *

#initialisation de pygame
pygame.init()

#ouverture de la fenêtre pygame
fenetre = pygame.display.set_mode((1920, 1080))


#chargement puis collage du fond
fond = pygame.image.load("fond.jpg").convert()


#chargement puis collage d'un personnage
goomba = pygame.image.load("perso.png").convert_alpha()
position_goomba = goomba.get_rect()



#Rafraichissement d'écran
pygame.display.flip()

#boucle infinie
continuer= 1
#<variables>
PA=5
black = pygame.Color(0,0,0)
smallfont = pygame.font.SysFont("comicsansms", 25)
text= smallfont.render("PA: "+str(PA), True, black)
#</variables>
while continuer :
    for event in pygame.event.get():        #on parcours la liste de tous les évenements reçus 
        print(event)
        text= smallfont.render("PA: "+str(PA), True, black)
        if event.type == QUIT:              #si un de ces évenements est de type QUIT
            continuer = 0                   #on arrête la boucle
        if event.type == KEYDOWN :          #éxecute les instructions indentées si une touche du clavier est enfoncée
            if event.key == K_F11 :
                pygame.display.toggle_fullscreen
            if event.key == K_UP:
                if PA>0 :
                    position_goomba = position_goomba.move(0,-100)
                    PA=PA-1
            if event.key == K_DOWN:
                if PA>0 :
                    position_goomba = position_goomba.move(0,100)
                    PA=PA-1
            if event.key == K_RIGHT:
                if PA>0 :
                    position_goomba = position_goomba.move(100,0)
                    PA=PA-1
            if event.key == K_LEFT:
                if PA>0 :
                    position_goomba = position_goomba.move(-100,0)
                    PA=PA-1
    fenetre.blit(fond, (0,0))
    fenetre.blit(goomba, position_goomba)
    fenetre.blit(text, (position_goomba.x+25,position_goomba.y-25))
    pygame.display.flip()

pygame.quit()
print(PA)
