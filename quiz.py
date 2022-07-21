from turtle import Turtle
import time


class QuizBrain(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt") as high_score_file:
            self.high_score = high_score_file.read()
        self.hideturtle()
        self.penup()
        self.speed("fastest")

    def move_text(self, x_cor, y_cor):
        self.goto(x_cor, y_cor)

    def display_text(self, answer, outcome):
        """Method that displays correct guesses in green and incorrect guesses in red"""
        if outcome == "correct":
            self.color("green")
            self.write(arg=answer, move=False, align='Center', font=('Courier', 10, 'bold'))
        elif outcome == "incorrect":
            self.color("red")
            self.write(arg=answer, move=False, align='Center', font=('Courier', 10, 'normal'))

    @staticmethod
    def display_outcome(guess, outcome):
        """Static method that checks if guess is right, wrong or already made and displays a message accordingly."""
        correct_answer = Turtle()
        correct_answer.hideturtle()
        correct_answer.speed("fastest")
        correct_answer.penup()
        correct_answer.goto(0, 0)
        if outcome == "correct":
            correct_answer.color("green")
            correct_answer.write(arg=f"Well done. Your guess of {guess} is correct!", align='Center', move=False,
                                 font=('Courier', 25, 'bold'))
        elif outcome == "incorrect":
            correct_answer.color("red")
            correct_answer.write(arg=f"Incorrect. Your guess of {guess} is wrong!", align='Center', move=False,
                                 font=('Courier', 25, 'bold'))
        elif outcome == "already guessed":
            correct_answer.write(arg=f"You already got {guess}. Try again.", align='Center', move=False,
                                 font=('Courier', 25, 'bold'))
        time.sleep(1)
        correct_answer.clear()

    def display_game_over(self, win_or_lose, score):
        """Method that takes a win/loss condition and displays a game over screen depending on win or loss"""
        game_over = Turtle()
        game_over.hideturtle()
        game_over.speed("fastest")
        game_over.penup()
        game_over.color("red")
        game_over.goto(0, -50)
        if score > int(self.high_score):
            self.high_score = score
            with open("high_score.txt", "w") as high_score_file:
                high_score_file.write(str(self.high_score))
        if win_or_lose == "win":
            game_over.color("green")
            game_over.write(arg=f"CONGRATULATIONS\n YOU HAVE WON!\n\nCorrectly guessed all {score} states",
                            align='Center', move=False, font=('Courier', 30, 'bold'))
        elif win_or_lose == "lose":
            game_over.write(
                arg=f"   GAME OVER\n OUT OF ATTEMPTS\n\nFINAL SCORE: {score}/50\n\nHIGH SCORE: {self.high_score}/50",
                align='Center', move=False, font=('Courier', 40, 'bold'))
        elif win_or_lose == "give up":
            game_over.color("black")
            game_over.write(arg=f"   YOU GAVE UP\n\nFINAL SCORE: {score}/50\n\nHIGH SCORE: {self.high_score}/50",
                            align='Center', move=False, font=('Courier', 40, 'bold'))
        time.sleep(4)
        game_over.clear()
