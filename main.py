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
    X = widthX / 2
    Y = heightY / 2

    # рандомная траектория точки
    dx = randrange(-2, 2)
    dy = randrange(-2, 2)

    # случайный цвет фигуры
    def random_color(self):
        r = rd.randint(0, 255)
        g = rd.randint(0, 255)
        b = rd.randint(0, 255)
        return (r, g, b)

    color = random_color('self')

    # толщина фигур
    lineTh = 6

    # размер окружности
    sizeCircle = 80

    # длина отрезка
    dlina = 50

    # ширина прямоугольника
    widthRect = 200
    # высота прямоугольника
    heightRect = 100

    # ширина прямоугольника
    widthEllipse = 300
    # высота прямоугольника
    heightEllipse = 200

    # расстояние между 3 точками для треугольника
    sizeTriangle = 100

    @staticmethod
    # метод движения фигур
    def newPos(self):
        pygame.display.set_caption('Случайное управление, для ручного нажмите [↑ ↓ ← →], [ESC] - выбор фигуры')
        if event.type != pygame.KEYDOWN:
            if select.dx == 0 or select.dy == 0:
                select.dx = randrange(-2, 2)
                select.dy = randrange(-2, 2)

            # проверка на ударение в Y стену
            if select.Y >= (heightY - sizeY) or select.Y < sizeY:
                # смена траектории
                select.dy *= -1
                select.dx = randrange(-2, 2)
                Figure.color = Figure.random_color('self')

            # проверка на ударение в X стену
            if select.X >= (widthX - sizeX) or select.X < sizeX:
                # смена траектории
                select.dx *= -1
                select.dy = randrange(-2, 2)
                screen.fill((0, 0, 0))
                Figure.color = Figure.random_color('self')

            # движение
            select.X += select.dx
            select.Y += select.dy

        if event.type == pygame.KEYDOWN:
            select.dx = 0
            select.dy = 0

            if event.key == pygame.K_UP:
                select.Y -= 5
                print("Нажата клавиша вверх")
            if event.key == pygame.K_DOWN:
                select.Y += 5
                print("Нажата клавиша вниз")
            if event.key == pygame.K_RIGHT:
                select.X += 5
                print("Нажата клавиша вправо")
            if event.key == pygame.K_LEFT:
                select.X -= 5
                print("Нажата клавиша влево")

            # возвращение фигур в другой конец экрана
            if select.Y >= (heightY - sizeY):
                select.Y = sizeY + 1
            if select.X >= widthX - sizeX:
                select.X = sizeX + 1

            if select.Y <= sizeY:
                select.Y = heightY - sizeY
            if select.X <= sizeX:
                select.X = widthX - sizeX

        return select.X, select.Y

# класс точка наследует класс фигуры
class Dot(Figure):
    # метод рисования точки
    def drawDot(self):
        pygame.draw.circle(screen, Figure.color, (Dot.X, Dot.Y), Figure.lineTh)

    # метод рисования отрезка
    def drawSegment(self):
        pygame.draw.line(screen, Figure.color, [Segment.X - Figure.dlina, Segment.Y],
                         [Segment.X + Figure.dlina, Segment.Y], Figure.lineTh)

    # метод рисования окружности
    def drawCircle(self):
        pygame.draw.circle(screen, Figure.color, (Circle.X, Circle.Y), Figure.sizeCircle, Figure.lineTh)

# класс окружности наследует класс точки
class Circle(Dot):
    # метод рисования эллипса
    def drawEllipse(self):
        pygame.draw.ellipse(screen, Figure.color, (Ellipse.X - Figure.widthEllipse / 2, Ellipse.Y - Figure.heightEllipse / 2,
                                                   Figure.widthEllipse, Figure.heightEllipse), Figure.lineTh)

# класс эллипс наследует класс окружности
class Ellipse(Circle):
    pass

# класс отрезок наследует класс точки
class Segment(Dot):
    # метод рисования прямоугольника
    def drawRectangle(self):
        pygame.draw.rect(screen, Figure.color, pygame.Rect(Rectangle.X - Figure.widthRect / 2,
                                                           Rectangle.Y - Figure.heightRect / 2, Figure.widthRect, Figure.heightRect), Figure.lineTh)

    # метод рисования треугольника
    def drawTriangle(self):
        pygame.draw.polygon(screen, Figure.color, [(Triangle.X - Figure.sizeTriangle, Triangle.Y + Figure.sizeTriangle),
                                                   (Triangle.X + Figure.sizeTriangle, Triangle.Y + Figure.sizeTriangle),
                                                   ((Triangle.X), Triangle.Y - Figure.sizeTriangle)], Figure.lineTh)

class Triangle(Segment):
    pass

# класс прямоугольника наследует класс отрезка
class Rectangle(Segment):
    pass

# инициализация классов
dot = Dot()
segment = Segment()
rectangle = Rectangle()
circle = Circle()
ellipse = Ellipse()
triangle = Triangle()

previewSelect = None
messageSelect = None

# обработчик событий при нажатии кнопок (предварительный просмотр и выбор)
def previewKeysSelect():
    # работаем с переменной внутри функции
    global previewSelect
    global sizeX
    global sizeY
    global messageSelect

    if event.type == pygame.KEYUP:
        # точка
        if event.key == pygame.K_1:
            print("Предпросмотр точки")
            screen.fill((0, 0, 0))
            dot.drawDot()

            #переменные границ
            sizeX = Figure.lineTh
            sizeY = Figure.lineTh

            messageSelect = 'ТОЧКА'
            pygame.display.set_caption(f'{messageSelect}, для подтверждения нажмите [Enter]')
            previewSelect = Dot

        # отрезок
        if event.key == pygame.K_2:
            print("Предпросмотр линии")
            screen.fill((0, 0, 0))
            dot.drawSegment()

            sizeX = Figure.dlina
            sizeY = Figure.lineTh / 2

            messageSelect = 'ОТРЕЗОК'
            pygame.display.set_caption(f'{messageSelect}, для подтверждения нажмите [Enter]')
            previewSelect = Segment


        # прямоугольник
        if event.key == pygame.K_3:
            print("Предпросмотр прямоугольника")
            screen.fill((0, 0, 0))
            rectangle.drawRectangle()

            sizeX = Figure.widthRect / 2
            sizeY = Figure.heightRect / 2

            messageSelect = 'ПРЯМОУГОЛЬНИК'
            pygame.display.set_caption(f'{messageSelect}, для подтверждения нажмите [Enter]')
            previewSelect = Rectangle


        # окружность
        if event.key == pygame.K_4:
            print("Предпросмотр окружности")
            screen.fill((0, 0, 0))
            circle.drawCircle()

            sizeX = Figure.sizeCircle
            sizeY = Figure.sizeCircle

            messageSelect = 'ОКРУЖНОСТЬ'
            pygame.display.set_caption(f'{messageSelect}, для подтверждения нажмите [Enter]')
            previewSelect = Circle


        # эллипс
        if event.key == pygame.K_5:
            print("Предпросмотр эллипса")
            screen.fill((0, 0, 0))
            ellipse.drawEllipse()

            sizeX = Figure.widthEllipse / 2
            sizeY = Figure.heightEllipse / 2

            messageSelect = 'ЭЛЛИПС'
            pygame.display.set_caption(f'{messageSelect}, для подтверждения нажмите [Enter]')
            previewSelect = Ellipse


        # треугольник
        if event.key == pygame.K_6:
            print("Предпросмотр треугольника")
            screen.fill((0, 0, 0))
            triangle.drawTriangle()

            sizeX = Figure.sizeTriangle
            sizeY = Figure.sizeTriangle

            messageSelect = 'ТРЕУГОЛЬНИК'
            pygame.display.set_caption(f'{messageSelect}, для подтверждения нажмите [Enter]')
            previewSelect = Triangle


        # подтверждение выбора ENTER
        if event.key == pygame.K_RETURN and previewSelect != None:
            select = previewSelect
            print(f'Выбранная фигура: {messageSelect}')
            pygame.display.set_caption(f'Выбранная фигура: {messageSelect}, [ESC] - выбор фигуры')
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

    print(select)
    # если выбор не сделан показываем превью фигур с возможностью выбора
    if select == None:
        select = previewKeysSelect()

    # если выбрана точка
    if select == Dot:
        Figure.newPos('self')
        screen.fill((0, 0, 0))
        dot.drawDot()

    # если выбран отрезок
    if select == Segment:
        Figure.newPos('self')
        screen.fill((0, 0, 0))
        segment.drawSegment()

    # если выбран прямоугольник
    if select == Rectangle:
        Figure.newPos('self')
        screen.fill((0, 0, 0))
        segment.drawRectangle()

    # если выбрана окружность
    if select == Circle:
        Figure.newPos('self')
        screen.fill((0, 0, 0))
        segment.drawCircle()

    # если выбран эллипс
    if select == Ellipse:
        Figure.newPos('self')
        screen.fill((0, 0, 0))
        ellipse.drawEllipse()

    # если выбран треугольник
    if select == Triangle:
        Figure.newPos('self')
        screen.fill((0, 0, 0))
        triangle.drawTriangle()

    # срабатывание клавиши ESC только если сделан выбор
    if event.type == pygame.KEYUP and select != None and event.key == pygame.K_ESCAPE:

        if event.key == pygame.K_ESCAPE:
            screen.fill((0, 0, 0))
            select.X = widthX / 2
            select.Y = heightY / 2
            # очищаем переменную выбранной фигуры
            previewSelect = None
            select = None
            messageSelect = None
            print(f"Выбранная фигура: {select}")
            pygame.display.set_caption('Выберите фигуру...')

    # обновление дисплея
    pygame.display.update()