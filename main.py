import turtle

import pandas
import os
image = os.path.join(os.path.dirname(__file__), "blank_states_img.gif")

import os
csv_path = os.path.join(os.path.dirname(__file__), "50_states.csv")
data = pandas.read_csv(csv_path)

screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape(image)
turtle.shape(image)


all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_states = screen.textinput(title="Guess the state", prompt="What's another state's name?")

    if answer_states =="Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
#IF answer_state is one of the status in all the states of the 50_states.csv
    if answer_states in all_states:
        guessed_states.append(answer_states)
    #If they got it right:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_states]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_states)
    #CREATE A turtle to write the name of the state at the state's x and y coordate

