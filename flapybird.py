import pygame
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

#define font
font = pygame.font.SysFont('Bauhaus 93', 40)

#define colours
white = (255, 255, 255)


#define game variables
screen_width = 432
screen_height = 468
ground_scroll = 0
scroll_speed = 3
flying = False
run = True
game_over=False
score=0
high_score=0

pass_pipe = False

delay_of_pipe=1000
last_pipe= pygame.time.get_ticks()

pipe_space=80

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Welcome to My Sami ! Flappy Bird Gamee')

#score function

def draw_score(text , font , colour, x , y ):

	img = font.render(text, True, colour)
	screen.blit(img,(x,y))

def draw_high_score(text , font , colour , y):
	img = font.render(text , True , colour)
	rect = img.get_rect(center=(screen_width // 2, y)) 
	screen.blit(img,rect)

def reset_game():
	pipe_group.empty()
	flappy.rect.x = 40
	flappy.rect.y = int(screen_height / 2)
	score = 0
	return score

#bird class
class Bird(pygame.sprite.Sprite):
	def __init__(self,x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images=[]
		self.index=0
		self.counter=0
		self.speed=0
		for num in range(1, 4):
			img = pygame.image.load(f"img/bird{num}.png")
			img_width=img.get_width()
			img_height=img.get_height()
			img=pygame.transform.scale(img ,(img_width // 2 , img_height // 2) )
			self.images.append(img)
		self.image=self.images[self.index]
		self.rect=self.image.get_rect()
		self.rect.center= [x,y]

	def update(self):

		# gravity
		if flying == True:
			self.speed=self.speed + 0.3
			if self.speed >= 8:
				self.speed = 8
			if self.rect.bottom < int(screen_height-height_ground_real):
				self.rect.y = self.rect.y + self.speed
		
		flappy_cooldown=5
		self.counter+=1
		if game_over == False :
			if self.counter > flappy_cooldown:
				self.index+=1
				self.counter=0
				if self.index >= len(self.images):
					self.index=0

			self.image=self.images[self.index]
			
			# jump
			keys= pygame.key.get_pressed()
			if keys[pygame.K_SPACE]:
				self.speed=-4

			# rotation

			self.image = pygame.transform.rotate(self.images[self.index], self.speed *-3)
		else:
			self.image = pygame.transform.rotate(self.images[self.index], -90)

#pipe class
class Pipe(pygame.sprite.Sprite):
	def __init__(self, x, y, position ):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("img/pipe.png")
		self.image_height=self.image.get_height()
		self.image_weith=self.image.get_width()
		self.image=pygame.transform.scale(self.image,(self.image_weith // 2, self.image_height // 2) )
		
		#1 for pipe from bottom , -1 for pipe from top
		if position == 1 :
			self.rect=self.image.get_rect()
			self.rect.topleft=[x,(y + int(pipe_space / 2))]
		if position == -1:
			self.image = pygame.transform.flip(self.image, False , True)
			self.rect=self.image.get_rect()
			self.rect.bottomleft = [x, (y - int (pipe_space / 2))]
		

	def update(self):
		self.rect.x -=scroll_speed
		if self.rect.right < 0:
			self.kill()



class Button():
	def __init__(self , image,x,y):
		self.image=image
		self.rect=self.image.get_rect()
		self.rect.center=[x,y]
		
	def draw(self):

		action = False
		#get mouse position
		mouse = pygame.mouse.get_pos()
	
		if self.rect.collidepoint(mouse):
		
			if pygame.mouse.get_pressed()[0] == 1:
				action=True


		screen.blit(self.image,(self.rect.x,self.rect.y))
		return action
	
		


#load images
bg = pygame.image.load("img/bg.png")
ground_img = pygame.image.load("img/ground.png")
restart_image=pygame.image.load("img/restart.png")
wight_bg=bg.get_width()
height_bg=bg.get_height()
wight_ground=ground_img.get_width()
height_ground=ground_img.get_height()
height_ground_real=height_ground / 2
bg=pygame.transform.scale(bg,(wight_bg // 2 , height_bg // 2))
ground_img=pygame.transform.scale(ground_img , (wight_ground // 2 , height_ground // 2))


bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

flappy = Bird(40,int(screen_height / 2))
bird_group.add(flappy)


#creating a button
button=Button(restart_image , screen_width // 2 , screen_height // 2 - 40)


while run:

	clock.tick(fps)

	#draw background
	screen.blit(bg, (0,0))

	bird_group.draw(screen)
	bird_group.update()
	pipe_group.draw(screen)
	



	screen.blit(ground_img, (ground_scroll, screen_height-height_ground_real))
	# check for collision
	if pygame.sprite.groupcollide(bird_group , pipe_group , False, False) or flappy.rect.top < 0 :
		game_over=True
		
	# check if bird has hit the bottom
	if flappy.rect.bottom >= int(screen_height-height_ground_real):
		game_over=True
		flying=False 
	
	# colculating the score
	if len(pipe_group) > 0 :
		if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
			and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
			and pass_pipe == False:
			pass_pipe = True
		if pass_pipe == True:
			if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
				score += 1
				pass_pipe = False

			

	# draw the score
	draw_score(str(score),font , white , screen_width/2 , 20 )

	#draw and scroll the ground
	if game_over == False and flying == True:
		time_now=pygame.time.get_ticks()
		
		
		# creating pipes
		if delay_of_pipe < time_now - last_pipe :
			pipe_hight=random.randint(-80,80)
			bttm_pipe = Pipe(screen_width ,int((screen_height / 2 + pipe_hight )),1)
			top_pipe=Pipe(screen_width ,int((screen_height / 2) + pipe_hight ),-1)
			pipe_group.add(bttm_pipe)
			pipe_group.add(top_pipe)
			last_pipe = time_now

		pipe_group.update()
		ground_scroll -= scroll_speed
		if abs(ground_scroll) > 16:
			ground_scroll = 0
		

	if game_over==True:
		if high_score < score:
			high_score = score
		draw_high_score('High score: ' + str(high_score),font , white , 100)
		if button.draw():
			score = reset_game()
			game_over = False
			

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN and flying == False and game_over==False:
			if event.key ==pygame.K_SPACE:
				flying=True

	pygame.display.update() 

pygame.quit()
