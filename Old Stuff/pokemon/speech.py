import speech_recognition as sr
import json
from operator import itemgetter
import re

def speechInput(name, move):

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

		### Compare learned moves with transcript ###
		for i in range(len(move)):
			checkMove = move[i].lower()
			print('move: ' + checkMove)

			for j in output['alternative']:
				transcript = j['transcript'].lower()
				print('checking: ' + transcript)

				### if pokemon name, 'use', and pokemon move are said, valid ###
				if (re.search(re.escape(name.lower()), transcript)):
					# if exceptions ('we don't', transcript) (weedle)

					if (re.search(re.escape(name.lower()), transcript).group() == name.lower()):
						# if exceptions

						print("pokemon called")
						if (re.search('use', transcript)):
							if (re.search('use', transcript).group() == 'use'):
								if (re.search(re.escape(checkMove), transcript)):
									if (re.search(re.escape(checkMove), transcript).group() == checkMove):
										print ("move found")
										#print (checkMove)
										return checkMove
									else:
										continue
								else:
									continue
							else:
								continue
						else:
							continue
					else:
						continue
				else:
					continue

		if (sr.UnknownValueError):
			print("Unknown command! Try again.")
			speechInput(name, move)
		elif (sr.RequestError):
			print("Command failed!")
		else:
			print("Unknown command! Try again.")

	else:
		print("No input")
		speechInput(name, move)