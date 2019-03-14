#imports
import pygame
from pygame.locals import *

#initialisation de pygame
pygame.init()

#ouverture de la fenêtre pygame
fenetre = pygame.display.set_mode((1920, 1080))


#chargement puis collage du fond
fond = pygame.image.load("fond.jpg").convert()
fenetre.blit(fond, (0,0))

#chargement puis collage d'un personnage
goomba = pygame.image.load("perso.png").convert_alpha()
position_goomba = goomba.get_rect()

fenetre.blit(goomba, position_goomba)

#Rafraichissement d'écran
pygame.display.flip()

#boucle infinie
continuer= 1
while continuer :
    for event in pygame.event.get():        #on parcours la liste de tous les évenements reçus 
        if event.type == QUIT:              #si un de ces évenements est de type QUIT
            continuer = 0                   #on arrête la boucle
        if event.type == KEYDOWN :           #éxecute les instructions indentées si une touche du clavier est enfoncée
            if key.type == K_RIGHT:
                postion_goomba.move(100,0)
                
pygame.quit()
    







