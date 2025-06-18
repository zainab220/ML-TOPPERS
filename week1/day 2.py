# task A
  class student:
    def __init__(x,name,age,grades):
        x.name=name
        x.age=age
        x.grades=grades
        
    def add_grade(x,subject,marks):
        x.grades[subject]=marks
        
    def calcAvg(x):
        return sum(x.grades.values())/len(x.grades)
        
    def assign_grades(x):
        avg=x.calcAvg()
        if avg>=80:
            return "A"
        elif 60<avg<=79:
            return "B"
        elif 40<avg<=59:
            return "C"
        else: 
            return "F"
    
    bonus = staticmethod(lambda grades: {subject: min(marks+5,100) for subject, marks in grades.items()})
    
    def generaterep(x):
        print(f"name: {x.name}")
        print(f"age: {x.age}")
        print("grades: ")
        for subject, marks in x.grades.items():
            print(f" {subject}:{marks}")
        avg= x.calcAvg()
        grade= x.assign_grades()
        print(f"average: {avg}")
        print(f"grade: {grade}")
        
    def savetofile(x,filename):
        with open(filename, 'w') as file:
            file.write(f"Name: {x.name}\n")
            file.write(f"Age: {x.age}\n")
            file.write("Grades:\n")
            for subject, marks in x.grades.items():
                file.write(f"  {subject}: {marks}\n")
            avg = x.calcAvg()
            grade = x.assign_grades()
            file.write(f"Average Marks: {avg}\n")
            file.write(f"grade: {grade}\n")
    
    @staticmethod
    def readfromfile(filename):
        with open(filename,"r") as file:
            con=file.read()
            print(con)
            
s1 = student("Ali", 17, {"Math": 78, "English": 85})
s1.add_grade("Science", 90)
s1.grades = student.bonus(s1.grades)
s1.generaterep()
s1.savetofile("report.txt")
student.readfromfile("report.txt")
