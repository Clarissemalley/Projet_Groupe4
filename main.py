#imports
import pygame
from pygame.locals import *
import random

#initialisation de pygame
pygame.init()

#ouverture de la fenêtre pygame
fenetre = pygame.display.set_mode((11*128, 7*128))
plateau = pygame.Rect(0,0,11*128,7*128)

#chargement puis collage du fond
fond = pygame.image.load("fond.gif").convert_alpha()


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
position_mechant1 = position_mechant1.move(9*128,1*128)

smechant2 = pygame.image.load("Satyre.gif").convert_alpha()
position_mechant2 = smechant2.get_rect()
position_mechant2 = position_mechant2.move(9*128,3*128)

smechant3 = pygame.image.load("Kappa.gif").convert_alpha()
position_mechant3 = smechant3.get_rect()
position_mechant3 = position_mechant3.move(9*128,5*128)

pointeur = pygame.image.load("pointeur.png").convert_alpha()
position_pointeur = pointeur.get_rect()

poubelle = pygame.Rect(-128,-128, 128, 128)

#Rafraichissement d'écran
pygame.display.flip()

#boucle infinie
continuer= 1
#<variables>
#[PV;PVmax;PA;PAmax;ATK;ACC;SPD;DEF;LCK]
listperso1=[14,14,5,5,7,60,70,2,40]
listperso2=[0,16,4,4,5,75,50,3,20]
listperso3=[10,10,6,6,3,80,65,0,30]
listperso4=[12,12,5,5,4,75,75,1,30]
listmechant1=[5,5,4,4,3,80,90,0,20]
listmechant2=[10,10,5,5,5,70,50,0,25]
listmechant3=[12,12,3,3,3,65,40,1,15]

black = pygame.Color(0,0,0)
font = pygame.font.SysFont("arial", 25)
numperso=1
numally=3
#<fonctions>
def selecperso(): #permet de changer de personnage utilisé en fonction de numperso
    global numperso
    global numally
    if numperso < 1 :
        numperso = 4
    if numperso > 7 :
        numperso = 1
    if numperso == 1 :
        if not listmechant1[0]<=0:
            mechant1()
        else:
            numperso=numperso+1
    if numperso == 2 :
        if not listperso3[0]<=0:
           numally=3
           perso3()
        else:
            numperso=numperso+1
    if numperso == 3 :
        if not listperso1[0]<=0:
            numally=1
            perso1()
        else:
            numperso=numperso+1
    if numperso == 4 :
        if not listperso4[0]<=0:
            numally=4
            perso4()
        else:
            numperso=numperso+1
    if numperso == 5 :
        if not listperso2[0]<=0:
            numally=2
            perso2()
        else:
            numperso=numperso+1
    if numperso == 6:
        if not listmechant2[0]<=0:
            mechant2()
        else:
            numperso=numperso+1
    if numperso == 7:
        if not listmechant3[0]<=0:
            mechant3()
        else :
            numperso=numperso+1
def interface(a):
    if a ==1 :
        statsbg1=font.render("PV: "+str(listperso1[0])+"/"+str(listperso1[1]),1, black)
        statsbg2=font.render("PA: "+str(listperso1[2])+"/"+str(listperso1[3]),1, black)
        statsbd1=font.render("ATK: "+str(listperso1[4])+" SPD:"+str(listperso1[5]),1, black)
        statsbd2=font.render("ACC: "+str(listperso1[6])+" DEF: "+str(listperso1[7]),1, black)
        statsbd3=font.render("LCK: "+str(listperso1[8]),1, black)
        position_pointeur=position_perso1.move(25,-25)
    elif a==2 :
        statsbg1=font.render("PV: "+str(listperso2[0])+"/"+str(listperso2[1]),1, black)
        statsbg2=font.render("PA: "+str(listperso2[2])+"/"+str(listperso2[3]),1, black)
        statsbd1=font.render("ATK: "+str(listperso2[4])+" SPD:"+str(listperso2[5]),1, black)
        statsbd2=font.render("ACC: "+str(listperso2[6])+" DEF: "+str(listperso2[7]),1, black)
        statsbd3=font.render("LCK: "+str(listperso2[8]),1, black)
        position_pointeur=position_perso2.move(25,-25)
    elif a==3 :
        statsbg1=font.render("PV: "+str(listperso3[0])+"/"+str(listperso3[1]),1, black)
        statsbg2=font.render("PA: "+str(listperso3[2])+"/"+str(listperso3[3]),1, black)
        statsbd1=font.render("ATK: "+str(listperso3[4])+" SPD:"+str(listperso3[5]),1, black)
        statsbd2=font.render("ACC: "+str(listperso3[6])+" DEF: "+str(listperso3[7]),1, black)
        statsbd3=font.render("LCK: "+str(listperso3[8]),1, black)
        position_pointeur=position_perso3.move(25,-25)
    elif a==4 :
        statsbg1=font.render("PV: "+str(listperso4[0])+"/"+str(listperso4[1]),1, black)
        statsbg2=font.render("PA: "+str(listperso4[2])+"/"+str(listperso4[3]),1, black)
        statsbd1=font.render("ATK: "+str(listperso4[4])+" SPD:"+str(listperso4[5]),1, black)
        statsbd2=font.render("ACC: "+str(listperso4[6])+" DEF: "+str(listperso4[7]),1, black)
        statsbd3=font.render("LCK: "+str(listperso4[8]),1, black)
        position_pointeur=position_perso4.move(25,-25)

    pvmechant1=font.render("PV: "+str(listmechant1[0])+"/"+str(listmechant1[1]),1, black)
    pvmechant2=font.render("PV: "+str(listmechant2[0])+"/"+str(listmechant2[1]),1, black)
    pvmechant3=font.render("PV: "+str(listmechant3[0])+"/"+str(listmechant3[1]),1, black)

    fenetre.blit(statsbg1,(0*128,4*128))
    fenetre.blit(statsbg2,(0*128,4*128+30))
    fenetre.blit(statsbd1,(10*128-70,4*128))    #Permet de definir l'endroit où les stats s'affichent
    fenetre.blit(statsbd2,(10*128-70,4*128+25))
    fenetre.blit(statsbd3,(10*128-70,4*128+50))
    fenetre.blit(pvmechant1,(0*128,0*128))
    fenetre.blit(pvmechant2,(1*128,0*128))
    fenetre.blit(pvmechant3,(2*128,0*128))
    fenetre.blit(pointeur,position_pointeur)
def mort_affichage():
    global position_perso1
    global position_perso2
    global position_perso3
    global position_perso4
    global position_mechant1
    global position_mechant2
    global position_mechant3
    if listperso1[0]<=0:
        position_perso1=position_perso1.clamp(poubelle)

    if listperso2[0]<=0:
        position_perso2=position_perso2.clamp(poubelle)

    if listperso3[0]<=0:
        position_perso3=position_perso3.clamp(poubelle)

    if listperso4[0]<=0:
        position_perso4=position_perso4.clamp(poubelle)

    if listmechant1[0]<=0:
        position_mechant1=position_mechant1.clamp(poubelle)

    if listmechant2[0]<=0:
        position_mechant2=position_mechant2.clamp(poubelle)

    if listmechant3[0]<=0:
        position_mechant3=position_mechant3.clamp(poubelle)


def degats(Att, Def):   #Permet de calculer les degats au Defenseur(Def) au terme de son combat contre l'Attaquant(Att)
    touche=0            #Variable egale a 0 si l'attaque rate sa cible ou a 1 si elle touche
    crit=0              #Variable egale a 0 si l'attaque est normale ou a 1 si elle est critique
    alea=random.randint(0, 99)

    if alea<=Att[5]:
       touche=1

    if touche==1:
       alea=random.randint(0, 99)
       if alea<=Att[8]:
          crit=1
       if crit==1:
          if Def[7]>=int(Att[4]*1.5):
             DGT=0
          else:
             DGT=int(Att[4]*1.5)-Def[7]
       else:
          if Def[7]>=Att[4]:
             DGT=0
          else:
             DGT=Att[4]-Def[7]

       Def[0]=Def[0]-DGT

def movemechant(mechant) :
    boucle = 1
    while boucle ==1:
      direction = random.randint(0, 3)
      if direction == 0 and plateau.contains(mechant.move(0, -128)) == 1:
         return("U")
         boucle = 0
      if direction == 1 and plateau.contains(mechant.move(0, 128)) == 1:
         return("B")
         boucle = 0
      if direction == 2 and plateau.contains(mechant.move(128, 0)) == 1:
         return("R")
         boucle = 0
      if direction == 3 and plateau.contains(mechant.move(-128, 0)) == 1:
         return("L")
         boucle = 0

def perso1(): #regroupe l'ensemble des evenements disponibles quand on utilise le personnage 1
        eventperso1()

def eventperso1():
        list_perso = [position_perso1, position_perso2, position_perso3, position_perso4, position_mechant1, position_mechant2, position_mechant3]
        list_mechant = [position_mechant1, position_mechant2, position_mechant3]
        list_statsmechant = [listmechant1, listmechant2, listmechant3]
        global position_perso1
        listperso1=[14,14,99,99,7,60,70,2,40]
        if event.key == K_UP :
            if listperso1[2]>0 :
                if position_perso1.move(0,-128).collidelist(list_perso) == -1 and position_perso1.move(0,-128).collidelist(list_mechant) == -1 and plateau.contains(position_perso1.move(0,-128)) == 1:
                    position_perso1 = position_perso1.move(0,-128)
                    listperso1[2]=listperso1[2]-1
        if event.key == K_DOWN:
            if listperso1[2]>0 :
                if position_perso1.move(0,128).collidelist(list_perso) == -1 and position_perso1.move(0,128).collidelist(list_mechant) == -1 and plateau.contains(position_perso1.move(0,128)) == 1:
                    position_perso1 = position_perso1.move(0,128)
                    listperso1[2]=listperso1[2]-1
        if event.key == K_RIGHT:
            if listperso1[2]>0 :
                if position_perso1.move(128,0).collidelist(list_perso) == -1 and position_perso1.move(128,0).collidelist(list_mechant) == -1 and plateau.contains(position_perso1.move(128,0)) == 1:
                    position_perso1 = position_perso1.move(128,0)
                    listperso1[2]=listperso1[2]-1
        if event.key == K_LEFT:
              if listperso1[2]>0 :
                  if position_perso1.move(-128,0).collidelist(list_perso) == -1 and position_perso1.move(-128,0).collidelist(list_mechant) == -1 and plateau.contains(position_perso1.move(-128,0)) == 1:
                      position_perso1 = position_perso1.move(-128,0)
                      listperso1[2]=listperso1[2]-1
        if pygame.mouse.get_pressed()[0]==1:
            curseur = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],2,2)
            if curseur.collidelist(list_mechant) != -1:
                if list_mechant[curseur.collidelist(list_mechant)].colliderect(position_perso1.inflate(5,5)):
                    degats(listperso1, list_statsmechant[curseur.collidelist(list_mechant)])
                    listperso1[2]=0

def perso2(): #regroupe l'ensemble des evenements disponibles quand on utilise le personnage 2
        eventperso2()
def eventperso2():
        list_perso = [position_perso1, position_perso2, position_perso3, position_perso4, position_mechant1, position_mechant2, position_mechant3]
        list_mechant = [position_mechant1, position_mechant2, position_mechant3]
        list_statsmechant = [listmechant1, listmechant2, listmechant3]
        global position_perso2
        listperso2=[16,16,99,99,5,75,50,3,20]
        if event.key == K_UP :
              if listperso2[2]>0 :
                  if position_perso2.move(0,-128).collidelist(list_perso) == -1 and position_perso2.move(0,-128).collidelist(list_mechant) == -1 and plateau.contains(position_perso2.move(0,-128)) == 1:
                     position_perso2 = position_perso2.move(0,-128)
                     listperso2[2]=listperso2[2]-1
        if event.key == K_DOWN:
             if listperso2[2]>0 :
                 if position_perso2.move(0,128).collidelist(list_perso) == -1 and position_perso2.move(0,128).collidelist(list_mechant) == -1 and plateau.contains(position_perso2.move(0,128)) == 1:
                    position_perso2 = position_perso2.move(0,128)
                    listperso2[2]=listperso2[2]-1
        if event.key == K_RIGHT:
              if listperso2[2]>0 :
                  if position_perso2.move(128,0).collidelist(list_perso) == -1 and position_perso2.move(128,0).collidelist(list_mechant) == -1 and plateau.contains(position_perso2.move(128,0)) == 1:
                     position_perso2 = position_perso2.move(128,0)
                     listperso2[2]=listperso2[2]-1
        if event.key == K_LEFT:
            if listperso2[2]>0 :
                if position_perso2.move(-128,0).collidelist(list_perso) == -1 and position_perso2.move(-128,0).collidelist(list_mechant) == -1 and plateau.contains(position_perso2.move(-128,0)) == 1:
                    position_perso2 = position_perso2.move(-128,0)
                    listperso2[2]=listperso2[2]-1
        if pygame.mouse.get_pressed()[0]==1:
            curseur = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],2,2)
            if curseur.collidelist(list_mechant) != -1:
                if list_mechant[curseur.collidelist(list_mechant)].colliderect(position_perso2.inflate(5,5)):
                    degats(listperso2, list_statsmechant[curseur.collidelist(list_mechant)])
                    listperso2[2]=0

def perso3(): #regroupe l'ensemble des evenements disponibles quand on utilise le personnage
        eventperso3()
def eventperso3():
        list_perso = [position_perso1, position_perso2, position_perso3, position_perso4, position_mechant1, position_mechant2, position_mechant3]
        list_mechant = [position_mechant1, position_mechant2, position_mechant3]
        list_statsmechant = [listmechant1, listmechant2, listmechant3]
        global position_perso3
        listperso3=[10,10,99,99,3,80,65,0,30]
        if event.key == K_UP :
            if listperso3[2]>0 :
                if position_perso3.move(0,-128).collidelist(list_perso) == -1 and position_perso3.move(0,-128).collidelist(list_mechant) == -1 and plateau.contains(position_perso3.move(0,-128)) == 1:
                    position_perso3 = position_perso3.move(0,-128)
                    listperso3[2]=listperso3[2]-1
        if event.key == K_DOWN:
            if listperso3[2]>0 :
                if position_perso3.move(0,128).collidelist(list_perso) == -1 and position_perso3.move(0,128).collidelist(list_mechant) == -1 and plateau.contains(position_perso3.move(0,128)) == 1:
                    position_perso3 = position_perso3.move(0,128)
                    listperso3[2]=listperso3[2]-1
        if event.key == K_RIGHT:
            if listperso3[2]>0 :
                if position_perso3.move(128,0).collidelist(list_perso) == -1 and position_perso3.move(128,0).collidelist(list_mechant) == -1 and plateau.contains(position_perso3.move(128,0)) == 1:
                    position_perso3 = position_perso3.move(128,0)
                    listperso3[2]=listperso3[2]-1
        if event.key == K_LEFT:
            if listperso3[2]>0 :
                if position_perso3.move(-128,0).collidelist(list_perso) == -1 and position_perso3.move(-128,0).collidelist(list_mechant) == -1 and plateau.contains(position_perso3.move(-128,0)) == 1:
                    position_perso3 = position_perso3.move(-128,0)
                    listperso3[2]=listperso3[2]-1
        if pygame.mouse.get_pressed()[0]==1:
            curseur = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],2,2)
            if curseur.collidelist(list_mechant) != -1:
                if list_mechant[curseur.collidelist(list_mechant)].colliderect(position_perso3.inflate(5,5)):
                    degats(listperso3, list_statsmechant[curseur.collidelist(list_mechant)])
                    listperso3[2]=0

def perso4(): #regroupe l'ensemble des evenements disponibles quand on utilise le personnage 4

        eventperso4()
def eventperso4():
        list_perso = [position_perso1, position_perso2, position_perso3, position_perso4]
        list_mechant = [position_mechant1, position_mechant2, position_mechant3]
        list_statsmechant = [listmechant1, listmechant2, listmechant3]
        global position_perso4
        listperso4=[12,12,99,99,4,75,75,1,30]
        if event.key == K_UP :
            if listperso4[2]>0 :
                if position_perso4.move(0,-128).collidelist(list_perso) == -1 and position_perso4.move(0,-128).collidelist(list_mechant) == -1 and plateau.contains(position_perso4.move(0,-128)) == 1:
                    position_perso4 = position_perso4.move(0,-128)
                    listperso4[2]=listperso4[2]-1
        if event.key == K_DOWN:
            if listperso4[2]>0 :
                if position_perso4.move(0,128).collidelist(list_perso) == -1 and position_perso4.move(0,128).collidelist(list_mechant) == -1 and plateau.contains(position_perso4.move(0,128)) == 1:
                    position_perso4 = position_perso4.move(0,128)
                    listperso4[2]=listperso4[2]-1
        if event.key == K_RIGHT:
            if listperso4[2]>0 :
                if position_perso4.move(128,0).collidelist(list_perso) == -1 and position_perso4.move(128,0).collidelist(list_mechant) == -1 and plateau.contains(position_perso4.move(128,0)) == 1:
                    position_perso4 = position_perso4.move(128,0)
                    listperso4[2]=listperso4[2]-1
        if event.key == K_LEFT:
            if listperso4[2]>0 :
                if position_perso4.move(-128,0).collidelist(list_perso) == -1 and position_perso4.move(-128,0).collidelist(list_mechant) == -1 and plateau.contains(position_perso4.move(-128,0)) == 1:
                    position_perso4 = position_perso4.move(-128,0)
                    listperso4[2]=listperso4[2]-1
        if pygame.mouse.get_pressed()[0]==1:
            curseur = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],2,2)
            if curseur.collidelist(list_mechant) != -1:
                if list_mechant[curseur.collidelist(list_mechant)].colliderect(position_perso4.inflate(5,5)):
                    degats(listperso4, list_statsmechant[curseur.collidelist(list_mechant)])
                    listperso4[2]=0
def mechant1():
    global position_mechant1
    list_perso = [position_perso1, position_perso2, position_perso3, position_perso4]
    list_mechant=[position_mechant1,position_mechant2,position_mechant3]
    list_statsperso=[listperso1, listperso2, listperso3, listperso4]
    while listmechant1[2] > 0:
        if position_mechant1.inflate(5,5).collidelist(list_perso) != -1:
           degats(listmechant1, list_statsperso[position_mechant1.inflate(5,5).collidelist(list_perso)])
           listmechant1[2]=0
        else:
            direction = movemechant(position_mechant1)
            if direction == "U":
                position_mechant1 = position_mechant1.move(0, -128)
            if direction == "B":
                position_mechant1 = position_mechant1.move(0, 128)
            if direction == "R":
                position_mechant1 = position_mechant1.move(128,0)
            if direction == "L":
                position_mechant1 = position_mechant1.move(-128,0)
            listmechant1[2]=listmechant1[2]-1
    listmechant1[2]=listmechant1[3]


def mechant2():
    global position_mechant2
    list_perso = [position_perso1, position_perso2, position_perso3, position_perso4]
    list_mechant=[position_mechant1,position_mechant2,position_mechant3]
    list_statsperso=[listperso1, listperso2, listperso3, listperso4]
    while listmechant2[2] > 0:
        if position_mechant2.inflate(5,5).collidelist(list_perso) != -1:
           degats(listmechant2, list_statsperso[position_mechant2.inflate(5,5).collidelist(list_perso)])
           listmechant2[2]=0
        else:
            direction = movemechant(position_mechant2)
            if direction == "U":
                position_mechant2 = position_mechant2.move(0, -128)
            if direction == "B":
                position_mechant2 = position_mechant2.move(0, 128)
            if direction == "R":
                position_mechant2 = position_mechant2.move(128,0)
            if direction == "L":
                position_mechant2 = position_mechant2.move(-128,0)
            listmechant2[2]=listmechant2[2]-1
    listmechant2[2]=listmechant2[3]


def mechant3():
    global position_mechant3
    list_perso = [position_perso1, position_perso2, position_perso3, position_perso4]
    list_mechant=[position_mechant1,position_mechant2,position_mechant3]
    list_statsperso=[listperso1, listperso2, listperso3, listperso4]
    while listmechant3[2] > 0:
        if position_mechant3.inflate(5,5).collidelist(list_perso) != -1:
           degats(listmechant3, list_statsperso[position_mechant3.inflate(5,5).collidelist(list_perso)])
           listmechant3[2]=0
        else:
            direction = movemechant(position_mechant1)
            if direction == "U":
                position_mechant3 = position_mechant3.move(0, -128)
            if direction == "B":
                position_mechant3 = position_mechant3.move(0, 128)
            if direction == "R":
                position_mechant3 = position_mechant3.move(128,0)
            if direction == "L":
                position_mechant3 = position_mechant3.move(-128,0)
            listmechant3[2]=listmechant3[2]-1
    listmechant3[2]=listmechant3[3]

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
            if event.key == K_SPACE :
                numperso= numperso+1
            selecperso()
    mort_affichage()
    fenetre.blit(fond, (0,0))
    fenetre.blit(sperso1, position_perso1)
    fenetre.blit(sperso2,position_perso2)
    fenetre.blit(sperso3, position_perso3)
    fenetre.blit(sperso4, position_perso4)
    fenetre.blit(smechant1, position_mechant1)
    fenetre.blit(smechant2, position_mechant2)
    fenetre.blit(smechant3, position_mechant3)

    interface(numally)

    pygame.display.flip()


pygame.quit()
