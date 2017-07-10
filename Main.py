# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 20:10:16 2017

@author: Tarun Rao
"""
import pygame,sys
from pygame.locals import *
#from utils import *

FPS = 25
BLACK = pygame.Color( 0 , 0  , 0  )
WHITE = pygame.Color(255, 255, 255)
RED   = pygame.Color(255, 0  , 0  )
GREEN = pygame.Color( 0 , 255, 0  )
BLUE  = pygame.Color( 0 , 0  , 255)
SCREENX=640
SCREENY=480
class grid:
    def __init__(self,screen,rows,columns):
        self.thick = 5
        self.border= 5
        self.length,self.breadth = pygame.display.get_surface().get_size()
        breadth=self.breadth-2*self.border
        length = self.length-2*self.border
        self.rows = rows
        self.columns = columns
        self.linesx=self.rows-1
        self.linesy=self.columns-1
        self.cellWidth = (length-(self.thick*self.linesy))/self.columns
        self.cellHeight = (breadth-(self.thick*self.linesx))/self.rows
        self.obj = [[0 for x in range(columns)] for x in range(rows)]
        for row in range (self.rows):
            y = self.border + (row*(self.cellHeight+self.thick))
            for column in range(self.columns):
                x = self.border + (column * (self.cellWidth+self.thick))
                self.obj[row][column]=pygame.Rect(x,y,self.cellWidth,self.cellHeight)
                pygame.draw.rect(SCREEN,BLUE,(x,y,self.cellWidth,self.cellHeight))

pygame.init()
pygame.display.set_caption('Snake Game')
SCREEN = pygame.display.set_mode((SCREENX,SCREENY))
fpsClock=pygame.time.Clock()

while True :
    SCREEN.fill(RED)
    for event in pygame.event.get():
        if(event.type==KEYDOWN):
            if(event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    GRID = grid(SCREEN,3,4)
    pygame.display.update()
    fpsClock.tick(FPS)
