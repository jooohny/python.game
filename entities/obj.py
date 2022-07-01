import random
import pygame
from glob import glob
from helpers.image import convert

class Object(pygame.sprite.Sprite):  ##класс обЬектов
    def __init__(self, speed, imagePattern, display):##__init__ помогает нам создать объект класса
        self.speed = speed   ##self ссылает на класс объекта
        self.images = [convert(f) for f in glob(imagePattern)]
        self.display = display

    def move(self):  ##move движение наших объектов класса self
        if self.x >=  -self.width:
            self.display.blit(self.image, (self.x, self.y))
            self.x -= self.speed  ##вычитывает display_w от скорости
            self.rect.x = self.x
            return True
        else:
            return False

    def return_self(self, x, y = None):
        self.x = x
        self.y = self.y if y == None else y
        self.rect.x = self.x
        self.rect.y = self.y

    def set_random_image(self):
        choice = random.randrange(len(self.images))
        self.image = self.images[choice]
        self.mask = pygame.mask.from_surface(self.image)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
