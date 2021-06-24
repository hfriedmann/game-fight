from tkinter import *
import keyboard


po = 0
pq = 0
pw = 0
pp = 0

def keybild():
    keyboard.on_press(moveplay)
    #while True:
     #   pass

def w():
    lbl = Label(window, text="W", font=("Arial Bold", 50))
    lbl.grid(column=0, row=0)

def q():
    lbl = Label(window, text="Q", font=("Arial Bold", 50))
    lbl.grid(column=0, row=0)

def o():
    lbl = Label(window, text="O", font=("Arial Bold", 50))
    lbl.grid(column=0, row=4)

def p():
    lbl = Label(window, text="P", font=("Arial Bold", 50))
    lbl.grid(column=0, row=4)

def moveplay(move):
    global pq
    global pw
    global po
    global pp

    pright = po - pq
    pleft = pw - pp
    if move.name == 'w':
        pw += 1
        w()
        clicked1()
    if move.name == 'q':
        pq += 1
        q()
        clicked1()
    if move.name == "o":
        po += 1
        o()
        clicked1()
    if move.name == "p":
        pp += 1
        p()
        clicked1()
    else:
        return()

def clicked1():
    global pq
    global pw
    global po
    global pp
    pright = po - pq
    pleft = pw - pp
    lbl = Label(window, text=("player1: ", pleft, "/", "player2: ", pright), font=("Arial Bold", 12))
    lbl.grid(column=2, row=1)
    if pright > pleft:
        lbl = Label(window, text="player 2!", font=("Arial Bold", 12))
        lbl.grid(column=2, row=2)
    elif pright == pleft:
        lbl = Label(window, text="A tie!", font=("Arial Bold", 12))
        lbl.grid(column=2, row=2)
    elif pleft > pright:
        lbl = Label(window, text="player 1!", font=("Arial Bold", 12))
        lbl.grid(column=2, row=2)
    else:
        lbl = Label(window, text="???", font=("Arial Bold", 12))
        lbl.grid(column=2, row=2)

def clicked2():
    global pq
    global pw
    global po
    global pp
    po = 0
    pp = 0
    pw = 0
    pq = 0
    pright = po - pq
    pleft = pw - pp
    lbl = Label(window, text=("player1: ", pleft, "/", "player2: ", pright), font=("Arial Bold", 12))
    lbl.grid(column=2, row=1)
    if pright > pleft:
        lbl = Label(window, text="player 2!", font=("Arial Bold", 12))
        lbl.grid(column=2, row=2)
    elif pright == pleft:
        lbl = Label(window, text="A tie!", font=("Arial Bold", 12))
        lbl.grid(column=2, row=2)
    elif pleft > pright:
        lbl = Label(window, text="player 1!", font=("Arial Bold", 12))
        lbl.grid(column=2, row=2)
    else:
        lbl = Label(window, text="???", font=("Arial Bold", 12))
        lbl.grid(column=2, row=2)

keybild()
window = Tk()

window.title("FIGHT CLUB")
window.geometry('700x300')
lbl0 = Label(window, text="?", font=("Arial Bold", 50))
lbl0.grid(column=0, row=0)
lbl0 = Label(window, text="?", font=("Arial Bold", 50))
lbl0.grid(column=0, row=4)
lbl = Label(window, text="Player 1: Press Q ou W", font=("Arial Bold", 12))
lbl.grid(column=0, row=1)
lbl = Label(window, text="Player 2: Press O or P", font=("Arial Bold", 12))
lbl.grid(column=0, row=2)
btn = Button(window, text="Points", bg="orange", fg="red", command=clicked1)
btn.grid(column=1, row=1)
btn = Button(window, text="Restart", bg="red", fg="orange", command=clicked2)
btn.grid(column=1, row=2)
lbl0 = Label(window, text="player 1: W> earns one point; Q> takes a point from player 2", font=("Arial Bold", 10))
lbl0.grid(column=0, row=5)
lbl0 = Label(window, text="player 2: O> earns one point; P> takes a point from player 1", font=("Arial Bold", 10))
lbl0.grid(column=0, row=6)

window.mainloop()
