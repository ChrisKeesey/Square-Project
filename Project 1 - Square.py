from Myro import *
init("sim") #if simulator is not running
turnBy(90)
forward(2,1)
turnBy(-90)
def DrawSquare (x,a):
    turnBy(a)
    penDown()
    forward(x,1)
    turnBy(90)
    forward(x,1)
    turnBy(90)
    forward(x,1)
    turnBy(90)
    forward(x,1)
DrawSquare(2,0)#Change x, size, and a, initial angle
penUp()
forward(2,1)
penDown()
def DrawOctagon (y):
    turnBy(-45)
    forward(y,1)
    turnBy(-45)
    forward(y,1)
    turnBy(-45)
    forward(y,1)
    turnBy(-45)
    forward(y,1)
    turnBy(-45)
    forward(y,1)
    turnBy(-45)
    forward(y,1)
    turnBy(-45)
    forward(y,1)
    turnBy(-45)
    forward(y,1)
DrawOctagon(1) #Change 1 to change size of octagon
turnBy(90)
penUp()
forward(3,1)
penDown()
def DrawTriangle (z):
    forward(z,1)
    turnBy(120)
    forward(z,1)
    turnBy(120)
    forward(z,1)
DrawTriangle(2) #Change 2 to change size of Triangle
penUp()
forward(2,1)
turnBy(-55)
def DrawC ():
    penDown()
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
    forward(1,.25)
    turnBy(10)
DrawC()
penUp()
forward(2,1)