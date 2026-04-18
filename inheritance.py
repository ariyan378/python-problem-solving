class Student:
    
    def __init__(self,s_name,s_id):
        self.s_name= s_name
        self.s_id = s_id
        
    def Introduction(self):
        
        return f"MY name is {self.s_name} and My id is {self.s_id}"
    
class Teacher(Student):
    
    def __init__(self,s_name,s_id,marks):
        super().__init__(s_name,s_id)
        self.marks= marks
        
    def student_marks(self):
        
        return f" Student Name : {self.s_name} . Student Id :{self.s_id} . Marks :{self.marks}"
        
student=Student("Himu",378)
teacher = Teacher("Himu",378, 12)

print(teacher.student_marks())
        
        