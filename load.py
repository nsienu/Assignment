from teacher import Teacher

class Load(Teacher):
    def __init__(self, subject):
        self.subject = subject

    def getProfsubject(self):
        return f'{self.subject}'
