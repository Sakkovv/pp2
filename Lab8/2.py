import pygame

# Функция для вычисления координат и размеров прямоугольника
def rectangle(x1, y1, x2, y2):
    x = min(x1, x2)  # Определяем координату x верхнего левого угла
    y = min(y1, y2)  # Определяем координату y верхнего левого угла
    w = abs(x1 - x2)  # Вычисляем ширину прямоугольника
    z = abs(y1 - y2)  # Вычисляем высоту прямоугольника
    return (x, y, w, z)  # Возвращаем координаты и размеры прямоугольника

# Инициализация Pygame
pygame.init()

# Создание окна Pygame
screen = pygame.display.set_mode((600, 600))
another_layer = pygame.Surface((600, 600))  # Создаем поверхность для временного хранения изображения

done = False
clock = pygame.time.Clock()
x1 = 10
y1 = 10
x2 = 10
y2 = 10

w = 100
z = 100
color = (99, 189, 153) #Зеленый цвет
isMouseDown = False
screen.fill((255, 255, 255))  # Заполнение экрана белым цветом

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                x1 = event.pos[0]  # Запоминаем координату x первой точки
                y1 = event.pos[1]  # Запоминаем координату y первой точки
                isMouseDown = True  # Устанавливаем флаг нажатия мыши

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Левая кнопка мыши
                isMouseDown = False  # Сбрасываем флаг нажатия мыши
                another_layer.blit(screen, (0, 0))  # Копируем изображение экрана на временную поверхность

        if event.type == pygame.MOUSEMOTION:
            if isMouseDown:
                x2 = event.pos[0]  # Обновляем координату x второй точки
                y2 = event.pos[1]  # Обновляем координату y второй точки
                screen.blit(another_layer, (0, 0))  # Отображаем временную поверхность на экране
                pygame.draw.rect(screen, color, pygame.Rect(rectangle(x1, y1, x2, y2)), 1)  # Рисуем прямоугольник

    pygame.display.flip()  # Обновляем экран
    clock.tick(60)  # Устанавливаем частоту кадров
