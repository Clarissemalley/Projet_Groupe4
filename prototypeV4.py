#imports
import pygame
from pygame.locals import *

#initialisation de pygame
pygame.init()

#ouverture de la fenêtre pygame
fenetre = pygame.display.set_mode((14*128, 8*128))
plateau = pygame.Rect(0,0,14*128,8*128)

#chargement puis collage du fond
fond = pygame.image.load("fond.gif").convert()


#chargement puis collage des personnages joueurs
sperso1 = pygame.image.load("Viking.gif").convert_alpha()
position_perso1 = sperso1.get_rect()
position_perso1 = position_perso1.move(1*128,0)

sperso2 = pygame.image.load("Samourai.gif").convert_alpha()
position_perso2 = sperso2.get_rect()
position_perso2 = position_perso2.move(3*128,2*128)

sperso3 = pygame.image.load("Athenien.gif").convert_alpha()
position_perso3 = sperso3.get_rect()
position_perso3 = position_perso3.move(0,4*128)

sperso4 = pygame.image.load("Pretresse.gif").convert_alpha()
position_perso4 = sperso4.get_rect()
position_perso4 = position_perso4.move(2*128,6*128)

smechant1 = pygame.image.load("Draugr.gif").convert_alpha()
position_mechant1 = smechant1.get_rect()
position_mechant1 = position_mechant1.move(12*128,3*128)

smechant2 = pygame.image.load("Draugr.gif").convert_alpha()
position_mechant2 = smechant2.get_rect()
position_mechant2 = position_mechant2.move(12*128,1*128)

smechant3 = pygame.image.load("Draugr.gif").convert_alpha()
position_mechant3 = smechant3.get_rect()
position_mechant3 = position_mechant3.move(12*128,2*128)





#Rafraichissement d'écran
pygame.display.flip()

#boucle infinie
continuer= 1
#<variables>
listperso1=[14,14,5,5,7,60,70,2,40]
listperso2=[16,16,4,4,5,75,50,3,20]
listperso3=[10,10,6,6,3,80,65,0,30]
listperso4=[12,12,5,5,4,75,75,1,30]
listmechant1=[5,5,4,4,3,80,90,0,20]
listmechant2=[5,5,4,4,3,80,90,0,20]
listmechant3=[5,5,4,4,3,80,90,0,20]

black = pygame.Color(0,0,0)
font = pygame.font.SysFont("arial", 25)
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
def interface(a):
    if a ==1 :
        statsbg1=font.render("PV: "+str(listperso1[0])+"/"+str(listperso1[1]),1, black)
        statsbg2=font.render("PA: "+str(listperso1[2])+"/"+str(listperso1[3]),1, black)
        statsbd1=font.render("ATK: "+str(listperso1[4])+" SPD:"+str(listperso1[5]),1, black)
        statsbd2=font.render("ACC: "+str(listperso1[6])+" DEF: "+str(listperso1[7]),1, black)
        statsbd3=font.render("LCK: "+str(listperso1[8]),1, black)
        position_pointeur=position_perso1
    elif a==2 :
        statsbg1=font.render("PV: "+str(listperso2[0])+"/"+str(listperso2[1]),1, black)
        statsbg2=font.render("PA: "+str(listperso2[2])+"/"+str(listperso2[3]),1, black)
        statsbd1=font.render("ATK: "+str(listperso2[4])+" SPD:"+str(listperso2[5]),1, black)
        statsbd2=font.render("ACC: "+str(listperso2[6])+" DEF: "+str(listperso2[7]),1, black)
        statsbd3=font.render("LCK: "+str(listperso2[8]),1, black)
    elif a==3 :
        statsbg1=font.render("PV: "+str(listperso3[0])+"/"+str(listperso3[1]),1, black)
        statsbg2=font.render("PA: "+str(listperso3[2])+"/"+str(listperso3[3]),1, black)
        statsbd1=font.render("ATK: "+str(listperso3[4])+" SPD:"+str(listperso3[5]),1, black)
        statsbd2=font.render("ACC: "+str(listperso3[6])+" DEF: "+str(listperso3[7]),1, black)
        statsbd3=font.render("LCK: "+str(listperso3[8]),1, black)
    elif a==4 :
        statsbg1=font.render("PV: "+str(listperso4[0])+"/"+str(listperso4[1]),1, black)
        statsbg2=font.render("PA: "+str(listperso4[2])+"/"+str(listperso4[3]),1, black)
        statsbd1=font.render("ATK: "+str(listperso4[4])+" SPD:"+str(listperso4[5]),1, black)
        statsbd2=font.render("ACC: "+str(listperso4[6])+" DEF: "+str(listperso4[7]),1, black)
        statsbd3=font.render("LCK: "+str(listperso4[8]),1, black)
    fenetre.blit(statsbg1,(10,570))
    fenetre.blit(statsbg2,(10,550))
    fenetre.blit(statsbd1,(1500,570))
    fenetre.blit(statsbd2,(1500,550))
    fenetre.blit(statsbd3,(1500,530))

def perso1(): #regroupe l'ensemble des ÃƒÆ’Ã‚Â©vÃƒÆ’Ã‚Â©nements disponibles quand on utilise le personnage 1
        eventperso1()

def eventperso1():
        list_perso = [position_perso1, position_perso2, position_perso3, position_perso4, position_mechant1, position_mechant2, position_mechant3]
        global position_perso1
        global listperso1
        if event.key == K_UP :
            if listperso1[2]>0 :
                if position_perso1.move(0,-128).collidelist(list_perso) == -1 and plateau.contains(position_perso1.move(0,-128)) == 1:
                    position_perso1 = position_perso1.move(0,-128)
                    listperso1[2]=listperso1[2]-1
        if event.key == K_DOWN:
            if listperso1[2]>0 :
                if position_perso1.move(0,128).collidelist(list_perso) == -1 and plateau.contains(position_perso1.move(0,128)) == 1:
                    position_perso1 = position_perso1.move(0,128)
                    listperso1[2]=listperso1[2]-1
        if event.key == K_RIGHT:
            if listperso1[2]>0 :
                if position_perso1.move(128,0).collidelist(list_perso) == -1 and plateau.contains(position_perso1.move(128,0)) == 1:
                    position_perso1 = position_perso1.move(128,0)
                    listperso1[2]=listperso1[2]-1
        if event.key == K_LEFT:
              if listperso1[2]>0 :
                  if position_perso1.move(-128,0).collidelist(list_perso) == -1 and plateau.contains(position_perso1.move(-128,0)) == 1:
                      position_perso1 = position_perso1.move(-128,0)
                      listperso1[2]=listperso1[2]-1

def perso2(): #regroupe l'ensemble des ÃƒÆ’Ã‚Â©vÃƒÆ’Ã‚Â©nements disponibles quand on utilise le personnage 2
        eventperso2()
def eventperso2():
        list_perso = [position_perso1, position_perso2, position_perso3, position_perso4, position_mechant1, position_mechant2, position_mechant3]
        global position_perso2
        global listperso2
        if event.key == K_UP :
              if listperso2[2]>0 :
                  if position_perso2.move(0,-128).collidelist(list_perso) == -1 and plateau.contains(position_perso2.move(0,-128)) == 1:
                     position_perso2 = position_perso2.move(0,-128)
                     listperso2[2]=listperso2[2]-1
        if event.key == K_DOWN:
             if listperso2[2]>0 :
                 if position_perso2.move(0,128).collidelist(list_perso) == -1 and plateau.contains(position_perso2.move(0,128)) == 1:
                    position_perso2 = position_perso2.move(0,128)
                    listperso2[2]=listperso2[2]-1
        if event.key == K_RIGHT:
              if listperso2[2]>0 :
                  if position_perso2.move(128,0).collidelist(list_perso) == -1 and plateau.contains(position_perso2.move(128,0)) == 1:
                     position_perso2 = position_perso2.move(128,0)
                     listperso2[2]=listperso2[2]-1
        if event.key == K_LEFT:
            if listperso2[2]>0 :
                if position_perso2.move(-128,0).collidelist(list_perso) == -1 and plateau.contains(position_perso2.move(-128,0)) == 1:
                    position_perso2 = position_perso2.move(-128,0)
                    listperso2[2]=listperso2[2]-1

def perso3(): #regroupe l'ensemble des ÃƒÆ’Ã‚Â©vÃƒÆ’Ã‚Â©nements disponibles quand on utilise le personnage
        eventperso3()
def eventperso3():
        list_perso = [position_perso1, position_perso2, position_perso3, position_perso4, position_mechant1, position_mechant2, position_mechant3]
        global position_perso3
        global listperso3
        if event.key == K_UP :
            if listperso3[2]>0 :
                if position_perso3.move(0,-128).collidelist(list_perso) == -1 and plateau.contains(position_perso3.move(0,-128)) == 1:
                    position_perso3 = position_perso3.move(0,-128)
                    listperso3[2]=listperso3[2]-1
        if event.key == K_DOWN:
            if listperso3[2]>0 :
                if position_perso3.move(0,128).collidelist(list_perso) == -1 and plateau.contains(position_perso3.move(0,128)) == 1:
                    position_perso3 = position_perso3.move(0,128)
                    listperso3[2]=listperso3[2]-1
        if event.key == K_RIGHT:
            if listperso3[2]>0 :
                if position_perso3.move(128,0).collidelist(list_perso) == -1 and plateau.contains(position_perso3.move(128,0)) == 1:
                    position_perso3 = position_perso3.move(128,0)
                    listperso3[2]=listperso3[2]-1
        if event.key == K_LEFT:
            if listperso3[2]>0 :
                if position_perso3.move(-128,0).collidelist(list_perso) == -1 and plateau.contains(position_perso3.move(-128,0)) == 1:
                    position_perso3 = position_perso3.move(-128,0)
                    listperso3[2]=listperso3[2]-1

def perso4(): #regroupe l'ensemble des ÃƒÆ’Ã‚Â©vÃƒÆ’Ã‚Â©nements disponibles quand on utilise le personnage 4
        eventperso4()
def eventperso4():
        list_perso = [position_perso1, position_perso2, position_perso3, position_perso4, position_mechant1, position_mechant2, position_mechant3]
        global position_perso4
        global listperso4
        if event.key == K_UP :
            if listperso4[2]>0 :
                if position_perso4.move(0,-128).collidelist(list_perso) == -1 and plateau.contains(position_perso4.move(0,-128)) == 1:
                    position_perso4 = position_perso4.move(0,-128)
                    listperso4[2]=listperso4[2]-1
        if event.key == K_DOWN:
            if listperso4[2]>0 :
                if position_perso4.move(0,128).collidelist(list_perso) == -1 and plateau.contains(position_perso4.move(0,128)) == 1:
                    position_perso4 = position_perso4.move(0,128)
                    listperso4[2]=listperso4[2]-1
        if event.key == K_RIGHT:
            if listperso4[2]>0 :
                if position_perso4.move(128,0).collidelist(list_perso) == -1 and plateau.contains(position_perso4.move(128,0)) == 1:
                    position_perso4 = position_perso4.move(128,0)
                    listperso4[2]=listperso4[2]-1
        if event.key == K_LEFT:
            if listperso4[2]>0 :
                if position_perso4.move(-128,0).collidelist(list_perso) == -1 and plateau.contains(position_perso4.move(-128,0)) == 1:
                    position_perso4 = position_perso4.move(-128,0)
                    listperso4[2]=listperso4[2]-1

#</fonctions>
while continuer :
    for event in pygame.event.get():        #on parcours la liste de tous les évenements reçus
        if event.type == KEYDOWN :
            if event.type == QUIT:              #si un de ces évenements est de type QUIT
                continuer = 0            #on arrête la boucle
            if event.key == K_p :
                continuer = 0
            if event.key == K_F11 :
                pygame.display.toggle_fullscreen()
            if event.key == K_a :
                numperso= numperso-1
            if event.key == K_e :
                numperso= numperso+1
            selecperso()
    

    fenetre.blit(fond, (0,0)
    fenetre.blit(sperso1, position_perso1)
    fenetre.blit(sperso2, position_perso2)
    fenetre.blit(sperso3, position_perso3)
    fenetre.blit(sperso4, position_perso4)
    fenetre.blit(smechant1, position_mechant1)
    fenetre.blit(smechant2, position_mechant2)
    fenetre.blit(smechant3, position_mechant3)
    interface(numperso)

    pygame.display.flip()

pygame.quit()
