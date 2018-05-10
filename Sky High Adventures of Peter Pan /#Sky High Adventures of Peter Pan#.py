##____________________________________________________________________Intro________________________________________________________________________________________#

# ***The SkyHigh Adventures of Peter Pan***

# Created by Raed Fayad on January 19, 2016

# This is a Fun, Addictive, and Amazing Graphics game following a storyline in which peter pan must run around trying to catch tinker bell as many times as he can to advance
# in levels. Later on, Hook will start challenging peter by firing a cannon at him. Eventually, Hook even starts to throw babies from his Floating ship, leaving  Peter Pan as
# their last hope...  Multiple Levels make this game even more addictive, leaving the player with no choice but to keep trying. Throughout the game, the player can Pause, or 
# Return to the Main Menu. Background Music is optional but highly recommended, and the sound effects will immerse the player in the Exciting and Dangerous World of Peter 
# Pan!     

# For Whom it May Concern, the caring, thoughtful, and Brave maker of this Amazing Game has decided to give players interested in his code a chance to experience the
# Game by creating a shortcut. By Pressing the Space Bar during GamePlay, Peter will Jump to the Next Level!    Your Welcome!   Now You will be able to experience the
# Entire Game, even if you don't have the skills needed to do so by yourself. 

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
		self.skips = k				# This will make sure user only gets one skip
		self.speed = s				# This will be a constant variable being added to or subtracted from the character's coordinates
		self.catches = 0			# Score (# of tinker bells caught)
		self.catchesneeded = 5			# This is the score needed to advance to the next level
		self.highscore = 0			# This is the highest score achieved 
	
	def procedure(self):		## This procedure will direct the program to where is nescessary 
		global gameOver
		global levelup1
		global pause1
		
		if self.catches == self.catchesneeded:  # Makes Peter level up when his score is right
			peter.levelup()
			self.catches = 0		# Resets the score
			
		if peter.health <= 0.0:			# Stops doing the gameOn loop, and instead starts the while gameOver loop (later on explained)		
			gameOver = True
			
		elif  pause1:				# Will pause the game (also later on explained)
			levelup1 = True			# Lets get a system going **Later On Explained ===== LOE***
			game.pause()
			
		elif self.level == 1:			# The rest of the procedure will change peter's, hook's, bullet's, and the baby's speeds according to the level
			self.catchesneeded = 8		# This changes the score needed for peter to move on to the next level also personalized for each level	
			peter.speed = 7
			game.level1()			# Also Each level has its own set of steps that must be followed **LOE**
			
		elif self.level == 2:
			self.catchesneeded = 5
			peter.speed = 6
			bullet.speed = 8
			hook.speed = 4		
			game.level2()
			
		elif self.level == 3:
			self.catchesneeded = 5
			peter.speed = 7
			bullet.speed = 9
			hook.speed = 6.5			
			game.level2()
			
		elif self.level == 4:
			hook2.speed = 7
			baby.speed = 4.8
			peter.speed = 8
			self.catchesneeded = 10
			game.level4()
			
		elif self.level == 5:
			hook.speed = 6
			hook2.speed = 5
			baby.speed = 3.5
			peter.speed = 7
			bullet.speed = 8
			self.catchesneeded = 13
			peter.skips = 0                                                           
			game.level5()	
			
		elif self.level == 6:
			game.finish()
		if peter.catches > peter.highscore:
			peter.highscore = peter.catches		
			
	def draw(self):		## This will do all the steps needed for peter to be a controlable character
		peter.move()				# Moves Peter based on user input
		self.bordercheck()			# Makes sure Peter doesn't leave the screen
		if peterLeft:				# Makes Peter Face the direction he is going
			screen.blit(revpeter,(self.X,self.Y))
		else:
			screen.blit(peter1,(self.X,self.Y)) 
			
	def reset(self):	## This will be used when going from level to level, and restarting the game 
		global up
		global down
		global left
		global right
		global peterLeft			# Here, characters will default to their original locations;
		
		left = False				# Resets Peter's Health, Peter's direction, and his Score
		right = False
		up = False
		down = False	
		peterLeft = False
		peter.health = 1
		if peter.level == 4:
			peter.health = 2		# Provides peter with 2 lives in level4
		peter.catches = 0
		peter.X = 200
		peter.Y = 200
		tinker.X = 300
		tinker.Y = 500
		hook.Y = 500
		hook2.X = 800
		bullet.X = hook.X			# Resets the bullet to Hook's cannon	
		
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
			
	def levelup(self):		## This function will allow Peter to move up a level, when he reaches the right score
		global levelup1
		levelupsound.play()			# Play some cool sounds for a second
		levelupsound.fadeout(1000)
		self.level = self.level +1
		levelup1 = True				# These flags are to whether or not display instructional pages for each level
		levelup2 = True
		if peter.level == 5 or peter.level == 4:
			baby.throw = False		# Resets the Baby's location of drop-off
			baby.RX = random.randint(200,screen_width -400)
		if peter.level == 6:
			finale.play()			# Plays clapping sounds for having finished the game
			levelupsound.stop()
		peter.reset()				# Resets the game characters
		peter.highscore = 0
		
		
#_________________________Tinker Bell_____________________________#

class Tinkerbell:
	def __init__(self,x,y):
		self.X = x
		self.Y = y
		self.speedX = 3		# Just to add a little fun by making Tinker go diagnally 
		self.speedY = 4
		
	def tag(self,catcher):		## This will allow peter to touch and catch Peter
		global tinkercaught
		if (peter.X +90 >= self.X) and (peter.X+90<= self.X +75) and (peter.Y+100 >= self.Y) and (peter.Y+100 <= self.Y + 100):
			fairydust.play()			# Plays some sparkling tunes			
			tinkercaught = True
				
			if self.speedY < 0 or self.speedX < 0:		# This will make tinker go in the oposite direction when she gets caught
				self.speedX = 3
				self.speedY = -4
			else:
				self.speedX = -3
				self.speedY = 4
				
			if peter.level == 4:					
				self.X = random.randint(100,screen_width-100)	# This spawns Tinker at a new location once she is caught by Peter
				self.Y = random.randint(200,screen_height - 200)								
			elif peter.level == 5:					# This is nescessary to make sure Tinker doen't spawn in Hook's path
				self.X = random.randint(100,screen_width-200)
				self.Y = random.randint(200,screen_height - 200)
			else:
				self.X = random.randint(100,screen_width-200)
				self.Y = random.randint(100,screen_height - 200)
			peter.catches = peter.catches + 1		# Increases the score
		else:
			tinkercaught = False
			
	def move(self):			## Moves Tinkerbell around the screen
		if peter.level == 2 or peter.level == 3:
			if self.X <= 0 or self.X >= screen_width - 200:		# Tinker will be bouncing off walls when this function is called
				self.speedX = -1*(self.speedX)
			if self.Y <= 0 or self.Y >= screen_height - 100:
				self.speedY = -1*(self.speedY)
		elif peter.level == 4:
			if self.X <= 0 or self.X >= screen_width - 100:		# Based on which level, Tinker will have different borders
				self.speedX = -1*(self.speedX)
			if self.Y <= 100 or self.Y >= screen_height - 100:
				self.speedY = -1*(self.speedY)
		elif peter.level == 5:
			if self.X <= 0 or self.X >= screen_width - 200:	
				self.speedX = -1*(self.speedX)
			if self.Y <= 100 or self.Y >= screen_height - 100:
				self.speedY = -1*(self.speedY)
		else:
			if self.X <= 0 or self.X >= screen_width - 100:	
				self.speedX = -1*(self.speedX)
			if self.Y <= 0 or self.Y >= screen_height - 100:
				self.speedY = -1*(self.speedY)
	
		self.X = self.X + self.speedX		# Moves Tinker
		self.Y = self.Y + self.speedY
		tinker.tag(peter)			# Checks if Peter has caught Tinker
		tinker.draw()	
		
	def draw(self):			## Displays Tinker after checking if she got caught
		if self.speedX <= 0:				# Tinker will be facing the way she is moving
			screen.blit(tinker3,(self.X,self.Y))
		elif self.speedX >= 0:
			screen.blit(revtinker2,(self.X,self.Y))		
		
		
#______________________Hook's Bullet_______________________________#

class Bullet:
	def __init__(self,n,x,y,s):
		self.name = n
		self.X = x
		self.Y = y
		self.speed = s
		self.border= False
		
	def tag(self,peter):		## Checks to see if the bullet has hit Peter
		if (self.Y >= peter.Y-120) and (self.X <= peter.X +100) and (self.X >= peter.X +50) and (self.Y <= peter.Y +70): 
			self.border = True		# If so, it kills Peter, and returns Hook's Cannon
			peter.health = peter.health - 1 
			hooklaugh.play()		# Then plays some evil laughs
			gameoversound.play()
		
	def bordercheck(self):		## This is what happens when the bullet misses Peter 
		if self.X <= 0:
			self.border = True		# Once its hits the left border, it raises the flag 
	
	def fire(self):			## Tells the Hook when to Fire
		if self.border:				# If the bullet misses or hits Peter, it jumps back to Hook's cannon, to get fired again
			self.X = hook.X
			self.Y = hook.Y
			self.border = False
			cannonexplode.play()		# Aslo comes with explosion sound effects, WOW!!	
			cannonexplode.fadeout(1000)
			
	def move(self):			## This actually moves the bullet, from the right to the left 	
		self.X = self.X - self.speed
		
	def draw(self):			## All the magic happens here
		bullet.fire()				# The Bullet Gets back to Hook's Cannon
		bullet.move()				# Then gets going
		bullet.bordercheck()			# Checks to see if it hit the wall yet
		bullet.tag(peter)			# Or if it had hit Peter
		screen.blit(self.name,(self.X,self.Y + 117 ))# Then displays it
		
		
#______________________Poor Little Baby_______________________________#

class Baby:
	def __init__(self,n,x,y,rx,s):
		self.name = n
		self.X = x
		self.Y = y
		self.RX = rx
		self.speed = s
		self.throw = False 
		
	def tag(self, peter):		## Sees whether Peter caught the baby
		if (peter.X +90 >= self.X) and (peter.X+90<= self.X +75) and (peter.Y+100 >= self.Y) and (peter.Y+100 <= self.Y + 100):
			self.RX = random.randint(200,screen_width -400) # If so, finds a new place for Hook to drop off the baby
			self.throw = False
			babylaugh.play()		# Plays some cute baby sounds
			babylaugh.fadeout(1400)
			
	def fire(self):			## Once the baby gets caught or dies, it respawns right back into Hook's Hands, not everyone has a gd destiny
		if (self.RX <= hook2.X + 6) and (self.RX >= hook2.X -6):  	# Checks to see if Hook is at the correct place to drop off the baby
			self.X = hook2.X+100					# Spawns the Baby at Hook's Hands		
			self.Y = hook2.Y+100	
			self.RX = -50						# Makes sure Hook doesn't reach the drop off point again, untill the baby returns to him
			self.throw = True
			babybyebye.play()
			
	def move(self):			## Moves Hook
		self.Y = self.Y + self.speed
		
	def bordercheck(self):		## Keeps Baby within the screen
		if self.Y >= screen_height:
			self.RX = random.randint(200,screen_width -200)
			self.throw = False					# This will reset the Baby's position back to Hook, once it touches the bottom
			peter.health = peter.health - 1
			hooklaugh.play()
			
	def draw(self):			## Were all the magic happens
		baby.fire()
		if self.throw:		
			baby.bordercheck()
			baby.move()
			baby.tag(peter)
			screen.blit(self.name,(self.X,self.Y))	
			
			
#__________________________Hook___________________________________#	

class Hook:
	def __init__(self,n,x,y,s):
		self.name = n
		self.X = x
		self.Y = y
		self.speed = s
		self.border = False
		
	def bordercheck(self):		## Allows Hook to go back and Forth
		if self == hook2:				# There must be different actions for the Hook going left to right and the up and down Hook			
			if self.X <= 0:				# makes the horizontal hook go the opposite directions once he gets to a screen border
				self.X = 0
				self.border = True
			if self.X >= (screen_width -100):
				self.X = screen_width -100
				self.border = False
		else:						# makes the vertical hook go the opposite direction once he hits a border
			if peter.level == 5: 
				if self.Y <= 150:
					self.Y = 150
					self.border = True
			else:
				if self.Y <= -5:
					self.Y = -5
					self.border = True	
			if self.Y >= (screen_height -155):
				self.Y = screen_height -155
				self.border = False
				
	def tag(self,peter):	## This will make Peter loose health when he comes in contact with Hook
		if (peter.X +130 >= self.X +50) and (peter.X <= self.X) and (peter.Y +170 >= self.Y) and (peter.Y <= self.Y +100):
			gameoversound.play()
			peter.health = peter.health - 0.005
			
	def move(self):		## Moves Hook based on which border he is at
		if self.border:
			if self == hook2:			
				self.X = self.X + self.speed		# left and right
			else:
				self.Y = self.Y + self.speed		# up and down
		else:
			if self == hook2:
				self.X = self.X - self.speed		# left and right
			else:
				self.Y = self.Y  - self.speed		# up and down
				
	def draw(self):		## Where more magic happens
		self.bordercheck()
		self.move()
		self.tag(peter)
		screen.blit(self.name,(self.X,self.Y))


#______________This is where the procedures for every level are__________#

class Levels:
	def __init__(self,n):
		self.name = n
		
	def pause(self):	## Pause Menu
		if levelup1:			# Shows it untill user presses enter (levelup1 becomes False)
			pause.draw()
			
	def level1(self):	## level 1	
		if levelup2:			# This shows the instructions page untill user presses enter
			intro1.draw()	
		else:				# Then the game starts
			neverland.draw()	# The  scenery is drawn
			tinker.move()		# Tinker runs around, and checks if Peter caught her
			peter.draw()		# User moves Peter around
			textdraw()		# Score and level is shown
		
	def level2(self):	##level 2 and level 3 (faster level 2)
		if levelup1:			# Shows level up screen untill user clicks return		
			levelup.draw()
		elif levelup2 and peter.level == 2:	# Shows instructions for level 2 untill user clicks enter
			intro2.draw()
		else:				# Then level 2 game starts
			neverland.draw()
			hook.draw()		# This time Hook is moved and drawn()
			bullet.draw()		# The Bullet is moved, and it checks if Peter got hit by it
			tinker.move()		# Tinker is now stationare, and changes positions when Peter catches her
			peter.draw()		# Peter is moved by user
			textdraw()		# score and level is shown during gameplay
			
	def level4(self):	## level4
		if levelup1:
			levelup.draw()
		elif not levelup2:
			intro3.draw()
		else:
			london.draw()
			hook2.draw()
			baby.draw()
			peter.draw()
			tinker.move()
			textdraw()
			
	def level5(self):	## level 5 (final level)
		if levelup1:
			levelup.draw()
		elif not levelup2:
			intro4.draw()
		else:
			london.draw()		# 2 Hooks, one up and down, one side to side. 
			hook.draw()		# Babies Dropping, and Bullets Flying
			hook2.draw()		# and Of coarse, Tinker bell just hanging around
			baby.draw()
			bullet.draw()
			tinker.move()
			peter.draw()
			textdraw()
			
	def finish(self):	## congratulations screen
		finish.draw()
		
		
#____________________Backgrounds___________________#	

class Background:
	def __init__(self,n,x,y):
		self.name = n
		self.X = x
		self.Y = y
		
	def draw(self):		## Simply draws the required background
		global musicon
		if musicon == True and self == mainmusic:		# This is what allows a line to show when you are about to turn off the music
			screen.blit(mainmusicoffpic,(self.X,self.Y))			
		else: 
			screen.blit(self.name,(self.X,self.Y))
			
			

#----------------------------------Loner Functions-------------------------------------------------#
			
def music():		## This function just starts and stops the background music based on the user's preference
	global musicon
	if musicon:				# If music already on, it turns it off and vise versa
		pygame.mixer.music.stop()
		musicon = False
	else:
		pygame.mixer.music.play(-1)
		musicon = True

def textdraw():		## Writes the score and the level on the game screen
	global scoretext
	global leveltext
	global tinkerleft
	scoretext = InfoFont.render('Score: ' + str(peter.catches*10), True, Red)	# For the score
	leveltext = InfoFont.render('Level: ' + str(peter.level), True, Red)		# For the Level
	tinkerleft = InfoFont.render("Tinkers Left: " + str(peter.catchesneeded - peter.catches), True, Red)	# For the # of tinkers needed to move on to next level
	screen.blit(scoretext,(5,5))			# Blits them all				
	screen.blit(leveltext,(810,5))
	screen.blit(tinkerleft,(5,30))
	
def highscoredraw():		## This will write the highscore at the gameOver screen
	highscoretext = InfoFont.render('Your High Score is ' + str(peter.highscore*10), True, White)
	screen.blit(highscoretext,(350,340))
	
	
#------------------------------------------------Loading Section---------------------------------------------------#

screen_width = 900			##Depects screen height and width
screen_height = 616
size = screen_width, screen_height
screen = pygame.display.set_mode(size)

#______Assignes RGB Tuples to colours_____#

Red = 150,0,0
White = 255,255,255

#_____________________Loads Images____________________________#

neverland = pygame.image.load("background1.jpg")
london = pygame.image.load("London.jpg")
main = pygame.image.load("beginning.png")
mainplay = pygame.image.load("beginning2.png")
mainvolume = pygame.image.load("beginning3.png")
mainmusic = pygame.image.load("beginning4.png")
mainmusicoffpic = pygame.image.load("mainmusicoff.png")
mainhelp = pygame.image.load("beginning5.png")
mainexit = pygame.image.load("exit.png")
buttonclick = pygame.mixer.Sound("buttonclick.wav")
pause = pygame.image.load("pause.png")
gameover = pygame.image.load("gameover1.png")
gameoverrestart = pygame.image.load("gameoverrestart.png")
gameoverskip = pygame.image.load("gameoverskip.png")
gameover3 = pygame.image.load("gameover1restart.png")
gameover3restart = pygame.image.load("gameover3restart.png")
gameoversound = pygame.mixer.Sound("gameover.wav")
finish = pygame.image.load("finish.png")
finale = pygame.mixer.Sound("finale.wav")
levelup = pygame.image.load("levelup.jpeg")
levelupsound = pygame.mixer.Sound("levelup.wav")
peter = pygame.image.load("peterpan1.png")
peter = pygame.transform.scale(peter,(150,200))
revpeter = pygame.transform.flip(peter,True,False)		#Flips the image as desired
peter1 = peter	
tinker2 = pygame.image.load("tinkerbell2.png") 
revtinker2 = pygame.transform.flip(tinker2,True,False)		#Flips the image as desired
tinker3 = tinker2
fairydust = pygame.mixer.Sound("fairydust.wav")
hook = pygame.image.load("hookandcannon.png")
hookalone = pygame.image.load("hook2.png")
hooklaugh = pygame.mixer.Sound("hooklaugh.wav")
bullet = pygame.image.load("bullet2.png")
bullet = pygame.transform.scale(bullet, (20,20))
cannonexplode = pygame.mixer.Sound("cannonexplode.wav")
baby = pygame.image.load("baby.png")
babybyebye = pygame.mixer.Sound("baby.byebye.wav")
babylaugh = pygame.mixer.Sound("babylaugh.wav")
intro = pygame.image.load("intro.png")
intro1 = pygame.image.load("intro1.jpg")
intro2 = pygame.image.load("intro6.jpg")
intro3 = pygame.image.load("intro5.jpg")
intro4 = pygame.image.load("intro4.jpg")


#_________________________Class Objects_______________________________#

hook = Hook(hook,785,500,1)
hook2 = Hook(hookalone,screen_width-200,0,1) 
bullet = Bullet(bullet,hook.X,hook.Y, 3)
baby = Baby(baby,hook2.X,hook2.Y,200, 1)
peter = Peter(1,3,250,180,1,3)
tinker = Tinkerbell(400,100)
neverland = Background(neverland,0,0)
london = Background(london,0,0)
main = Background(main,0,0)
mainplay = Background(mainplay,0,0)
mainvolume = Background(mainvolume,0,0)
mainmusic = Background(mainmusic,0,0)
mainmusicoff = Background(mainmusicoffpic,0,0)
mainhelp = Background(mainhelp,0,0)
mainexit = Background(mainexit,0,0)
intro = Background(intro,0,0)
intro1 = Background(intro1,0,0)
intro2 = Background(intro2,0,0)
intro3 = Background(intro3,0,0)
intro4 = Background(intro4,0,0)
pause = Background(pause,0,0)
gameover = Background(gameover,0,0)
gameoverrestart = Background(gameoverrestart,0,0)
gameoverskip = Background(gameoverskip,0,0)
gameover3 = Background(gameover3,0,0)
gameover3restart = Background(gameover3restart,0,0)
finish = Background(finish,0,0)
game = Levels("one")
levelup = Background(levelup,0,0)

#_________________Background Music and Fonts____________________#

InfoFont = pygame.font.SysFont("viner hand itc", 20)	## Loads the font
pygame.mixer.music.load("newtheme.wav")			## Loads background music	
pygame.mixer.music.play(-1)				## Infinitly plays the music


#_____________________Global Variables____________________#

levelup1 = False	# To Flag wehter or not Enter has been pressed
levelup2 = False	# Same Here
musicon = True		# To know wether or not to play background music
play = False		# To know wether the user has started pressed play
pause1 = False		# To flag wether user wants to pause or not
gameOver = False	# To Show she gameOver screen once Peter Dies
up = False		# These flags will be used to determine which direction he is going
down = False
left = False
right = False
peterLeft= False	# This is a speacial one, only used to see which direction Peter is facing	
gameOn = True		# And finally, this is to quit the program once user wishes to do so


#---------------------------------------------------------Game Loop---------------------------------------------------------------#

while gameOn:					#Loops until user exits
	
#______________________________________Main Menu________________________________________________#
	
	while play is False:
		for event in pygame.event.get():
			main.draw ()			# Draws the main menu
			
			if event.type == QUIT:
				play = True		# Stops the Game Loop if user exits
				gameOn = False
				break
			
			x,y = pygame.mouse.get_pos()	# Gets the mouse's position
			if (x >=300) and (x <=620) and (y>=182) and (y<=311):		# Depending on where the user is hovering the mouse, it show a highlight of buttons 
				mainplay.draw()						# they can click
			elif (x >=480) and (x <=590) and (y>=330) and (y<=380):
				mainmusic.draw()
			elif (x >=340) and (x <=450) and (y>=320) and (y<=390):
				mainvolume.draw()
			elif (x >=260) and (x <=470) and (y>=390) and (y<=470):
				mainhelp.draw()
			elif (x >=530) and (x <=650) and (y>=390) and (y<=470):
				mainexit.draw()
				
			if event.type == MOUSEBUTTONDOWN:	# Once they actually click an option
				buttonclick.play()
				
				if (x >=300) and (x <=620) and (y>=182) and (y<=311):	# Pressing this button makes the game start
					play = True
					levelup1 = True					# Displays the info screens
					levelup2 = True
				elif (x >=480) and (x <=590) and (y>=330) and (y<=380):
					music()						# Stops or starts the Music
				elif (x >=260) and (x <=470) and (y>=390) and (y<=470):
					levelup1 = True					# Shows the instructions page
				elif (x >=530) and (x <=650) and (y>=390) and (y<=470):
					play = True
					gameOn = False					# Exits the program
					break
				
			elif event.type == KEYDOWN:
				if event.key == K_RETURN:
					levelup1 = False		# Returns to the main menu after displaying the instructions
			if levelup1:					
				intro.draw()				# Shows the instructions page if user clicks the Help button
			pygame.display.flip()		# Displays what we have drawn onto the screen
		
#______________________________________Game Over Screen_______________________________________________#
			
	while gameOver:
		x,y = pygame.mouse.get_pos()		# Gets Mouse Position
		
		if peter.skips == 1: 			# Checks if user has used his 1 skip
			gameover.draw()
			if (x >=130) and (x <=370) and (y>=400) and (y<=515):
				gameoverrestart.draw()				# Highlights the button that the user is hovering over
			elif (x >=500) and (x <=740) and (y>=400) and (y<=520):
				gameoverskip.draw()				# Same Here
		else:
			gameover3.draw()					# Same Here expect if doesn't include the skip button
			if (x >=320) and (x <=560) and (y>=410) and (y<=530):
				gameover3restart.draw()
		highscoredraw()				# Displays the Highest Score 
		pygame.display.flip()			# This is so you can see highlighted button without clicking it
		
		for event in pygame.event.get():
			if event.type == QUIT:		# Quits the game
				gameOver = False
				gameOn = False
				play = False
				break
			
			elif event.type == MOUSEBUTTONDOWN:
				buttonclick.play()
				if peter.skips == 1:
					if (x >=130) and (x <=370) and (y>=400) and (y<=515): # The restart button sends Peter back to level 1 
						gameoverrestart.draw()
						peter.level = 1
						peter.skips = 1
						gameOver = False
						peter.reset()			# Resets Peter's Info like speed, and location
					elif (x >=500) and (x <=740) and (y>=400) and (y<=520): # The skip button alows Peter to redew a level
						gameoverskip.draw()
						peter.skips = 0			# Peter's score will also rest
						gameOver = False
						peter.health = 1
						peter.reset()			# Along with his coordinates
				else:					
					if (x >=320) and (x <=560) and (y>=410) and (y<=530): # Same thing as before, just doens't provide a skip option
						gameover3restart.draw()
						peter.level = 1
						peter.skips = 1
						gameOver = False
						peter.reset()
					else:
						gameover3.draw()
				
			elif event.type == KEYDOWN:		# This is to alow the user to return to the main menu if enter is clicked
				if event.key == K_RETURN:
					gameOver = False
					play = False
					peter.reset()
					peter.level = 1
			levelup1 = False	# Doesn't show the instructional pages any more
			levelup2 = False		
			highscoredraw()		# Writes the High Score
			pygame.display.flip()	# Shows everything we have drawn
	
	if gameOn is False:	# These 4 lines are to overcome the computer's urge to go through the next part of the code, even if the user Exited the Game
		play = False
	if play is False:	# So There isn't a single frame of gameplay after the user exits the program
		continue
	
	
#___________________________________________Actual Game__________________________________________________________#	
	
	for event in pygame.event.get():		# goes through every possible input
		if event.type == QUIT: 
			gameOn = False			# stops the game when user quit
		
		elif event.type == KEYDOWN:		# does the following when a key is pressed
			if event.key == K_SPACE:        # if user presses space bar, they will level up
				peter.levelup()
			elif event.key == K_RETURN:	# here, is where the user can press enter to move through instructional pages
				if pause1:		
					play = False
				levelup1 = False
				if levelup2:
					levelup2 = False
				else:							
					levelup2 = True					
			elif event.key == K_ESCAPE:	# clicking Escape will exit the game
				gameOn = False
			elif event.key == K_p:		# Pressing P will activate the Pause Menu
				if pause1:
					levelup1 = False
					pause1 = False
				else:
					pause1 = True
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
				
	
	peter.procedure()		# Calls for the Procedure (the function that leads to all other functions)
	clock.tick(60)			# Making the clock tick for 60 miliseconds inbetween frames, allows the speed of the program to be the same no matter the computer
	
	pygame.display.flip()		# Displays the images
	
pygame.quit()		#Quits Pygame





##-----------------------------------------------------------------The End-------------------------------------------------------------------------------#