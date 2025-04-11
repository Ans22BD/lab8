import pygame
import random

pygame.init()

# Размер блока и экрана
BLOCK_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
WIDTH = BLOCK_SIZE * GRID_WIDTH
HEIGHT = BLOCK_SIZE * GRID_HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Color Change")

# Цвета
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Шрифт
font = pygame.font.SysFont("Verdana", 20)

# Функция генерации случайного цвета
def random_color():
    return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

# Настройки игры
clock = pygame.time.Clock()
speed = 5
snake = [(5, 5)]
snake_dir = (1, 0)
walls = [(10, y) for y in range(5, 15)] + [(20, y) for y in range(5, 15)]
food = None
score = 0
level = 1
snake_color = RED  # Начальный цвет змеи

# Генерация еды
def generate_food():
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in snake and pos not in walls:
            return pos

food = generate_food()

# Главный игровой цикл
running = True
while running:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, 1):
                snake_dir = (0, -1)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -1):
                snake_dir = (0, 1)
            elif event.key == pygame.K_LEFT and snake_dir != (1, 0):
                snake_dir = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-1, 0):
                snake_dir = (1, 0)

    # Новая голова
    head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

    # Проверка на поражение
    if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
        print("Вы проиграли: выход за пределы поля")
        break
    if head in snake or head in walls:
        print("Вы проиграли: столкновение")
        break

    # Добавляем голову
    snake.insert(0, head)

    # Проверка еды
    if head == food:
        score += 1
        food = generate_food()

        # Меняем цвет змеи каждые 3 очка
        if score % 3 == 0:
            snake_color = random_color()
            level += 1
            speed += 1
    else:
        snake.pop()

    # Отрисовка
    screen.fill(BLACK)

    # Стены
    for wall in walls:
        pygame.draw.rect(screen, BLUE, (wall[0] * BLOCK_SIZE, wall[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # Змея
    for segment in snake:
        pygame.draw.rect(screen, snake_color, (segment[0] * BLOCK_SIZE, segment[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # Еда
    pygame.draw.rect(screen, RED, (food[0] * BLOCK_SIZE, food[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # Текст
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()