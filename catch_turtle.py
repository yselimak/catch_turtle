import turtle
import random

#catch the turtle - kaplumbayı yakala!

#create screen
turtle_game_board = turtle.Screen()
turtle_game_board.title("Catch the Turtle")
turtle_game_board.bgcolor("purple")

FONT = ('Arial', 30 , 'normal')
score = 0
game_over = 0

#create timer turtle
timer_turtle = turtle.Turtle()

#crate score turtle
score_turtle = turtle.Turtle()
def setup_score_turtle():
    score_turtle.hideturtle() #turtle'ı gizlemeye yarar
    score_turtle.color("white")
    score_turtle.penup() #hiçbir zaman çizmez

    #y position
    y_height = turtle_game_board.window_height()
    y = y_height*0.8
    score_turtle.setposition(0,y/2)

    #writing
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)

grid_size = 10
turtle_lists = []
def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x,y):
        global score
        score+=1
        score_turtle.clear()
        score_turtle.write(arg="Score : {}".format(score), move=False, align="center", font=FONT)
    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("yellow")
    t.goto(x*grid_size,y*grid_size)
    turtle_lists.append(t)

#create 5*5 grid
def setup_turtle():
    for i in range(5):
        for j in range(5):
            make_turtle(-20+(j*10), 20-(i*10))

def hide_turtle():
    for t in turtle_lists:
        t.hideturtle()

def show_turtle_random():
    if game_over==0:
        hide_turtle()
        a = random.randint(0,21)
        turtle_lists[a].showturtle()
        turtle_game_board.ontimer(show_turtle_random, 500)
        turtle_game_board.ontimer(hide_turtle, 500)
    else:
        return 0

def action_timer_turtle(time):
    timer_turtle.hideturtle()
    timer_turtle.penup()
    timer_height = turtle_game_board.window_height()
    y_timer = timer_height * 0.7
    timer_turtle.setposition(0, y_timer / 2)
    timer_turtle.clear()
    if time>0:
        timer_turtle.clear()
        timer_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        turtle_game_board.ontimer(lambda : action_timer_turtle(time-1),1000)
    else:
        global game_over
        game_over = 1
        timer_turtle.clear()
        hide_turtle()
        timer_turtle.write(arg="GAME OVER!", move=False, align="center", font=FONT)


turtle.tracer(0)
setup_turtle()
setup_score_turtle()
hide_turtle()
show_turtle_random()
action_timer_turtle(5)
turtle.tracer(1)

#the game shouldn't close
turtle_game_board.mainloop()