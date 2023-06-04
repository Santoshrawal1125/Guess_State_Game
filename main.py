import turtle
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

data = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
guessed_state = []
state_list = data["state"].to_list()
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state's "
                                                                                            "name? ").title()
    if answer_state == "Exit":
        missing_state = []
        for state in state_list:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("missing states.csv")

        break

    if answer_state in state_list:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row = data[data.state == answer_state]
        t.goto(int(state_row.x), int(state_row.y))
        t.write(answer_state)


