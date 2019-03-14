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
while continuer :
    for event in pygame.event.get():        #on parcours la liste de tous les évenements reçus 
        print(event)
        if event.type == QUIT:              #si un de ces évenements est de type QUIT
            continuer = 0                   #on arrête la boucle
        if event.type == KEYDOWN :          #éxecute les instructions indentées si une touche du clavier est enfoncée
            if event.key == K_UP:
                position_goomba = position_goomba.move(0,-100)
            if event.key == K_DOWN:
                position_goomba = position_goomba.move(0,100)
            if event.key == K_RIGHT:
                position_goomba = position_goomba.move(100,0)
            if event.key == K_LEFT:
                position_goomba = position_goomba.move(-100,0)
                
    fenetre.blit(fond, (0,0))
    fenetre.blit(goomba, position_goomba)
    pygame.display.flip()

pygame.quit()
