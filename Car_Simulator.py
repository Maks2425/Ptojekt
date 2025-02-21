import pygame
import random
from enum import Enum

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
lvl1 = pygame.transform.smoothscale(lvl1, (69, 111))
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

lvl6 = pygame.image.load("assets/6.png")
lvl6_rect = lvl6.get_rect(center=(600, 300))

lvl7 = pygame.image.load("assets/7.png")
lvl7_rect = lvl7.get_rect(center=(700, 300))

lvl8 = pygame.image.load("assets/8.png")
lvl8_rect = lvl8.get_rect(center=(800, 300))

lvl9 = pygame.image.load("assets/9.png")
lvl9_rect = lvl9.get_rect(center=(900, 300))

lvl10 = pygame.image.load("assets/10.png")
lvl10_rect = lvl10.get_rect(center=(1000, 300))

car = pygame.image.load("assets/car2.png")
car = pygame.transform.smoothscale(car, (150, 70))  
car_rect = car.get_rect(center=(500,500))

ShowMoney = pygame.image.load("assets/ShowMoney.png")
ShowMoney_rect = ShowMoney.get_rect(center=(1500,130))

Backpng = pygame.image.load("assets/back.png")
Backpng_rect = Backpng.get_rect(center=(30, HEIGHT - 30))

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

rock = pygame.image.load("assets/rock.png")
rock = pygame.transform.smoothscale(rock, (100, 111))
rock_rect = rock.get_rect(center=(200, 300))

is_benzin_on_right = True
money = 0
car_speed = 1
barruer_box = False
point = 0
f1 = pygame.font.Font(None, 36)
Car_Flipp = False
SpeedMax = False
Gas_Left = 1500
Health_Bar = 100


# екрани
class Screen(Enum):
    MENU = 1
    LOBBY = 2
    LEVEL1 = 3
    LEVEL1_COMPLETED = 4
    LEVEL2 = 5
    LEVEL2_COMPLETED = 6
    LEVEL3 = 7
    LEVEL3_COMPLETED = 8
    LEVEL4 = 9
    LEVEL4_COMPLETED = 10
    LEVEL5 = 11
    LEVEL5_COMPLETED = 12
    LEVEL6 = 13
    LEVEL6_COMPLETED = 14
    LEVEL7 = 15
    LEVEL7_COMPLETED = 16
    LEVEL8 = 17
    LEVEL8_COMPLETED = 18
    LEVEL9 = 19
    LEVEL9_COMPLETED = 20
    LEVEL10 = 21
    LEVEL10_COMPLETED = 22
    SHOP = 23
    MONEY = 24
    NOT_ENOUGH_MONEY = 25

current_screen = Screen.MENU



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
    Health_Bar_text = f1.render( f"Helth:{Health_Bar}", True, (0, 0, 0))
    Health_bar_rect = Health_Bar_text.get_rect(center=(1600, 260))
    
    if current_screen == Screen.MENU:
        screen.blit(menu_bg, (0, 0))
        screen.blit(playImg, playImg_rect)
        screen.blit(quit_img, quit_img_rect)
    
    elif current_screen == Screen.LEVEL1:
        
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
        screen.blit(rock, rock_rect )
        screen.blit(Health_Bar_text, (50 ,200))
    
    elif current_screen == Screen.LEVEL3:
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
        

    elif current_screen == Screen.LEVEL4:
         
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




    elif current_screen == Screen.LEVEL5:
        
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


    elif current_screen == Screen.LEVEL2:
        
        screen.blit(level1_bg, (0, 0))
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


    elif current_screen == Screen.LEVEL5:
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

    elif current_screen == Screen.LEVEL6:
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

    elif current_screen == Screen.LEVEL7:
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

    elif current_screen == Screen.LEVEL8:
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


    elif current_screen == Screen.LEVEL9:
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

    elif current_screen == Screen.LEVEL10:
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
    
    elif current_screen == Screen.LEVEL1_COMPLETED:
        screen.fill(orange)
        screen.blit(quit2,quit2_rect)
        screen.blit(Lobby,Lobby_rect)
        screen.blit(Won,won_rect)
    
    elif current_screen == Screen.NOT_ENOUGH_MONEY:
        screen.fill(orange)
        screen.blit(Money_enogh, Money_enogh_rect)
        screen.blit(Lobby, Lobby_rect)

    elif current_screen == Screen.LEVEL2_COMPLETED:
        screen.fill(orange)
        screen.blit(quit2,quit2_rect)
        screen.blit(Lobby,Lobby_rect)
        screen.blit(Won,won_rect)



    elif current_screen == Screen.LEVEL3_COMPLETED:
        screen.fill(orange)
        screen.blit(quit2,quit2_rect)
        screen.blit(Lobby,Lobby_rect)
        screen.blit(Won,won_rect)


    elif current_screen == Screen.LEVEL4_COMPLETED:
        screen.fill(orange)
        screen.blit(quit2,quit2_rect)
        screen.blit(Lobby,Lobby_rect)
        screen.blit(Won,won_rect)


    elif current_screen == Screen.LEVEL5_COMPLETED:
        screen.fill(orange)
        screen.blit(quit2,quit2_rect)
        screen.blit(Lobby,Lobby_rect)
        screen.blit(Won,won_rect)

    elif current_screen == Screen.LEVEL6_COMPLETED:
        screen.fill(orange)
        screen.blit(quit2,quit2_rect)
        screen.blit(Lobby,Lobby_rect)
        screen.blit(Won,won_rect)

    elif current_screen == Screen.LEVEL7_COMPLETED:
        screen.fill(orange)
        screen.blit(quit2,quit2_rect)
        screen.blit(Lobby,Lobby_rect)
        screen.blit(Won,won_rect)

    elif current_screen == Screen.LEVEL8_COMPLETED:
        screen.fill(orange)
        screen.blit(quit2,quit2_rect)
        screen.blit(Lobby,Lobby_rect)
        screen.blit(Won,won_rect)

    elif current_screen == Screen.LEVEL9_COMPLETED:
        screen.fill(orange)
        screen.blit(quit2,quit2_rect)
        screen.blit(Lobby,Lobby_rect)
        screen.blit(Won,won_rect)


    elif current_screen == Screen.LEVEL10_COMPLETED:
        screen.fill(orange)
        screen.blit(quit2,quit2_rect)
        screen.blit(Lobby,Lobby_rect)
        screen.blit(Won,won_rect)
    
    # elif Dont_enough_Money_menu:
    #     Dont_enough_Money_menu = True



    elif current_screen == Screen.SHOP:
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
        screen.blit(text2, (400, 400))
        if car_speed == 7 :
            SpeedMax = True
            screen.blit(CantBuy,CantBuy_rect) 

    elif current_screen == Screen.LOBBY:
        screen.blit(menu_bg, (0, 0))
        screen.blit(off, off_rect)
        screen.blit(lvl1, lvl1_rect)
        screen.blit(lvl2, lvl2_rect)
        screen.blit(lvl3, lvl3_rect)
        screen.blit(lvl4, lvl4_rect)
        screen.blit(lvl5, lvl5_rect)
        screen.blit(lvl6, lvl6_rect)
        screen.blit(lvl7, lvl7_rect)
        screen.blit(lvl8, lvl8_rect)
        screen.blit(lvl9, lvl9_rect)
        screen.blit(lvl10, lvl10_rect)
        screen.blit(Levels, Levels_rect)
        screen.blit(ShowMoney, ShowMoney_rect)
        screen.blit(Shop_button, ShopButton_rect)
        point = 0



    
    
    for event in pygame.event.get():
        # вихід з гри
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        
        # кліки по кнопках
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if SpeedMax == True and UpgradeButton_rect.collidepoint(event.pos):
                car_speed = 6
                
            if Gas_rect.collidepoint(event.pos):
                if money >= 5:  
                    Gas_Left += 3000
                    money -= 5
            if playImg_rect.collidepoint(event.pos):
                current_screen = Screen.LOBBY
            if quit_img_rect.collidepoint(event.pos) or off_rect.collidepoint(event.pos) or quit2_rect.collidepoint(event.pos):
                running = False
            if lvl1_rect.collidepoint(event.pos): 
                current_screen = Screen.LEVEL1
            if lvl2_rect.collidepoint(event.pos): 
                current_screen = Screen.LEVEL2
            if lvl3_rect.collidepoint(event.pos): 
                current_screen = Screen.LEVEL3
            if lvl4_rect.collidepoint(event.pos): 
                current_screen = Screen.LEVEL4
            if lvl5_rect.collidepoint(event.pos): 
                current_screen = Screen.LEVEL5

            if lvl6_rect.collidepoint(event.pos): 
                current_screen = Screen.LEVEL6


            if lvl7_rect.collidepoint(event.pos): 
                current_screen = Screen.LEVEL7

            if lvl8_rect.collidepoint(event.pos): 
                current_screen = Screen.LEVEL8

            if lvl9_rect.collidepoint(event.pos): 
                current_screen = Screen.LEVEL9

            if lvl10_rect.collidepoint(event.pos): 
                current_screen = Screen.LEVEL10

            if ShowMoney_rect.collidepoint(event.pos): 
                current_screen = Screen.MONEY

            if money == -1 :
                current_screen = Screen.NOT_ENOUGH_MONEY
                car_speed = 1
                money = 0

            if UpgradeButton_rect.collidepoint(event.pos): 
                car_speed += 1
                money -=1

            if Lobby_rect.collidepoint(event.pos): 
                current_screen = Screen.LOBBY


            if Backpng_rect.collidepoint(event.pos): 
                current_screen = Screen.LOBBY
            

            if ShopButton_rect.collidepoint(event.pos):   
                current_screen = Screen.SHOP
                    

    if current_screen == Screen.MONEY:
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
    # перевірка на зіткнення з бар'єрами
    if car_rect.colliderect(barruercopy_rect) or car_rect.colliderect(barruer_rect) or car_rect.colliderect(barruercopyright_rect) or car_rect.colliderect(barruercopyright2_rect) or car_rect.colliderect(barruerupp_rect) or car_rect.colliderect(barruerupp2_rect) or car_rect.colliderect(barruerdown_rect) or car_rect.colliderect(barruerdown2_rect):
        barruer_box = True


    if car_rect.colliderect(rock_rect):
        Health_Bar -= 10
        rock_rect = rock.get_rect(center=(random.randint(0,1000) , random.randint(0,1000)))
    
    # перевірка на зіткнення з бензином
    if car_rect.colliderect(benzin_rect):
        point += 1
        Gas_Left += 1000

        if is_benzin_on_right:
            benzin_rect = benzin.get_rect(center=(random.randint(100, int(WIDTH / 2) - 100), random.randint(100, HEIGHT - 100)))
            is_benzin_on_right = False
        else:
            benzin_rect = benzin.get_rect(center=(random.randint(int(WIDTH / 2), WIDTH - 100), random.randint(100, HEIGHT - 100)))
            is_benzin_on_right = True


    # перехід на наступний рівень 
    if point == 5 and current_screen == Screen.LEVEL1:
        money += 5
        current_screen = Screen.LEVEL1_COMPLETED




    if point == 10 and current_screen == Screen.LEVEL2:
        money += 10
        current_screen = Screen.LEVEL2_COMPLETED

    if point == 15 and current_screen == Screen.LEVEL3:
        money += 20
        current_screen = Screen.LEVEL3_COMPLETED

    if point == 20 and current_screen == Screen.LEVEL4:
        money += 25
        current_screen = Screen.LEVEL4_COMPLETED

    if point == 25 and current_screen == Screen.LEVEL5:
        money += 25
        current_screen = Screen.LEVEL5_COMPLETED

    if point == 30 and current_screen == Screen.LEVEL6:
        money += 35
        current_screen = Screen.LEVEL6_COMPLETED

    if point == 35 and current_screen == Screen.LEVEL7:
        money += 45
        current_screen = Screen.LEVEL7_COMPLETED


    if point == 50 and current_screen == Screen.LEVEL8:
        money += 70
        current_screen = Screen.LEVEL8_COMPLETED

    if point == 100 and current_screen == Screen.LEVEL9:
        money += 150
        current_screen = Screen.LEVEL9_COMPLETED

    if point == 150 and current_screen == Screen.LEVEL10:
        money += 300
        current_screen = Screen.LEVEL10_COMPLETED



    
 

    # рух машини
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if Car_Flipp == False:  
            Car_Flipp = True
            car = pygame.transform.flip(car, True, False)
        car_rect.x -= car_speed
        Gas_Left -= 1
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if Car_Flipp == True:  
            Car_Flipp = False
            car = pygame.transform.flip(car, True, False)
        car_rect.x += car_speed
        Gas_Left -= 1
    if keys[pygame.K_w] or keys[pygame.K_UP]:  
        car_rect.y -= car_speed
        Gas_Left -= 1
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:  
        car_rect.y += car_speed
        Gas_Left -= 1

    # перевірка на вичерпання газу
    if Gas_Left <= 0:
        Gas_Left = 0
        car_speed = 0


    text2 = f1.render(f'Money {money}', 1, (0, 0, 0))
    text1 = f1.render(f'points {point}', 1, (0, 0, 0))
    pygame.display.flip()

pygame.quit()