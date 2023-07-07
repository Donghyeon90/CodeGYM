import pygame
import os
#import button
###
#Credit to https://www.youtube.com/watch?v=jO6qQDNa2UY&t=625s
###

#Problem #1
#when the yellow health go below or equal to 0, game is supposed to be stopped.
#However, here game does not end and it continuesly go on.

#Problem #1 solved
#The problem was that the variable winner_text spelling was wrong.
#So, it did not pass the string to the winner_text.

#To use the font, you need to initiate font first
pygame.font.init()
#sound effect
pygame.mixer.init()

#Constant value are 
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#set the game name
pygame.display.set_caption("Don's first game!")

#color
WHITE=(255,255,255)
BLACK= (0,0,0)
RED=(255,0,0)
YELLOW =(255,255,0)
#This border will be the one in the middle of the screen to split two separate spaces for each player
#We use the // instead of / because we dont want any floating point here
BORDER= pygame.Rect(WIDTH//2-5,0,10,HEIGHT)

#sound effect
BULLET_HIT_SOUND= pygame.mixer.Sound(os.path.join('Assets','Grenade+1.mp3'))
BULLET_FIRE_SOUND=pygame.mixer.Sound(os.path.join('Assets','Gun+Silencer.mp3'))

HEALTH_FONT= pygame.font.SysFont('comicsans',40)
WINNER_FONT = pygame.font.SysFont('comicsans',100)
#how many frames per second 
FPS = 60 
#Velocity (change the spaceship's velocity)
VEL=5
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40
BULLET_VEL =7
MAX_BULLETS=3

#Has to be different number (Unique event id)
YELLOW_HIT=pygame.USEREVENT +1
RED_HIT =pygame.USEREVENT +2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join(
    'Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP= pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 90 )
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join(
    'Assets', 'spaceship_red.png'))
RED_SPACESHIP= pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

SPACE =pygame.transform.scale(pygame.image.load(os.path.join('Assets','space.png')),(WIDTH,HEIGHT))

def draw_window(red, yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    #For the color 
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN,BLACK,BORDER)
    #
    red_health_text= HEALTH_FONT.render("health: " +str(red_health),1,WHITE )
    yellow_health_text= HEALTH_FONT.render("health: " +str(yellow_health),1,WHITE)

    WIN.blit(red_health_text,(WIDTH - red_health_text.get_width()-10,10))
    WIN.blit(yellow_health_text,(10,10))
    
    WIN.blit(YELLOW_SPACESHIP,(yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)
        
    pygame.display.update()

def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x >WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x <0:
            red_bullets.remove(bullet)

def yellow_handle_movement(keys_pressed,yellow):
            #yellow 
    if keys_pressed[pygame.K_a] and yellow.x -VEL>0: #LEFT
        yellow.x-=VEL
    if keys_pressed[pygame.K_d]and yellow.x +VEL+yellow.width<BORDER.x: #RIGHT
        yellow.x+=VEL
    if keys_pressed[pygame.K_w]and yellow.y - VEL>0: #UP
        yellow.y-=VEL
    if keys_pressed[pygame.K_s]and yellow.y +VEL+yellow.width< HEIGHT: #DOWN
        yellow.y+=VEL  

def red_handle_movement(keys_pressed,red):
            #red 
    if keys_pressed[pygame.K_KP4]and red.x -VEL>BORDER.x+BORDER.width: #LEFT
        red.x-=VEL
    if keys_pressed[pygame.K_KP6]and red.x +VEL + red.width<WIDTH: #RIGHT
        red.x+=VEL
    if keys_pressed[pygame.K_KP8]and red.y - VEL>0: #UP
        red.y-=VEL
    if keys_pressed[pygame.K_KP5]and red.y +VEL+red.width< HEIGHT: #DOWN
        red.y+=VEL  

def draw_winner(text):
    draw_text= WINNER_FONT.render(text,1,WHITE)
    WIN.blit(draw_text,(WIDTH/2 - draw_text.get_width()/2,HEIGHT/2- draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    
    red =pygame.Rect(700,300, SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow =pygame.Rect(100,300, SPACESHIP_WIDTH,SPACESHIP_HEIGHT)

    red_bullets=[]
    yellow_bullets=[]

    red_health=10
    yellow_health=10

    #set the frame per second
    clock = pygame.time.Clock()
    #it will be main game while loop and this will be terminated when the game ends
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run= False
                pygame.quit()

            if event.type ==pygame.KEYDOWN:
                if event.key==pygame.K_f and len(yellow_bullets) < MAX_BULLETS:
                    #We use the // instead of / because we dont want any floating point here
                    bullets=pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 -2, 10, 5)
                    yellow_bullets.append(bullets)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_KP1 and len(red_bullets) < MAX_BULLETS:
                    #We use the // instead of / because we dont want any floating point here
                    bullets=pygame.Rect(red.x , red.y + red.height//2 +2, 10, 5)
                    red_bullets.append(bullets)  
                    BULLET_FIRE_SOUND.play()                  

            if event.type==RED_HIT:
                red_health -=1
                BULLET_HIT_SOUND.play()

            if event.type==YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        winner_text=""
        if red_health<=0:
            winner_text="YELLOW WINS!"

        if yellow_health<=0:
            winner_text="RED WINS!"

        if winner_text!="":
            draw_winner(winner_text)
            break

        #debug bullets
        #print(red_bullets,yellow_bullets)
        keys_pressed=pygame.key.get_pressed()

        #yellow 
        yellow_handle_movement(keys_pressed,yellow)        
        #red 
        red_handle_movement(keys_pressed,red)

        handle_bullets(yellow_bullets,red_bullets,yellow,red)

        draw_window(red,yellow,red_bullets,yellow_bullets, red_health,yellow_health)

    #pygame.quit()
    #use main function to restart the game instead of quit the game
    main()

#name of the file
if __name__== "__main__":
    main()

