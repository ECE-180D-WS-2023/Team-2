'''
	listen for pokemon name and 'use'
	store the rest of the input as a string
	compare that string to the moves that pokemon knows
'''
import speech_recognition as sr
import json
from operator import itemgetter
import re


x = open('pokemon/pokemon_moves.json', encoding="utf-8")
moves = json.load(x)

#move_first = moves['pokemon_moves'][0]['identifier'].lower()

#for entry in moves['pokemon_moves'][1:]:
#	move_root = insert(move_root, entry['identifier'].upper())


def speechInput(move):

	input_device_index = 1

	r = sr.Recognizer()
	r.energy_threshold = 500
	r.dynamic_energy_threshold = False
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source, duration = 1.0)
		print("Waiting for player command")
		audio = r.listen(source, phrase_time_limit = 8.0)

	output = r.recognize_google(audio, language = "en-US", show_all = True)
	print(output)
	### output is a JSON ###

	### skip if nothing is heard ###
	if (output != []):

		#MOVE_FOUND = False
		#full_move = ["", "", ""]

		### Compare learned moves with transcript ###
		for i in moves['pokemon_moves']:
			checkMove = i['identifier'].lower()
			print('move: ' + checkMove)

			for j in output['alternative']:
				transcript = j['transcript'].lower()
				print('checking: ' + transcript)
				##maybe remove whitespace as well##

				if (re.search(re.escape(checkMove), transcript)):
					if (re.search(re.escape(checkMove), transcript).group() == checkMove):
						print ("mwahaha FOUND")
						#MOVE_FOUND= True
						print (checkMove)
						return checkMove
					else:
						continue
				else:
					continue

		#if (MOVE_FOUND == True):
			#print(full_move[2])
			### do the game stuff here ###
			#return
		if (sr.UnknownValueError):
			print("Unknown command!")
			speechInput(move)
		elif (sr.RequestError):
			print("Command failed!")
		else:
			print("Unknown command!")

	else:
		print("No input")
		speechInput(move)