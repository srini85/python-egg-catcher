from tkinter import *
from tkinter import messagebox
from itertools import cycle
from random import randrange

canvas_width = 800
canvas_height = 400

window = Tk()
window.title("Egg Catcher Game")
window.configure(background="sea green")

catcher_width = 100
catcher_height = 100

catcher_color = "black"
catcher_start_x = canvas_width / 2 - catcher_width / 2 
catcher_start_y = canvas_height  - catcher_height - 20
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height

def verifyUser():
    loginCorrect = 0
    user = StringVar()    
    user = "i shouldnt see this"
    pwd = StringVar()
    eUser = eUsername.get()
    ePass = ePassword.get()
    eQuizValue = eQuiz.get()
    if (eUser == "srini"):
        if (ePass == "xyz"):
            if (eQuizValue == "20"):
                user = "Welcome " + eUser
                print(user)
                create_eggs()
                move_eggs()
                catcher_check()
                loginCorrect = 1
                c.bind('<Left>', moveLeft)
                c.bind('<Right>', moveRight)
                c.focus_set()

    if (loginCorrect == 0):
        print("You have entered incorrect login details")

lUsername = Label(window, text="Username", bg="orange", fg="white", width=18)
lUsername.pack()
eUsername = Entry(window, width=20)
eUsername.pack()
lPassword = Label(window, text="Password", bg="orange", fg="white", width=18)
lPassword.pack()
ePassword = Entry(window, width=20)
ePassword.pack()
lQuiz = Label(window, text="Quiz (5 * 4)", bg="orange", fg="green", width=18)
lQuiz.pack()
eQuiz = Entry(window, width=20)
eQuiz.pack()
bLogin = Button(window, text="Login", bg="orange", width=20, command=verifyUser)
bLogin.pack()

c = Canvas(window, width=canvas_width, height = canvas_height, background="sky blue")
c.create_rectangle(-5, canvas_height - 100, canvas_width + 5, canvas_height + 5, fill="sea green", width=0)
c.create_oval(-80, -80, 120,120, fill="orange", width=0)

catcher = c.create_arc(catcher_start_x, catcher_start_y, catcher_start_x2, catcher_start_y2, 
    start=200, extent=140, style="arc", outline=catcher_color, width=5)

colour_list = ['light blue', 'blue', 'green', 'light green', 'red', 'orange', 'purple', 'black', 'white']
colour_cycle = cycle(colour_list)

egg_width = 45
egg_height = 55
egg_score = 15
egg_speed = 100
egg_interval = 4000
difficulty_factor = 0.8
score = 0

lives_remaining = 3
lives_text = c.create_text(100, 10, anchor='ne', font=('Arial', 18, 'bold'), fill='darkblue', 
text='Lives: ' + str(lives_remaining))

score_text = c.create_text(100, 40, anchor='ne', font=('Arial', 18, 'bold'), fill='darkblue', 
text='Score: ' + str(score))

c.pack()

eggs=[]
def create_eggs():
    x = randrange(20, 760)
    y = 20
    new_egg = c.create_oval(x,y,x+egg_width,y+egg_height, fill=next(colour_cycle), width=0)
    eggs.append(new_egg)
    window.after(egg_interval, create_eggs)

def move_eggs():
    for egg in eggs:
        (egg_x1, egg_y1, egg_x2, egg_y2) = c.coords(egg)
        c.move(egg, 0, 5)
        if (egg_y2 > canvas_height):
            egg_dropped(egg)
    window.after(egg_speed, move_eggs)

def egg_dropped(egg):
    eggs.remove(egg)
    c.delete(egg)
    lose_a_life()
    print("egg was dropped")

def lose_a_life():
    global lives_remaining
    lives_remaining -= 1    
    c.itemconfigure(lives_text, text='Lives: ' + str(lives_remaining))

    if (lives_remaining == 0):
        window.destroy()
        messagebox.showinfo('Score board', "Game over. Your Score: " + str(score))

def moveLeft(event):
    print("moving catcher left")
    (x1,y1,x2,y2)=c.coords(catcher)
    if (x1 > 0):
        c.move(catcher, -20, 0)

def moveRight(event):
    print("moving catcher right")
    (x1,y1,x2,y2)=c.coords(catcher)
    if (x2 < 800):
        c.move(catcher, +20, 0)

def catcher_check():
    (cx1,cy1,cx2,cy2) = c.coords(catcher)
    for egg in eggs:
        (ex1,ey1,ex2,ey2) = c.coords(egg)
        if (cx1<ex1 and ex2<cx2 and cy2-ey2 < 40):
           eggs.remove(egg)
           c.delete(egg)
           inc_score(egg_score) 

    window.after(100, catcher_check)

def inc_score(s):
    global score, egg_speed, egg_interval
    score = score + s # shortform is: score +=s
    c.itemconfigure(score_text, text='Score: ' + str(score))
    egg_speed = int(egg_speed * difficulty_factor)
    egg_interval = int(egg_interval * difficulty_factor)

window.mainloop()

