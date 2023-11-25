import pandas
import turtle


FONT = ("Courier", 8, "normal")


# create the screen
screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
# create a new shape
screen.addshape(image)
turtle.shape(image)

# make a list of states from 50_states.csv
data = pandas.read_csv("50_states.csv")
states = data["state"]
states_as_list = data["state"].to_list()
# print(states_as_list)

game_is_on = True
correct_answers = 0
guessed_states = []
not_guessed = data["state"].to_list()


while correct_answers < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in states_as_list and answer_state not in guessed_states:
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        correct_answers += 1
        guessed_states.append(answer_state)
        not_guessed.remove(answer_state)
        correct_state = data[data["state"] == answer_state]
        # print(correct_state)

        # get the coordinates of the state
        x_coordinate = int(correct_state.x.item())
        y_coordinate = int(correct_state.y.item())
        writer.goto(x_coordinate, y_coordinate)
        writer.write(arg=answer_state, align="Center", font=FONT)
        # break

# turtle.mainloop()
missing_states = pandas.DataFrame(not_guessed)
missing_states.to_csv("states_to_learn.csv")
