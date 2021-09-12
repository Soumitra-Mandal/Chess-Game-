# -*- coding: utf-8 -*-
'''
Make a Chess Game Engine Using Pygame.
Main execution file.
Pygame version: 2.0.1
'''
'''
x-> 32 to 77
y-> 430 to 455
'''

# Import and initialize the pygame library
import pygame
from chessClasses import ChessBoard, colors, Text, Button
pygame.init()

# Setting up the drawing window
screen = pygame.display.set_mode([440, 480])
pygame.display.set_caption("Soumitra's Chess")
screen.fill(colors["white"])

# Initialising the chess board with theme
chessBoard = ChessBoard('retro')
# Testing: button layout -> RW1 = Rook("black")
start = Text('start','Arial',20, 'white')
startButton = Button('maroon',45,25,7,1)

# Run until the user asks to quit 
running = True
while running:
    # Draw the chessboard
    chessBoard.draw(screen)
    # Testing: button draw -> RW1.draw(15,15,screen)
    boundary = startButton.draw(32, 430, start, screen)
    
    # Break loop if user closed window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False     
        # Check for mouse Click
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if(pos[0]>boundary[0] and pos[0]<boundary[1] and pos[1]>boundary[2] and pos[1]<boundary[3]):
                print("Start!")
    # Update the Screen
    pygame.display.flip()

# Quit the program
pygame.quit()

