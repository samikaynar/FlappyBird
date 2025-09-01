import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60


#define game variables
screen_width = 432
screen_height = 468
ground_scroll = 0
scroll_speed = 4
flying = False
run = True
game_over=False



screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Welcome to my Flappy Bird Gamee')

#bird class
class Bird(pygame.sprite.Sprite):
	def __init__(self,x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images=[]
		self.index=0
		self.counter=0
		self.speed=0
		for num in range(1, 4):
			img = pygame.image.load(f'C:\\Users\\kayna\\OneDrive\\Masaüstü\\python\\flapybird\\bird{num}.png')
			img_width=img.get_width()
			img_height=img.get_height()
			img=pygame.transform.scale(img ,(img_width // 2 , img_height // 2) )
			self.images.append(img)
		self.image=self.images[self.index]
		self.rect=self.image.get_rect()
		self.rect.center= [x,y]

	def update(self):
		flappy_cooldown=5
		self.counter+=1
		if self.counter > flappy_cooldown:
			self.index+=1
			self.counter=0
			if self.index >= len(self.images):
				self.index=0

		self.image=self.images[self.index]
		# gravity
		if flying == True:
			self.speed=self.speed + 0.3
			if self.speed >= 8:
				self.speed = 8
			if self.rect.bottom < int(screen_height-height_ground_real):
				self.rect.y = self.rect.y + self.speed
	
		# jump
		keys= pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			self.speed=-6

		# rotation

		self.image = pygame.transform.rotate(self.images[self.index], self.speed *-3)




bird_group = pygame.sprite.Group()

flappy = Bird(40,int(screen_height / 2))

bird_group.add(flappy)


#load images
bg = pygame.image.load('C:\\Users\\kayna\\OneDrive\\Masaüstü\\python\\flapybird\\bg.png')
ground_img = pygame.image.load('C:\\Users\\kayna\\OneDrive\\Masaüstü\\python\\flapybird\\ground.png')
wight_bg=bg.get_width()
height_bg=bg.get_height()
wight_ground=ground_img.get_width()
height_ground=ground_img.get_height()
height_ground_real=height_ground / 2
bg=pygame.transform.scale(bg,(wight_bg // 2 , height_bg // 2))
ground_img=pygame.transform.scale(ground_img , (wight_ground // 2 , height_ground // 2))




while run:

	clock.tick(fps)

	#draw background
	screen.blit(bg, (0,0))
	bird_group.draw(screen)
	bird_group.update()

	screen.blit(ground_img, (ground_scroll, screen_height-height_ground_real))

	# check if bird has hit the bottom
	if flappy.rect.bottom > int(screen_height-height_ground_real):
		game_over=True
		flying=False 

	#draw and scroll the ground
	if game_over == False:
		ground_scroll -= scroll_speed
		if abs(ground_scroll) > 16:
			ground_scroll = 0


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN and flying == False and game_over==False:
			if event.key ==pygame.K_SPACE:
				flying=True

	pygame.display.update() 

pygame.quit()
