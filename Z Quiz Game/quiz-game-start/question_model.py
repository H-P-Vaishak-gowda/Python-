# class Question:
#
#     def __init__(self):
#         self.text = text              *There is no way to recieve text value from object(new_question)becoz u know why.
#         self.answer = answer
# new_question=Question("abcdefghij","True")

class Question:

    def __init__(self,q_text,q_answer):             #Now it can recieve values
        self.text=q_text
        self.answer=q_answer
