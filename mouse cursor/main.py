import pygame

pygame.init()

w = 300
h = 300
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("герой двигается")

size = 100
speed = 10
x = w // 2 - size // 2
y = h - size - 10

image = pygame.image.load("data/creature.png")
image = pygame.transform.scale(image, (size, size))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    k = pygame.key.get_pressed()
    if k[pygame.K_LEFT]:
        x -= speed
    if k[pygame.K_RIGHT]:
        x += speed
    if k[pygame.K_UP]:
        y -= speed
    if k[pygame.K_DOWN]:
        y += speed
    screen.fill('white')
    screen.blit(image, (x, y))
    pygame.display.flip()
    pygame.time.delay(30)
pygame.quit()
