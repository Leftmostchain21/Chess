# This file will render the chess board and pieces using pygame.

import pygame
import GameEngine

# Resolutions/Constants

WIDTH = 800
HEIGHT = 800

# Colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
IMAGES = {}


# Create a function that will draw the board

def loadImages():
    pieces = ["Nb", "Rb", "Bb", "Qb", "Kb", "Pb", "Pw", "Rw", "Nw", "Kw", "Qw", "Bw"]
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("Chess_Working/images/" + piece + ".png"), (WIDTH / 8, HEIGHT / 8))
    # We can now access an image by saying 'IMAGES['wp']'

def draw_board(board):
    pygame.init()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    # Draw the board
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                pygame.draw.rect(surface, RED, (row * WIDTH / 8, col * HEIGHT / 8, WIDTH / 8, HEIGHT / 8))
            else:
                pygame.draw.rect(surface, GREEN, (row * WIDTH / 8, col * HEIGHT / 8, WIDTH / 8, HEIGHT / 8))

def draw_pieces(board):
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    # Draw the pieces
    for row in range(8):
        for col in range(8):
            if board[col][row][-1:] == "w":
                surface.blit(IMAGES[board[col][row]], pygame.Rect(col * WIDTH / 8, row * HEIGHT / 8, WIDTH / 8, HEIGHT / 8))
            elif board[col][row][-1:] == "b":
                surface.blit(IMAGES[board[col][row]], pygame.Rect(col * WIDTH / 8, row * HEIGHT / 8, WIDTH / 8, HEIGHT / 8))
    pygame.display.update()