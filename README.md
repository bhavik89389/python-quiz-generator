# python-quiz-generator

the quiz generoator here is written in parts and using import function we combined all the parts to the main() file which is quiz.py
each .py file in this repository do its own part of work
all the .py files together make the final output file 
1. data.py:
this  programme is used to link an API and get the questions to display in our programme
brief explantion:
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
This line sends an HTTP GET request to the Open Trivia Database API (https://opentdb.com/api.php) with the specified query parameters.
2.model
 a.The Question class is designed to represent a single trivia question and its answer.
 b.When an object of the Question class is created, the __init__ method initializes the text (question) and answer attributes using the values passed as arguments (q_text and q_answer).
 c.This allows you to create and store multiple trivia questions and answers using the Question class.
3.quiz brain:
this programme acts as the brain of the programme it saves the answer finds whether the answer is right or wrong
The QuizBrain class manages the flow of a trivia quiz, including keeping track of the current question, checking answers, and updating the score.
Key Functions:
 a.still_has_questions(): Checks if there are more questions to ask.
 b.next_question(): Retrieves and formats the next question for the user.
 c.check_answer(): Compares the user's answer with the correct answer and updates the score accordingly.
4.ui.py
this python file is used to make user friendly interface HTML is called in this file and designing is done

5. quiz.py
as stated before this is the main part of the generator it calls all the other sub programmes and displays it to the user according to situation
 a.Data Preparation: The question_data is used to create Question objects, which are stored in the question_bank list.
 b.Quiz Setup: The QuizBrain class is instantiated with the question_bank, and a QuizUI is created for handling the user interface.
 c.Quiz Execution: The quiz is run inside a loop where questions are presented one-by-one. The user answers each question, and the quiz keeps track of the score.
 d.End of Quiz: After all questions are answered, the final score is displayed.
