import pandas , turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_data = pandas.read_csv("50_states.csv")
data = state_data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}Guess the Sate",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        customer_list = []
        for state in data:
            if state not in guessed_states:
                customer_list.append(state)
        df = pandas.DataFrame(customer_list)
        df.to_csv("states_to_learn_csv")

    if answer_state in data:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_x = int(state_data[state_data.state == answer_state].x)
        state_y = int(state_data[state_data.state == answer_state].y)
        t.goto(state_x,state_y)
        t.write(answer_state)

screen.exitonclick()

#def get_mouse_click_coor(x, y):
#   print(x, y)

#turtle.onscreenclick(get_mouse_click_coor) 마우스 클릭시 좌표값 구하는 함수


