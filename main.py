# Импорт библиотеки Pygame, random
import pygame
from random import*
import random as rd

widthX = 800
heightY = 600

screen = pygame.display.set_mode((widthX, heightY))
pygame.display.set_caption('Выберите фигуру')

# кадры в секунду
FPS = 60
clock = pygame.time.Clock()

run = True

# класс родитель фигура
class Figure:
    # случайный цвет
    def random_color(self):
        r = rd.randint(0, 255)
        g = rd.randint(0, 255)
        b = rd.randint(0, 255)
        return (r, g, b)

    # толщина фигур
    lineTh = 10

# класс точка наслежует класс фигуры
class Dot(Figure):

    # метод рисования точки
    def drawDot(self):
        color = Figure.random_color(self)
        pygame.draw.circle(screen, color,(widthX / 2, heightY / 2), Figure.lineTh)

    # метод рисования отрезка
    def drawSegment(self):
        dlina = 50
        color = Figure.random_color(self)
        pygame.draw.line(screen, color,[widthX / 2 - dlina, heightY / 2],
                         [widthX / 2 + dlina, heightY / 2], Figure.lineTh)

    def drawCircle(self):
        color = Figure.random_color(self)
        size = 50 # размер
        pygame.draw.circle(screen, color,(widthX / 2, heightY / 2), size, Figure.lineTh)

# класс окружности
class Circle(Dot):
    def drawEllipse(self):
        color = Figure.random_color(self)
        Wd = 300 # ширина
        Hg = 200 # высота
        pygame.draw.ellipse(screen, color, (widthX / 2 - Wd / 2, heightY / 2 - Hg / 2, Wd, Hg), Figure.lineTh)

# класс эллипс наследует класс окружности
class Ellipse(Circle):
    pass

# класс отрезок наследует класс точки
class Segment(Dot): # класс линии наследует класс точки
    # метод рисования прямоугольника
    def drawRectangle(self):
        color = Figure.random_color(self)
        size = 100
        pygame.draw.rect(screen, color, pygame.Rect(widthX / 2 - size / 2, heightY / 2 - size / 2, size, size), Figure.lineTh)

# класс прямоугольника наследует класс отрезка
class Rectangle(Segment):
    pass

# инициализация точки
dot = Dot()
# инициализация линии
segment = Segment()
# инициализация прямоугольника
rectangle = Rectangle()
# инициализация окружности
circle = Circle()
# инициализация элиипса
ellipse = Ellipse()

# обработчик событий при нажатии кнопок
def keys():

    keys = pygame.key.get_pressed()

    # точка
    if keys[pygame.K_1]:
        screen.fill((0, 0, 0))
        dot.drawDot()
        pygame.display.set_caption('Выбрана ТОЧКА для подтверждения нажмите [Enter]')

    # линия
    if keys[pygame.K_2]:
        screen.fill((0, 0, 0))
        dot.drawSegment()
        pygame.display.set_caption('Выбран ОТРЕЗОК для подтверждения нажмите [Enter]')

    # прямоугольник
    if keys[pygame.K_3]:
        screen.fill((0, 0, 0))
        rectangle.drawRectangle()
        pygame.display.set_caption('Выбран ПРЯМОУГОЛЬНИК для подтверждения нажмите [Enter]')

    # окружность
    if keys[pygame.K_4]:
        screen.fill((0, 0, 0))
        circle.drawCircle()
        pygame.display.set_caption('Выбрана ОКРУЖНОСТЬ для подтверждения нажмите [Enter]')

    # Эллипс
    if keys[pygame.K_5]:
        screen.fill((0, 0, 0))
        ellipse.drawEllipse()
        pygame.display.set_caption('Выбран ЭЛЛИПС для подтверждения нажмите [Enter]')

    # выход из программы ESC
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # обновляет дисплей
    pygame.display.flip()

    # вызов функции события клавиш
    keys()










