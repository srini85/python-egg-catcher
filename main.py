from tkinter import *
from itertools import cycle

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
egg_score = 10
egg_speed = 500
egg_interval = 4000
difficulty_factor = 0.95

# As homework, we need to create a function called create_eggs
# For the time being, the create_eggs function should be called and should 
# print a message to say "eggs being created"
# we should call the function we created after we have logged in successfully
# Hint: You should call the create_eggs function after the line print(user)

c.pack()

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

window.mainloop()

