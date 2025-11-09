# welcome to project 
import csv
class Student:
  def __init__(self,roll,name,age,course):
    self.roll= roll
    self.name= name
    self.age= age
    self.course= course

class StudentManager:
  def __init__(self,filename="students.csv"):
    self.filename= filename
    
  def add_student(self):
    roll= int(input("Enter your roll no : "))
    name= input("Enter Your name : ")
    age = int(input("Enter your age : "))
    course = input("Enter Your Course : ")
    
    student= Student(roll,name,age,course)
    
    with open(self.filename,"a",newline="") as file:
      writer= csv.writer(file)
      writer.writerow([student.roll,student.name,student.age,student.course])
      print(f"\n Student '{student.name}' added successfully!\n")
  
  def view_students(self):
    try:
      with open(self.filename,"r") as file:
        reader= csv.reader(file)
        students = list(reader)
        
        if not students:
          print("\n no student records found \n")
          return
        print("\n All Studnets\n")
        
        print("{:<10} {:<15} {:<5} {:<10}".format("Roll","Name","Age","Course"))
        print("-"*45)
        
        for s in students:
           print("{:<10} {:<15} {:<5} {:<10}".format(s[0], s[1], s[2], s[3]))
    
    except FileNotFoundError:
      print("\n No student records found add some first\n")
      
  def menu(self):
    while True:
      print("=== Student Management System ===")
      print("1.Add Student")
      print("2. Search Student")
      print("3. Update Student")
      print("4. View Students")
      print("5. Delete Student ")
      print("6. Exit ")
      
      c = int(input("Enter Your Choice :"))
      
      if c == 1:
        self.add_student()
      elif c== 2:
        print("Vidya add you")
      elif c== 3:
        print("Vidya add you")
      elif c== 4:
        self.view_students()
      elif c== 5:
        print("Vidya add you")
      elif c== 6:
        print("\n Exiting........")
        break
      else:
        print("\n Invaild Choice")
if __name__ == "__main__"     :
  manager= StudentManager()
  manager.menu()