from entities.player import Player
from entities.obj import Object
import pygame
import random
from helpers.image import convert
from glob import glob

pygame.init()

display_w = 800
display_h = 600

ground_level = 100

choice = random.randrange(0,5)

display = pygame.display.set_mode((display_w, display_h))  ##меняет размер дисплея
pygame.display.set_caption("RunGame")  ##меняет название
logo = pygame.image.load("assets/ic.png")  ##загружает иконку
pygame.display.set_icon(logo)  ##меняет иконку

def rungame():
    game = True
    enemies = []
    create_enemies(enemies, display)
    grass, cloud, stone = create_objects(display)
    land = pygame.image.load("assets/BG.png")
    pers_x = display_w // 4
    pers_y = display_h - ground_level - 125
    player = Player(pers_x, pers_y, 60, 100, display)

    while game:  ##пока игра
        for event in pygame.event.get():  ##event.get() забирает событие в pygame
            if event.type == pygame.QUIT:  ##event.type присваивает pygame.QUIT /// if он выбирает какое действие следует выполнить в момоент проверки условия
                pygame.quit()  ##pygame вызывается событие quit, позволяет закрыть окно
                quit()  ##выход их         player.check_keyboard()
            if  event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pause()

        display.blit(land, (0, 0))##меняет цвет дисплея
        player.check_keyboard()
        player.draw()
        draw_enemies(enemies)  ##рисует врага
        draw_objects(grass, cloud, stone)
        if player.check_collision(enemies):
            pause()
        pygame.display.update()  ##постоянное изменение дисплея
        pygame.time.Clock().tick(60)

def print_text(message, x, y, font_color = (200, 0, 100), font_type = ("assets/comic.ttf"), font_size = 30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if  event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                paused = False

        print_text("Paused. Press ESCAPE to continue", 160, 300)

        pygame.display.update()
        pygame.time.Clock().tick(15)

def create_enemies(enemies, display):
    enemy_x = [display_w + 25, display_w + 300, display_w + 550]
    for i in range(len(enemy_x)):
        enemy = Object(5, 'assets/enemies/en*.png', display)
        enemy.set_random_image()
        enemy.return_self(enemy_x[i], display_h - ground_level - enemy.height)
        enemies.append(enemy)

def draw_enemies(enemies):  ##рисование врагов, функция которая определяет необходимую кординату
    for e in enemies:
        check = e.move()  ##запускает движение врагов с начала экрана
        if not check:
            radius = find_radius(enemies)  ##нахождение значения radius
            e.set_random_image()
            e.return_self(radius, display_h - ground_level - e.height)  ##изменение значение кординатов в зависимости от расстояния

def draw_objects(grass, cloud, stone):
    if not grass.move():
        grass.set_random_image()
        grass.return_self(display_w + grass.width, random.randrange(display_h - ground_level - grass.height,  display_h - grass.height))  ##появление обьукта на случайном расстоянии
    if not cloud.move():
        cloud.set_random_image()
        cloud.return_self(display_w + cloud.width, random.randrange(ground_level - cloud.height, cloud.height))
    if not stone.move():
        stone.set_random_image()
        stone.return_self(display_w + stone.width, random.randrange(display_h - ground_level - stone.height,  display_h - stone.height))

def find_radius(objects):
    x_arr = []
    for o in objects:
        x_arr.append(o.x)
    maximum = max(x_arr)  ##maximum получает кординату обьектов
    if maximum < display_w:
        radius = display_w
        if radius - maximum < 50:
            radius += 150
    else:
        radius = maximum

    if choice == 0:
        radius += random.randrange(5, 20)  ##генерирует случайный радиус соперников в зоне 5, 20
    else:
        radius += random.randrange(200, 350)  ##генерирует случайный radius в зоне 200, 350
    return radius  ##возращение radius

def create_objects(display):
    grass = Object(4, "assets/objects/grass*.png", display)
    grass.set_random_image()
    grass.return_self(display_h - ground_level - grass.height,  display_h - grass.height)

    cloud = Object(4, "assets/objects/cloud*.png", display)
    cloud.set_random_image()
    cloud.return_self(ground_level - cloud.height, cloud.height)

    stone = Object(4, "assets/objects/stone*.png", display)
    stone.set_random_image()
    stone.return_self(display_h - ground_level - stone.height, display_h - stone.height)

    return grass, cloud, stone

rungame()  ##запускает игру


