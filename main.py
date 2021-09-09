# -*- coding: utf-8 -*-
'''
Make a Chess Game Engine Using Pygame.
Main execution file.
Pygame version: 2.0.1
'''


# Import and initialize the pygame library
import pygame
from chessClasses import ChessBoard
pygame.init()

# Setting up the drawing window
screen = pygame.display.set_mode([400, 400])

# Initialising the chess board with theme
chessBoard = ChessBoard('funky')

# Run until the user asks to quit
running = True
while running:
    # Draw the chessboard
    chessBoard.draw(screen)
    # Break loop if user closed window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False      
    #Update the Screen
    pygame.display.flip()

# Quit the program
pygame.quit()

