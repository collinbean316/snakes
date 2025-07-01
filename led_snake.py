import pygame
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time
import random

# Initialize pygame (for keyboard input)
pygame.init()
pygame.display.set_mode((100, 100))  # Small hidden window for capturing input

# LED matrix config
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'
matrix = RGBMatrix(options=options)

WIDTH = 64
HEIGHT = 32

# Game variables
snake = [(10, 15), (9, 15), (8, 15)]
direction = (1, 0)  # Start moving right
food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
speed = 0.15

def draw():
    matrix.Clear()
    for x, y in snake:
        matrix.SetPixel(x, y, 0, 255, 0)  # Green snake
    fx, fy = food
    matrix.SetPixel(fx, fy, 255, 0, 0)  # Red food

def move_snake():
    global food
    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx, head_y + dy)

    # Check collisions
    if not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        return False  # Wall hit
    if new_head in snake:
        return False  # Self collision

    snake.insert(0, new_head)

    if new_head == food:
        food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
    else:
        snake.pop()

    return True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            dx, dy = direction
            if event.key == pygame.K_UP and dy == 0:
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and dy == 0:
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and dx == 0:
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and dx == 0:
                direction = (1, 0)

    if not move_snake():
        running = False  # Game over

    draw()
    time.sleep(speed)

matrix.Clear()
pygame.quit()
