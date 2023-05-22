from cmu_graphics import *
from cmu_graphics.cmu_graphics import *
import time
import highscore


leftPaddle: Line
rightPaddle: Line
ball_speed_X: int
ball_speed_Y: int
ball: Circle
to: int
t1: int
total: int


def calculateGameTime():
    t1 = time.time()
    total = t1 - t0
    return rounded(total)

#Röra paddlarna
def onKeyHold(key):
    if leftPaddle.centerY >= 70:
        if 'w' in key:
            leftPaddle.centerY -= 6
    if leftPaddle.centerY <= 430:
        if 's' in key:
            leftPaddle.centerY += 6

def init():
    app.stepsPerSecond = 60

    global visible, leftPaddle, rightPaddle, ball_speed_X, ball_speed_Y, ball

    #Bakgrunden
    app.background = 'black'

    #Synlighet
    visible = True

    #Planen
    Rect(10, 10, 5, 480, fill='white')
    Rect(685, 10, 5, 480, fill='white')
    Rect(10, 10, 680, 5, fill='white')
    Rect(10, 485, 680, 5, fill='white')

    #Mittenlinje
    Line(350.5, 10, 350.5, 485, lineWidth=5, dashes=True, fill='white', visible=visible)

    #Paddlarna
    leftPaddle = Line(35, 200, 35, 300, lineWidth=10, fill='white', visible=visible)
    rightPaddle = Line(665, 200, 665, 300, lineWidth=10, fill='white', visible=visible)

    #Bollen
    ball = centerBoll()

    #Bollens hastighet
    ball_speed_X = -10
    ball_speed_Y = -1

def onStep():
    global ball_speed_X, ball_speed_Y, ball, t1, time

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
        highscore.add(name , calculateGameTime())
        init()

def centerBoll():
    return Circle(350, 250, 8, fill='white', visible=visible)



def rules():
    global t0
    print('Du använder "W" för att styra paddeln uppåt och "S" för att styra paddeln neråt')
    time.sleep(1)
    print('Klara dig så länge som möjligt!')
    time.sleep(1)
    print('Bollens hastighet kommer att öka efter varje träff!')
    time.sleep(1)
    print('Lycka till!')
    time.sleep(1)


def start():
    global t0
    print('Välkommen till ett modifierat pong')
    time.sleep(1)
    knowRules = input('Vill du veta reglerna? Ja/Nej').lower().strip()
    if knowRules == 'ja':
        rules()
    print('Let´s goo')
    t0 = time.time()
    cmu_graphics.run()



init()
start()
