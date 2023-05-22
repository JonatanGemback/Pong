import time
import highscore

def askWay():
    question = 0
    while question != '4':
        print('Välkommen!')
        print('1. Vill du se reglerna?')
        print('2. Vill du se topplistan?')
        print('3. Vill du söka i topplistan?')
        print('4. Vill du spela?')
        question = input('').strip()

        if question == '1':
            rules()
        elif question == '2':
            highscore.p(10)
        elif question == '3':
            highscore.search()


def rules():
    print('Du använder "W" för att styra paddeln uppåt och "S" för att styra paddeln neråt')
    time.sleep(1)
    print('Klara dig så länge som möjligt!')
    time.sleep(1)
    print('Bollens hastighet kommer att öka efter varje träff!')
    time.sleep(1)
    print('Lycka till!')
