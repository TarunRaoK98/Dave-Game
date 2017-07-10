# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 20:10:16 2017

@author: Tarun Rao
"""
from utils import *

pygame.init()
pygame.display.set_caption('Dave Game')
SCREEN = pygame.display.set_mode((SCREENX,SCREENY))
fpsClock=pygame.time.Clock()

while True :
    SCREEN.fill(GREEN)
    for event in pygame.event.get():
        if(event.type==KEYDOWN):
            if(event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    GRID = grid(SCREEN,3,4)
    GRID.show(BLUE)
    GRID.locate(R.randint(0,SCREENX),R.randint(0,SCREENY))
    pygame.display.update()
    fpsClock.tick(FPS)
