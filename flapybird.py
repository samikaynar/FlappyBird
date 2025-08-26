import pygame
import random

def draw_pipe(xx,yy):
    screen.blit(pipe_image,(xx,yy))


def draw_bird(x,y):
    screen.blit(bird_image,(x,y))

def draw_bg():
    screen.blit(bg_image,(0,0))

def draw_ground():
    screen.blit(ground_image, (0, screen.get_height() - ground_image.get_height()))

def game():
    x=100
    y=150
    xx=400
    yy=random.randint(-80,-5)
    speed=0
    gravity=0.5
    jump=-10
    

    running=True
    clock=pygame.time.Clock()
    while running:
        
        clock.tick(60)  # 60 frames per second
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

        key=pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            speed=jump

        speed=speed+gravity
        y=y+speed
        xx=xx-5

        
        draw_bg()
        draw_bird(x,y)
        draw_pipe(xx,yy)
        draw_ground()
        pygame.display.update()
    
    

pygame.init()
screen=pygame.display.set_mode((427,468))

pygame.display.set_caption("Welcome to my flapy bird game!!")
bird_image = pygame.image.load("C:\\Users\\kayna\\OneDrive\\Masaüstü\\python\\flapybird\\bird1.png")
pipe_image=pygame.image.load("C:\\Users\\kayna\\OneDrive\\Masaüstü\\python\\flapybird\\pipe.png")
bg_image=pygame.image.load("C:\\Users\\kayna\\OneDrive\\Masaüstü\\python\\flapybird\\bg.png")
ground_image=pygame.image.load("C:\\Users\\kayna\\OneDrive\\Masaüstü\\python\\flapybird\\ground.png")
bird_image = pygame.transform.scale(bird_image, (bird_image.get_width() // 2, bird_image.get_height() // 2))
pipe_image = pygame.transform.scale(pipe_image, (pipe_image.get_width() // 2, pipe_image.get_height() // 2))
bg_image = pygame.transform.scale(bg_image, (bg_image.get_width() // 2, bg_image.get_height() // 2))
ground_image=pygame.transform.scale(ground_image, (ground_image.get_width() // 2, ground_image.get_height() // 2))

game()

    
    





pygame.quit()