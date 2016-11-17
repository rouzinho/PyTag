# coding: utf8
import pygame

from pygame.locals import *


pygame.init()


#Ouverture de la fenetre Pygame

fenetre = pygame.display.set_mode((640, 480))


#Chargement et collage du fond

fond = pygame.image.load("background.jpg").convert()

fenetre.blit(fond, (0,0))


#Chargement et collage du personnage

perso = pygame.image.load("perso.png").convert()

font = pygame.font.Font(None, 76)

t = "ça marche"
text = font.render(t.decode('utf-8'), 1, (10, 10, 10))
textpos = text.get_rect()
textpos.centerx = fenetre.get_rect().centerx
fenetre.blit(text, textpos)

#fenetre.blit(perso, (200,300))


#Rafraichissement de l'ecran

pygame.display.flip()


#BOUCLE INFINIE

continuer = 1

while continuer:

    continuer = int(input())
