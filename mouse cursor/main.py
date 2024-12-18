import pygame


pygame.init()
width, height = 500, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("свой курсор мыши")
cursor_image = pygame.image.load("data/arrow.png")
rect = cursor_image.get_rect()
pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((0, 0, 0))
    if pygame.mouse.get_focused():
        x, y = pygame.mouse.get_pos()
        rect.topleft = (x, y)
        screen.blit(cursor_image, rect)
    pygame.display.flip()
