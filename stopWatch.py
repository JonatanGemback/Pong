from cmu_graphics.cmu_graphics import *
import time

t0: int

def startTime():
    global t0
    t0 = time.time()
    return t0

def stopTime():
    t1 = time.time()
    total = t1 - t0
    return rounded(total)
