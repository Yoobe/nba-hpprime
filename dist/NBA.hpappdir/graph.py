try:
    from hpprime import *
    platform = "hp"
except ImportError or ModuleNotFoundError:
    platform = "win"

from math import *

# Color codes
black = 0x000000
white = 0xf8f8f8
blue = 0x0000f8
green = 0x00f800
red = 0xf80000
cyan = 0x00f8f8
magenta = 0xf800f8
yellow = 0xf8f800
bg = 0xbff0ff

# Player sprite coordinate in PNG file
player = [ [225, 175, 240, 130, 15, 45], [207, 175, 223, 130, 16, 45], [190, 175, 203, 130, 13, 45], [175, 175, 187, 130, 12, 45],[160, 175, 170, 130, 10, 45],[146, 175, 160, 130, 14, 45],[132, 175, 145, 130, 13, 45],[116, 175, 130, 130, 14, 45],[101, 175, 115, 130, 14, 45],]

# Reset Screen Function
def resetScreen():
    fillrect(0, 0, 0, 320, 240, white, white)
    eval("G0:=AFiles(\"bg.png\")")
    fillrect(0, 0, 121, 241, 176-121, bg, bg)
    fillrect(0, 0, 194, 320, 240, white, white)
    
# Load all sprites for player animation to G1
def loadPlayers():
    eval("G1:=AFiles(\"bg.png\")")
    
# Display 1 player sprite
def loadPlayer(num, x, y):
    strblit2(0, x, y - player[num][5], player[num][4], player[num][5], 1, player[num][0], player[num][3],player[num][4], player[num][5])

# Loop to player sprite to animate player
def animatePlayer(x, y):
    for i in range (0, 8):
        fillrect(0, x, y-45, 30, 45, bg, bg)
        loadPlayer(i, x, y)
        eval("WAIT(0.1)")

# Move the ball according velocity and angle
def drawTrajectory(startX, startY, vel, angle, h, scale):
    # clean the ball from sprite
    fillrect(0, startX - 6 , 131, 5, 5, bg, bg)
    
    # contant def for earth attraction force
    g = 9.81
    
    # Convert angle from Degree to Radian
    angle = angle * 3.141592 / 180

    # Init vars
    x = 0
    y = 0
    drawX = startX
    drawY = startY
    oDrawX = 0
    oDrawY = 0
    # y = startY
    while drawX < 320 and drawY < 175: # loop from x = 0 to reach end of play area
        # Projectile motion formula with Angle, Velocity.
        y = (x * tan(angle) - g * (x * x) / (2 * vel * vel * cos(angle) * cos(angle)))
        
        # ball coordinate with scale, starting point
        drawX = (startX + x * scale)
        drawY = ((startY + h) + y * scale)
        # Flip Y coordinate for Cartesian X,Y
        drawY = 240 - drawY
        
        if platform == "win": # Debug code
            if drawX < 320 and drawX > 0 and drawY > 0 and drawY < 240:
                print(drawX, drawY, x, y, 'x:', x, 'y:', y)
            else:
                print(int(drawX), int(drawY), 'x:', x, 'y:', y)
        else:
            if drawX < 320 and drawX > 0 and drawY > 0 and drawY < 240:
                # clear old position
                fillrect(0, oDrawX - 2 , oDrawY - 2, 4, 5, bg, bg)
                
                # restort basket if deleted
                strblit2(0, 268 , 123, 320-268, 178-123, 1, 268, 123, 320-268, 178-123)

                # draw ball
                strblit2(0, drawX -2 , drawY-2, 4, 5, 1, 112, 130, 4, 5)
                
                eval("WAIT(0.005)") # wait 5ms
                oDrawX = drawX
                oDrawY = drawY

                # check if we hit the basket.
                if drawX > 271 and drawX < 275 and drawY > 136 and drawY < 140:
                    return 1
        x += 0.1 # Next point.
    return 0

def checkNum(k, x, y):
    result = ""
    if k == 32:
        textout(0, x, y, "7", blue)
        result = "7"
    elif k == 33:
        textout(0, x, y, "8", blue)
        result = "8"
    elif k == 34:
        textout(0, x, y, "9", blue)
        result = "9"
    elif k == 37:
        textout(0, x, y, "4", blue)
        result = "4"
    elif k == 38:
        textout(0, x, y, "5", blue)
        result = "5"
    elif k == 39:
        textout(0, x, y, "6", blue)
        result = "6"
    elif k == 42:
        textout(0, x, y, "1", blue)
        result = "1"
    elif k == 43:
        textout(0, x, y, "2", blue)
        result = "2"
    elif k == 44:
        textout(0, x, y, "3", blue)
        result = "3"
    elif k == 47:
        textout(0, x, y, "0", blue)
        result = "0"
    elif k == 48:
        textout(0, x, y, ".", blue)
        result = "."
    return result