from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
S_FONT = ('arial', 14,)
Q_FONT = ('arial', 20, 'italic')


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("q u i z  m e")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.grid()

        self.score_label = Label(font=S_FONT, text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1, pady=(0, 20))

        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="!!!", font=Q_FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.true_image = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=self.true_image, command=self.mark_true)
        self.true_button.grid(row=2, column=0, pady=(20, 20))

        self.false_image = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=self.false_image, command=self.mark_false)
        self.false_button.grid(row=2, column=1, pady=(20, 20))

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=text)
        else:
            self.canvas.itemconfig(self.question_text, text="Finished!")
            self.false_button.config(state='disabled')
            self.true_button.config(state='disabled')

    def mark_true(self):
        user_answer = "True"
        is_right = self.quiz.check_answer(user_answer=user_answer)
        self.feed_back(is_right)

    def mark_false(self):
        user_answer = "False"
        is_right = self.quiz.check_answer(user_answer=user_answer)
        self.feed_back(is_right)

    def feed_back(self, is_right):
        if is_right == "True":
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
