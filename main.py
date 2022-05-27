# Импорт библиотек
import pygame
from random import*
import random as rd
from sys import exit

# разрешение экрана
widthX = 1000
heightY = 800

screen = pygame.display.set_mode((widthX, heightY))
pygame.display.set_caption('Выберите фигуру... || Управление: [ESC] - назад || [1 - 6] - пердпросмотр фигуры || [ENTER] - выбор фигуры')

# кадры в секунду
FPS = 60
clock = pygame.time.Clock()

# класс родитель фигура
class Figure:
    X = widthX / 2
    Y = heightY / 2

    # рандомная траектория точки
    dx = randrange(-1, 2)
    dy = randrange(-1, 2)

    # случайный цвет фигуры
    def random_color(self):
        r = rd.randint(0, 255)
        g = rd.randint(0, 255)
        b = rd.randint(0, 255)
        return (r, g, b)

    color = random_color('self')

    # толщина фигур
    lineTh = 8
    # размер окружности
    sizeCircle = 80

    @staticmethod
    # метод движения фигур
    def newPos(self):

        if select.dx == 0 or select.dy == 0:
            select.dx = randrange(-1, 2)
            select.dy = randrange(-1, 2)

        # проверка на ударение в Y стену
        if select.Y >= (heightY - size) or select.Y < size:
            # смена траектории
            select.dy *= -1
            select.dx = randrange(-5, 5)

        # проверка на ударение в X стену
        if select.X >= (widthX - size) or select.X < size:
            # смена траектории
            select.dx *= -1
            select.dy = randrange(-5, 5)
            screen.fill((0, 0, 0))

        # движение
        select.X += select.dx
        select.Y += select.dy
        return select.X, select.Y

# класс точка наследует класс фигуры
class Dot(Figure):
    # метод рисования точки
    def drawDot(self):
        pygame.draw.circle(screen, Figure.color,(Dot.X, Dot.Y), Figure.lineTh)


    # метод рисования отрезка
    def drawSegment(self):
        dlina = 50
        pygame.draw.line(screen, Figure.color,[widthX / 2 - dlina, heightY / 2],
                         [widthX / 2 + dlina, heightY / 2], Figure.lineTh)

    # метод рисования окружности
    def drawCircle(self):

        pygame.draw.circle(screen, Figure.color,(Circle.X, Circle.Y), Figure.sizeCircle, Figure.lineTh)

# класс окружности
class Circle(Dot):

    def drawEllipse(self):
        Wd = 250 # ширина
        Hg = 150 # высота
        pygame.draw.ellipse(screen, Figure.color, (widthX / 2 - Wd / 2, heightY / 2 - Hg / 2, Wd, Hg), Figure.lineTh)

# класс эллипс наследует класс окружности
class Ellipse(Circle):
    pass

# класс отрезок наследует класс точки
class Segment(Dot):
    # метод рисования прямоугольника
    def drawRectangle(self):
        # ширина
        widthRect = 200
        # высота
        heightRect = 100
        pygame.draw.rect(screen, Figure.color, pygame.Rect(widthX / 2 - widthRect / 2,
                                                           heightY / 2 - heightRect / 2, widthRect, heightRect), Figure.lineTh)

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
# инициализация эллипса
ellipse = Ellipse()
# инициализация треугольника
triangle = Triangle()

# обработчик событий при нажатии кнопок (предварительный просмотр и выбор)
def previewKeysSelect():
    # работаем с переменной внутри функции
    global previewSelect
    global size
    global mes
    if event.type == pygame.KEYUP:

        # точка
        if event.key == pygame.K_1:
            print("Предпросмотр точки")
            screen.fill((0, 0, 0))
            dot.drawDot()
            size = Figure.lineTh
            mes = 'ТОЧКА'
            pygame.display.set_caption(f'{mes}, для подтверждения нажмите [Enter]')
            previewSelect = Dot

        # линия
        if event.key == pygame.K_2:
            print("Предпросмотр линии")
            screen.fill((0, 0, 0))
            dot.drawSegment()
            mes = 'ОТРЕЗОК'
            pygame.display.set_caption(f'{mes}, для подтверждения нажмите [Enter]')
            previewSelect = Segment

        # прямоугольник
        if event.key == pygame.K_3:
            print("Предпросмотр прямоугольника")
            screen.fill((0, 0, 0))
            rectangle.drawRectangle()
            mes = 'ПРЯМОУГОЛЬНИК'
            pygame.display.set_caption(f'{mes}, для подтверждения нажмите [Enter]')
            previewSelect = Rectangle

        # окружность
        if event.key == pygame.K_4:
            print("Предпросмотр окружности")
            screen.fill((0, 0, 0))
            circle.drawCircle()
            size = Figure.sizeCircle
            mes = 'ОКРУЖНОСТЬ'
            pygame.display.set_caption(f'{mes}, для подтверждения нажмите [Enter]')
            previewSelect = Circle

        # эллипс
        if event.key == pygame.K_5:
            print("Предпросмотр эллипса")
            screen.fill((0, 0, 0))
            ellipse.drawEllipse()
            mes = 'ЭЛЛИПС'
            pygame.display.set_caption(f'{mes}, для подтверждения нажмите [Enter]')
            previewSelect = Ellipse

        # треугольник
        if event.key == pygame.K_6:
            print("Предпросмотр треугольника")
            screen.fill((0, 0, 0))
            triangle.drawTriangle()
            mes = 'ТРЕУГОЛЬНИК'
            pygame.display.set_caption(f'{mes}, для подтверждения нажмите [Enter]')
            previewSelect = Triangle

        # previewSelect.X = widthX / 2
        # previewSelect.Y = heightY / 2

        # подтверждение выбора ENTER
        if event.key == pygame.K_RETURN and previewSelect != None:
            select = previewSelect
            previewSelect = None
            print(f'Выбранная фигура: {mes}')
            pygame.display.set_caption(f'Выбранная фигура: {mes} || [ESC] - назад')
            return select

global select
select = None
print(select)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        # выход из программы нажатием на крестик или нажатием на ESC
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # если выбор не сделан показываем превью фигур с возможностью выбора
        if select == None:
            select = previewKeysSelect()

    # если выбрана точка
    if select == Dot:
        Figure.newPos('self')
        screen.fill((0, 0, 0))
        dot.drawDot()

    if select == Circle:
        Figure.newPos('self')
        screen.fill((0, 0, 0))
        circle.drawCircle()

    # срабатывание клавиши ESC только если сделан выбор
    if event.type == pygame.KEYUP and select != None:
        if event.key == pygame.K_ESCAPE:
            screen.fill((0, 0, 0))
            select.X = widthX / 2
            select.Y = heightY / 2
            # очищаем переменную выбранной фигуры
            select = None
            print(f"Выбранная фигура: {select}")
            pygame.display.set_caption('Выберите фигуру... || Управление: [ESC] - назад || [1 - 6] - пердпросмотр фигуры || [ENTER] - выбор фигуры')

    # обновление дисплея
    pygame.display.update()