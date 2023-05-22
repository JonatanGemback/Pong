import pickle


high_scores = []
fileName = 'score.pong'

def __read():
    global high_scores
    try:
        with open(fileName, 'rb') as f:
            high_scores = pickle.load(f)
    except FileNotFoundError:
            pass
            #Ingen fil

def __write():
    with open(fileName, 'wb') as f:
        pickle.dump(high_scores, f)

def load():
    __read()

def add(name, total):
    global high_scores
    high_scores.append((name, total))
    high_scores.sort(key=lambda x: x[1], reverse = True)
    __write()

def p(listLengt):
    print("Topplistan: ")
    for i, (name, total) in enumerate(high_scores):
        if i > listLengt-1:
            break
        else:
            print(f"{i+1}. {name}: {total} sekunder")


def search():
    searchedName = input('Vilket namn vill du söka efter?')

    for i, (name, total) in enumerate(high_scores):
        if searchedName == name:
            print(f"{i+1}. {name}: {total} sekunder")
            print('')
