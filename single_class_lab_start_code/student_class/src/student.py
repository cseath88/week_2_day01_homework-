class Student:
    def __init__(self, input_name, input_cohort):
        self.student_name = input_name
        self.cohort = input_cohort

    def get_name(self):
        return self.student_name
    
    def get_cohort(self):
        return self.cohort
    
    def set_cohort(self, cohort):
        self.cohort = cohort

    def student_talk(self):
        return "I can talk!"
    
    def say_favourite_language(self, input_language):
        if input_language == "Python":
            return "I love Python"
        






