import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions (classic phone style)
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("📟 Classic Snake (Nokia Style)")

# Colors
black = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
dark_green = (0, 100, 0)

# Grid settings
cell_size = 10
clock = pygame.time.Clock()
snake_speed = 10

# Fonts (pixel-style)
font = pygame.font.SysFont('Courier', 20, bold=True)

def draw_border():
    pygame.draw.rect(screen, dark_green, [0, 0, width, height], 10)

def draw_snake(snake_list):
    for segment in snake_list:
        pygame.draw.rect(screen, green, [segment[0], segment[1], cell_size, cell_size])

def draw_food(food_pos):
    pygame.draw.rect(screen, white, [food_pos[0], food_pos[1], cell_size, cell_size])

def show_score(score):
    score_text = font.render("SCORE: " + str(score), True, green)
    screen.blit(score_text, [10, 10])

def message(text):
    msg = font.render(text, True, white)
    screen.blit(msg, [width / 10, height / 2])

def game_loop():
    game_over = False
    game_close = False

    # Snake start position and movement
    x, y = width // 2, height // 2
    dx, dy = 0, 0

    snake = []
    snake_length = 1

    food = [random.randrange(1, (width - cell_size) // cell_size) * cell_size,
            random.randrange(1, (height - cell_size) // cell_size) * cell_size]

    while not game_over:
        while game_close:
            screen.fill(black)
            message("Game Over! Q-Quit | R-Restart")
            show_score(snake_length - 1)
            pygame.display.update()

            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if e.key == pygame.K_r:
                        game_loop()

        # Events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game_over = True
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -cell_size, 0
                elif e.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = cell_size, 0
                elif e.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -cell_size
                elif e.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, cell_size

        x += dx
        y += dy

        # Hit wall
        if x < 0 or x >= width or y < 0 or y >= height:
            game_close = True

        screen.fill(black)
        draw_border()

        draw_food(food)

        head = [x, y]
        snake.append(head)

        if len(snake) > snake_length:
            del snake[0]

        # Snake hit itself
        for segment in snake[:-1]:
            if segment == head:
                game_close = True

        draw_snake(snake)
        show_score(snake_length - 1)

        pygame.display.update()

        # Eat food
        if x == food[0] and y == food[1]:
            food = [random.randrange(1, (width - cell_size) // cell_size) * cell_size,
                    random.randrange(1, (height - cell_size) // cell_size) * cell_size]
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
