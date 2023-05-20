import speech_recognition as sr
import json
from operator import itemgetter
import re


def menuSpeech():

	input_device_index = 1

	r = sr.Recognizer()
	r.energy_threshold = 500
	r.dynamic_energy_threshold = False
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source, duration = 1.0)
		print("Waiting for player command")
		audio = r.listen(source, phrase_time_limit = 6.0)

	output = r.recognize_google(audio, language = "en-US", show_all = True)
	print(output)

	if (output != []):
		for i in output["alternative"]:
			transcript = i["transcript"].lower()

			if (re.search("fight", transcript)):
				return "fight"
			elif (re.search("bag", transcript)):
				return "bag"
			else:
				continue

		if (sr.UnknownValueError):
			print("Unknown command! Try again.")
			menuSpeech()
		elif (sr.RequestError):
			print("Command failed!")
		else:
			print("Unknown command! Try again.")

	else:
		print("No input")
		menuSpeech()


def moveSpeech(name, move):

	input_device_index = 1

	r = sr.Recognizer()
	r.energy_threshold = 500
	r.dynamic_energy_threshold = False
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source, duration = 1.0)
		print("Waiting for player command")
		audio = r.listen(source, phrase_time_limit = 6.0)

	output = r.recognize_google(audio, language = "en-US", show_all = True)
	print(output)
	### output is a JSON ###

	### skip if nothing is heard ###
	if (output != []):

		### Compare current move with transcript ###
		checkMove = move.lower()
		print("move: " + checkMove)

		for i in output["alternative"]:
			transcript = i["transcript"].lower()
			print("checking: " + transcript)

			### exit ###
			if (re.search("cancel", transcript)):
				return "back"
			elif (re.search("back", transcript)):
				return "back"
			elif (re.search("exit", transcript)):
				return "back"

			### if pokemon name, "use", and pokemon move are said, valid ###
			elif (re.search(re.escape(name.lower()), transcript)):
				# if exceptions ("we don't", transcript) (weedle)

				if (re.search(re.escape(name.lower()), transcript).group() == name.lower()):
					# if exceptions
					print("pokemon called")
					if (re.search("use", transcript)):
						if (re.search("use", transcript).group() == "use"):
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
			moveSpeech(name, move)
		elif (sr.RequestError):
			print("Command failed!")
		else:
			print("Unknown command! Try again.")

	else:
		print("No input")
		moveSpeech(name, move)

#print(menuSpeech())