
import pygame
import random

Black = (0,0,0)
White = (255,255,255)
Green = (0,255,0)
Red = (255,0,0)

class knight(pygame.sprite.Sprite):
	
	def __init__(self, color=(0,0,0), width=100, height=100, herotype = 0):
		super(type(self),self)._init_()
		
		self.imagelist = []
		self.hplist = [10]
		self.attack_powerlist = [1]
		
		self.projspeedlist = [5]
		
		self.apslist = [1]
		
		
		
		self.hp = self.hplist[herotype]
		self.attack_power = self.attack_powerlist[herotype]
		self.projspeed = self.projspeedlist[herotype]
		self.aps = self.apslist[herotype]
		
		self.image = pygame.Surface([width,height])
		self.image.fill(color)
		
		self.rect = self.image.get_rect()
		
	def reset_pos(self):
		pass
	def update(self):
		pass

class pirate(pygame.sprite.Sprite):
	def__init__(self, color=(0,0,0), width=100, height=100
		super(type(self),self).__init__()
		
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		
		self.rect = self.image.get_rect()
		
	def reset_pos(self):
		pass
	
	def update(self):
		pass

pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

knights_list = pygame.sprite.Group()
pirates_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

done = False
clock = pygame.time.Clock()
money = 0


while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	all_sprites_list.update()
	
	for aknight in knights_list:
		hit_list = pygame.sprite.spritecollide(aknight, pirates_list, False)
		for guy in hit_list:
			pass
			
	screen.fill(WHITE)
	all_sprites_list.draw(screen)
	clock.tick(20)
	pygame.display.flip()
