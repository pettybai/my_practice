# 把方法变成属性
# @property

class Exam(object):
    def __init__(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score
    


class Exam_Propery(object):
    def __init__(self, score):
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score


exam = Exam(90)
print(exam.get_score())
exam.set_score(80)
print(exam.get_score())

exam_new = Exam_Propery(70)
print(exam_new.score)
exam_new.score=60
print(exam_new.score)
