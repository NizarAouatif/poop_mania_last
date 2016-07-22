from pygame.locals import *
import pygame
import sys
import time
import random
import math
 
image_resources = "app_resources/image_resources/"
sound_resources = "app_resources/sound_resources/"

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()

width,height = 1280,640
size = (width,height)

COCO_SPEED = 4
ROCK_SPEED = 3 
clock = pygame.time.Clock()
#pygame.display.set_caption("The Feint Game: 9riyed ou lBanane")
FPS = 3000

pygame.mixer.music.load("app_resources/sound_resources/leekspin.mp3")
pygame.mixer.music.set_volume(5)
pygame.mixer.music.play(-1)

coin_offset = 60
coin2_offset = 60
points = 1
kill_switch = 0
 
def quit_game():
    pygame.quit()
    sys.exit("System exit.")

class load:
    def image(self,image):
        return (image_resources + image)
    def sound(self,sound):
        return (sound_resources + sound)

#image_1 = load().image("bg_solid_black_square.jpg")
#image_2 = load().image("ball_blue.png")




class GetSource:
    def background(self,image):
        return pygame.image.load(image_resources + image).convert()
    def player(self,image):
        return pygame.image.load(image_resources + image).convert_alpha()
   
class Wall(pygame.sprite.Sprite):
    def __init__(self,color,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width,height))
        self.image.fill(pygame.color.Color(color))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
class Player(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_resources + image).convert_alpha()
        self.rect = self.image.get_rect()
       
class Coin(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_resources + image).convert_alpha()
        self.rect = self.image.get_rect()

class Coin2(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_resources + image).convert_alpha()
        self.rect = self.image.get_rect()
       
pygame.init()
 
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Poop Mania (copyright)")
background = GetSource().background("test.jpg")
player = GetSource().player("awesome.png").convert_alpha()
player_dimension = player.get_width()
 
rock = pygame.image.load("app_resources/image_resources/Rock.png")
rock = pygame.transform.scale(rock, (75, 75))

coco = pygame.image.load("app_resources/image_resources/Coconut.png")
coco = pygame.transform.scale(coco, (75, 75))

x,y = width/2-player_dimension,height/2-player_dimension
movex,movey = 0,0
 
walls = pygame.sprite.Group()
players = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
 
wall_1 = Wall("white", 0, 0, width, 5)
wall_2 = Wall("white", 0, 0, 5, height)
wall_3 = Wall("white", 0, height-5, width, 5)
wall_4 = Wall("white", width-5, 0, 5, height)
player = Player("awesome.png")
coin = Coin("banana.png")
coin2 = Coin2("poop.png")

Vie = 2

walls.add(wall_1,wall_2,wall_3,wall_4)
players.add(player)
coins.add(coin)
coins.add(coin2)
all_sprites.add(wall_1,wall_2,wall_3,wall_4,player,coin,coin2)
fond = "awesome.png"

rock_x = random.randrange(0, width)
rock_y = -75

coco_x = random.randrange(0, width)
coco_y = -95

flag = 0
score = 1

imgm = pygame.image.load("app_resources/image_resources/game-over.jpg")

done = False
game_over = False



#def main():
while not done:

    game_over = False

    if points <10:
        ROCK_SPEED=0
        COCO_SPEED=0
    elif points >= 10 and points < 20:
        ROCK_SPEED=3
        COCO_SPEED=0
    elif points >=20:
        COCO_SPEED=4
    
 
    clock.tick(FPS)

    rock_rect = rock.get_rect(center = (rock_x, rock_y))

    coco_rect = coco.get_rect(center = (coco_x, coco_y))
 
    ticks = pygame.time.get_ticks()
   
    collide_list_1 = pygame.sprite.spritecollideany(wall_1,players)
    collide_list_2 = pygame.sprite.spritecollideany(wall_2,players)
    collide_list_3 = pygame.sprite.spritecollideany(wall_3,players)
    collide_list_4 = pygame.sprite.spritecollideany(wall_4,players)
    collide_list_5 = pygame.sprite.spritecollideany(coin, players)
    collide_list_6 = pygame.sprite.spritecollideany(coin2, players)

    #if points <= (-10) :
        #game_over = True

    #elif points > (-10):
        #game_over = False


    if not game_over:
   
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit_game()
                elif event.key == K_LEFT or event.key == K_a:
                    #fond = pygame.image.load("awesome.png")
                    movex = -4
                elif event.key == K_RIGHT or event.key == K_d:
                    movex = 4
                elif event.key == K_UP or event.key == K_w:
                    movey = -4
                elif event.key == K_DOWN or event.key == K_s:
                    movey = 4
                elif event.key == K_SPACE:
                    Vie = 2
                    points = 0
                    rock_y=-65
                    coco_y=-95
               
            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_a or event.key == K_RIGHT or event.key == K_d:
                    movex = 0
                if event.key == K_UP or event.key == K_w or event.key == K_DOWN or event.key == K_s:
                    movey = 0
 
        if collide_list_1 != None:
            movey = 0
            y += 1
        if collide_list_2 != None:
            movex = 0
            x += 1
        if collide_list_3 != None:
            movey = 0
            y -= 1
        if collide_list_4 != None:
            movex = 0
            x -= 1
        else:    
            x += movex
            y += movey
    
        player.rect.x = x
        player.rect.y = y
 
        screen.blit(background, (0,0))
 
        if  kill_switch == 0:
            coin.rect.x = random.randint(0,width-coin_offset)
            coin.rect.y = random.randint(0,height-coin_offset)
            kill_switch = 1

        if  kill_switch == 0:
            coin2.rect.x = random.randint(0,width-coin2_offset)
            coin2.rect.y = random.randint(0,height-coin2_offset)
            kill_switch = 1
       
        #pygame.display.set_caption("Points: "+str(points))
   
        if collide_list_5 != None:
            points += 1
            score += 1
            coin.rect.x = random.randint(0,width-coin_offset)
            coin.rect.y = random.randint(0,height-coin_offset)
            coin2.rect.x = random.randint(0,width-coin2_offset)
            coin2.rect.y = random.randint(0,height-coin2_offset)

        if collide_list_6 != None:
            points -= 2
            score -= 2
            coin2.rect.x = random.randint(0,width-coin2_offset)
            coin2.rect.y = random.randint(0,height-coin2_offset)
            coin.rect.x = random.randint(0,width-coin_offset)
            coin.rect.y = random.randint(0,height-coin_offset)


        rock_y = rock_y + ROCK_SPEED

        coco_y = coco_y + COCO_SPEED
    
        if rock_y > height:
            rock_y = -75
            rock_x = random.randrange(0, width)

        if coco_y > height:
            coco_y = -95
            coco_x = random.randrange(0, width)

        black = (0, 0, 0)
    
        message = "Lives:  "+str(Vie)
        font = pygame.font.Font(None, 40)
        text = font.render(message, Vie, black)
        screen.blit(text, (1150,10))                                 
        screen.blit(rock, (rock_x, rock_y))
        screen.blit(coco, (coco_x, coco_y))

        if (x <= rock_x + 50 and x >= rock_x - 50) and (y <=rock_y + 50 and y >= rock_y -50 ):
            Vie -= 1
            rock_x = random.randrange(0, width)
            rock_y = -5

        if (x <= coco_x + 50 and x >= coco_x - 50) and (y <=coco_y + 50 and y >= coco_y -50 ):
            Vie -= 1
            coco_x = random.randrange(0, width)
            coco_y = -5

        if score % 20 != 0:
            flag = 0
    
        elif flag == 1 and score != 0:
                Vie += 1
                score = 0
                flag = 2 
            
        elif flag == 0:
            flag = 1


        if Vie <= 0 or points <= -10:
            game_over = True
            #pygame.quit()
        else: game_over = False

    
    
        message = "Points: "+str(points)
        font = pygame.font.Font(None, 40)
        text = font.render(message, points, black)
        screen.blit(text, (10,10))                                 
    
        all_sprites.draw(screen)
        all_sprites.update()
        WHITE = (255, 255, 255)
        #if points < 0:
            #quit_game()
    if game_over:
        #Deaths = 2
        
            #message = "Game Over! Deaths", str(Deaths)
            #font = pygame.font.Font(None, 100)
            #text3 = font.render("GAME OVER!", True , black)
            #screen.blit(text3, (600,320))
            # If game over is true, draw game over
            #text = font.render("Game Over", True, WHITE)
            #text_rect = text.get_rect()
            #text_x = screen.get_width() / 2 - text_rect.width / 2
            #text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.fill(WHITE)
        screen.blit(imgm,(0,0))
        pygame.display.flip()
        #for event in pygame.event.get():
        

    #print(Vie)
                
        
        
                
            #screen.blit(text, (600,320)

            #screen.blit(fond, player_dimension) 
        
    pygame.display.update()
