import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Abi Game')

x = 50
y = 50 
width = 60
height = 60
speed = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
        
    if keys[pygame.K_RIGHT]:
        x += speed
    pygame.draw.rect(win, (225,0,0), (x,y, width, height))
    pygame.display.update()
pygame.quit()