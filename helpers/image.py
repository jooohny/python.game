import pygame

def convert(image):
    return pygame.image.load(image).convert_alpha()
