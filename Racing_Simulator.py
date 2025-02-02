import pygame

pygame.init()

blue = (102, 102, 255)
white = (255, 255, 255)
orange = (255, 171, 0)
rgb = (30, 105, 185)

WIDTH, HEIGHT = 1920, 1280
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Race Simulator")

#завантаження зображень
image = pygame.image.load("play.png")
image_rect = image.get_rect(center=(900, 500))

image1 = pygame.image.load("quite.png")
image_rect1 = image1.get_rect(center=(900, 700))

Levels = pygame.image.load("LEVELS.png")
Levels_rect = Levels.get_rect(center=(900, 200))

image2 = pygame.image.load("off.png")
image_rect2 = image2.get_rect(center=(50, 130))

image11 = pygame.image.load("1.png")
image_rect11 = image11.get_rect(center=(100, 400))


image22 = pygame.image.load("2.png")
image_rect22 = image22.get_rect(center=(200, 400))

car = pygame.image.load("car.png")
car_rect = car.get_rect(center=(500,500))

Menu3 = False
Menu = True
Menu2 = False  

running = True
while running:
    screen.fill(orange)

    
    if Menu:
        screen.blit(image, image_rect)
        screen.blit(image1, image_rect1)
    elif Menu2: 
        
        screen.fill(rgb)
        screen.blit(car, car_rect)
    elif Menu3:
        screen.fill(white)
        screen.blit(car,car_rect)

    else:
        screen.blit(image2, image_rect2)
        screen.blit(image11, image_rect11)
        screen.blit(image22, image_rect22)
        screen.blit(Levels, Levels_rect)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if Menu:
                if image_rect.collidepoint(event.pos):
                    Menu = False  
                elif image_rect1.collidepoint(event.pos):
                    running = False  
            else:
                if image_rect2.collidepoint(event.pos):
                    running = False 
                if image_rect11.collidepoint(event.pos): 
                    Menu2 = True  
                    Menu = False  
                if image_rect22.collidepoint(event.pos): 
                    Menu3 = True  
                    Menu = False
    pygame.display.flip()

pygame.quit()