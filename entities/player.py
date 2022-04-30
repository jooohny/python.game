import pygame
from glob import glob

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, display):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dy = 18
        self.dh = 10
        self.make_UP = False
        self.make_jump = False
        self.display = display
        self.image_counter = 0
        self.images = [self.convert(f) for f in glob("assets/pers/pers*.png")]

    def convert(self, image):
        return pygame.image.load(image).convert_alpha();


    def check_keyboard(self):
        keys = pygame.key.get_pressed()  ##обработка нажатия клавиш
        if keys[pygame.K_SPACE]:  ##задается клавиша space
            self.make_jump = True  ##включение прыжка
        if self.make_jump:  ##если make_jump истинно то, персонаж совершает прыжок
            self.jump()
        if keys[pygame.K_UP]:
            self.make_UP = True
        if self.make_UP:
            self.uparrow()

    def draw(self):
        if self.image_counter == 30:
            self.image_counter = 0
        self.display.blit(self.images[self.image_counter // 5], [self.x, self.y])
        self.image_counter += 1

    def jump(self):
        if self.dy >= -18:  ##если dy  больше или равно, то
            self.y -= self.dy  ##по кардинате y рисваивается и вычитается
            self.dy -= 1  ##падение с ускорением
        else:
            self.dy = 18
            self.make_jump = False  ##выключение прыжка

    def uparrow(self):
        if self.dh >= -10:
            self.height -= self.dh
            self.dh -= 1
        else:
            self.dh = 10
            self.make_UP = False
