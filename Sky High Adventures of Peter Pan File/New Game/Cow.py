##==============================================================_______Script______================================================================================#

#-------------------------'Pre-Code'---------------------------------------------------------------#
import pygame				# Importing the following will allow pygame and the other modules to run 
import random
import pygame.mixer
from pygame.locals import*			# Imports all local pygame functions
pygame.init()

clock = pygame.time.Clock()		# Here, the speed of the entire game can be controlled, later on you will see how


#---------------------------Classes---------------------------------------------------------------#

#________________Peter_______________________________________#

class Peter: 						
	def __init__(self,l,h,x,y,k,s):
		self.health = h				# Moniters his health
		self.level = l				# Keeps track of his level 
		self.X = x				# Thoughout this program, self.X and self.Y are the character's coordinates
		self.Y = y
		self.speed = s				# This will be a constant variable being added to or subtracted from the character's coordinates

	def procedure(self):		## This procedure will direct the program to where is nescessary 
		global gameOver
		global levelup1
		global pause1
			
		if self.level == 1:			# The rest of the procedure will change peter's, hook's, bullet's, and the baby's speeds according to the level
			peter.speed = 4
			game.level1()			# Also Each level has its own set of steps that must be followed **LOE**
					
			
	def draw(self):		## This will do all the steps needed for peter to be a controlable character
		peter.move()				# Moves Peter based on user input
		self.bordercheck()			# Makes sure Peter doesn't leave the screen
		if peterLeft:				# Makes Peter Face the direction he is going
			screen.blit(revpeter,(self.X,self.Y))
		else:
			screen.blit(peter1,(self.X,self.Y)) 
			
		
	def bordercheck(self):		## Here such as all the other bordercheck defenitions, when the character crosses
		global up				# a boreder, they will be quickly respawned inside the border, and they will be stopped;
		global down				# making them seem like they cannot cross that border
		global left				
		global right
		if self.X <= 0:
			self.X = 0
			left = False
		if self.X >= screen_width - 130:
			self.X = screen_width -130
			right = False			
		if self.Y <= 0:
			self.Y = 0
			up = False
		if self.Y >= screen_height-190:
			self.Y = screen_height-190
			down = False
		
	def move(self):		## This will move peter based on the user's input
		global up
		global down
		global right
		global left
		if up and down :			# This will make peter stop if user chose opposite directions
			self.speed = 0
			up = False
			down = False
		if left and right:		 
			self.speed = 0
			left = False
			right = False
		if left:				# These Flags will determine which direction the user wants Peter to move			
			self.X = self.X - self.speed	# Based on the direction, the speed will be added or deducted from Peter's coordinates
		elif right:
			self.X = self.X + self.speed
		elif up:
			self.Y = self.Y - self.speed	
		elif down:
			self.Y = self.Y + self.speed
	
#__________________________Hook___________________________________#	

class Hook:
	def __init__(self,n,x,y,s):
		self.name = n
		self.X = x
		self.Y = y
		self.speed = s
		self.border = False
		
	def bordercheck(self):		## Allows Hook to go back and Forth
		if self.X <= 0:
			self.X = 0
		if self.X >= screen_width - 130:
			self.X = screen_width -130
		if self.Y <= 0:
			self.Y = 0
		if self.Y >= screen_height-190:
			self.Y = screen_height-190

	def tag(self,peter):	## This will make Peter loose health when he comes in contact with Hook
		if (peter.X +130 >= self.X +50) and (peter.X <= self.X) and (peter.Y +170 >= self.Y) and (peter.Y <= self.Y +100):
			gameoversound.play()
			peter.health = peter.health - 0.005
			
	def move(self):		## Moves Hook based on which border he is at
		pass
				
	def draw(self):		## Where more magic happens
		self.bordercheck()
		self.move()
		self.tag(peter)
		screen.blit(self.name,(self.X,self.Y))


#______________This is where the procedures for every level are__________#

class Levels:
	def __init__(self,n):
		self.name = n
			
	def level1(self):	## level 1	
		neverland.draw()	# The  scenery is drawn
		hook.move()		# Tinker runs around, and checks if Peter caught her
		peter.draw()		# User moves Peter around

		
#____________________Backgrounds___________________#	

class Background:
	def __init__(self,n,x,y):
		self.name = n
		self.X = x
		self.Y = y
		
	def draw(self):		## Simply draws the required background
		screen.blit(self.name,(self.X,self.Y))
			
	
	
#------------------------------------------------Loading Section---------------------------------------------------#

screen_width = 900			##Depects screen height and width
screen_height = 616
size = screen_width, screen_height
screen = pygame.display.set_mode(size)

#_____________________Loads Images____________________________#

neverland = pygame.image.load("background1.jpg")
buttonclick = pygame.mixer.Sound("buttonclick.wav")
gameover3 = pygame.image.load("gameover1restart.png")
gameover3restart = pygame.image.load("gameover3restart.png")
gameoversound = pygame.mixer.Sound("gameover.wav")
peter = pygame.image.load("peterpan1.png")
revpeter = pygame.transform.flip(peter,True,False)		#Flips the image as desired
hook = pygame.image.load("hookandcannon.png")


#_________________________Class Objects_______________________________#

hook = Hook(hook,785,500,1)
peter = Peter(1,3,250,180,1,3)
gameover3 = Background(gameover3,0,0)
gameover3restart = Background(gameover3restart,0,0)


#_________________Background Music and Fonts____________________#

pygame.mixer.music.load("newtheme.wav")			## Loads background music	
pygame.mixer.music.play(-1)				## Infinitly plays the music


#_____________________Global Variables____________________#

play = False		# To know wether the user has started pressed play
gameOver = False	# To Show she gameOver screen once Peter Dies
up = False		# These flags will be used to determine which direction he is going
down = False
left = False
right = False
peterLeft= False	# This is a speacial one, only used to see which direction Peter is facing	
gameOn = True		# And finally, this is to quit the program once user wishes to do so


#---------------------------------------------------------Game Loop---------------------------------------------------------------#

while gameOn:					#Loops until user exits
#______________________________________Game Over Screen_______________________________________________#
			
	while gameOver:
		x,y = pygame.mouse.get_pos()		# Gets Mouse Position
		
		
		gameover3.draw()					# Same Here expect if doesn't include the skip button
		if (x >=320) and (x <=560) and (y>=410) and (y<=530):
			gameover3restart.draw()
			                                # Displays the Highest Score 
		pygame.display.flip()			# This is so you can see highlighted button without clicking it
		
		for event in pygame.event.get():
			if event.type == QUIT:		# Quits the game
				gameOver = False
				gameOn = False
				play = False
				break
			
			elif event.type == MOUSEBUTTONDOWN:
				buttonclick.play()
				if (x >=320) and (x <=560) and (y>=410) and (y<=530): # Same thing as before, just doens't provide a skip option
					gameover3restart.draw()
					peter.level = 1
					peter.health = 1
					gameOver = False
				else:
					gameover3.draw()
				
		pygame.display.flip()	# Shows everything we have draw
	
	
#___________________________________________Actual Game__________________________________________________________#	
	
	for event in pygame.event.get():		# goes through every possible input
		if event.type == QUIT: 
			gameOn = False			# stops the game when user quit
		
		elif event.type == KEYDOWN:		# does the following when a key is pressed			
			if event.key == K_ESCAPE:	# clicking Escape will exit the game
				gameOn = False
			elif event.key == K_UP:		# These Flags are set based on user input
				up = True		# So if up is True, the Peter will move up
			elif event.key == K_DOWN:	
				down = True
			elif event.key == K_LEFT:	
				left = True
				peterLeft= True		# Peterleft is used to determine which side he should be facing
			elif event.key == K_RIGHT:	
				right = True
				peterLeft= False
			
		elif event.type == KEYUP:		# when a key is released the following occurs
			if event.key == K_UP:	
				right =	False		# Resting the Left and right flags when an up or down key is released makes sure 
				left = False  		# Peter doesn't go diagonally, same thing with the left and right keys              
			elif event.key == K_DOWN:		
				right =	False		
				left = False		
			elif event.key == K_LEFT:		
				up = False		 
				down = False		
			elif event.key == K_RIGHT:	
				up = False		
				down = False
				
	peter.procedure()
	clock.tick(60)			# Making the clock tick for 60 miliseconds inbetween frames, allows the speed of the program to be the same no matter the computer
	
	pygame.display.flip()		# Displays the images
	
pygame.quit()		#Quits Pygame
