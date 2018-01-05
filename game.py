
import pygame
import random

class Block(pygame.sprite.Sprite):
	
	def __init__(self, color, width, height,num):
	
		super(type(self),self).__init__()
		a = ["Baby Dragon 1.png","Hogpog.png"]
		self.b = int(10*random.random())
		self.image = pygame.Surface([width, height]).convert_alpha()
		self.image.fill(color)
		self.yosh = pygame.image.load(a[num]).convert_alpha()
		self.yosh = pygame.transform.scale(self.yosh, (width,height))
		self.image.fill((0,0,0,0))
		self.image.blit(self.yosh, (0,0))
			
		self.rect = self.image.get_rect()
			
	def update(self):
		
		self.rect.y += self.b
			
		if self.rect.y > 410:
			self.rect.y = random.randrange(-300, -20)
			self.rect.x = random.randrange(0, screen_width)
				
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (150, 0, 150)
YELLOW = (255, 255, 120)

pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

block_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()

for i in range(70):
	
	
	block = Block(BLUE, 30, 65,0)
	
	block.rect.x = random.randrange(screen_width)
	block.rect.y = random.randrange(screen_height)
	
	block_list.add(block)
	all_sprites_list.add(block)

player = Block(RED, 50, 50, 1)
all_sprites_list.add(player)

done = False

clock = pygame.time.Clock()

score = 0

backg = pygame.Surface([screen_width, screen_height]).convert_alpha()
pic = pygame.image.load("background.jpg").convert_alpha()
pic = pygame.transform.scale(pic, (screen_width,screen_height))
backg.fill((0,0,0,0))
backg.blit(pic, (0,0))

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	screen.fill(WHITE)
	screen.blit(backg,(0,0))
	all_sprites_list.update()
	
	pos = pygame.mouse.get_pos()
	player.rect.x = pos[0]
	player.rect.y = pos[1]
	
	blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
	
	for block in blocks_hit_list:
		score += 1
		print(score)
			
		block.rect.y = random.randrange(-300, -20)
		block.rect.x = random.randrange(0, screen_width)
		
	all_sprites_list.draw(screen)
	
	clock.tick(20)
	
	pygame.display.flip()
