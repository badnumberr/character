import pygame
import random


pygame.init()
w = 800
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("фруктомания")


player_size = 100
player_speed = 10
player_x = w // 2 - player_size // 2
player_y = h - player_size - 10


circle_size = 20
circle_speed = 3
circles = []


score = 0
font = pygame.font.Font(None, 36)


circle_timer = 2000
last_circle = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    k = pygame.key.get_pressed()
    if k[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if k[pygame.K_RIGHT] and player_x < w - player_size:
        player_x += player_speed


    current_time = pygame.time.get_ticks()
    if current_time - last_circle >= circle_timer:
        last_circle = current_time
        x = random.randint(circle_size, w - circle_size)
        y = -circle_size
        circles.append([x, y])
    for i in range(len(circles) - 1, -1, -1):
        circles[i][1] += circle_speed
        circle_x = circles[i][0]
        circle_y = circles[i][1]
        if (player_x < circle_x + circle_size and player_x + player_size > circle_x - circle_size and
                player_y < circle_y + circle_size and player_y + player_size > circle_y - circle_size):
            score += 1
            circles.pop(i)
        elif circles[i][1] > h + circle_size:
            circles.pop(i)



    screen.fill('black')
    pygame.draw.rect(screen, 'white', (player_x, player_y, player_size, player_size))
    for circle in circles:
        pygame.draw.circle(screen, 'yellow', (circle[0], circle[1]), circle_size)
    text = font.render(f"{score}", True, 'white')
    screen.blit(text, (10, 10))
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()