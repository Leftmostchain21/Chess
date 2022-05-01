# This file will render the chess board and pieces using pygame.

import colorama
from numpy import imag
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


surface = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a function that will draw the board

def load_Images():
    pieces = ["Nb", "Rb", "Bb", "Qb", "Kb", "Pb", "Pw", "Rw", "Nw", "Kw", "Qw", "Bw"]
    for piece in pieces:
        # Load the image and then convert it to be a transparent png
        image_loading = pygame.image.load("Chess/images/" + piece + ".png").convert_alpha()
        IMAGES[piece] = pygame.transform.scale(image_loading, (WIDTH / 8, HEIGHT / 8))
    # We can now access an image by saying 'IMAGES['Pw']'

def draw_board():
    pygame.init()
    pygame.display.set_caption("Chess")
    # Draw the board
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                pygame.draw.rect(surface, RED, (row * WIDTH / 8, col * HEIGHT / 8, WIDTH / 8, HEIGHT / 8))
            else:
                pygame.draw.rect(surface, GREEN, (row * WIDTH / 8, col * HEIGHT / 8, WIDTH / 8, HEIGHT / 8))
    pygame.display.update()

def draw_pieces(board):
    # Draw the pieces
    for row in range(8):
        for col in range(8):
            if board[row][col][-1:] == "w":
                surface.blit(IMAGES[f"{board[row][col]}"], pygame.Rect(col * WIDTH / 8, row * HEIGHT / 8, WIDTH / 8, HEIGHT / 8))
            elif board[row][col][-1:] == "b":
                surface.blit(IMAGES[f"{board[row][col]}"], pygame.Rect(col * WIDTH / 8, row * HEIGHT / 8, WIDTH / 8, HEIGHT / 8))
    pygame.display.update()