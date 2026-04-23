import pygame, sys, random, time
from pygame.locals import *


pygame.init()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
CELL_SIZE = 20
COLS = WINDOW_WIDTH // CELL_SIZE
ROWS = WINDOW_HEIGHT // CELL_SIZE


BLACK = (0, 0, 0)
WHITE = (255, 255, 255) # Вес 3
GREEN = (0, 255, 0)
RED = (255, 0, 0)     # Вес 1
YELLOW = (255, 255, 0) # Вес 2

# Настройка экрана
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake: Weights & Timers")
clock = pygame.time.Clock()

def generate_food(snake_body):
    """Генерирует еду со случайным весом и временем появления"""
    while True:
        x = random.randint(0, COLS - 1)
        y = random.randint(0, ROWS - 1)
        # Проверяем, чтобы еда не попала на тело
        if (x, y) not in snake_body:
            weight = random.randint(1, 3) # Случайный friut от 1 до 3
            spawn_time = pygame.time.get_ticks() # Время появления
            return (x, y, weight, spawn_time)

# Игровые переменные
snake = [(COLS // 2, ROWS // 2)]
direction = (1, 0)
food_x, food_y, food_weight, food_timer = generate_food(snake)
score = 0
level = 1
foods_eaten = 0
speed = 5
running = True
FOOD_LIFETIME = 5000 # Время жизни еды (5 секунд)

while running:
    # 1. Проверка таймера еды
    current_time = pygame.time.get_ticks()
    if current_time - food_timer > FOOD_LIFETIME:
        # Если время вышло, генерируем новую еду
        food_x, food_y, food_weight, food_timer = generate_food(snake)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

   
    if new_head[0] < 0 or new_head[0] >= COLS or new_head[1] < 0 or new_head[1] >= ROWS or new_head in snake:
        running = False
        continue

    snake.insert(0, new_head)

   
    if new_head[0] == food_x and new_head[1] == food_y:
    
        score += food_weight * 10
        foods_eaten += 1
   
        food_x, food_y, food_weight, food_timer = generate_food(snake)
        
        # Повышение уровня
        if foods_eaten % 3 == 0:
            level += 1
            speed += 1
    else:
        # Убираем хвост, если ничего не съели
        snake.pop()

    # Отрисовка
    screen.fill(BLACK)

    # Выбираем цвет еды в зависимости от веса
    if food_weight == 1:
        f_color = RED
    elif food_weight == 2:
        f_color = YELLOW
    else:
        f_color = WHITE

   
    food_rect = pygame.Rect(food_x * CELL_SIZE, food_y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, f_color, food_rect)

  
    for segment in snake:
        seg_rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, GREEN, seg_rect)

    # Информационная панель
    # Добавим индикатор времени до исчезновения (в секундах)
    time_left = max(0, (FOOD_LIFETIME - (current_time - food_timer)) // 1000)
    info_str = f"Score: {score}  Lvl: {level}  Food Timer: {time_left}s"
    info_text = pygame.font.SysFont("Verdana", 15).render(info_str, True, WHITE)
    screen.blit(info_text, (10, 10))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()
sys.exit()