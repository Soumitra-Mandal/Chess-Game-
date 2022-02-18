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
from chessClasses import ChessBoard, colors, Text, Button, Rook, init_pos_opponent, Bishop, King, Queen, Pawn, Knight
pygame.init()

# Setting up the drawing window
screen = pygame.display.set_mode([440, 480])
pygame.display.set_caption("Soumitra's Chess")
screen.fill(colors["white"])

# Initialising the chess board with theme
chessBoard = ChessBoard('classic')
# Testing: button layout -> RW1 = Rook("black")
start = Text('start','Arial',20, 'white')
startButton = Button('maroon',45,25,7,1)
rook = Rook("white")

# Run until the user asks to quit 
running = True
while running:
    # Draw the chessboard
    chessBoard.draw(screen)
    # Testing: button draw -> RW1.draw(15,15,screen)
    boundary = startButton.draw(32, 430, start, screen)
    
    #Testing opponent draw
    rook1 = Rook("white")
    rook2 = Rook("white")
    bishop1 = Bishop("white")
    bishop2 = Bishop("white")
    knight1 = Knight("white")
    knight2 = Knight("white")
    king = King("white")
    queen = Queen("white")
    pawns = [Pawn("white") for i in range(8)]

    rook1.draw(init_pos_opponent["rook1"][0], init_pos_opponent["rook1"][1], screen)
    rook2.draw(init_pos_opponent["rook2"][0], init_pos_opponent["rook2"][1], screen)
    bishop1.draw(init_pos_opponent["bishop1"][0], init_pos_opponent["bishop1"][1], screen)
    bishop2.draw(init_pos_opponent["bishop2"][0], init_pos_opponent["bishop2"][1], screen)
    knight1.draw(init_pos_opponent["knight1"][0], init_pos_opponent["knight1"][1], screen)
    knight1.draw(init_pos_opponent["knight2"][0], init_pos_opponent["knight2"][1], screen)
    king.draw(init_pos_opponent["king"][0], init_pos_opponent["king"][1], screen)
    queen.draw(init_pos_opponent["queen"][0], init_pos_opponent["queen"][1], screen)

    for i in range(8):
        pawns[i].draw(init_pos_opponent["pawns"][i][0], init_pos_opponent["pawns"][i][1], screen)

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

