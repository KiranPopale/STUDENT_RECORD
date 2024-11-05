import os
os.system('cls')
import pandas as pd

class student:
    No_of_studnets=0
    def __init__(self):
        avg=0
        self.student_count()


    def getinfo(self):
        self.name=input("Enter Name of Student: ")
        self.roll=int(input("Enter Roll Number of Student: "))
        self.math=int(input("Enter Marks of Mathematics of Student: "))
        self.sci=int(input("Enter Marks of Science of Student: "))
        self.eng=int(input("Enter Marks of English of Student: "))
        self.avg=int((self.math+self.sci+self.eng)/3)
        

    @classmethod
    def student_count(cls):
        cls.No_of_studnets+=1
        

n=int(input("Enter Number of Students: "))
student_list=[]
student_name=[]
student_roll=[]
student_math_marks=[]
student_sci_marks=[]
student_eng_marks=[]
student_avg=[]
student_info={}

for i in range (0,n):
    newstudent=student()
    newstudent.getinfo()
    student_list.append(newstudent)

for obj in student_list:
    student_name.append(obj.name)
    student_roll.append(obj.roll)
    student_math_marks.append(obj.math)
    student_sci_marks.append(obj.sci)
    student_eng_marks.append(obj.eng)
    student_avg.append(obj.avg)

student_info={"Name of Students":student_name,
              "Roll Number of Students": student_roll,
              "Mark in Mathematics":student_math_marks,
              "Mark in Science":student_sci_marks,
              "Mark in English":student_eng_marks,
              "Average of Marks":student_avg}
#              "Total Students":student.No_of_studnets}

print(f"\n*****Result of {student.No_of_studnets} Students*****")
df=pd.DataFrame(student_info)
print("\n",df)

df.to_csv("Student_Data.csv")
df.to_excel("Student_data.xlsx")