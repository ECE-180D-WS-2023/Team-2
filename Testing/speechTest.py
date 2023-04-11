import sys
import os
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import pokemon.speech as speech
import random as rand
import time

names = [
	"Bulbasaur", 
	"Charmander", 
	"Squirtle", 
	"Caterpie", 
	"Weedle", 
	"Pidgey", 
	"Rattata", 
	"Spearow", 
	"Ekans", 
	"Pikachu", 
	"Sandshrew"
]

moves = [
	"Tackle", 
	"Growl", 
	"Vine Whip", 
	"Razor Leaf", 
	"Scratch", 
	"Ember", 
	"Dragon Breath", 
	"Water Gun", 
	"Bite", 
	"String Shot", 
	"Bug Bite", 
	"Poison Sting", 
	"Gust", 
	"Sand Attack", 
	"Quick Attack", 
	"Tail Whip", 
	"Peck", 
	"Assurance", 
	"Aerial Ace", 
	"Leer", 
	"Acid", 
	"Nuzzle", 
	"Thunder Shock", 
	"Electro Ball", 
	"Defense Curl", 
	"Fury Cutter"
]

# choose random pokemon and move name
try:
	while True:
		n_int = rand.randint(0, 10)
		m_int = rand.randint(0, 25)
		p_int = rand.randint(0, 3)

		p_name = names[n_int]
		p_move = []

		for i in range(0,4):
			p_move.append(moves[rand.randint(0, 25)])

		print('Say:\n"' + p_name + ' use ' + p_move[p_int] + '"\n')
		speech.speechInput(p_name, p_move)

		time.sleep(1)
		print("Done testing? Ctrl/Cmd + s to save to txt file!")
		time.sleep(1)
except KeyboardInterrupt:
	pass