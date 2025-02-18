import pygame
import random

pygame.init()


blue = (102, 102, 255)
white = (255, 255, 255)
orange = (0, 162, 255)
rgb = (30, 105, 185)
rgb2 = (0, 255, 179)
rgb3 = (30, 225, 79)
rgb4 = (42, 52, 233)

# Отримуємо розміри екрану
# info = pygame.display.Info()
# WIDTH, HEIGHT = info.current_w, info.current_h  # Динамічні розміри екрану

# screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)  # Повноекранний режим
# pygame.display.set_caption("Car Simulator")

# # Перевіримо розміри екрану
# print(f"Screen size: {WIDTH}x{HEIGHT}")


# Отримуємо розміри екрану
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w - 50, info.current_h - 100  # Динамічні розміри екрану
# WIDTH, HEIGHT = 1920, 1280
#screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Car Simulator")


playImg = pygame.image.load("assets/play.png")
playImg_rect = playImg.get_rect(center=(WIDTH / 2, HEIGHT / 2)) 

barruer = pygame.image.load("assets/barruer.png")
barruer_rect = barruer.get_rect(center=(0, 400))

Upgrade_button = pygame.image.load("assets/upgrade.png")
UpgradeButton_rect = Upgrade_button.get_rect(center=(280, 200))

Gas_button = pygame.image.load("assets/Gas.png")
Gas_rect = Gas_button.get_rect(center=(1550, 200))

barruerupp = pygame.image.load("assets/uppbarruer.png")
barruerupp_rect = barruerupp.get_rect(center=(300, 0))

barruerupp2 = pygame.image.load("assets/uppbarruer2.png")
barruerupp2_rect = barruerupp2.get_rect(center=(1390, 0))

barruerdown = pygame.image.load("assets/barruerdown.png")
barruerdown_rect = barruerdown.get_rect(center=(300, 1200))

barruerdown2 = pygame.image.load("assets/barruerdown2.png")
barruerdown2_rect = barruerdown2.get_rect(center=(1300, 1200))

barruercopy = pygame.image.load("assets/barruercopy.png")
barruercopy_rect = barruercopy.get_rect(center=(0, 100))

barruercopy_right = pygame.image.load("assets/barruercopy.png")
barruercopyright_rect = barruercopy_right.get_rect(center=(0, 900))

barruercopy_right2 = pygame.image.load("assets/barruercopy.png")
barruercopyright2_rect = barruercopy_right2.get_rect(center=(2000, 400))

quit_img = pygame.image.load("assets/quit.png")
quit_img_rect = quit_img.get_rect(center=(WIDTH / 2, playImg_rect.bottom + 50))

Levels = pygame.image.load("assets/Levels.png")
Levels_rect = Levels.get_rect(center=(350, 130))

off = pygame.image.load("assets/off.png")
off = pygame.transform.smoothscale(off, (80, 111))
off_rect = off.get_rect(center=(50, 130))

benzin = pygame.image.load("assets/benzin.png")
benzin = pygame.transform.smoothscale(benzin, (69, 80))
benzin_rect = benzin.get_rect(center=(900, 630))

#bg2 = pygame.image.load("assets/bg2.png")
#bg2 = pygame.transform.smoothscale(bg2, (1920, 1080))
#bg2_rect = bg2.get_rect(center=(0, 0))


lvl1 = pygame.image.load("assets/1.png")
lvl1 = pygame.transform.smoothscale(lvl1, (69, 80))
lvl1_rect = lvl1.get_rect(center=(100, 300))


menu_bg = pygame.image.load("assets/menu_bg.webp")
menu_bg = pygame.transform.scale(menu_bg, (WIDTH+50, HEIGHT+100))


level1_bg = pygame.image.load("assets/level1_bg.webp")
level1_bg = pygame.transform.scale(level1_bg, (WIDTH+50, HEIGHT+100))


Shop_button = pygame.image.load("assets/shop.png")
Shop_button = pygame.transform.smoothscale(Shop_button, (370, 105))
ShopButton_rect = Shop_button.get_rect(center=(1000, 130))


lvl3 = pygame.image.load("assets/3.png")
lvl3 = pygame.transform.smoothscale(lvl3, (69, 111))
lvl3_rect = lvl3.get_rect(center=(300, 300))

lvl4 = pygame.image.load("assets/4.png")
lvl4 = pygame.transform.smoothscale(lvl4, (69, 111))
lvl4_rect = lvl4.get_rect(center=(400, 300))

lvl5 = pygame.image.load("assets/5.png")
lvl5 = pygame.transform.smoothscale(lvl5, (69, 111))
lvl5_rect = lvl5.get_rect(center=(500, 300))

lvl2 = pygame.image.load("assets/2.png")
lvl2 = pygame.transform.smoothscale(lvl2, (69, 111))
lvl2_rect = lvl2.get_rect(center=(200, 300))

car = pygame.image.load("assets/car2.png")
car = pygame.transform.smoothscale(car, (150, 70))  
car_rect = car.get_rect(center=(500,500))

ShowMoney = pygame.image.load("assets/ShowMoney.png")
ShowMoney_rect = ShowMoney.get_rect(center=(1500,130))

Backpng = pygame.image.load("assets/back.png")
Backpng_rect = Backpng.get_rect(center=(30,1050))

Dollars = pygame.image.load("assets/Dollars.png")
Dollars_rect = Dollars.get_rect(center=(300,600))

Dollars2 = pygame.image.load("assets/Dollars2.png")
Dollars2_rect = Dollars2.get_rect(center=(700,400))

Dollars3 = pygame.image.load("assets/Dollars3.png")
Dollars3_rect = Dollars3.get_rect(center=(1000,400))

quit2 = pygame.image.load("assets/Quite2.png")
quit2_rect = quit2.get_rect(center=(900,600))

Won = pygame.image.load("assets/Uwon.png")
won_rect = Won.get_rect(center=(900,200))

Lobby = pygame.image.load("assets/LOBBY.png")
Lobby_rect = Lobby.get_rect(center=(900,400))

is_benzin_on_right = True
FiveftLevelScreen = False
FiveftLevelComletedScreen = False
FourdLevelScreen = False
FourdLevelComletedScreen = False
ThirdLevelScreen = False
ThirdLevelComletedScreen = False
money = 0
car_speed = 1
SecondLevelScreen = False
Menu = True
FirstLevelScreen = False  
FirstLevelCompletedScreen = False
SecondLevelCompletedScreen = False
barruer_box = False
point = 0
MenuMoney = False
f1 = pygame.font.Font(None, 36)
Car_Flipp = False
Shop_Menu= False
Dont_enough_Money_menu = False
SpeedMax = False
Gas_Left = 1500


running = True
while running:
    screen.fill(orange)
    text1 = f1.render(f'Points: {point}', True, (0, 0, 0))
    Gas_Left_Text = f1.render(f'Gas Left: {Gas_Left}', True, (0, 0, 0))
    Current_Speed = f1.render(f'Current speed: {car_speed}', True, (0, 0, 0))
    Current_Speed_rect = Current_Speed.get_rect(center=(100, 250))
    Money_enogh = f1.render('You dont have enough money', True, (0, 0, 0))
    Money_enogh_rect = Money_enogh.get_rect(center=(500, 500))
    Cost = f1.render( "Cost: 1 Money", True, (0, 0, 0))
    Cost_rect = Cost.get_rect(center=(300, 250))
    CantBuy = f1.render( "Max speed, you can't buy more", True, (0, 0, 0))
    CantBuy_rect = CantBuy.get_rect(center=(250, 450))
    Cost2 = f1.render( "Cost: 5 Money", True, (0, 0, 0))
    Cost2_rect = Cost.get_rect(center=(1400, 260))
    Current_Gas = f1.render( f"Current gas:{Gas_Left}", True, (0, 0, 0))
    Current_Gas_rect = Current_Gas.get_rect(center=(1600, 260))
    
    if Menu:
        screen.blit(menu_bg, (0, 0))
        screen.blit(playImg, playImg_rect)
        screen.blit(quit_img, quit_img_rect)
    elif FirstLevelScreen:
        
        screen.blit(level1_bg, (0, 0))
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
        screen.blit(text1, (50, 50))
        screen.blit(Gas_Left_Text, (50, 120))
    elif ThirdLevelScreen:
        
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
        screen.blit(text1, (50, 50))
        screen.blit(Gas_Left_Text, (50, 120))
        

    elif FourdLevelScreen:
         
        screen.fill(rgb4)
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
        screen.blit(text1, (50, 50))
        screen.blit(Gas_Left_Text, (50, 120))




    elif FiveftLevelScreen:
        
        screen.fill(rgb3)
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
        screen.blit(text1, (50, 50))
        screen.blit(Gas_Left_Text, (50, 120))


    elif SecondLevelScreen:
        
        screen.fill(rgb3)
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
        screen.blit(text1, (50, 50))
        screen.blit(Gas_Left_Text, (50, 120))
    elif FirstLevelCompletedScreen:
        screen.fill(orange)
        screen.blit(quit2,quit2_rect)
        screen.blit(Lobby,Lobby_rect)
        screen.blit(Won,won_rect)
    elif Dont_enough_Money_menu:
        screen.fill(orange)
        screen.blit(Money_enogh, Money_enogh_rect)
        screen.blit(Lobby, Lobby_rect)

    elif SecondLevelCompletedScreen:
        screen.fill(orange)
        screen.blit(quit2,quit2_rect)
        screen.blit(Lobby,Lobby_rect)
        screen.blit(Won,won_rect)



    elif ThirdLevelComletedScreen:
        screen.fill(orange)
        screen.blit(quit2,quit2_rect)
        screen.blit(Lobby,Lobby_rect)
        screen.blit(Won,won_rect)


    elif FourdLevelComletedScreen:
        screen.fill(orange)
        screen.blit(quit2,quit2_rect)
        screen.blit(Lobby,Lobby_rect)
        screen.blit(Won,won_rect)


    elif FiveftLevelComletedScreen:
        screen.fill(orange)
        screen.blit(quit2,quit2_rect)
        screen.blit(Lobby,Lobby_rect)
        screen.blit(Won,won_rect)
    elif Dont_enough_Money_menu:
        Dont_enough_Money_menu = True



    elif Shop_Menu:
        screen.fill(orange)
        screen.blit(Upgrade_button, UpgradeButton_rect)
        screen.blit(Current_Speed , Current_Speed_rect)
        car_rect = car.get_rect(center=(100 , 100))
        screen.blit(car , car_rect)
        screen.blit(Backpng, Backpng_rect)
        screen.blit(Cost , Cost_rect)
        screen.blit(Gas_button , Gas_rect)
        screen.blit(Cost2 , Cost2_rect)
        screen.blit(Current_Gas , Current_Gas_rect)
        benzin_rect = benzin.get_rect(center=(1500 , 100))
        screen.blit(benzin , benzin_rect)
        if car_speed == 6 :
            SpeedMax = True
            screen.blit(CantBuy,CantBuy_rect) 



   



    else:
        screen.blit(menu_bg, (0, 0))
        screen.blit(off, off_rect)
        screen.blit(lvl1, lvl1_rect)
        screen.blit(lvl2, lvl2_rect)
        screen.blit(lvl3, lvl3_rect)
        screen.blit(lvl4, lvl4_rect)
        screen.blit(lvl5, lvl5_rect)
        screen.blit(Levels, Levels_rect)
        screen.blit(ShowMoney, ShowMoney_rect)
        screen.blit(Shop_button, ShopButton_rect)



    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # екстриний вихід
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if Menu:
                if playImg_rect.collidepoint(event.pos):
                    Menu = False  
                elif quit_img_rect.collidepoint(event.pos):
                    running = False  
            else:
                if off_rect.collidepoint(event.pos):
                    running = False 
                if lvl1_rect.collidepoint(event.pos): 
                    FirstLevelScreen = True  
                    Menu = False  
                if lvl2_rect.collidepoint(event.pos): 
                    SecondLevelScreen = True  
                    Menu = False
                    
                if lvl3_rect.collidepoint(event.pos): 
                    ThirdLevelScreen = True  
                    Menu = False

                if lvl4_rect.collidepoint(event.pos): 
                    FourdLevelScreen = True  
                    Menu = False 

                if lvl5_rect.collidepoint(event.pos): 
                    FiveftLevelScreen = True  
                    Menu = False      

                if ShowMoney_rect.collidepoint(event.pos): 
                    MenuMoney = True  
                    Menu = False

                if money < 0 :
                    Dont_enough_Money_menu = True
                    car_speed = 1
                    money = 0

                

                if quit2_rect.collidepoint(event.pos): 
                    running = False


                if UpgradeButton_rect.collidepoint(event.pos): 
                    car_speed += 1
                    money -=1

                if Lobby_rect.collidepoint(event.pos): 
                    FirstLevelScreen = False
                    SecondLevelScreen = False
                    FirstLevelCompletedScreen = False
                    Menu = False
                    MenuMoney = False
                    SecondLevelCompletedScreen = False
                    Dont_enough_Money_menu = False


                if Backpng_rect.collidepoint(event.pos): 
                    FirstLevelScreen = False
                    SecondLevelScreen = False
                    FirstLevelCompletedScreen = False
                    Menu = False
                    MenuMoney = False
                    SecondLevelCompletedScreen = False
                    Shop_Menu = False


                if ShopButton_rect.collidepoint(event.pos):   
                    Menu = False
                    Shop_Menu = True




        
                if Gas_rect.collidepoint(event.pos):
                    print(f"Координати кнопки: {Gas_rect.topleft}, Розмір: {Gas_rect.size}")
                    Gas_Left += 3000
                    money -= 5
                    print(f"Gas_Left: {Gas_Left}, Money: {money}") 
    #pygame.    draw.rect(screen, (255, 0, 0), Gas_rect, 2)  # Червона рамка навколо кнопки

    #for event in pygame.event.get():
       # if event.type == pygame.MOUSEBUTTONDOWN:  # Переконуємося, що це подія миші
            #if Gas_rect.collidepoint(event.pos):
                
                #Gas_Left += 3000
                #money -= 5
               # print(f"Gas_Left: {Gas_Left}, Money: {money}")  # Вивід для перевірки

        #elif event.type == pygame.MOUSEBUTTONDOWN:
            #if Gas_rect.collidepoint(event.pos):   
                #Gas_Left += 3000
                #money -= 5
                    

    if MenuMoney == True:
        screen.fill(orange)
        screen.blit(text2, (400, 400))
        screen.blit(Backpng, Backpng_rect)
        screen.blit(Dollars, Dollars_rect)
        screen.blit(Dollars2, Dollars2_rect)
        screen.blit(Dollars3, Dollars3_rect)

    if barruer_box == True:
        car_rect = car.get_rect(center=(500,500))
        barruer_box = False
        

    keys = pygame.key.get_pressed()
    if car_rect.colliderect(barruercopy_rect) or car_rect.colliderect(barruer_rect) or car_rect.colliderect(barruercopyright_rect) or car_rect.colliderect(barruercopyright2_rect) or car_rect.colliderect(barruerupp_rect) or car_rect.colliderect(barruerupp2_rect) or car_rect.colliderect(barruerdown_rect) or car_rect.colliderect(barruerdown2_rect):
        barruer_box = True
    
    if car_rect.colliderect(benzin_rect):
        point += 1
        Gas_Left += 1000
        
        

        if is_benzin_on_right:
            benzin_rect = benzin.get_rect(center=(random.randint(100, int(WIDTH / 2) - 100), random.randint(100, HEIGHT - 100)))
            is_benzin_on_right = False
        else:
            benzin_rect = benzin.get_rect(center=(random.randint(int(WIDTH / 2), WIDTH - 100), random.randint(100, HEIGHT - 100)))
            is_benzin_on_right = True


    if point == 5 and FirstLevelScreen == True:
        money += 5
        FirstLevelScreen = False
        FirstLevelCompletedScreen = True


    if Menu == False and FirstLevelScreen == False and SecondLevelScreen == False and ThirdLevelScreen == False and FourdLevelScreen == False and FiveftLevelScreen == False:
        point = 0

    if point == 10 and SecondLevelScreen == True:
        SecondLevelCompletedScreen = True
        SecondLevelScreen = False
        money += 10



    if point == 15 and ThirdLevelScreen == True:
        ThirdLevelComletedScreen = True
        ThirdLevelScreen = False
        money += 20


    if point == 20 and FourdLevelScreen == True:
        FourdLevelComletedScreen = True
        FourdLevelScreen = False
        money += 25



    if point == 25 and FiveftLevelScreen == True:
        FiveftLevelComletedScreen = True
        FiveftLevelScreen = False
        money += 25



    if event.type == pygame.MOUSEBUTTONDOWN:  
        if SpeedMax == True and UpgradeButton_rect.collidepoint(event.pos):
            car_speed = 6
        
    


    if FirstLevelScreen or SecondLevelScreen or ThirdLevelScreen or FourdLevelScreen or FiveftLevelScreen:
        if  keys[pygame.K_a]:
            if Car_Flipp == False:  
                Car_Flipp = True
                car = pygame.transform.flip(car, True, False)
            car_rect.x -= car_speed
            Gas_Left -= 1
        if  keys[pygame.K_d]:
            if Car_Flipp == True:  
                Car_Flipp = False
                car = pygame.transform.flip(car, True, False)
            car_rect.x += car_speed
            Gas_Left -= 1
        if  keys[pygame.K_w]:  
            car_rect.y -= car_speed
            Gas_Left -= 1
        if  keys[pygame.K_s]:  
            car_rect.y += car_speed
            Gas_Left -= 1

    if Gas_Left <= 0:
        Gas_Left = 0
        car_speed = 0


    text2 = f1.render(f'Money {money}', 1, (0, 0, 0))
    text1 = f1.render(f'points {point}', 1, (0, 0, 0))
    pygame.display.flip()

pygame.quit()