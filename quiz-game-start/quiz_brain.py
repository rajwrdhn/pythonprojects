class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        
        self.check_answer(ans, current_question.answer)

    def questions_remain(self):
        l_q_list = len(self.question_list)

        if self.question_number < l_q_list:
            return True
        else:
            return False
    
    def check_answer(self, ans, correct_ans):
        if ans.lower() == correct_ans.lower():
            self.score += 1
            print("You got it right!")
            print(f"Your current score is: {self.score}/{self.question_number}.")
        else:
            print("That's Wrong!")
        
        print(f"The correct answer was: {correct_ans}.")