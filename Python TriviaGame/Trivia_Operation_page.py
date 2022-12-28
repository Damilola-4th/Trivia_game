from tkinter import *
from random import choice
from tkvideo import tkvideo
from Gui_App_page import gameFrame
from tkinter import messagebox
from PIL import ImageTk, Image

class Trivia_game:

    def __init__(self, questions, answers, answer):
        self.questions = questions
        self.answers = answers
        self.answer = answer

class Trivia_manager:

    def __init__(self, questions_answers):
        self.questions_answers = questions_answers
        self.number = 0
        self.animation_list = ['Dancing_man.mp4', 'pendulum2.mp4', 'bouncingb_.mp4']
        #lastly time to calculate the score
        self.score = 0
        self.pictures = self.picture_list()

    #outputs the current question and its answer choice out to the screen
    def showquestions_answers(self):
        if self.number < len(self.questions_answers):
            # get current question with answer from the question_answers list in our Questions and answers set file
            curr_questionWans = self.questions_answers[self.number]
            #store the current question as an attribute(Questions) and answer as an attribute(answers) to our Trivia_game class
            Question_Answerpage = Trivia_game(curr_questionWans['Question'], curr_questionWans['Answers'], curr_questionWans['Answer'])
            # get current question and answer choices as variables to be used in this method
            curr_question, curr_answers, answer = Question_Answerpage.questions, Question_Answerpage.answers, Question_Answerpage.answer
            if Label:
                Label(gameFrame, text=curr_question).pack()
            self.radiobutton_ANSW(curr_answers, answer)
            self.number += 1
        else:
            self.clearscreen()
            user_response = messagebox.askyesno('you have completed the test', f'Your score{self.score}/8 would you like to play again:')
            #Label(gameFrame, text='THANK YOU SO MUCH FOR PLAYING :D').pack()
            self.check_userresponse(user_response)
            #Label(gameFrame, text='THANK YOU SO MUCH FOR PLAYING :D').pack()

#thinking....
    #after the game is over the function will run to check if the user wants to play the trivia game again or just close the application
    def check_userresponse(self, user_response):
        try:
            if user_response == 1:
                self.number, self.score = 0, 0
                self.showquestions_answers()
            elif user_response == 0:
                Label(gameFrame, text='THANK YOU SO MUCH FOR PLAYING :D', bg='blue').pack()
                frame = LabelFrame(gameFrame)
                frame.pack()
                Label(frame, image=choice(self.pictures)).grid(row=0,column=0)
        except:
            print('Note: Tkvideo has thrown an error because the current frame has been clreared, so when it tries to loop from the file it''ll not that it can''t find the frame anymore' )

    #outputs the answer choices as radiobutton the the GUI application
    def radiobutton_ANSW(self, curr_answers, answer):
        global var
        var = StringVar()
        var.set('O.o')
        for answ_choice in curr_answers:
            Radiobutton(gameFrame,text=answ_choice, variable=var, value=answ_choice,command=lambda: self.check(var.get(), answer)).pack(ancho=W)
    #this will clear the screen when call on
    def clearscreen(self):
        for widgets in gameFrame.winfo_children():
            widgets.destroy()

    #works to check the answer, if the answer is correct, the function will output a random animation and tally up the scroe, else if it is wrong it will show an error message box and tell the user the currect answer
    def check(self,varr, answer):
        if self.number == 4:
            #clearing animation on the fourth question to keep memore usage on a low due to the tkvideo constant looping consuming alot of memory
            self.clearscreen()
        if varr == answer:
            self.show_animation()
            self.score += 1
            self.showquestions_answers()
        elif varr != 'O.o':
            messagebox.showerror('Answer is incorrect', f'correct answer is: {answer}')
            self.showquestions_answers()

    #shows the animation onto the screen
    def show_animation(self):
        video_page = Label(gameFrame)
        label1 = Label(gameFrame, text='CORRECT!!!!!')
        video_page.pack()

        player = tkvideo(choice(self.animation_list), video_page, loop=1, size=(800, 500))
        player.play()
        label1.pack()

    #create a list from the pictures imported
    def picture_list(self):
        my_img1 = ImageTk.PhotoImage(Image.open('Chistmas_girl.png'))
        my_img2 = ImageTk.PhotoImage(Image.open('Lissandra_DHunter.jpg'))
        my_img3 = ImageTk.PhotoImage(Image.open('kiyonna.jpg'))
        my_img4 = ImageTk.PhotoImage(Image.open('The_butler.jpg'))

        return [my_img1,my_img2,my_img3,my_img4]


