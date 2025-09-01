import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 432
screen_height = 468
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

		self.speed=self.speed + 0.2
		if self.speed >= 6:
			self.speed = 6
		if self.rect.bottom < int(screen_height-height_ground_real):
			self.rect.y = self.rect.y + self.speed

		print(self.speed)




bird_group = pygame.sprite.Group()

flappy = Bird(40,int(screen_height / 2))

bird_group.add(flappy)

#define game variables
ground_scroll = 0
scroll_speed = 4

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

run = True
while run:

	clock.tick(fps)

	#draw background
	screen.blit(bg, (0,0))
	bird_group.draw(screen)
	bird_group.update()

	#draw and scroll the ground
	screen.blit(ground_img, (ground_scroll, screen_height-height_ground_real))
	ground_scroll -= scroll_speed
	if abs(ground_scroll) > 16:
		ground_scroll = 0


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()
