#imports
import pygame
from pygame.locals import *

#initialisation de pygame
pygame.init()

#ouverture de la fenêtre pygame
fenetre = pygame.display.set_mode((1800, 900))


#chargement puis collage du fond
fond = pygame.image.load("fond.jpg").convert()


#chargement puis collage des personnages joueurs
sperso1 = pygame.image.load("perso1.png").convert_alpha()
position_perso1 = sperso1.get_rect()

sperso2 = pygame.image.load("perso2.png").convert_alpha()
position_perso2 = sperso2.get_rect()

sperso3 = pygame.image.load("perso3.png").convert_alpha()
position_perso3 = sperso3.get_rect()

sperso4 = pygame.image.load("perso4.png").convert_alpha()
position_perso4 = sperso4.get_rect()





#Rafraichissement d'écran
pygame.display.flip()

#boucle infinie
continuer= 1
#<variables>
PA=99
black = pygame.Color(0,0,0)
smallfont = pygame.font.SysFont("comicsansms", 25)
text= smallfont.render("PA: "+str(PA), True, black)
numperso=1
#</variables>

#<fonctions>
def selecperso(): #permet de changer de personnage utilisé en fonction de numperso
    global numperso
    if numperso < 1 :
        numperso = 4
    if numperso > 4 :
        numperso = 1
    if numperso == 1 :
        perso1()
    if numperso == 2 :
        perso2()
    if numperso == 3 :
        perso3()
    if numperso == 4 :
        perso4()


def perso1(): #regroupe l'ensemble des événements disponibles quand on utilise le personnage 1
        global PA
        eventperso1()

def eventperso1():
        global position_perso1
        listperso1=[14,14,99,99,7,60,70,2,40]
        if event.key == K_UP :
            if listperso1[2]>0 :
                position_perso1 = position_perso1.move(0,-100)
                listperso1[2]=listperso1[2]-1
        if event.key == K_DOWN:
            if listperso1[2]>0 :
                position_perso1 = position_perso1.move(0,100)
                listperso1[2]=listperso1[2]-1
        if event.key == K_RIGHT:
            if listperso1[2]>0 :
                position_perso1 = position_perso1.move(100,0)
                listperso1[2]=listperso1[2]-1
        if event.key == K_LEFT:
              if listperso1[2]>0 :
                  position_perso1 = position_perso1.move(-100,0)
                  listperso1[2]=listperso1[2]-1

def perso2(): #regroupe l'ensemble des événements disponibles quand on utilise le personnage 2
        global PA
        eventperso2()
def eventperso2():
        global position_perso2
        listperso2=[16,16,99,99,5,75,50,3,20]
        if event.key == K_UP :
              if listperso2[2]>0 :
                 position_perso2 = position_perso2.move(0,-100)
                 listperso2[2]=listperso2[2]-1
        if event.key == K_DOWN:
             if listperso2[2]>0 :
                position_perso2 = position_perso2.move(0,100)
                listperso2[2]=listperso2[2]-1
        if event.key == K_RIGHT:
              if listperso2[2]>0 :
                 position_perso2 = position_perso2.move(100,0)
                 listperso2[2]=listperso2[2]-1
        if event.key == K_LEFT:
            if listperso2[2]>0 :
                position_perso2 = position_perso2.move(-100,0)
                listperso2[2]=listperso2[2]-1
def perso3(): #regroupe l'ensemble des événements disponibles quand on utilise le personnage 3
        global PA
        eventperso3()
def eventperso3():
        global position_perso3
        listperso3=[10,10,99,99,3,80,65,0,30]
        if event.key == K_UP :
            if listperso3[2]>0 :
                position_perso3 = position_perso3.move(0,-100)
                listperso3[2]=listperso3[2]-1
        if event.key == K_DOWN:
            if listperso3[2]>0 :
                position_perso3 = position_perso3.move(0,100)
                listperso3[2]=listperso3[2]-1
        if event.key == K_RIGHT:
            if listperso3[2]>0 :
                position_perso3 = position_perso3.move(100,0)
                listperso3[2]=listperso3[2]-1
        if event.key == K_LEFT:
            if listperso3[2]>0 :
                position_perso3 = position_perso3.move(-100,0)
                listperso3[2]=listperso3[2]-1
def perso4(): #regroupe l'ensemble des événements disponibles quand on utilise le personnage 4
        global PA
        eventperso4()
def eventperso4():
        global position_perso4
        listperso4=[12,12,99,99,4,75,75,1,30]
        if event.key == K_UP :
            if listperso4[2]>0 :
                position_perso4 = position_perso4.move(0,-100)
                listperso4[2]=listperso4[2]-1
        if event.key == K_DOWN:
            if listperso4[2]>0 :
                position_perso4 = position_perso4.move(0,100)
                listperso4[2]=listperso4[2]-1
        if event.key == K_RIGHT:
            if listperso4[2]>0 :
                position_perso4 = position_perso4.move(100,0)
                listperso4[2]=listperso4[2]-1
        if event.key == K_LEFT:
            if listperso4[2]>0 :
                position_perso4 = position_perso4.move(-100,0)
                listperso4[2]=listperso4[2]-1
#</fonctions>
while continuer :
    for event in pygame.event.get():        #on parcours la liste de tous les évenements reçus
        if event.type == KEYDOWN :
            if event.type == QUIT:              #si un de ces évenements est de type QUIT
                continuer = 0            #on arrête la boucle
            if event.key == K_F11 :
                pygame.display.toggle_fullscreen()
            if event.key == K_a :
                numperso= numperso-1
            if event.key == K_e :
                numperso= numperso+1
            selecperso()

    fenetre.blit(fond, (0,0))
    fenetre.blit(sperso1, position_perso1)
    fenetre.blit(sperso2, position_perso2)
    fenetre.blit(sperso3, position_perso3)
    fenetre.blit(sperso4, position_perso4)

    pygame.display.flip()

pygame.quit()
print(PA)
