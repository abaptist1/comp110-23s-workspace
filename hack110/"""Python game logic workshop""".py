"""Python game logic workshop"""

import pygame
import sys
from random import randint

#Starts window

pygame.init()

#Constants to deine window size and set FPS
HEIGHT = 450
WIDTH = 400
FPS = 60

#Create clock object to limit FPS
FramePerSec = pygame.time.Clock()

# Create surface to draw objects on
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

