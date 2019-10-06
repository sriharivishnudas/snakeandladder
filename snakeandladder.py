import random
import math

class Person():
	def __init__(self,name):
		self.name = name
		self.score = 1
		self.switch = True
		self.counter = 0
		
	def dice():
		dice =  math.floor((random.uniform(0,1) * 6) + 1)
		return dice
	
	def roll(self):
		self.counter = self.counter + 1
		print('The score before rolling is ' + str(self.score))
		roll_value = Person.dice()
		print('The dice has rolled ' + str(roll_value))
		if ((self.score + roll_value) <= 30):
			self.score = self.score + roll_value
			snake(self)
			ladder(self)
			print('The score after rolling is ' + str(self.score))
		else:
			print('Need accurate roll to finish')
			print('The score is still ' + str(self.score))	 
		if self.score == 30:
			print('Congo!! You win,you took ' + str(self.counter) + ' turns')
			self.switch = False
		

def snake(Person):
		if Person.score == 27:
			print('Snaked')
			Person.score = 1
		elif Person.score == 21:
			print('Snaked')
			Person.score = 9
		elif Person.score == 19:
			print('Snaked')
			Person.score = 7
		elif Person.score == 17:
			print('Snaked')
			Person.score = 4
	
def ladder(Person):
		if Person.score == 5:
			print('Laddered')
			Person.score = 8
		elif Person.score == 3:
			print('Laddered')
			Person.score = 22
		elif Person.score == 11:
			print('Laddered')
			Person.score = 26
		elif Person.score == 20:
			print('Laddered')
			Person.score = 29

player = input('Enter the name of player : ')
player_1 = Person(player)

while player_1.switch:
	print('1. Start')
	print('2. Roll')
	print('3. Exit')
	choice = input('Enter your choice (1 or 2 or 3)')
	if choice == '1':
		print('The game has begun !')
		print(player_1.name + ' score is ' + str(player_1.score))
		print('Reach score 30 to win')
		print('\n')
	elif choice == '2':
		player_1.roll()
		if player_1.switch == False:
			break
		print('\n')
	elif choice == '3':
		break
