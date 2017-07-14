# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 00:14:16 2017

@author: ktaru
"""
from Configuration import *
class grid:
    # Rows and Columns start from 0 unless specified
    def __init__(self,screen,rows,columns):
        self.screen=screen
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
    def show(self,color):
        for row in range(self.rows):
            for column in range(self.columns):
                cell=self.obj[row][column]
                pygame.draw.rect(self.screen,color,(cell.left,cell.top,cell.width,cell.height))

    def highlight(self,points):
        # Rows and Columns start from 1
        for point in points:
            cell=self.obj[point[0]-1][point[1]-1]
            pygame.draw.rect(self.screen,HIGHLIGHTER,(cell.left,cell.top,cell.width,cell.height))
    def locate(self,x,y):
        i=j=-1
        for row in range(self.rows):
            if y in range(self.obj[row][0].top,self.obj[row][0].bottom):
                i=row
        for column in range(self.columns):
            if x in range(self.obj[0][column].left,self.obj[0][column].right):
                j=column
        return [i,j]
class dave:
    def __init__(self,x,y,GRID):
        self.weight=5
        self.x=x
        self.y=y
        self.grid=GRID
        self.screen=GRID.screen
        self.leap=GRID.cellWidth
        self.jump=GRID.cellHeight
        self.image=pygame.image.load("block.jpg")
    def move(self,direction):
        self.cell= self.grid.locate(self.x,self.y)
        if direction == 'up' and self.cell[0] != 0:
            self.y -=self.jump
        elif direction == 'right' and self.cell[1] != self.grid.columns-1:
            self.x +=self.leap
        elif direction == 'left' and self.cell[1] != 0:
            self.x -= self.leap
        elif direction == 'Lup' and self.cell[0] != 1:
            self.y -= self.jump*2
        elif direction == 'down' and self.cell[0] != self.grid.rows-1:
            self.y +=self.jump
        elif direction == 'fall' and self.cell[0] != self.grid.rows-1:
            self.y +=self.jump/5
    def draw(self):
        self.cell= self.grid.locate(self.x,self.y)
        self.body=pygame.Rect(self.grid.obj[self.cell[0]][self.cell[1]])
        if -1 not in self.cell:
            #pygame.draw.rect(self.screen,RED,(self.body.left,self.body.top,self.body.width,self.body.height))
            self.screen.blit(self.image,(self.body.left, self.body.top))