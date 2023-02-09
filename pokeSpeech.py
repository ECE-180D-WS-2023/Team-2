import speech_recognition as sr
import json

### BST ###
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def insert(root, key):
	if root is None:
		return Node(key)
	else:
		if root.val == key:
			return root
		elif root.val > key:
			root.left = insert(root.left, key)
		else:
			root.right = insert(root.right, key)
	return root
###########

### print BST ###
def printBST(root):
	if root:
		printBST(root.left)
		print(root.val)
		printBST(root.right)
#################

### returns true if in BST ###
def check(root, key):
	if root is None or root.val == key:
		return root

	elif root.val > key:
		return check(root.left, key)

	return check(root.right, key)
##################

### returns the move ###
def search(root, key):
	if root is None or root.val == key:
		return root.val

	elif root.val > key:
		return search(root.left, key)

	return search(root.right, key)
########################

x = open('moves.json')
moves = json.load(x)

root = Node(moves['pokemon_moves'][0]['identifier'])

for entry in moves['pokemon_moves'][1:]:
	root = insert(root, entry['identifier'])

#printBST(root)

input_device_index = 1

r = sr.Recognizer()
r.energy_threshold = 4000
r.dynamic_energy_threshold = True
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	print("Waiting for player command")
	audio = r.listen(source)

if (check(root, r.recognize_google(audio))):
	print("__ used " + str(search(root, r.recognize_google(audio))) + "!")
else:
	print("Unknown command!")