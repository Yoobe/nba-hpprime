# Local
from graph import *

# System
if platform != "win":
    from hpprime import *
    from urandom import *
from math import *
import sys

# Keyboard
def GetKey():  # determine  what to do next
    keyCode = 0
    if keyboard():
        keyCode = eval('GETKEY()')
    return keyCode

# Main function
def main():
    # Init the game and initial player position
    if platform != "win": 
        resetScreen()
        loadPlayers()
        playerX = randint(24, 247)
        playerY = 175
        loadPlayer(0, playerX, playerY)
        
    k = 0
    bInput = 0
    cY = 0
    sAngle = ""
    sVel = ""
    score = 0
    
    if platform != "win":
        while True:        
            k = GetKey()
            
            if k > 0:
                if k == 46:   # Press ON to leave game
                    break
                elif bInput == 0 and k == 30: # 'Enter' to start input value (Angle)
                    # clear text area (in case we need to clean previous shoot)
                    resetScreen()
                    loadPlayer(0, playerX, playerY)
                    fillrect(0, 4, 3, 6, 10, bg, bg)
                    textout(0, 5, 4, str(score), blue)
                    fillrect(0, 0, 194, 320, 240, white, white)
                    textout(0, 10, 200, "Angle : ", black)
                    cY = 0
                    sAngle = ""
                    sVel = ""
                    
                    # Start input session 1
                    bInput = 1
                elif bInput == 1:  # Input 'Angle' Session
                    res = checkNum(k, 10 + 50 + cY, 200)  # Read keyboard for numeric key or .
                    if res != "":
                        cY += 6
                        sAngle += res
                    if k == 30:    # 'Enter' to finish enter angle
                        bInput = 2   # Start Velocity input Session
                        textout(0, 10, 220, "Force : ", black)
                        cY = 0
                elif bInput == 2:  # Input 'Velocity' Session
                    res = checkNum(k, 10 + 50 + cY, 220) # Read keyboard for numeric key or .
                    if res != "":
                        cY += 6
                        sVel += res
                    if k == 30:    # 'Enter' to finish Velocity session
                        bInput = 0   # Reset Sessions
                        
                        if len(sVel) > 0 and len(sAngle) > 0: # Check if angle and velocity is set
                            
                            # Animate Player shoot
                            animatePlayer(playerX, playerY)
                            
                            # Move the ball
                            if drawTrajectory(playerX+15, 240-playerY, float(sVel), float(sAngle), 175-132, 8.85): # Check if score
                                if playerX > 180: # 2points
                                    textout(0, 5, 15, "Scored !!!!! 2 Points ", red)
                                    score += 2 # Increment the Global Score
                                else: # 3 points
                                    textout(0, 5, 15, "Scored !!!!! 3 Points", red)
                                    score += 3 # Increment the Global Score
                                fillrect(0, 4, 3, 75, 8, bg, bg)
                                textout(0, 5, 4, "Score : " + str(score), blue)
                                
                            # new position for the plater for next round.
                            playerX = randint(24, 247)
                            
                        fillrect(0, 0, 194, 320, 240, white, white) # Clean text area
                        continue

# Start the main function
main()
