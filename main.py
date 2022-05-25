# Импорт библиотек
import pygame
from random import*
import random as rd
from sys import exit

# разрешение экрана
widthX = 800
heightY = 600

screen = pygame.display.set_mode((widthX, heightY))
pygame.display.set_caption('Выберите фигуру...')

# кадры в секунду
FPS = 60
clock = pygame.time.Clock()

# класс родитель фигура
class Figure:
    # случайный цвет
    def random_color(self):
        r = rd.randint(0, 255)
        g = rd.randint(0, 255)
        b = rd.randint(0, 255)
        return (r, g, b)

    # случайный цвет фигуры
    color = random_color('self')

    # толщина фигур
    lineTh = 5

# класс точка наслежует класс фигуры
class Dot(Figure):

    X = widthX / 2
    Y = heightY / 2

    # метод рисования точки
    def drawDot(self):
        pygame.draw.circle(screen, Figure.color,(Dot.X, Dot.Y), Figure.lineTh)

    def set_new_position(self):
        Dot.X += 1
        Dot.Y += 1
        self.draw()

    # метод рисования отрезка
    def drawSegment(self):
        dlina = 50
        pygame.draw.line(screen, Figure.color,[widthX / 2 - dlina, heightY / 2],
                         [widthX / 2 + dlina, heightY / 2], Figure.lineTh)

    def drawCircle(self):
        size = 50 # размер
        pygame.draw.circle(screen, Figure.color,(widthX / 2, heightY / 2), size, Figure.lineTh)

# класс окружности
class Circle(Dot):
    def drawEllipse(self):
        Wd = 300 # ширина
        Hg = 200 # высота
        pygame.draw.ellipse(screen, Figure.color, (widthX / 2 - Wd / 2, heightY / 2 - Hg / 2, Wd, Hg), Figure.lineTh)

# класс эллипс наследует класс окружности
class Ellipse(Circle):
    pass

# класс отрезок наследует класс точки
class Segment(Dot): # класс линии наследует класс точки
    # метод рисования прямоугольника
    def drawRectangle(self):
        size = 100
        pygame.draw.rect(screen, Figure.color, pygame.Rect(widthX / 2 - size / 2, heightY / 2 - size / 2, size, size), Figure.lineTh)

    def drawTriangle(self):
        size = 100
        pygame.draw.polygon(screen, Figure.color, [(widthX / 2 - size, heightY / 2 + size),
                                                   (widthX / 2 + size, heightY / 2 + size), ((widthX / 2), heightY / 2 - size)], Figure.lineTh)

class Triangle(Segment):
    pass

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
# инициализация треугольника
triangle = Triangle()

# обработчик событий при нажатии кнопок предварительный просмотр
def PreviewKeys(choice):
    if event.type == pygame.KEYDOWN:

        # точка
        if event.key == pygame.K_1:
            screen.fill((0, 0, 0))
            dot.drawDot()
            pygame.display.set_caption('Выбрана ТОЧКА для подтверждения нажмите [Enter]')
            choice = 1

        # линия
        if event.key == pygame.K_2:
            screen.fill((0, 0, 0))
            dot.drawSegment()
            pygame.display.set_caption('Выбран ОТРЕЗОК для подтверждения нажмите [Enter]')
            choice = 2

        # прямоугольник
        if event.key == pygame.K_3:
            screen.fill((0, 0, 0))
            rectangle.drawRectangle()
            pygame.display.set_caption('Выбран ПРЯМОУГОЛЬНИК для подтверждения нажмите [Enter]')
            choice = 3

        # окружность
        if event.key == pygame.K_4:
            screen.fill((0, 0, 0))
            circle.drawCircle()
            pygame.display.set_caption('Выбрана ОКРУЖНОСТЬ для подтверждения нажмите [Enter]')
            choice = 4

        # Эллипс
        if event.key == pygame.K_5:
            screen.fill((0, 0, 0))
            ellipse.drawEllipse()
            pygame.display.set_caption('Выбран ЭЛЛИПС для подтверждения нажмите [Enter]')
            choice = 5
        # Эллипс
        if event.key == pygame.K_6:
            screen.fill((0, 0, 0))
            triangle.drawTriangle()
            pygame.display.set_caption('Выбран ТРЕУГОЛЬНИК для подтверждения нажмите [Enter]')
            choice = 6

        # выход из программы ESC
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()

    return choice

# выбор после предварительного просмотра
def Change():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:

            if choice == 1:
                print("Выбрана фигура 1")
            if choice == 2:
                print("Выбрана фигура 2")
            if choice == 3:
                print("Выбрана фигура 3")
            if choice == 4:
                print("Выбрана фигура 4")
            if choice == 5:
                print("Выбрана фигура 5")
            if choice == 6:
                print("Выбрана фигура 6")

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        else:
            # обновление дисплея
            pygame.display.update()
            # возвращаем значение предпросмотра choice
            choice = PreviewKeys(choice)
            Change()