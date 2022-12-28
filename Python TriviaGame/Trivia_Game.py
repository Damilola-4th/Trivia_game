from Questions_and_answer_set import questions_answers #going to pass the question and answers list into Trivia Manager
from Trivia_Operation_page import Trivia_manager
from Gui_App_page import root

#starts the trivia game by calling the showquestions_answers method in the trivia_manager
trial = Trivia_manager(questions_answers)
trial.showquestions_answers()

root.mainloop()

