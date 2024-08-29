from quizdata import question_data
from question_model import Question
from quiz_brain import QuizBrain



questionBank = []
for question in question_data:
    q_text = question['text']
    q_answer = question['answer']
    q = Question(q_text, q_answer)
    questionBank.append(q)

quiz = QuizBrain(questionBank)

while quiz.has_questions_left():
    quiz.next_question()


print(f"You've completed the quiz! Your final score was {quiz.score}/{quiz.question_number}")
