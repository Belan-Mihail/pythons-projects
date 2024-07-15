import turtle
import time

WIDTH, HEIGHT = 500, 500




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


def init_turtle():
	# create turtle screen
    screen = turtle.Screen()
	# middle position will be x:0 y:0. top-middle: x:0 y:250px (HEIGHT / 2). bottom-middle: x:0 y:-250px (HEIGHT / 2)
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

racers = get_number_of_racers()
init_turtle()

# we use this module to can change the object
racer = turtle.Turtle()

# racer will move forward for 100 px
racer.forward(100)
# 90 degree to turn to the left
racer.left(90)
# racer will move forward for 100 px
racer.forward(100)
# 90 degree to turn ti the right
racer.right(90)
time.sleep(5)