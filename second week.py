from pygame import *
from pygame.sprite import *

pygame.init()                   #starts up pyGame
c = 500
screen = display.set_mode((c, c))
display.set_caption("LordCraft")

a = 0
b = 240

playgame = True

box = pygame.Surface((20,20))
box.fill((255,150,255))
x = 0
y = 0

left = False
right = False
up = False
down = False

herosize = int(c/5)
hero = pygame.Surface((herosize,herosize)).convert_alpha()
yosh = pygame.image.load("Baby Dragon 1.png").convert_alpha()
yosh = transform.scale(yosh, (herosize,herosize))
hero.fill((0,0,0,0))
hero.blit(yosh, (0,0))
heroedge = c - herosize

# the overakk event loop
while playgame:
	
	for e in pygame.event.get():
		#e = event.wait()          #pause until event occurs
		if e.type == QUIT:
			pygame.quit()         #shut down pyGame
			break
	print e


	if e.type == 5 and e.button== 3 :
		playgame = False
		pass
	if e.type == 2 and e.key == 32:
		playgame = False
	if e.type == 2:
		if e.key == 273:
			up = True
		if e.key == 274:
			down = True
		if e.key == 275:
			right = True
		if e.key == 276:
			left = True
		
	if e.type == 3:
		if e.key == 273:
			up = False
		if e.key == 274:
			down = False
		if e.key == 275:
			right = False
		if e.key == 276:
			left = False
	
	a = a + .1
	if a > 255:
		a = 0
		b = b - 80
	if b < 0:
		b = 240
		
	if left:
		x -= .1
	if right:
		x += .1
	if up:
		y -= .1
	if down:
		y += .1
		
	if x < 0:
		x =500
	if x > 500:
		x = 0
	if y < 0:
		y = 0
	if y > 490:
		y = 490
		
		
	#if e.type == 4:
		#x = e.pos[0]
		#y = e.pos[1]
	screen.fill(( int(a), int(255 - a) , int(b)))
	screen.blit(yosh,(int(x),int(y)))
	display.update()
	
	
		
