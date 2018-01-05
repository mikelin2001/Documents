import pygame
import random

pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
person_size = 100


BLACK = (0, 0, 0,0)
WHITE = (255, 255, 255,0)
GREEN = (0, 255, 0,0)
RED = (255, 0, 0,0)
BLUE = (0,0,255,0)

imagelist = [	[	["0r0.png","0r1.png","0r2.png","0r3.png","0r4.png"],
					["0a0.png","0a1.png","0a2.png","0a3.png","0a4.png"],
					["0d0.png","0d1.png","0d2.png","0d3.png","0d4.png"],	
					["0d4.png"] ],
				[	["1r0.png","1r1.png","1r2.png","1r3.png","1r4.png"],
					["1a0.png","1a1.png","1a2.png","1a3.png","1a4.png"],
					["1d0,png","1d1.png","1d2.png","1d3.png","1d4.png"]	]	]


metapiclist = []
for herotype in range(0,1):
	piclist = []
	for all_images in imagelist[herotype]:
		all_pics = []
		for an_image in all_images:
			a_pic = pygame.image.load(an_image).convert_alpha()
			a_pic = pygame.transform.scale(a_pic,(person_size,person_size))
			all_pics.append(a_pic)
		piclist.append(all_pics)
	metapiclist.append(piclist)
	
imagelist2 = [	[	["p0r0.png","p0r1.png","p0r2.png","p0r3.png","p0r4.png","p0r5.png","p0r6.png","p0r7.png","p0r8.png","p0r9.png","p0r10.png","p0r11.png","p0r12.png","p0r13.png","p0r14.png","p0r15.png"],
					["p0a0.png","p0a1.png","p0a2.png","p0a3.png","p0a4.png","p0a5.png","p0a6.png","p0a7.png","p0a8.png","p0a9.png"],
					["p0d0.png","p0d1.png","p0d2.png","p0d3.png","p0d4.png","p0d5.png","p0d6.png","p0d7.png","p0d8.png","p0d9.png","p0d10.png","p0d11.png","p0d12.png","p0d13.png","p0d14.png"],
					["p0d14.png"]	],
				[	["1r0.png","1r1.png","1r2.png","1r3.png","1r4.png"],
					["1a0.png","1a1.png","1a2.png","1a3.png","1a4.png"],
					["1d0.png","1d1.png","1d2.png","1d3.png","1d4.png"],
					["1d4.png"]	]	]

metapiclist2 = []
for villaintype in range(0,1):
	piclist = []
	for all_images in imagelist2[villaintype]:
		all_pics = []
		for an_image in all_images:
			a_pic = pygame.image.load(an_image).convert_alpha()
			a_pic = pygame.transform.scale(a_pic,(person_size,person_size))
			all_pics.append(a_pic)
		piclist.append(all_pics)
	metapiclist2.append(piclist)					
					
class knight(pygame.sprite.Sprite):
	def __init__(self, color=(0,0,0), width=100, height=100, herotype = 0,x=0,y=0):
		super(type(self),self).__init__()
		
		global metapiclist
		

		self.mode = 0
		self.step = 0
		self.piclist=metapiclist[herotype]
	
			
		self.pic = self.piclist[self.mode][self.step]
						  
		self.hplist = [10]
		self.attack_powerlist = [1]
		self.projspeedlist = [5]
		self.apslist = [1]
		self.speedlist = [3]
		
		self.hp = self.hplist[herotype]
		self.attack_power = self.attack_powerlist[herotype]
		self.projspeed = self.projspeedlist[herotype]
		self.aps = self.apslist[herotype]
		self.speed = self.speedlist[herotype]
		self.cost = self.hp + self.attack_power + self.speed
		
		self.image = pygame.Surface([width, height]).convert_alpha()
		self.image.fill((0,0,0,0))
		self.image.blit(self.pic, (0,0))
		
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	
	def reset_pos(self):
		self.step +=1
		if self.step > 4: 
			if self.mode == 2:
				self.mode = 3
			self.step = 0
		if self.mode == 0:
			self.rect.x +=3
		self.pic = self.piclist[self.mode][self.step]
		self.image.fill((0,0,0,0))
		self.image.blit(self.pic, (0,0))
		pass
	
	def update(self):
		self.reset_pos()
		pass

class pirate(pygame.sprite.Sprite):
	def __init__(self, color=(0,0,0), width=100, height=100, villaintype = 0, x = 0, y = 0):
		super(type(self),self).__init__()
		global metapiclist2
		
		self.mode = 0
		self.step = int(9 * random.random())
		self.piclist=metapiclist2[villaintype]
		
		self.pic = self.piclist[self.mode][self.step]
		
		self.hplist = [10]
		self.attack_powerlist = [1]
		self.projspeedlist = [3]
		self.apslist = [1]
		self.speedlist = [3]
		self.number_of_images = [15,9,14,0]
		
		self.hp = self.hplist[villaintype]
		self.attack_power = self.attack_powerlist[villaintype]
		self.projspeed = self.projspeedlist[villaintype]
		self.aps = self.apslist[villaintype]
		self.speed = self.speedlist[villaintype]
		self.cost = self.hp + self.attack_power + self.speed
		
		self.image = pygame.Surface([width, height]) .convert_alpha()
		self.image.fill((0,0,0,0,))
		self.image.blit(self.pic, (0,0))
	
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	
	def reset_pos(self):
		self.step +=1
		if self.step > self.number_of_images[self.mode]:
				if self.mode == 2:
					self.mode = 3
				self.step = 0
		if self.mode == 0:
			self.rect.x -=3
		self.pic = self.piclist[self.mode][self.step]
		self.image.fill((0,0,0,0))
		self.image.blit(self.pic, (0,0))
		pass
		
	def update(self):
		self.reset_pos()
		pass
		
class projectile(pygame.sprite.Sprite):
	def __init__(self, color=(0,0,0), width=100, height=100, projectiletype = 0):
		super(type(self),self).__init__()
		self.imagelist = []
		self.damagelist = [5]
		self.speedlist = [3]
		
		self.damage = self.damagelist[projectiletype]
		self.speed=self.speedlist[projectiletype]
		
		self.image=self.imagelist[projectiletype]
		self.image.fill(color)
	
		self.rect = self.image.get_rect()
	
	def reset_pos(self):
		pass
	
	def update(self):
		pass

class projectile2(pygame.sprite.Sprite):
	def __init__(self, color=(0,0,0), width=100, height=100, projectiletype = 0):
		super(type(self),self).__init__()
		self.imagelist = []
		self.damagelist = [5]
		self.speedlist = [3]
		
		self.damage = self.damagelist[projectiletype]
		self.speed=self.speedlist[projectiletype]
		
		self.image=self.imagelist[projectiletype]
		self.image.fill(color)
	
		self.rect = self.image.get_rect()
	
	def reset_pos(self):
		pass
	
	def update(self):
		pass

myfont = pygame.font.SysFont('Comic San Ms', 30)
tx1 = myfont.render('HP:100', False, (200,50,50))
tx2 = myfont.render('HP:100', False, (200,50,50))
tx3 = myfont.render('$0', False, (250,200,50))
tx4 = myfont.render('$0', False, (250,200,50))

knights_list = pygame.sprite.Group()

knights_by_row = []
for row in range(0,6):
	knights_by_row.append(pygame.sprite.Group())

pirates_list = pygame.sprite.Group()

pirates_by_row = []
for row in range(0,6):
	pirates_by_row.append(pygame.sprite.Group())
	
all_sprites_list = pygame.sprite.Group()

bg1 = pygame.Surface([screen_width,screen_height]).convert_alpha()
pic1 = pygame.image.load("Background.png").convert_alpha()
pic1 = pygame.transform.scale(pic1, (screen_width,int(screen_height/4)))
bg1.fill((0,0,0,0))
bg1.blit(pic1, (0,0))

bg2 = pygame.Surface([screen_width,screen_height]).convert_alpha()
pic2 = pygame.image.load("board05.png").convert_alpha()
pic2 = pygame.transform.scale(pic2, (screen_width,screen_height))
bg2.fill((0,0,0,0))
bg2.blit(pic2, (0,0))

cloud = pygame.Surface([screen_width*2,screen_height*2]).convert_alpha()
pic3 = pygame.image.load("cloudsz3.png").convert_alpha()
pic3 = pygame.transform.scale(pic3, (screen_width*2,screen_height*2))
cloud.fill((0,0,0,0))
cloud.blit(pic3, (0,0))
cloud.set_alpha(0)

show_ending = True
done = False
clock = pygame.time.Clock()
my_money = 200
royal_health = 3
pirate_ship = 150

pirate_counter = 0

#Cloud starting positions
c0 = screen_height + 40
c1 = screen_height
c2 = int(screen_height/2)
c3 = int(screen_height/4)
c4 = 0

# -------- Main Program Loop -----------
while not done:
	for event in pygame.event.get():
		print event
		if event.type == pygame.QUIT:
			done = True
			show_ending = False
		if event.type == 6:
			pos = pygame.mouse.get_pos()
			yy = pos[1]
			if yy > 346:
				row = 5
				x1 = 0
			elif yy > 294:
				row = 4
				x1 = 13
			elif yy > 240:
				row = 3
				x1 = 26
			elif yy > 192:
				row = 2
				x1 = 39
			elif yy > 144:
				row = 1
				x1 = 52
			elif yy > 100:
				row = 0
				x1 = 65
			else:
				row = 10
			
			if row < 6:
				y1 = row * 50 + 25	
				newguy = knight(x=x1,y=y1)
				if my_money + 1 > newguy.cost:
					my_money -= newguy.cost
					knights_by_row[row].add(newguy)
					knights_list.add(newguy)
					all_sprites_list.add(newguy)
					
	if royal_health < 1:
		done = True
	if pirate_ship < 1:
		done = True
		
	my_money += 1
	
		
	pirate_counter += 1
	if pirate_counter > 15:
		pirate_counter = 0
		random_row = int(6 * random.random())
		y1 = random_row * 50 + 25
		new_pirate = pirate(x = 700, y = y1)
		pirates_by_row [random_row].add(new_pirate)
		pirates_list.add(new_pirate)
		all_sprites_list.add(new_pirate)
		
	for piratess in pirates_list:
		if piratess.mode == 3:
			piratess.kill()
	
	for piratess in pirates_list:
		if piratess.rect.x<10:
			royal_health-=piratess.attack_power
			piratess.kill()
	
	for knightss in knights_list:
		if knightss.mode == 3:
			knightss.kill()
			
	for knightss in knights_list:
		if knightss.rect.x>700:
			pirate_ship-=knightss.attack_power
			knightss.kill()
	
	tx1 = myfont.render('HP:'+str(royal_health), False, (200,50,50))
	tx2 = myfont.render('HP:'+str(pirate_ship), False, (200,50,50))
	tx3 = myfont.render('$'+str(int(my_money)), False, (250,200,50))
	#tx4 = myfont.render('$0', False, (250,200,50))
	
	
	all_sprites_list.update()
	
	for row in range(0,6):
		for guy in pirates_by_row[row]:
			guy.mode = 0
		for aknight in knights_by_row[row]:
			aknight.mode = 0
			
			hit_list = pygame.sprite.spritecollide(aknight, pirates_by_row[row], False)
			if len(hit_list) > 0 :
				aknight.mode = 1
			for guy in hit_list:
				guy.mode = 1
				aknight.hp -= guy.attack_power
				guy.hp -= aknight.attack_power
				if guy.hp < 1:
					guy.mode = 2
					guy.step = -1
					pirates_by_row[row].remove(guy)
			if aknight.hp < 1:
					aknight.mode = 2
					aknight.step = -1
					knights_by_row[row].remove(aknight)
	
	# Cloud Movement Math
	c0 -= 1
	c1 -= 3
	c2 -= 5
	c3 -= 7
	c4 -= 9
	
	if c0 < -screen_width*2:
		c0 = screen_width
	if c1 < -screen_width*2:
		c1 = screen_width
	if c2 < -screen_width*2:
		c2 = screen_width
	if c3 < -screen_width*2:
		c3 = screen_width
	if c4 < -screen_width*2:
		c4 = screen_width
	# End Cloud movement math
	
	screen.fill(WHITE)
	screen.blit(bg1,(0,0))
	screen.blit(cloud,(c0,c1))
	screen.blit(cloud,(c1,c2))
	screen.blit(cloud,(c2,c3))
	screen.blit(cloud,(c3,c4))
	screen.blit(cloud,(c4,c1))
	screen.blit(bg2,(0,0))

	all_sprites_list.draw(screen)
	screen.blit(tx1,(100,0))
	screen.blit(tx2,(480,0))
	screen.blit(tx3,(220,0))
	screen.blit(tx4,(600,0))
	pygame.display.flip()
	
	clock.tick(20)

myfont2 = pygame.font.SysFont('Comic San Ms', 100)
if royal_health > 0:
	my_message = "You're Win!"
else:
	my_message = "You're Dead!"

tx5 = myfont2.render(my_message, False, (200,50,50))

screen.blit(tx5,(50,150))
pygame.display.flip()

while show_ending:
	for event in pygame.event.get():
		print event
		if event.type == pygame.QUIT:
			done = True
			show_ending = False
