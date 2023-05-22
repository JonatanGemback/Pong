from cmu_graphics import *
from cmu_graphics.cmu_graphics import *
#import time
import highscore
import stopWatch
import meny

leftPaddle: Line
rightPaddle: Line
ball_speed_X: int
ball_speed_Y: int
ball: Circle

#Röra paddlarna
def onKeyHold(key):
    if leftPaddle.centerY >= 70:
        if 'w' in key:
            leftPaddle.centerY -= 6
    if leftPaddle.centerY <= 430:
        if 's' in key:
            leftPaddle.centerY += 6

def start():
    app.stepsPerSecond = 60

    global leftPaddle, rightPaddle, ball_speed_X, ball_speed_Y, ball

    #Bakgrunden
    app.background = 'black'

    #Planen
    Rect(10, 10, 5, 480, fill='white')
    Rect(685, 10, 5, 480, fill='white')
    Rect(10, 10, 680, 5, fill='white')
    Rect(10, 485, 680, 5, fill='white')

    #Mittenlinje
    Line(350.5, 10, 350.5, 485, lineWidth=5, dashes=True, fill='white')

    #Paddlarna
    leftPaddle = Line(35, 200, 35, 300, lineWidth=10, fill='white')
    rightPaddle = Line(665, 200, 665, 300, lineWidth=10, fill='white')

    #Bollen
    ball = centerBoll()

    #Bollens hastighet
    ball_speed_X = -10
    ball_speed_Y = -1

    #Startar tiden
    stopWatch.startTime()

def onStep():
    global ball_speed_X, ball_speed_Y, ball

    ball.centerX -= ball_speed_X
    ball.centerY += ball_speed_Y

    rightPaddle.centerY = ball.centerY

    if rightPaddle.centerY <= 65:
        rightPaddle.centerY = 65
    elif rightPaddle.centerY >= 435:
        rightPaddle.centerY = 435

    if ball.centerY >= 480 or ball.centerY <= 20:
        ball_speed_Y *= -1

    #Få bollen att stutsa tillbaka beroende på vart den träffar paddeln. Och öka hastighet för varje träff
    if (655 <= ball.centerX <= 665) and (rightPaddle.centerY - 50) <= ball.centerY <= (rightPaddle.centerY + 50):
        ball_speed_X -= 0.2
        if (rightPaddle.centerY - 20) <= ball.centerY <= (rightPaddle.centerY + 20):
            ball_speed_X *= -1
        elif ball.centerY < (rightPaddle.centerY - 20):
            ball_speed_Y = -1
            ball_speed_X *= -1
        elif ball.centerY > (rightPaddle.centerY + 20):
            ball_speed_Y = 1
            ball_speed_X *= -1

    if (35 <= ball.centerX <= 45) and (leftPaddle.centerY - 50) <= ball.centerY <= (leftPaddle.centerY + 50):
        ball_speed_X += 0.2
        if ball.centerY < (leftPaddle.centerY - 20):
            ball_speed_Y = -1
            ball_speed_X *= -1
        elif (leftPaddle.centerY - 20) <= ball.centerY <= (leftPaddle.centerY + 20):
            ball_speed_X *= -1
        elif ball.centerY > (leftPaddle.centerY + 20):
            ball_speed_Y = 1
            ball_speed_X *= -1

    if ball.centerX <= 15:
        rightPaddle.centerY = 250
        ball.visible = False
        name = app.getTextInput('Vad heter du? ')
        if name == '':
            app.stop()
        highscore.add(name , stopWatch.stopTime())
        highscore.p(10)
        start()

def centerBoll():
    return Circle(350, 250, 8, fill='white')


highscore.load()
meny.askWay()
start()

print('Let´s goo')
cmu_graphics.run()
