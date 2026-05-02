class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score =0

    """Challenge2: Create method called still_has_questions().
        Return a boolean depending on the value of question_number.
        Use the While loop to show the next question untill the end. """

    def still_has_questions(self):
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     False
        """Or simply to return boolean value u can do like this"""
        return self.question_number < len(self.question_list)



    """Challenge1: Retrieve the item at the currents question_number from the question_list.
    use the input() function to show the user the question text and ask for the user's answer. """

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number +=1
        user_answer=input(f"Q.{self.question_number}: {current_question.text} (True/False):  ")
        self.check_answer(user_answer,current_question.answer)



    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")

        else:
            print("That's! wrong.")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")


    """Add a score class, increment it 1 everytime user gets a right answer"""


