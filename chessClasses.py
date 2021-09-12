# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:22:46 2021

@author: Soumitra
All Classes here and global objects here

"""
# Import important packages
import pygame
from pygame.locals import Rect

# Color Dictionary
colors = {
    "white"  : (255,255,255),
    "black"  : (0,0,0),
    "red"    : (255,0,0),
    "blue"   : (0,0,255),
    "yellow" : (255,255,0),
    "lime"   : (0,255,0),
    "cyan"   : (0,255,255),
    "magenta": (255,0,255),
    "orange" : (255,165,0),
    "gray"   : (128,128,128),
    "silver" : (192,192,192),
    "brown"  : (165,42,42),
    "green"  : (0,128,0),
    "teal"   : (0,128,128),
    "purple" : (128,0,128),
    "maroon" : (128,0,0),
    "olive"  : (128,128,0)
    }

# Chessboard themes
themes = {
        "classic" : [colors['black'], colors['white']],
        "retro"   : [colors['brown'], colors['yellow']],
        "funky"   : [colors['purple'],colors['cyan']]        
        }

# ChessBoard Layout class
class ChessBoard:
    def __init__(self,theme):
        '''Initialize the chessboard.'''
        self.width = 50
        self.height = 50
        self.left = 50
        self.top = 50   
        self.theme = theme
    def draw(self,screen):
        ''' Draw Function: Draws the Chess Board '''
        for row_count in range(0,8):
            for col_count in range(0,8):
                r = Rect(self.left*row_count+20,self.top*col_count+20,self.width,self.height)
                colour = themes[self.theme][(row_count+col_count)%2]
                pygame.draw.rect(screen,colour,r) 



class Text:
    def __init__(self, data , fontName, fontSize, color):
        self.data = data
        self.fontName = fontName
        self.fontSize = fontSize
        self.color = colors[color]
        
    def draw(self,x,y,screen):
        smallfont = pygame.font.SysFont(self.fontName,self.fontSize)
        text = smallfont.render(self.data , True , self.color)
        screen.blit(text,(x,y))

    
class Button:
    def __init__(self,color,width,height,l,t):
        self.color = colors[color]
        self.width = width
        self.height = height
        self.pos = (l,t)
    def draw(self,x,y,text,screen):
        pygame.draw.rect(screen, self.color, Rect(x,y,self.width,self.height),0,3)
        text.draw(x+self.pos[0],y+self.pos[1],screen)
        return (x,self.width+x,y,self.height+y)


class Rook:
    def __init__(self,piece_color):
        self.piece_color = piece_color
        self.img = pygame.image.load("./assets/rook_"+self.piece_color+".png")
    def draw(self,x,y,screen):
        screen.blit(self.img,(x,y))
        

class Bishop:
    def __init__(self,piece_color,x,y):
        self.piece_color = piece_color
        self.img = pygame.image.load("./assets/bishop_white.png")
        self.x = x
        self.y = y
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
        