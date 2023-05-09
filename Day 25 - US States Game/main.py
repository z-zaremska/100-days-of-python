import pandas as pd
import turtle

states = pd.read_csv('50_states.csv', index_col='state')

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

guessed_states = []

counter = 0
game_on = True
while game_on:
    answer_state = screen.textinput(title=f'Guess the state ({counter}/50)', prompt="What's another state's name")
    # If answer is correct and did not occur yet display it's name on the map
    if answer_state.title() in states.index and answer_state not in guessed_states:
        counter += 1
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        x = states.loc[answer_state, 'x']
        y = states.loc[answer_state, 'y']
        state.goto((x, y))
        state.write(f'{answer_state.title()}', align='center')
        guessed_states.append(answer_state)
    # If answer already was given continue
    elif answer_state in guessed_states:
        continue
    # If state doesn't exist end the game and display the score.
    else:
        game_on = False
        game_over = turtle.Turtle()
        game_over.hideturtle()
        game_over.penup()
        game_over.write(f"You've guessed {counter} out of 50 states.", align='center')


screen.exitonclick()
