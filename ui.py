from tkinter import *
from quizbrain import QuizBrain

GREY = "#393e46"
BLACK = "#222831"
WHITE = "#EEEEEE"
GREEN = "#61b15a"
ORANGE = "#db6400"
FONT = ("Arial", 12, "normal")
CANVAS_FONT = ("Arial", 18, "italic")
DELAY = 1000


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.wd = Tk()
        self.wd.title("Quizzy")
        self.wd.config(padx=20, pady=20, bg=GREY)
        self.score = Label(text="Score:", fg=WHITE, bg=GREY, font=FONT)
        self.score.grid(column=1, row=0)
        self.canvas = Canvas(height=250, width=300, bg=BLACK, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Quiz Text",
            fill=WHITE,
            font=CANVAS_FONT
        )
        self.false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(
            image=self.false_img,
            bg=GREY,
            highlightthickness=0,
            activebackground=ORANGE,
            command=self.true_press
        )
        self.false_btn.grid(column=1, row=2)

        self.true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(
            image=self.true_img,
            bg=GREY,
            highlightthickness=0,
            activebackground=ORANGE,
            command=self.false_press
        )
        self.true_btn.grid(column=0, row=2)

        self.get_next_question()

        self.wd.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=BLACK)
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_press(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_press(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=ORANGE)
        self.wd.after(1000, self.get_next_question)

