THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:

    def sendtrue(self):
        is_right= self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def sendfalse(self):
        is_right= self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.score.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)


    def __init__(self, quizbrain:QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, pady=50)
        self.window.title("Quizzler")
        self.canvas = Canvas(bg="white", height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, font=("Arial",20, "italic"), text="test", width =280)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.score = Label(text="Score:", fg="white")
        self.score.config(bg=THEME_COLOR)
        self.score.grid(row=0, column=1, padx=20, pady=20)
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.sendtrue)
        self.true_button.grid(row=2, column=0)

        false_image= PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.sendfalse)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):

        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz motha fucka ")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
