import pygame

pygame.init()
w, h = 400, 400
s = pygame.display.set_mode((w, h))
pygame.display.set_caption('Желтый круг')
circle = 0
pos = (0, 0)
gr = False
v = 10
clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            circle = 0
            gr = True
    s.fill('blue')
    if gr:
        circle += v * (clock.get_time() / 1000)
    pygame.draw.circle(s, 'yellow', pos, int(circle))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
