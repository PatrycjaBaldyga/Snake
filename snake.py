"""
SNAKE

This is a classic snake game.
Eat the red apples that appear on the screen. Press the arrows on the keyboard to move the snake. Dont let the snake eat its own tail!
"""


import pygame
import random


#class for cell objects
class Square:

    # init method; x,y - coordinates
    def __init__(self, x, y, color, width):
        self.x = x
        self.y = y
        self.color = color
        self.width = width

    #draws a square
    def draw_square(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width), 0)


#class for a grid object
class Grid:

    #init method
    def __init__(self, size, distance, color):
        self.size = size
        self.distance = distance
        self.color = color
        self.square = []
        x = 0
        y = 0
        #creates a grid by appending squares and distances inbetween them across the screen size
        for i in range(self.size ** 2):
            self.square.append(Square(x, y, self.color, self.size))
            x += self.size + self.distance
            if x >= s_width:
                x = 0
                y += self.size + self.distance


#class for a snake object
class Snake:
    def __init__(self, length, color):
        self.square = []
        self.color = color
        self.length = length
        self.points = length
        x = 0
        y = 0
        #make a snake of a given number of squares
        for i in range(length):
            self.square.append(Square(x, y, color, grid.size))
            x -= grid.size + grid.distance
    #add a square to the end of the snake
    def draw_square(self):
        for i in range(len(self.square)):
            self.square[i].draw_square()

    #make each of the squares of the snake move together at a given speed
    def move(self):
        for i in range(len(self.square) - 1, 0, -1):
            self.square[i].x = self.square[i - 1].x
            self.square[i].y = self.square[i - 1].y
        self.square[0].x += (grid.size + grid.distance) * x_speed
        self.square[0].y += (grid.size + grid.distance) * y_speed
        #don't let the snake escape the window
        if self.square[0].x >= s_width:
            self.square[0].x = 0
        if self.square[0].y >= s_height:
            self.square[0].y = 0
        if self.square[0].x < 0:
            self.square[0].x = s_width - (grid.size + grid.distance)
        if self.square[0].y < 0:
            self.square[0].y = s_width - (grid.size + grid.distance)

    #if snake and food coordinates meet, the points are incremented and snake gets longer by a square
    def check_food(self):
        if self.square[0].x == food.x and self.square[0].y == food.y:
            food_xy()
            self.points += 1
            self.square.append(Square(-100, -100, self.color, grid.size))

    #checks if the first and any other snake square cross and if so, deletes all gained squares
    def check_if_dead(self):
        for i in range(1, len(self.square), 1):
            if self.square[0].x == self.square[i].x and self.square[0].y == self.square[i].y:
                for j in range(len(self.square) - 1, self.length - 1, -1):
                    del self.square[j]
                    self.points = self.length
                break

#depending on the key pressed (up, down, left or right), the movement on the x and y axis changes, making the snake to change direction; moving diagonally and backwards is prevented
def movement():
    global x_speed
    global y_speed
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y_speed != 1:
                    x_speed = 0
                    y_speed = 0
                    y_speed = -1
                    break
            if event.key == pygame.K_DOWN:
                if y_speed != -1:
                    x_speed = 0
                    y_speed = 0
                    y_speed = 1
                    break
            if event.key == pygame.K_RIGHT:
                if x_speed != -1:
                    x_speed = 0
                    y_speed = 0
                    x_speed = 1
                    break
            if event.key == pygame.K_LEFT:
                if x_speed != 1:
                    x_speed = 0
                    y_speed = 0
                    x_speed = -1
                    break


#generates random food coordinates on the grid, but not where the snake is
def food_xy():
    food.x = random.randint(0, (s_width / (grid.size + grid.distance)) - 1) * (grid.size + grid.distance)
    food.y = random.randint(0, (s_height / (grid.size + grid.distance)) - 1) * (grid.size + grid.distance)
    for i in range(len(snake.square)):
        if snake.square[i].x == food.x and snake.square[i].y == food.y:
            food_xy()

if __name__ == "__main__":
    #initialize all imported pygame modules
    pygame.init()

    # setting screen size
    s_width = 500
    s_height = 500
    screen_size = [s_width, s_height]
    screen = pygame.display.set_mode(screen_size)

    # set a caption of the window
    pygame.display.set_caption("Snake")

    # create an object to help track time
    clock = pygame.time.Clock()

    # used colors
    GREEN = (107, 142, 35)
    RED = (220, 20, 60)
    WHITE = (255, 255, 255)

    #initial speed on the x and y axis of the board
    x_speed = 1
    y_speed = 0

    #creating objects of the grid, snake and food class
    grid = Grid(22, 3, WHITE)
    snake = Snake(1, GREEN)
    food = Square(-100, -100, RED, grid.size)
    food_xy()

    #run until the user clicks the close button
    running = True

    while running:
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        """

        #draw the grid
        pygame.draw.rect(screen, WHITE, (0, 0, s_width, s_height), 0)

        #using created methods
        movement()
        snake.move()
        snake.check_food()
        snake.check_if_dead()
        snake.draw_square()
        food.draw_square()

        #update screen display
        pygame.display.update()

        #frames per second
        clock.tick(5)

    # uninitialize all pygame modules
    pygame.quit()
