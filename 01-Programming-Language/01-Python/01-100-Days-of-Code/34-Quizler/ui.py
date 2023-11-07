from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        img_true = PhotoImage(file="01-Programming-Language\\01-Python\\01-100-Days-of-Code\\34-Quizler\\images\\true.png")
        img_false = PhotoImage(file="01-Programming-Language\\01-Python\\01-100-Days-of-Code\\34-Quizler\\images\\false.png")
        # img_true = PhotoImage(file="34-Quizler\\images\\true.png")
        # img_false = PhotoImage(file="34-Quizler\\images\\false.png")

        ## Canvas
        self.canvas = Canvas(width=300,height=250,highlightthickness=0,bg="white")
        self.question_text = self.canvas.create_text(150,125,text="Question Text Here...",font=("Arial",15,"italic"),width=280)

        ## Label
        self.label_score = Label(text=f"Score: 0",bg=THEME_COLOR,fg="white",font=("Arial",10,"bold"))

        ## Buttons
        self.button_true = Button(image=img_true,highlightthickness=0,command=self.true)
        self.button_false = Button(image=img_false,highlightthickness=0,command=self.false)

        ## Grid
        self.label_score.grid(column=1,row=0)
        self.canvas.grid(column=0,row=1,columnspan=2, pady=20)
        self.button_false.grid(column=1, row=2, pady=20)
        self.button_true.grid(column=0, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            q_text = "You have come to the end of the Quiz!"
            self.canvas.itemconfig(self.question_text,text=q_text)
            self.button_false.config(state="disabled")
            self.button_true.config(state="disabled")

    def true(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)
        self.label_score.config(text=f"Score: {self.quiz.score}")


    def false(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)
        self.label_score.config(text=f"Score: {self.quiz.score}")


    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)