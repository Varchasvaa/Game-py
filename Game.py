import pygame
import time
import random 

pygame.init()
pygame.font.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Varchasva")


BG= pygame.transform.scale(pygame.image.load("BG test 2.webp"),(SCREEN_WIDTH,SCREEN_HEIGHT))

player= pygame.Rect((350,250,50,50))
ply_vel=10

star_time = 2000
star_count= 0 
stars=[]
STAR_WIDTH = 10 
STAR_HEIGHT= 20
STAR_VEL=8

font = pygame.font.SysFont("TimesNewRoman",30)
font_lost = pygame.font.SysFont("TimesNewRoman",50)

clock = pygame.time.Clock()
start_time = time.time()
elaptime= 0

x=0
l=3
f=5

hit=False
run = True 
while run:
    time_text= font.render(f"Time: {round(elaptime)}s",1,"white")

    screen.blit(BG,(0,0))

    star_count+=clock.tick(60)
    if star_count > star_time:
        for _ in range(0,l+x):
            star_x =random.randint(0,SCREEN_WIDTH-STAR_WIDTH)
            star = pygame.Rect(star_x,-STAR_HEIGHT,STAR_WIDTH,STAR_HEIGHT)
            stars.append(star)
        star_time= max(200,star_time-50)
        star_count=0

    elaptime = time.time() - start_time
    p=int(elaptime)

    if p==f and x<10 :
        x=x+1
        f=f+5

    pygame.draw.rect(screen,"purple",player)

    for star in stars: 
        pygame.draw.rect(screen,"pink",star)

    screen.blit(time_text,(10,10))

    key = pygame.key.get_pressed()

    if key[pygame.K_a] and player.x - ply_vel >=0:
        player.x -= ply_vel

    elif key[pygame.K_d] and player.x + ply_vel <= SCREEN_WIDTH - 50:
        player.x+=ply_vel

    elif key[pygame.K_s] and player.y + ply_vel <= SCREEN_HEIGHT - 50:
        player.y+=ply_vel
        
    elif key[pygame.K_w] and player.y - ply_vel >=0:
        player.y-=ply_vel
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for star in stars[:]:
        star.y = star.y + STAR_VEL 
        if star.y > SCREEN_HEIGHT:
            stars.remove(star)
        elif star.y + STAR_HEIGHT >= player.y and star.colliderect(player):
            stars.remove(star)
            hit=True 
            break 
    
    if hit==True:
        lost_text= font_lost.render("You Lost",1,"white")
        screen.blit(lost_text,(SCREEN_WIDTH/2-lost_text.get_width()/2,SCREEN_HEIGHT/2-lost_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(4000)
        break   
    

    pygame.display.update()
pygame.quit()