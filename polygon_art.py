import turtle
import random

class Simulation:
    def start(self):
        response = input("Which art do you want to generate? Enter a number between 1 to 8, inclusive: ")
        if response == '1':
            polygon = [Polygon(3) for _ in range(30)]
            for art in polygon:
                art.draw()

        elif response == '2':
            polygon = [Polygon(4) for _ in range(30)]
            for art in polygon:
                art.draw()

        elif response == '3':
            polygon = [Polygon(5) for _ in range(30)]
            for art in polygon:
                art.draw()

        elif response == '4':
            polygon = [Polygon(random.randint(3,5)) for _ in range(30)]
            for art in polygon:
                art.draw()

        elif response == '5':
            polygon = [Polygon(3) for _ in range(20)]
            for art in polygon:
                art.draw()
                small = art.draw_small()
                small.draw_small()

        elif response == '6':
            polygon = [Polygon(4) for _ in range(20)]
            for art in polygon:
                art.draw()
                small = art.draw_small()
                small.draw_small()


        elif response == '7':
            polygon = [Polygon(5) for _ in range(20)]
            for art in polygon:
                art.draw()
                small = art.draw_small()
                small.draw_small()

        elif response == '8':
            polygon = [Polygon(random.randint(3,5)) for _ in range(20)]
            for art in polygon:
                art.draw()
                small = art.draw_small()
                small.draw_small()

class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.border_size = random.randint(1, 10)

    def draw(self):
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.setheading(self.orientation)
        turtle.penup()

    def draw_small(self):
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.right(90)

        small = Polygon(self.num_sides)

        small.size = self.size
        small.orientation = self.orientation
        small.color = self.color
        small.border_size = self.border_size
        small.location[0] = turtle.pos()[0]
        small.location[1] = turtle.pos()[1]

        # adjust the size according to the reduction ratio
        small.size *= reduction_ratio

        small.draw()

        return small

def setup():
    global reduction_ratio
    turtle.speed(0)
    turtle.bgcolor('black')
    turtle.tracer(0)
    turtle.colormode(255)
    reduction_ratio = 0.618

setup()
sim = Simulation()
sim.start()
turtle.done()
