import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
x, y = 400, 300
radius = 25
speed = 20

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
  
    if keys[pygame.K_UP] and y - speed >= radius: y -= speed
    if keys[pygame.K_DOWN] and y + speed <= 600 - radius: y += speed
    if keys[pygame.K_LEFT] and x - speed >= radius: x -= speed
    if keys[pygame.K_RIGHT] and x + speed <= 800 - radius: x += speed

    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    pygame.display.flip()
    clock.tick(60)