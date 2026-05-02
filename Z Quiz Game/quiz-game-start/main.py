from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]

# I did this
# for i in range (len(question_data)):
#     q1=Question(question_data[i]["text"],question_data[i]["answer"])
#     question_bank.append(q1)
#
# print(question_bank)

for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=Question(question_text,question_answer)                #Object created
    question_bank.append(new_question)

# print(question_bank)
# print(question_bank[4].answer)

quiz=QuizBrain(question_bank)
# quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()                            #if it still has question then go to the next question.

print("\n\n\nYou've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")