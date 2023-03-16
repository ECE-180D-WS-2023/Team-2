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



### pokemon move BST ###
y = open('pokemon/moves.json', encoding="utf-8")
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

def speechInput(move):

	input_device_index = 1

	r = sr.Recognizer()
	r.energy_threshold = 500
	r.dynamic_energy_threshold = False
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source, duration = 1)
		print("Waiting for player command")
		audio = r.listen(source, timeout = 8.0, phrase_time_limit = 8.0)

	try:
		output = r.recognize_google(audio, language = "en-US", show_all = True)
		print(output)
		### output is a JSON ###

		### skip if nothing is heard ###
		if (output != []):

			index = 0
			MOVE_FOUND = False

			full_move = ["", "", ""]

			### Find which object has the command that's in the tree ###
			for i in output['alternative']:

				# turn transcript result into an array with each element being one word
				transcript = i['transcript'].split()

				for j in range(len(transcript)):

					if (check(move_root, transcript[j].upper())):
						MOVE_FOUND = True
						full_move[2] = search(move_root, transcript[j].upper())
						break

					### two word exceptions (a lot) ###
					### add MOVE_INDEX = j to the rest as well ###
					elif (j < len(transcript)):
						try:
							if (transcript[j].upper() == "KARATE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CHOP"):
										MOVE_FOUND = True
										MOVE_INDEX = j
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:	
							if (transcript[j].upper() == "DOUBLE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SLAP"):
										MOVE_FOUND = True
										MOVE_INDEX = j
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "COMET"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PUNCH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MEGA"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PUNCH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "PAY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DAY"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FIRE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PUNCH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ICE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PUNCH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "THUNDER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PUNCH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "VICE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "GRIP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "RAZOR"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "WIND"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SWORDS"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DANCE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "WING"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ATTACK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "VINE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "WHIP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DOUBLE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "KICK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MEGA"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "KICK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break
						
						try:
							if (transcript[j].upper() == "HIGH"):
								if (transcript[j + 1].upper() == "JUMP"):
									if (transcript[j + 2].upper() == "KICK"):
										MOVE_FOUND = True
										full_move[2] = "High Jump Kick"
										break
						except IndexError:
							break

						try:
							if (transcript[j].upper() == "JUMP"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "KICK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ROLLING"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "KICK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SAND"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ATTACK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HORN"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ATTACK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FURY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ATTACK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HORN"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DRILL"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "BODY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SLAM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "TAKE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DOWN"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DOUBLE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "EDGE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "TAIL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "WHIP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "POISON"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "STING"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "TWIN"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "NEEDLE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "PIN"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "NEEDLE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SONIC"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BOOM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "WATER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "GUN"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HYDRO"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PUMP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ICE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BEAM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "BUBBLE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BEAM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "AURORA"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BEAM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DOUBLE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SLAP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HYPER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BEAM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DRILL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PECK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "LOW"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "KICK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SEISMIC"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "TOSS"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MEGA"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DRAIN"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "LEECH"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SEED"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "RAZOR"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "LEAF"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SOLAR"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BEAM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "POISON"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "POWDER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "STUN"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SPORE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SLEEP"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "POWDER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "PETAL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DANCE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "STRING"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SHOT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DRAGON"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "RAGE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FIRE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SPIN"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "THUNDER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SHOCK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "THUNDER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "WAVE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ROCK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "THROW"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "QUICK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ATTACK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "NIGHT"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SHADE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DOUBLE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "TEAM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "CONFUSE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "RAY"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DEFENSE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CURL"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "LIGHT"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SCREEN"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FOCUS"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ENERGY"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MIRROR"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "MOVE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SELF"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DESTRUCT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "EGG"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BOMB"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "BONE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CLUB"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FIRE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BLAST"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SKULL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BASH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SPIKE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CANNON"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SOFT"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BOILED"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DREAM"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "EATER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "POISON"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "GAS"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "LEECH"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "LIFE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "LOVELY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "KISS"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SKY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ATTACK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DIZZY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PUNCH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ACID"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ARMOR"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FURY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SWIPES"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ROCK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SLIDE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HYPER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "FANG"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "TRI"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ATTACK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SUPER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "FANG"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "TRIPLE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "KICK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SPIDER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "WEB"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MIND"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "READER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FLAME"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "WHEEL"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "CONVERSION"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "2"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "COTTON"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SPORE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "POWDER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SNOW"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MACH"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PUNCH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SCARY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "FACE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FEINT"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ATTACK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SWEET"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "KISS"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "BELLY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DRUM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SLUDGE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BOMB"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MUD"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SLAP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ZAP"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CANNON"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DESTINY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BOND"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "PERISH"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SONG"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ICY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "WIND"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "BONE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "RUSH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "LOCK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ON"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "GIGA"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DRAIN"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FALSE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SWIPE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MILK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DRINK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FURY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CUTTER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "STEEL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "WING"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MEAN"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "LOOK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SLEEP"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "TALK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HEAL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BELL"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "PAIN"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SPLIT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SACRED"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "FIRE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DYNAMIC"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PUNCH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DRAGON"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BREATH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "BATON"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PASS"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "RAPID"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SPIN"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SWEET"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SCENT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "IRON"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "TAIL"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "METAL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CLAW"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "VITAL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "THROW"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MORNING"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SUN"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HIDDEN"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "POWER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "CROSS"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SHOP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "RAIN"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DANCE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SUNNY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DAY"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MIRROR"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "COAT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "PSYCH"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "UP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "EXTREME"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SPEED"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ANCIENT"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "POWER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SHADOW"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BALL"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FUTURE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SIGHT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ROCK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SMASH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "BEAT"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "UP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FAKE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "OUT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SPIT"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "UP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HEAT"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "WAVE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						## pronunciation lol (can be confused for wish and willow) ##
						try:
							if (transcript[j].upper() == "WILLOW"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "WISP"):
										MOVE_FOUND = True
										full_move[2] = "Will-O-Wisp"
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FOCUS"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PUNCH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SMELLING"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SALTS"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FOLLOW"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ME"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "NATURE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "POWER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HELPING"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "HAND"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ROLE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PLAY"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MAGIC"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "COAT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "BRICK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BREAK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "KNOCK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "OFF"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SKILL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SWAP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SECRET"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "POWER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "LEECH"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "LIFE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ARM"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "THRUST"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "TAIL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "GLOW"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MIST"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BALL"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FEATHER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DANCE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "TEETER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DANCE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "BLAZE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "KICK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MUD"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SPORT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ICE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BALL"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "NEEDLE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ARM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SLACK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "OFF"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HYPER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "VOICE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "POISON"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "FANG"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "CRUSH"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CLAW"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "BLAST"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BURN"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HYDRO"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CANNON"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "METEOR"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "MASH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "WEATHER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BALL"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FAKE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "TEARS"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "AIR"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CUTTER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ODOR"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SLEUTH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ROCK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "TOMB"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SILVER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "WIND"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "METAL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SOUND"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "GRASS"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "WHISTLE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "COSMIC"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "POWER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "WATER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SPOUT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SIGNAL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BEAM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SHADOW"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PUNCH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SKY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "UPPERCUT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SAND"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "TOMB"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SHEER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "COLD"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MUDDY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "WATER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "BULLET"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SEED"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "AERIAL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ACE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ICICLE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SPEAR"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "IRON"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DEFENSE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DRAGON"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CLAW"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FRENZY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PLANT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "BULK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "UP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MUD"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SHOT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "POISON"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "TAIL"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "VOLT"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "TACKLE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MAGICAL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "LEAF"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "WATER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SPORT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "CALM"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "MIND"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "LEAF"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BLADE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DRAGON"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DANCE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ROCK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BLAST"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SHOCK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "WAVE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "WATER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PULSE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DOOM"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DESIRE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "PSYCHO"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BOOST"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MIRACLE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "EYE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "WAKE"):
								if (transcript[j + 1].upper() == "UP"):
									if (transcript[j + 2].upper() == "SLAP"):
										MOVE_FOUND = True
										full_move[2] = "Wake Up Slap"
										break
						except IndexError:
							break

						try:
							if (transcript[j].upper() == "HAMMER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ARM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "GYRO"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BALL"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HEALING"):
								if (transcript[j + 1].upper() == "WISH"):
									MOVE_FOUND = True
									full_move[2] = "Healing Wish"
									break
						except IndexError:
							break

						try:
							if (transcript[j].upper() == "NATURAL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "GIFT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "METAL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BURST"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "U"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "TURN"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "CLOSE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "COMBAT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "PSYCHO"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SHIFT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "TRUMP"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CARD"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HEAL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BLOCK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "WRING"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "OUT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "POWER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "TRICK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "GASTRO"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ACID"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "LUCKY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CHANT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ME"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "FIRST"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "POWER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SWAP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "GUARD"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SWAP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "LAST"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "RESORT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "WORRY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SEED"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SUCKER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PUNCH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "TOXIC"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SPIKES"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HEART"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SWAP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "AQUA"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "RING"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MAGNET"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "RISE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FLARE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BLITZ"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FORCE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PALM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "AURA"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SPHERE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "WAKE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "LIFE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ROCK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "POLISH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "POISON"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "JAB"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DARK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PULSE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "NIGHT"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SLASH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "AQUA"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "TAIL"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SEED"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BOMB"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "AIR"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SLASH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "X"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SCISSOR"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "BUG"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BUZZ"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DRAGON"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PULSE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DRAGON"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "RUSH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "POWER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "GEM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DRAIN"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PUNCH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "VACUUM"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "WAVE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FOCUS"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BLAST"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ENERGY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BALL"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "BRAVE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BIRD"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "EARTH"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "POWER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "GIGA"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "IMPACT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "NASTY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PLOT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "BULLET"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PUNCH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ICE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SHARD"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SHADOW"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CLAW"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "THUNDER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "FANG"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ICE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "FANG"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FIRE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "FANG"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SHADOW"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SNEAK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MUD"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BOMB"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "PYSCHO"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CUT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ZEN"):
								if (transcript[j + 1].upper() == "HEADBUTT"):
									MOVE_FOUND = True
									full_move[2] = "Zen Headbutt"
									break
						except IndexError:
							break

						try:
							if (transcript[j].upper() == "MIRROR"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SHOT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FLASH"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CANNON"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ROCK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CLIMB"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "TRICK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ROOM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DRACO"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "METEOR"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "LAVA"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PLUME"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "LEAF"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "STORM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "POWER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "WHIP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ROCK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "WRECKER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "CROSS"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "POISON"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "GUNK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SHOT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "IRON"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "HEAD"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MAGNET"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BOMB"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "STEALTH"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ROCK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "GRASS"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "KNOT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "BUG"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BITE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "CHARGE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BEAM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "WOOD"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "HAMMER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "AQUA"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "JET"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ATTACK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ORDER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DEFEND"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ORDER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HEAL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ORDER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HEAD"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SMASH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DOUBLE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "HIT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ROAR"):
								if (transcript[j + 1].upper() == "OF"):
									if (transcript[j + 2].upper() == "TIME"):
										MOVE_FOUND = True
										full_move[2] = "Roar of Time"
										break
						except IndexError:
							break

						try:
							if (transcript[j].upper() == "SPACIAL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "REND"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "LUNAR"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DANCE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "CRUSH"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "GRIP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MAGMA"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "STORM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DARK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "VOID"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SEED"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "FLARE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "OMNIOUS"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "WIND"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SHADOW"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "FORCE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HONE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CLAWS"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "WIDE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "GUARD"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "GUARD"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SPLIT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "POWER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SPLIT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "WONDER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ROOM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "RAGE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "POWDER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MAGIC"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ROOM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SMACK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DOWN"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "STORM"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "THROW"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FLAME"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BURST"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SLUDGE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "WAVE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "QUIVER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DANCE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HEAVY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SLAM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ELECTRO"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BALL"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FLAME"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CHARGE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "LOW"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SWEEP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ACID"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SPRAY"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FOUL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PLAY"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SIMPLE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BEAM"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "AFTER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "YOU"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ECHOED"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "VOICE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "CHIP"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "AWAY"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "CLEAR"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SMOG"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "STORED"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "POWER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "QUICK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "GUARD"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ALLY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SWITCH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SHELL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SMASH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HEAL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PULSE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SKY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DROP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SHIFT"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "GEAR"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "CIRCLE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "THROW"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "REFLECT"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "TYPE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FINAL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "GAMBIT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "WATER"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PLEDGE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FIRE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PLEDGE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "GRASS"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PLEDGE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "VOLT"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SWITCH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "STRUGGLE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BUG"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FROST"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BREATH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DRAGON"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "TAIL"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "WORK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "UP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "WILD"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CHARGE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DRILL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "RUN"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "DUAL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CHOP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HEART"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "STAMP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HORN"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "LEECH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SACRED"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SWORD"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "RAZOR"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SHELL"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HEAT"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CRASH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "LEAF"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "TORNADO"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "COTTON"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "GUARD"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "NIGHT"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DAZE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "TAIL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SLAP"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "HEAD"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CHARGE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "GEAR"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "GRIND"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SEARING"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SHOT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "TECHNO"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BLAST"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "RELIC"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SONG"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "SECRET"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SWORD"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "BOLT"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "STRIKE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "BLUE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "FLARE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FIERY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DANCE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FREEZE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "SHOCK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ICE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BURN"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ICICLE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CRASH"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "V"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CREATE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FUSION"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "FLARE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FUSION"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BOLT"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FLYING"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "PRESS"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "MAT"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "BLOCK"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "STICKY"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "WEB"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "FELL"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "STINGER"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "PHANTOM"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "FORCE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						'''
						try:
							if (transcript[j].upper() == "TRICK"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "OR"):
										for m in range(1, len(transcript) - k):
											if (transcript[j + m].upper() == "TREAT"):
												MOVE_FOUND = True
												full_move[2] = " ".join(itemgetter(j, j + k, j + m)(transcript)).title()
												break
											break
						except IndexError:	# exit if out of bounds
							break
						'''


						try:
							if (transcript[j].upper() == "NOBLE"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "ROAR"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "ION"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "DELUGE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

						try:
							if (transcript[j].upper() == "PARABOLIC"):
								for k in range(1, len(transcript) - j):
									if (transcript[j + k].upper() == "CHARGE"):
										MOVE_FOUND = True
										full_move[2] = " ".join(itemgetter(j, j + k)(transcript)).title()
										break
									
						except IndexError:	# exit if out of bounds
							break

							#### ADD LIKE 400 MORE AAAAAAHHH!!!!! ###

			for i in range(len(move)):
				if (full_move[2].lower() == move[i]):
					return full_move[2].lower()
			
			if (MOVE_FOUND == True):
				print(full_move[2])
				### do the game stuff here ###

		else:
			return "No input"

	except (sr.UnknownValueError):
		print("Unknown command!")
	except (sr.RequestError):
		print("Command failed!")
	except (WaitTimeoutError):
		print('Timed out!')
	except:
		print("Unknown command!")