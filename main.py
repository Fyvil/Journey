import turtle
import pandas
from quiz import QuizBrain

CORRECT_GUESSES = 0
NUM_ATTEMPTS = 5

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("U.S. States Quiz by Prajit")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

quiz = QuizBrain()
states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.tolist()
new_states_list = []

game_on = True
while game_on:
    # Prompting user to guess the name of a state
    if NUM_ATTEMPTS == 1:
        guess = screen.textinput(title=f"Guess a state name!",
                                 prompt=f"{CORRECT_GUESSES} / 50 states guessed\nONLY 1 INCORRECT ATTEMPT LEFT!").title().strip()
    else:
        guess = screen.textinput(title=f"Guess a state name!",
                                 prompt=f"{CORRECT_GUESSES} / 50 states guessed\nIncorrect attempts left: {NUM_ATTEMPTS}").title().strip()
    screen.listen()

    # Checking if user wants to quit program
    if guess == "Exit":
        game_on = False

    # Checking if guess is correct and displaying the correct guess on the map
    elif guess in states_list:
        CORRECT_GUESSES += 1
        quiz.display_outcome(guess, "correct")

        # Checking if user has won a.k.a. guessed all 50 states correctly
        if CORRECT_GUESSES == 50:
            quiz.display_game_over("win", CORRECT_GUESSES)
            game_on = False

        # Moving the correct guess to the corresponding location of guessed state
        quiz.move_text(int(states_data[states_data.state == guess].x),
                       int(states_data[states_data.state == guess].y))
        quiz.display_text(guess, "correct")
        new_states_list.append(guess)
        states_list.remove(guess)

    # Checking if guess has already been made
    elif guess in new_states_list:
        quiz.display_outcome(guess, "already guessed")
        continue

    # If user hasn't input text, prompt the user again
    elif guess == "":
        continue

    # Displaying incorrect guess and checking if game over a.k.a. user ran out of attempts
    else:
        if NUM_ATTEMPTS <= 1:
            quiz.display_outcome(guess, "incorrect")
            quiz.display_game_over("lose", CORRECT_GUESSES)
            for states in states_list:
                # sending text to x and y coordinates of guess via move_text method
                quiz.move_text(int(states_data[states_data.state == states].x),
                               int(states_data[states_data.state == states].y))
                quiz.display_text(states, "incorrect")
            game_on = False
        elif guess == "Give Up":
            quiz.display_game_over("give up", CORRECT_GUESSES)
            for states in states_list:
                quiz.move_text(int(states_data[states_data.state == states].x),
                               int(states_data[states_data.state == states].y))
                quiz.display_text(states, "incorrect")
            game_on = False
        elif NUM_ATTEMPTS > 1:
            quiz.display_outcome(guess, "incorrect")
        NUM_ATTEMPTS -= 1
        continue


# Creating a new csv file from missing states
x_cor_list = [int(states_data[states_data.state == states].x) for states in states_list]
y_cor_list = [int(states_data[states_data.state == states].y) for states in states_list]

missed_states = {
    "Missed State": states_list,
    "x": x_cor_list,
    "y": y_cor_list
}

missed_states_data = pandas.DataFrame(missed_states)
missed_states_data.to_csv(f"missing_states_data.csv")
# print(pandas.read_csv("missing_states_data.csv"))
turtle.mainloop()
