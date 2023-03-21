'''
	listen for pokemon name and 'use'
	store the rest of the input as a string
	compare that string to the moves that pokemon knows
'''
import speech_recognition as sr
import json
from operator import itemgetter


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


### util ###
# This function traverse the skewed binary tree and
# stores its nodes pointers in vector nodes[]
def storeBSTNodes(root,nodes):
	if not root:
		return

	storeBSTNodes(root.left,nodes)
	nodes.append(root)
	storeBSTNodes(root.right,nodes)
 
# Recursive function to construct binary tree
def buildTreeUtil(nodes,start,end):
	if start>end:
		return None
 
	mid=(start+end)//2
	node=nodes[mid]

	node.left=buildTreeUtil(nodes,start,mid-1)
	node.right=buildTreeUtil(nodes,mid+1,end)
	return node
#############


### Turn BST into Balanced BST ###
def buildTree(root):
     
	# Store nodes of given BST in sorted order
	nodes=[]
	storeBSTNodes(root,nodes)
 
	# Constructs BST from nodes[]
	n=len(nodes)
	return buildTreeUtil(nodes,0,n-1)
###################################


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
		return root.val.capitalize()

	elif root.val > key:
		return search(root.left, key).capitalize()

	return search(root.right, key).capitalize()
########################

### BST node into array

def multi(move):
	if (len(move.split()) > 1):		# if string has multiple words (ie moves like 'karate chop' or 'never ending nightmare')
		return move.split()
####


### pokemon name BST ###
x = open('all_pokemon.json', encoding="utf-8")
names = json.load(x)

name_first = names['pokemon_info'][0]['Name'].upper()
name_root = Node(name_first)

for entry in names['pokemon_info'][1:]:
	name_root = insert(name_root, entry['Name'].upper())

# balance for O(log n)
name_root = buildTree(name_root)
#########################


### pokemon move BST ###
y = open('moves.json', encoding="utf-8")
moves = json.load(y)

move_first = moves['pokemon_moves'][0]['identifier'].upper()
move_root = Node(move_first)

for entry in moves['pokemon_moves'][1:]:
	move_root = insert(move_root, entry['identifier'].upper())

# balance for O(log n)
move_root = buildTree(move_root)
#########################

#printBST(name_root)
#printBST(move_root)

input_device_index = 1

r = sr.Recognizer()
r.dynamic_energy_threshold = False
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source, duration = 1)
	if r.energy_threshold < 200:
		r.energy_threshold = 200
	print("Waiting for player command")
	audio = r.listen(source, timeout = 5.0, phrase_time_limit = 5.0)

output = r.recognize_google(audio, language = "en-US", show_all = True)
print(output)
### output is a JSON ###

### skip if nothing is heard ###
if (output != []):

	index = 0
	NAME_FOUND = False
	COMMAND_FOUND = False
	MOVE_FOUND = False
	COMPLETE_COMMAND = False

	full_move = ["", "", ""]

	### Find which object has the command that's in the tree ###
	for i in output['alternative']:
		print(i['transcript'])

		# turn transcript result into an array with each element being one word
		transcript = i['transcript'].split()

		for j in range(len(transcript)):
			#print(transcript[j])

			if (check(name_root, transcript[j].upper())):
				print("name found")
				NAME_FOUND = True
				NAME_INDEX = j
				full_move[0] = transcript[j].title()
				pass
			elif (transcript[j] == 'use'):
				print("command found")
				COMMAND_FOUND = True
				COMMAND_INDEX = j
				full_move[1] = 'used'
				pass
			elif (check(move_root, transcript[j].upper())):
				MOVE_FOUND = True
				MOVE_INDEX = j
				full_move[2] = search(move_root, transcript[j].upper())
				break

		if ((NAME_FOUND and COMMAND_FOUND and MOVE_FOUND == True) and NAME_INDEX < COMMAND_INDEX < MOVE_INDEX):
			COMPLETE_COMMAND = True
			break
		else:
			index = index + 1

	#print(index)
	#print(result)
	if (COMPLETE_COMMAND == True):
		print(full_move[0] + " " + full_move[1] + " " + full_move[2] + "!")
		### do the game stuff here ###
	elif (sr.UnknownValueError):
		print("Unknown command!")
	elif (sr.RequestError):
		print("Command failed!")
	else:
		print("Unknown command!")

else:
	print("No Input Detected")