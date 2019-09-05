import pygame

pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Quiz')

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(window, pygame.Color('red'), pygame.Rect(x, y, width, height))
    pygame.display.update 

pygame.quit()

