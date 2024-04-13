import pygame as pg
import time
import datetime
import math

# Инициализация Pygame
pg.init()

# Определение размеров экрана и его середины
RES = WIDTH ,HEIGHT = 1000,1000
midle = WIDTH//2 , HEIGHT//2
RADIUS = 1000

# Создание окна Pygame
screen = pg.display.set_mode((RES))

# Создание объекта Clock для управления кадрами в секунду
clock = pg.time.Clock()

# Установка заголовка окна
pg.display.set_caption("Mickey Clock")

# Загрузка изображений для стрелок часов и фона часов
sec = pg.image.load("pict/leftarm.png").convert_alpha()
minute = pg.image.load("pict/rightarm.png").convert_alpha()
background = pg.image.load("pict/mainclock.png")

# Получение прямоугольников для стрелок
rectsec = sec.get_rect()
rectmin = minute.get_rect()
rectmin.center = rectsec.center = midle

# Основной игровой цикл
run =True
angle1 = 0
angle2 = 0
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    # Получение текущего времени
    time = datetime.datetime.now()
    minuteTime = time.minute
    secondTime = time.second

    # Вычисление углов поворота для стрелок
    angle1 = -minuteTime*6  # 6 градусов в одной минуте
    angle2 = -secondTime*6  # 6 градусов в одной секунде

    # Поворот изображений стрелок
    leg1 = pg.transform.rotate(minute, angle1)
    leg2 = pg.transform.rotate(sec, angle2)

    # Получение прямоугольников для повернутых изображений
    rect1 = leg1.get_rect()
    rect2 = leg2.get_rect()
    rect1.center = rectmin.center
    rect2.center = rectsec.center

    # Отображение фона и стрелок на экране
    screen.blit(background, (-200, -20))
    screen.blit(leg1, rect1)
    screen.blit(leg2, rect2)
    
    # Обновление экрана
    pg.display.flip()

    # Установка частоты обновления экрана
    clock.tick(60)
