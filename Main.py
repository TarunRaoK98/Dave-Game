# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 20:10:16 2017

@author: Tarun Rao
"""
from utils import *

pygame.init()
pygame.display.set_caption('Dave Game')
SCREEN = pygame.display.set_mode((SCREENX,SCREENY))
GRID = grid(SCREEN,10,17)
DAVE=dave(1260,132,GRID)
fpsClock=pygame.time.Clock()

while True :
    SCREEN.fill(WHITE)
    for event in pygame.event.get():
        if(event.type==KEYDOWN):
            if(event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif (event.key==K_DOWN ):
                DAVE.move('down')
            elif(event.key==K_LEFT ):
                DAVE.move('left')
            elif(event.key==K_UP):
                DAVE.move('Lup')
            elif(event.key==K_RIGHT ):
                DAVE.move('right')
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    GRID.show(BLUE)
    DAVE.draw()
    DAVE.move('fall')
    pygame.display.update()
    fpsClock.tick(FPS)
