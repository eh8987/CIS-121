import pygame 


running = True



screen = pygame.display.set_mode((500,500))








pygame.display.flip()

while running:

    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            running = False