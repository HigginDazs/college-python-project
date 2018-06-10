from tkinter import *
from tkinter.ttk import *
from turtle import RawTurtle
import math
import random
from fractalInfo import *

## define the turtle functions     
def tree(n, l):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(45)
     tree(n-1, l/2)
     pen.right(90)
     tree(n-1, l/2)
     pen.left(45)
     pen.backward(l)
#end tree

def dandelion(n, l):
     '''
     dandelion constructs a quad tree with 4 similar branches symetrically positioned.
     '''
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(90)
     dandelion(n-1, l/2)
     pen.right(60)
     dandelion(n-1, l/2)
     pen.right(60)
     dandelion(n-1, l/2)
     pen.right(60)
     dandelion(n-1, l/2)
     pen.left(90)
     pen.backward(l)
#end dandelion

def fern(n, l):
     '''
     this constructs a fern with 3 branches angled with 45, 30 and 10 degrees
     '''
     if n==0 or l<2 :
          return
     #endif
     pen.forward(0.3*l)
     pen.left(45); fern(n-1, l/2); pen.right(45)
     pen.forward(0.7*l)
     pen.right(30); fern(n-1, l/2); pen.left(30)
     pen.forward(l)
     pen.left(10); fern(n-1, 0.75*l); pen.right(10)
     pen.backward(2*l)
#end fern

def gasketEmpty(n, l, side):
     a = 360/side
     '''
     this creates an unfilled gasket with any number of sides
     '''
     if n==0 or l<2 :
          for i in range(side):
               pen.forward(l); pen.left(a)
          #endfor
          return
     #endif
     for i in range(side):
          pen.begin_fill()
          if side == 3:
               gasketEmpty(n-1, l/2, side); pen.forward(l); pen.left(a)
          elif side in [4, 5, 6]:
               gasketEmpty(n-1, l/3, side); pen.forward(l); pen.left(a)
          else:
               gasketEmpty(n-1, l/4, side); pen.forward(l); pen.left(a)
          #endif
          pen.fillcolor("red"); pen.end_fill()
     #endfor
#end gasketEmpty

def gasketFull(n, l, side):
     a = 360/side
     b = (180 - a)/2
     arad = a * (math.pi/180)
     '''
     this creates a filled gasket with any number of sides
     '''
     if n==0 or l<2 :
          for i in range(side):
               pen.forward(l); pen.left(a)
          #endfor
          return
     #endif
     for i in range(side):
          pen.begin_fill()
          if side == 3:
               gasketFull(n-1, l/2, side); pen.forward(l); pen.left(a)
          elif side in [4, 5, 6]:
               gasketFull(n-1, l/3, side); pen.forward(l); pen.left(a)
          else:
               gasketFull(n-1, l/4, side); pen.forward(l); pen.left(a)
          #endif
          pen.fillcolor("red"); pen.end_fill()
     #endfor

     if side == 3:
          pen.up(); pen.left(b); pen.forward( 1.35 * math.sqrt( (l**2)/(2*(1-math.cos(arad))) ) )
          pen.down(); pen.right(b);
          pen.begin_fill()
          pen.left(180); gasketFull(n-1, l*.35, side); pen.right(180)
          pen.fillcolor("red"); pen.end_fill()
          pen.up(); pen.left(b); pen.backward( 1.35 * math.sqrt( (l**2)/(2*(1-math.cos(arad))) ) )
          pen.down(); pen.right(b)
     elif side in [4, 5, 6]:
          pen.up(); pen.left(b); pen.forward( 4/3 * math.sqrt( (l**2)/(2*(1-math.cos(arad))) ) )
          pen.down(); pen.right(b);
          pen.begin_fill()
          pen.left(180); gasketFull(n-1, l/3, side); pen.right(180)
          pen.fillcolor("red"); pen.end_fill()
          pen.up(); pen.left(b); pen.backward( 4/3 * math.sqrt( (l**2)/(2*(1-math.cos(arad))) ) )
          pen.down(); pen.right(b)
     else:
          pen.up(); pen.left(b); pen.forward( 3/2 * math.sqrt( (l**2)/(2*(1-math.cos(arad))) ) )
          pen.down(); pen.right(b);
          pen.begin_fill()
          pen.left(180); gasketFull(n-1, l/2, side); pen.right(180)
          pen.fillcolor("red"); pen.end_fill()
          pen.up(); pen.left(b); pen.backward( 3/2 * math.sqrt( (l**2)/(2*(1-math.cos(arad))) ) )
          pen.down(); pen.right(b)
     #endif
#end gasketFull

def koch(n, l):
     if n==0 or l<2 :
          pen.forward(l)
          return
     #endif
     koch(n-1, l/3); pen.left(60)
     koch(n-1, l/3); pen.right(120)
     koch(n-1, l/3); pen.left(60)
     koch(n-1, l/3)
#end koch

def kochCirc(n, l):
     if n==0 or l<2 :
          pen.forward(l)
          return
     #endif
     kochCirc(n-1, l/2); pen.left(90)
     kochCirc(n-1, l/3); pen.left(180)
     pen.circle(l/6, -180); pen.right(180)
     kochCirc(n-1, l/3); pen.left(90)
     kochCirc(n-1, l/2)
#end kochCirc

def snow(n, l):
     if n==0 or l<2 :
          return
     #endif
     for i in range(3):
          koch(n, l); pen.right(120)
     #endfor
#end snow

def antiSnow(n, l):
     if n==0 or l<2 :
          return
     #endif
     for i in range(3):
          koch(n, l); pen.left(120)
     #endfor
#end antiSnow

def cross(n, l):
     if n==0 or l<2 :
          return
     #endif
     for i in range(4):
          kochCirc(n, l); pen.right(90)
     #endfor
#end cross

def jigsaw(n, l):
     if n==0 or l<2 :
          return
     #endif
     for i in range(4):
          kochCirc(n, l); pen.left(90)
     #endfor
#end jigsaw

def pytha(n, l, a):
     adeg = a
     arad = a * (math.pi/180)
     
     if n==0 or l<2 :
          pen.begin_fill()
          for i in range(4):
               pen.forward(l); pen.right(90)
          #endfor
          pen.fillcolor(24, 139, 34)
          pen.end_fill()
          return
     #endif
     pen.begin_fill()
     for i in range(4):
          pen.forward(l); pen.right(90)
     #endfor
     pen.fillcolor(139, 90, 0)
     pen.end_fill()
     
     pen.left(adeg+90); pen.forward(l*math.cos(arad))
     pen.right(90); pytha(n-1, l*math.cos(arad), adeg)
     pen.left(90); pen.backward(l*math.cos(arad))
     pen.right(90); pen.forward(l*math.cos(arad)); pen.forward(l*math.sin(arad))
     pen.right(90); pytha(n-1, l*math.sin(arad), adeg)
     pen.left(90); pen.backward(l*math.sin(arad)); pen.backward(l*math.cos(arad))
     pen.right(adeg)
#end pytha

def broken(n, l):
     if n==0 or l<2 :
          pen.forward(l)
          return
     #endif
     broken(n-1, l/4); pen.left(90)
     broken(n-1, l/4); pen.right(90)
     broken(n-1, l/4); pen.right(90)
     broken(n-1, l/4); broken(n-1, l/4); pen.left(90)
     broken(n-1, l/4); pen.left(90)
     broken(n-1, l/4); pen.right(90)
     broken(n-1, l/4)
#end broken

def puzzle(n, l):
     if n==0 or l<2:
          return
     #endif
     for i in range(4):
          broken(n, l); pen.right(90)
     #endfor
#end puzzle

def htree(n, l):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l/2)
     pen.right(90); pen.forward(l/2)
     pen.left(90); htree(n-1, l/2)
     pen.left(90); pen.forward(l)
     pen.right(90); htree(n-1, l/2)
     pen.left(90); pen.backward(l/2)
     pen.right(90); pen.backward(l)
     pen.left(90); pen.backward(l/2)
     pen.right(90); htree(n-1, l/2)
     pen.left(90); pen.forward(l)
     pen.right(90); htree(n-1, l/2)
     pen.left(90); pen.backward(l/2)
     pen.right(90); pen.forward(l/2)
#end htree  

def circFrac(n, l):
     if n==0 or l<2 :
          return
     #endif
     r = -(3-2*math.sqrt(3))*l
     for i in range(3):
          pen.circle(l, 120); circFrac(n-1, r)
     #endfor
#end circFrac

autumnColours = [(209, 206, 197), (153, 124, 103), (117, 83, 48),
                 (176, 112, 60), (219, 167, 46), (227, 204, 161),
                 (255, 163, 26), (204, 82, 0), (179, 0, 0)]

springColours = [(81,99,51), (126,181,80), (142,219,89),
                 (170,253,111), (232,254,216), (153,204,153),
                 (39,188,75), (87,239,30), (23,171,90)]

def circTree(n, l, season):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.right(90)
     pen.begin_fill()
     if season in ["Autumn", "autumn"]:
          pen.fillcolor(autumnColours[random.randint(0, len(autumnColours) - 1)])
     elif season in ["Spring", "spring"]:
          pen.fillcolor(springColours[random.randint(0, len(springColours) - 1)])
     else:
          return
     #endif
     pen.circle(l/4)
     pen.end_fill()
     pen.left(90)
     pen.left(60); circTree(n-1, l/2, season)
     pen.right(60); circTree(n-1, l/2, season)
     pen.right(60); circTree(n-1, l/2, season)
     pen.left(60)
     pen.backward(l)
#end circTree

def circTreeDraw(n, l, season):
     pen.left(90); pen.pencolor(139, 90, 0)
     circTree(n, l, season)
     pen.right(90); pen.pencolor(0, 0, 0)
#end circTreeDraw



## dictionary for the functions
chooseFunc = {"Tree" : tree,
              "Dandelion" : dandelion,
              "Fern" : fern,
              "Gasket (Empty)" : gasketEmpty,
              "Gasket (Filled)" : gasketFull,
              "Snowflake" : snow,
              "Antiflake" : antiSnow,
              "Cross" : cross,
              "Jigsaw" : jigsaw,
              "Pythagoras Tree" : pytha,
              "Puzzle" : puzzle,
              "H-Tree" : htree,
              "Circle Gasket" : circFrac,
              "Seasonal Tree" : circTreeDraw
              }



## contruct the Tk window
root = Tk()
root.title("Turtle Fractals")

## setup turtle screen
wide = root.winfo_screenwidth()
high = root.winfo_screenheight()
canvas = Canvas(root, width = wide, height = high)
canvas.pack()

pen = RawTurtle(canvas)
screen = pen.getscreen()
pen.speed(0)
pen.width(3)
screen.colormode(255)
screen.bgcolor((199, 248, 255))

## define handlers

def onClearScreen():
     # clear the canvas
     screen.resetscreen()
     pen.speed(0)
     pen.width(3)
     screen.colormode(255)
     screen.bgcolor((199, 248, 255))
#end onClearScreen

def onDraw():
     order = int(orderStr.get())
     length = int(lengthStr.get())
     if var.get() in ["Gasket (Empty)", "Gasket (Filled)", "Pythagoras Tree"]:
          auxillary = int(auxStr.get())
          chooseFunc[var.get()](order, length, auxillary)
     elif var.get() == "Seasonal Tree":
          chooseFunc[var.get()](order, length, auxStr.get())
     else:
          chooseFunc[var.get()](order, length)
     #endif
#end onDraw

def onClear():
     # clear the input boxes
     orderStr.set("")
     lengthStr.set("")
     auxStr.set("")
#end onClear     

def onInfo():
     textBox.delete(1.0, END)
     textBox.insert(INSERT, infoList[var.get()])
#end onInfo

def onLoc():
     screen.onclick(moveCur)
#end onLoc

def moveCur(x,y):
     pen.up()
     pen.goto(x,y)
     pen.down()
     screen.onclick(None)
#end moveCur

def onQuit():
    root.destroy()
    root.quit()
#end onQuit


## make the interface
frame = Frame(canvas, style = "RedBack.TFrame")
frame.place(relx=0, rely=0, anchor=NW)

titleLabel = Label(frame, text = "Turtle Interface")
titleLabel.grid(row = 0, column = 0, columnspan = 2)

orderLabel = Label(frame, text = "Order")
orderLabel.grid(row = 1, column = 0)

lengthLabel = Label(frame, text = "Length")
lengthLabel.grid(row = 2, column = 0)

auxLabel = Label(frame, text = "Auxillary")
auxLabel.grid(row = 3, column = 0)

orderStr = StringVar()
orderEntry = Entry(frame, textvariable = orderStr)
orderEntry.grid(row = 1, column = 1)

lengthStr = StringVar()
lengthEntry = Entry(frame, textvariable = lengthStr)
lengthEntry.grid(row = 2, column = 1)

auxStr = StringVar()
auxEntry = Entry(frame, textvariable = auxStr)
auxEntry.grid(row = 3, column = 1)

drawButton = Button(frame, text = "Draw", command = onDraw)
drawButton.grid(row = 4, column = 0)

optionList = ["Tree", "Dandelion", "Fern", "Gasket (Empty)","Gasket (Filled)", "Snowflake", "Antiflake", "Cross", "Jigsaw", "Pythagoras Tree", "Puzzle", "H-Tree", "Circle Gasket", "Seasonal Tree"]
var = StringVar()
fracList = OptionMenu(frame, var, "Please Select", *optionList)
fracList.grid(row = 4, column = 1)

clearButton = Button(frame, text = "Clear Text", command = onClear)
clearButton.grid(row = 5, column = 0)

infoButton = Button(frame, text = "Fractal Information", command = onInfo)
infoButton.grid(row = 5, column = 1)

clearScreenButton = Button(frame, text = "Clear Screen", command = onClearScreen)
clearScreenButton.grid(row = 6, column = 0)

locButton = Button(frame, text = "Cursor Location", command = onLoc)
locButton.grid(row = 6, column = 1)

Style().configure("Quit.TButton", foreground = "red")
quitButton = Button(frame, text = "Quit", command = onQuit, width = 28, style = "Quit.TButton")
quitButton.grid(row = 7, column = 0, columnspan = 2)

textBox = Text(frame, width = 36, height = 7, wrap = WORD)
textBox.grid(row = 8, column = 0, columnspan = 2, pady = 5)
textBox.insert(INSERT, 'Please select "Fractal Information" to display info on a specific fractal shape. Choose an appropriate cursor location, based on the fractal draw direction.')

mainloop()

