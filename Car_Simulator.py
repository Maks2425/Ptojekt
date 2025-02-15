import pygame
import random

pygame.init()

blue = (102, 102, 255)
white = (255, 255, 255)
orange = (0, 162, 255)
rgb = (30, 105, 185)
rgb2 = (0, 255, 179)



WIDTH, HEIGHT = 1920, 1280
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Simulator")


image = pygame.image.load("play.png")
image_rect = image.get_rect(center=(900, 600))

barruer = pygame.image.load("barruer.png")
barruer_rect = barruer.get_rect(center=(0, 400))

barruerupp = pygame.image.load("uppbarruer.png")
barruerupp_rect = barruerupp.get_rect(center=(300, 100))

barruerupp2 = pygame.image.load("uppbarruer2.png")
barruerupp2_rect = barruerupp2.get_rect(center=(1390, 100))

barruerdown = pygame.image.load("barruerdown.png")
barruerdown_rect = barruerdown.get_rect(center=(300, 1200))

barruerdown2 = pygame.image.load("barruerdown2.png")
barruerdown2_rect = barruerdown2.get_rect(center=(1300, 1200))

barruercopy = pygame.image.load("barruercopy.png")
barruercopy_rect = barruercopy.get_rect(center=(0, 900))

barruercopy_right = pygame.image.load("barruercopy.png")
barruercopyright_rect = barruercopy_right.get_rect(center=(2000, 900))

barruercopy_right2 = pygame.image.load("barruercopy.png")
barruercopyright2_rect = barruercopy_right2.get_rect(center=(2000, 400))

image1 = pygame.image.load("quit.png")
image_rect1 = image1.get_rect(center=(900, 700))

Levels = pygame.image.load("Levels.png")
Levels_rect = Levels.get_rect(center=(900, 200))

image2 = pygame.image.load("off.png")
image_rect2 = image2.get_rect(center=(50, 130))

benzin = pygame.image.load("benzin.png")
benzin_rect = benzin.get_rect(center=(900, 630))


image11 = pygame.image.load("1.png")
image_rect11 = image11.get_rect(center=(100, 400))


image22 = pygame.image.load("2.png")
image_rect22 = image22.get_rect(center=(200, 400))

car = pygame.image.load("car.png")
car_rect = car.get_rect(center=(500,500))

ShowMoney = pygame.image.load("ShowMoney.png")
ShowMoney_rect = ShowMoney.get_rect(center=(1500,200))

quit2 = pygame.image.load("Quite2.png")
quit2_rect = quit2.get_rect(center=(900,600))

Won = pygame.image.load("Uwon.png")
won_rect = Won.get_rect(center=(900,200))

Lobby = pygame.image.load("LOBBY.png")
Lobby_rect = Lobby.get_rect(center=(900,400))

money = 0
car_speed = 1
Menu3 = False
Menu = True
Menu2 = False  
barruer_box = False
point = 0
MenuMoney = False
f1 = pygame.font.Font(None, 36)


running = True
while running:
    screen.fill(orange)
    text1 = f1.render(f'points {point}', 1, (0, 0, 0))
    text2 = f1.render(f'Money {money}', 1, (0, 0, 0))
    if Menu:
        screen.blit(image, image_rect)
        screen.blit(image1, image_rect1)
    elif Menu2: 
        screen.fill(rgb)
        screen.blit(car, car_rect)
        screen.blit(barruer,barruer_rect)
        screen.blit(barruercopy,barruercopy_rect)
        screen.blit(barruercopy_right,barruercopyright_rect)
        screen.blit(barruercopy_right2,barruercopyright2_rect)
        screen.blit(barruerupp,barruerupp_rect)
        screen.blit(barruerupp2,barruerupp2_rect)
        screen.blit(barruerdown,barruerdown_rect)
        screen.blit(barruerdown2,barruerdown2_rect)
        screen.blit(benzin, benzin_rect)
        screen.blit(text1, (400, 400))
    elif Menu3:
        screen.fill(rgb2)
        screen.blit(car,car_rect)
        screen.blit(barruer,barruer_rect)
        screen.blit(barruercopy,barruercopy_rect)
        screen.blit(barruercopy_right,barruercopyright_rect)
        screen.blit(barruercopy_right2,barruercopyright2_rect)
        screen.blit(barruerupp,barruerupp_rect)
        screen.blit(barruerupp2,barruerupp2_rect)
        screen.blit(barruerdown,barruerdown_rect)
        screen.blit(barruerdown2,barruerdown2_rect)
        screen.blit(benzin, benzin_rect)
        screen.blit(text1, (400, 400))

    else:
        screen.blit(image2, image_rect2)
        screen.blit(image11, image_rect11)
        screen.blit(image22, image_rect22)
        screen.blit(Levels, Levels_rect)
        screen.blit(ShowMoney, ShowMoney_rect)

    
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
                    

                if ShowMoney_rect.collidepoint(event.pos): 
                    MenuMoney = True  
                    Menu = False

                if quit2_rect.collidepoint(event.pos): 
                    running = False

                if Lobby_rect.collidepoint(event.pos): 
                    Menu2 = False
                    Menu3 = False
                    Menu = False
                    MenuMoney = False

    if MenuMoney == True:
        screen.fill(orange)
        screen.blit(text2, (400, 400))
        screen.blit(Lobby, Lobby_rect)

    if barruer_box == True:
        car_rect = car.get_rect(center=(500,500))
        barruer_box = False
        car_speed = 1

    keys = pygame.key.get_pressed()
    if car_rect.colliderect(barruercopy_rect) or car_rect.colliderect(barruer_rect) or car_rect.colliderect(barruercopyright_rect) or car_rect.colliderect(barruercopyright2_rect) or car_rect.colliderect(barruerupp_rect) or car_rect.colliderect(barruerupp2_rect) or car_rect.colliderect(barruerdown_rect) or car_rect.colliderect(barruerdown2_rect):
        car_speed = 0
        barruer_box = True
    
    if car_rect.colliderect(benzin_rect):
        point += 1
        benzin_rect = benzin.get_rect(center=(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)))
        

    if point == 5 and Menu2 == True:
        screen.fill(orange)
        screen.blit(quit2,quit2_rect)
        screen.blit(Lobby,Lobby_rect)
        screen.blit(Won,won_rect)
        money += 1
        
    if Menu == False and Menu2 == False and Menu3 == False:
        point = 0

    if point == 10 and Menu3 == True:
        screen.fill(orange)
        screen.blit(quit2,quit2_rect)
        screen.blit(Lobby,Lobby_rect)
        screen.blit(Won,won_rect)
        money += 1
        
    


    if Menu2 or Menu3:
        if  keys[pygame.K_a]:  
            car_rect.x -= car_speed
        if  keys[pygame.K_d]:  
            car_rect.x += car_speed
        if  keys[pygame.K_w]:  
            car_rect.y -= car_speed
        if  keys[pygame.K_s]:  
            car_rect.y += car_speed





    pygame.display.flip()

pygame.quit()