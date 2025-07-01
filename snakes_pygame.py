import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('🐍 Snake Game')

# Set up clock
clock = pygame.time.Clock()
SPEED = 10

# Snake and food
snake = [(100, 100), (80, 100), (60, 100)]
direction = (20, 0)
food = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
        random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)

# Game loop
def game_over():
    font = pygame.font.SysFont(None, 50)
    text = font.render("Game Over", True, RED)
    screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 25))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

def move_snake():
    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx, head_y + dy)
    snake.insert(0, new_head)
    if new_head == food:
        return True
    else:
        snake.pop()
        return False

def draw():
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.flip()

# Main game loop
running = True
global food
while running:
    clock.tick(SPEED)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            dx, dy = direction
            if event.key == pygame.K_UP and dy == 0:
                direction = (0, -BLOCK_SIZE)
            elif event.key == pygame.K_DOWN and dy == 0:
                direction = (0, BLOCK_SIZE)
            elif event.key == pygame.K_LEFT and dx == 0:
                direction = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT and dx == 0:
                direction = (BLOCK_SIZE, 0)

    # Move and check for collisions
    if move_snake():
        food = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)

    head = snake[0]
    if (
        head in snake[1:] or
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT
    ):
        game_over()

    draw()
