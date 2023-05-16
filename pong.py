from cmu_graphics import *
from cmu_graphics.cmu_graphics import *

leftPaddle: Line
rightPaddle: Line
ball_speed_X: int
ball_speed_Y: int
leftScore: Label
rightScore: Label
ball: Circle



#Startmeny
visible = True
#meny = True

#startGame = Rect(310, 146, 80, 40, border='white', visible=meny)
#Label('Start', 350, 166, size=30, fill='white', visible=meny)

#quitGame = Rect(310, 280, 80, 40, border='white', visible=meny)
#Label('Quit', 350, 300, size=30, fill='white', visible=meny)

#def onMousePress(mouseX, mouseY):
#    global visible
#    global meny
#    if startGame.hits(mouseX,mouseY):
#        visible = True
#        meny = False
#    if quitGame.hits(mouseX, mouseY):
#        breakpoint()
#     return visible, meny




#Röra paddlarna
def onKeyHold(key):
    if leftPaddle.centerY >= 70:
        if 'w' in key:
            leftPaddle.centerY -= 6
    if leftPaddle.centerY <= 430:
        if 's' in key:
            leftPaddle.centerY += 6
    if rightPaddle.centerY >= 70:
        if 'up' in key:
            rightPaddle.centerY -= 6
    if rightPaddle.centerY <= 430:
        if 'down' in key:
            rightPaddle.centerY += 6


def onStep():
    global ball_speed_X, ball_speed_Y, ball

    ball.centerX -= ball_speed_X
    ball.centerY += ball_speed_Y

    if ball.centerY >= 480 or ball.centerY <= 20:
        ball_speed_Y *= -1

    if (ball.centerX >= 655) and (ball.centerY <= (rightPaddle.centerY+50) and (ball.centerY >= (rightPaddle.centerY-50))):
        ball_speed_X *= -1


    if (ball.centerX <= 45) and (ball.centerY <= (leftPaddle.centerY+50) and (ball.centerY >= (leftPaddle.centerY-50))):
        ball_speed_X *= -1

    if ball.centerX >= 685:
        updateScore('leftScoreLabel')
    elif ball.centerXq <= 15:
        updateScore('rightScoreLabel')

def centerBoll():
    return Circle(350, 250, 8, fill='white', visible=visible)


def updateScore(score):
    global ball
    ball.visible = False
    ball = centerBoll()

    if score == 'leftScoreLabel':
        leftScore.value += 1
    elif score == 'rightScoreLabel':
        rightScore.value += 1


def init():
    app.stepsPerSecond = 60

    global leftPaddle, rightPaddle, ball_speed_X, ball_speed_Y, leftScore, rightScore, ball

    #Bakgrunden
    app.background = 'black'

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
    ball_speed_X = -1
    ball_speed_Y = -1

    #Score
    leftScore = Label(0, 180, 50, size=30, fill='white', visible=visible)
    rightScore = Label(0, 520, 50, size=30, fill='white', visible=visible)


init()



cmu_graphics.run()
