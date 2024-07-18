import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']




def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric... Try Again!')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('Number not in range 2-10. Try Again!')


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            # random move from 1 to 20 px
            distance = random.randrange(1, 20)

            # move racer forward
            racer.forward(distance)

            # give us pos of turtle
            x, y = racer.pos()
            if y >= HEIGHT / 2 - 10:
                # we look for winnig colors use index of racer in turtles list
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacingX = WIDTH / (len(colors) + 1)
    
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        # to turn racer up
        racer.left(90)
        racer.penup()
        # position of racers: x pos: -WIDTH / 2 (i + 1) * spacingX, y pos: -HEIGHT / 2 + 20
        racer.setpos(-WIDTH / 2 + (i + 1) * spacingX, -HEIGHT / 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

    # enumerate give us a index and value for each items we lopp through
    # ['red', 'green']
    # first loops itteration: i = 0, color = 'red' 
    # second loops itteraction i = 1, color = 'green' 
        
    

# https://docs.python.org/3/library/turtle.html TURTLE DOCS

def init_turtle():
    # create turtle screen
    screen = turtle.Screen()
    # middle position will be x:0 y:0. top-middle: x:0 y:250px (HEIGHT / 2). bottom-middle: x:0 y:-250px (HEIGHT / 2)
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

racers = get_number_of_racers()
init_turtle()

# random shuffle colors inside
random.shuffle(COLORS)

# we slice our shuffled list accroding number of racers that we have
colors = COLORS[:racers]
winner = race(colors)
print('The winner is turtle with color:', winner)
time.sleep(5)


# we use this module to can change the object - turtle
# racer = turtle.Turtle()



# # change racer speed
# racer.speed(2)

# # no line behind the turtle
# racer.penup()

# # change icon (arrow => turtle)
# racer.shape('turtle')

# # change color of racer
# racer.color('cyan')

# # racer will move forward for 100 px
# racer.forward(100)
# # 90 degree to turn to the left
# racer.left(90)
# # racer will move forward for 100 px

# # return line behind the turtle
# racer.pendown()

# racer.forward(100)
# # 90 degree to turn ti the right
# racer.right(90)



# # create one more racer
# racer2 = turtle.Turtle()
# # change racer speed
# racer2.speed(5)

# # no line behind the turtle
# racer2.penup()

# # change icon (arrow => turtle)
# racer2.shape('turtle')

# # change color of racer
# racer2.color('red')

# # racer will move forward for 100 px
# racer2.forward(150)
# # 90 degree to turn to the left
# racer2.left(90)
# # racer will move forward for 100 px

# # return line behind the turtle
# racer2.pendown()

# racer2.forward(100)
# # 90 degree to turn ti the right
# racer2.right(90)

# 4:13:11