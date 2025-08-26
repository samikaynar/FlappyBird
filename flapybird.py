import pygame

def draw_pipe(x,y):
    screen.blit(pipe_image,(x,y))


def draw_bird(x,y):
    screen.blit(bird_image,(x,y))

def game():
    x=100
    y=150
    speed=0
    gravity=0.5
    jump=-10
    

    running=True

    while running:
        clock=pygame.time.Clock()
        clock.tick(60)  # 60 frames per second
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

        key=pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            speed=jump

        speed=speed+gravity
        y=y+speed

        

        
        screen.fill((135,206,235))
        draw_bird(x,y)
        draw_pipe(300,-10)
        pygame.display.update()
    
    

pygame.init()
screen=pygame.display.set_mode((600,400))

pygame.display.set_caption("Welcome to my flapy bird game!!")
bird_image = pygame.image.load("C:\\Users\\kayna\\OneDrive\\Masaüstü\\python\\flapybird\\images-removebg-preview.png").convert_alpha()
bird_image = pygame.transform.scale(bird_image, (50, 50))
pipe_image=pygame.image.load("C:\\Users\\kayna\\OneDrive\\Masaüstü\\python\\flapybird\\flappy-bird-pipe-png-steel-casing-pipe-11562902157uauyp2h0pu-removebg-preview.png").convert_alpha()


game()

    
    





pygame.quit()