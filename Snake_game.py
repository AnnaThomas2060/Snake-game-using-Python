import turtle
import time
import random


delay = 0.1
score = 0
high_score = 0
body_food_color = [ "violet", "light blue", "light green", "yellow", "orange", "red"]

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0) #turns off animation, screen updates

# Snake head
snake_head = turtle.Turtle()
snake_head.speed(0) #animation speed of turtle - fastest
snake_head.shape("square")
snake_head.color("yellow")
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "stop"

#Snake food
snake_food = turtle.Turtle()
snake_food.speed(0) #animation speed of turtle - fastest
snake_food.shape("circle")
snake_food.color("red")
snake_food.penup()
snake_food.goto(0, 100)

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-50,260)
pen.write("Score: 0   High Score: 0", align="center", font=("Courier",24,"normal"))

def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"
def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"
def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"
def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"




# Functions
def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y+20)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y-20)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x-20)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x+20)

#keyboard bindings

window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")


#main game loop
while True:
    window.update()
    #check for collision
    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        time.sleep(1)
        snake_head.goto(0, 0)
        snake_head.direction = "stop"

        #hide segments
        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()
        score = 0

        #reset delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    if snake_head.distance(snake_food) < 20: #basic turtle shapes are 20 px wide and 20px tall
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        #a = random.randint(0, len(body_food_color)-1)
        #Snake_food.color("red")
        snake_food.goto(x, y)

        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        a = random.randint(0, len(body_food_color) - 1)
        new_segment.color(body_food_color[a])
        new_segment.penup()
        segments.append(new_segment)

        #shorten delay
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center",  font=("Courier",24,"normal"))

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

        #move segment zero to where head is
    if len(segments) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        segments[0].goto(x, y)

    move()

    #check for head collisions
    for segment in segments:
        if segment.distance(snake_head) < 20:
            time.sleep(1)
            snake_head.goto(0,0)
            snake_head.direction = "stop"

            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()
            score=0

            #reset delay
            delay = 0.1
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

window.mainloop()

