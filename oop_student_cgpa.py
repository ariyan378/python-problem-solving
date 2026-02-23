         
              
class student:
    
    def __init__(self , name , age , gender , grade = None):
        
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__grade = grade or {}
        
    def __set_grades (self,course , grade):
        
        self.__grade[course] = grade
    
    def get_grade(self, course):
        return self.__grade[course]       
            
            
    def get_CGPA(self):
        return sum (self.__grade.values())/len(self.__grade)
    
 
HIMU = student('Himu' , 23, 'Male',{"Compiler" : 3.5})
print(HIMU.get_grade('Compiler'))            