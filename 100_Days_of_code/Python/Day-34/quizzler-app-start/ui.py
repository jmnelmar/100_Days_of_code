THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.is_game_end = False

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="some Question Text", 
            fill=THEME_COLOR,
            font=("Arial",20,"italic")
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def get_next_question(self):
        q_text=""
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.get_score()
        else:
            self.get_score()
            q_text = f"Game over\n Final Score {self.quiz.score}/10"
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.is_game_end = True
        self.set_bg_white()

    def true_pressed(self):
        self.answer_bg(self.quiz.check_answer("True"))
        

    def false_pressed(self):
        self.answer_bg(self.quiz.check_answer("False"))
        

    def answer_bg(self, answer:bool):
        if self.is_game_end == False:
            if answer:
                self.canvas.config(bg="green")
            else:
                self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)
        
    def set_bg_white(self):
        self.canvas.config(bg="white")
        