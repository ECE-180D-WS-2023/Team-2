# from pathlib import Path
# import sys
# path_root = Path(__file__).parents[1]
# sys.path.append(str(path_root))
# print(path_root)
# print(sys.path)

############################################################# imports #########################################################
# for esp communication
import paho.mqtt.client as mqtt
import numpy as np
import os
import time

# for game engine
import pokemon
import pokemon.battle

# for computer eyes 
import mediapipe as mp
import cv2

# for speech recognition
import pokemon.speech as speech

os.chdir('C:/Users/Ming Guo 69/Desktop/180DA-WarmUp/gesture_data_2')

#################################################################### mqtt stuff #################################################
# decalre global functions 
recog = 0

# 0. define callbacks - functions that run when events happen.
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))

  # Subscribing in on_connect() means that if we lose the connection and
  # reconnect then subscriptions will be renewed.
    client.subscribe("meme/main", qos=1)
    client.subscribe("meme/recog", qos = 1)

# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Unexpected Disconnect')
    else:
        print('Expected Disconnect')

# The default message callback.
# (you can create separate callbacks per subscribed topic)
def on_message(client, userdata, message):
    global start 
    global recog 
    if message.topic == 'meme/main': 
        start = message.payload
    if message.topic == 'meme/recog':
        recog = int(message.payload)
        print("REceived")
    else:
        pass

    #print('Received message: "' + str(message.payload) + '" on topic "' +
    #   message.topic + '" with QoS ' + str(message.qos))


# function for exporting somthing 
def export(array, name):
    array_np = np.array(array)
    array_np = np.reshape(array_np, (-1, 150))
    np.savetxt(name, 
               array_np,
               delimiter =", ", 
               fmt ='% s')

# 1. create a client instance.
cli_name = "ash_ketucm"
client = mqtt.Client(cli_name)
# add additional client options (security, certifications, etc.)
# many default options should be good to start off.
# add callbacks to client.
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

# 2. connect to a broker using one of the connect*() functions.
# client.connect_async("test.mosquitto.org")
client.connect_async('mqtt.eclipseprojects.io')
# client.connect("test.mosquitto.org", 1883, 60)
# client.connect("mqtt.eclipse.org")

# 3. call one of the loop*() functions to maintain network traffic flow with the broker.
client.loop_start()
# client.loop_forever()

#################################################### mediapipe stuff##################################################################

#shoelace formula to calculate area of body
#https://stackoverflow.com/questions/41077185/fastest-way-to-shoelace-formula
#polygonBoundary = ((5, 0), (6, 4), (4, 5), (1, 5), (1, 0))
def shoelace_formula(polygonBoundary, absoluteValue = True):
    nbCoordinates = len(polygonBoundary)
    nbSegment = nbCoordinates - 1

    l = [(polygonBoundary[i+1][0] - polygonBoundary[i][0]) * (polygonBoundary[i+1][1] + polygonBoundary[i][1]) for i in range(nbSegment)]

    if absoluteValue:
        return abs(sum(l) / 2.)
    else:
        return sum(l) / 2.

# initiate mediapipe 
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode = True, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# vars for cv2.putText
# font
font = cv2.FONT_HERSHEY_SIMPLEX
# org
org = (50, 50)
# fontScale
fontScale = 1
# Blue color in BGR
color = (255, 0, 0)
# Line thickness of 2 px
thickness = 2

# start the camera 
cap = cv2.VideoCapture(0)

game = True

################################################################# game ##############################################################

while (game == True):
    
    # for mediapipe
    # Take each frame
    _, frame = cap.read()
    
    
    # 2. player body is big enough from the camera 
    # Convert BGR to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # make 2 copys
    img1 = rgb.copy()
    img2 = rgb.copy()
    # process images with mediapipe
    result = pose.process(img1)
    
    try:
        # get all 4 points
        l_shol = [result.pose_landmarks.landmark[11].x, result.pose_landmarks.landmark[11].y]
        r_shol = [result.pose_landmarks.landmark[12].x, result.pose_landmarks.landmark[12].y]
        l_hip = [result.pose_landmarks.landmark[23].x, result.pose_landmarks.landmark[23].y]
        r_hip = [result.pose_landmarks.landmark[24].x, result.pose_landmarks.landmark[24].y]
        dot_list = [l_shol, r_shol, l_hip, r_hip]
 
    
        # unnormalize the points
        for coord in dot_list:
            coord[0] = round(coord[0]*img2.shape[1])
            coord[1] = round(coord[1]*img2.shape[0])
        # graph it 
        for coord in dot_list:
            cv2.circle(img2,tuple(coord),radius=5, color=(0, 0, 255), thickness=-1)
            
        # calculate the size of the body, img
        body_size = shoelace_formula(dot_list)
        img_size = img2.shape[0]*img2.shape[1]
        
        img2 = cv2.putText(img2, str(body_size), (50,200), font, 
           0.5, color, thickness, cv2.LINE_AA)
    
        
        # compare above 2
        if(body_size > 0.2*img_size):
            
            img2 = cv2.putText(img2, "bigg!", (50,100), font, 
                   0.5, color, thickness, cv2.LINE_AA)
            print("bigg")
                
        else:
            img2 = cv2.putText(img2, "smaaaawwll!", (50,100), font, 
                   0.5, color, thickness, cv2.LINE_AA)
            print("small")
            
            
        


    except:
        img2 = cv2.putText(img2, "none", (50,200), font, 
           0.5, (0,255,0), thickness, cv2.LINE_AA)
    
    #paint it the 
    cv2.imshow('frame_cv2',img2)
    
    
    # only start if 
    # 1. mqtt regsiters forward 
    print("what you doin ASH, KETCHUM???")
    print(recog)
    if(recog == 1):
        print("SUmmonning my MiniON!!!!")
        print(recog)
        time.sleep(2) # Sleep for 3 seconds
        

    

    if(recog == 1):
        #cap.release()
        cv2.destroyAllWindows()
        
        ################################ game logic ##########################################################################
        red_moves = ['tackle', 'hyper beam', 'hydro pump', 'leech life']
        blue_moves = ['hydro pump', 'tackle', 'cut', 'surf']

        if __name__ == '__main__':
            red_team = pokemon.battle.Team([
                pokemon.Pokemon(pokemon.find_species('rattata'), level=9, moves=[
                    pokemon.find_move(move) for move in red_moves])])
            blue_team = pokemon.battle.Team([
                pokemon.Pokemon(pokemon.find_species('gengar'), level=10, moves=[
                    pokemon.find_move(move) for move in blue_moves])])
            teams = (red_team, blue_team)
            whichteam = []

            while not any(team.blacked_out() for team in teams):
                for team in teams:
                    print(f'{team.fighter.name} has {team.fighter.hp} hp')
                move_choices = []
                for i, team in enumerate(teams):
                    other_team = teams[(i + 1) % 2]
                    print(f'What will {team.fighter.name} do?')
                    print(*list(team.fighter.moves.keys()), sep='\n')
                    if (team == red_team):
                        whichteam = red_moves
                    elif (team == blue_team):
                        whichteam = blue_moves
                    move_name = speech.speechInput(whichteam)
                    move_choices.append(pokemon.battle.MoveChoice(
                        fighter=team.fighter, move=move_name, target=other_team.fighter))
                for result in pokemon.battle.fight(move_choices):
                    print(f'{result.move_choice.fighter.name} used {result.move_choice.move}!')
                    if result.miss:
                        print(f'{result.move_choice.move} missed!')
                        continue
                    if result.damage.critical_hit:
                        print('Critical hit!')
                    print(f'{result.damage.effectiveness}x effective')
                    if result.ko:
                        print(f'{result.move_choice.target.name} died!')
                    else:
                        print(f'{result.move_choice.target.name} now has {result.move_choice.target.hp} hp')
                print('\n==================\n')

            if red_team.blacked_out():
                print(f'Red blacked out!')
                recog = 0
                game = False
            elif blue_team.blacked_out():
                print(f'Blue blacked out!')
                recog = 0
                game = False
    ##################################################################################################################################
    
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
            
            
cap.release()
#writer.release()
cv2.destroyAllWindows()
