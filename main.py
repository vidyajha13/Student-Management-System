# welcome to project Student Management System
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
  def search_student(self):
        roll = input("Enter Roll No to Search: ")
        found = False
        try:
            with open(self.filename, "r") as f:
                reader = csv.reader(f)
                for s in reader:
                    if s and s[0] == roll:
                        print(f"\n Found Roll: {s[0]}, Name: {s[1]}, Age: {s[2]}, Course: {s[3]}\n")
                        found = True
                        break
            if not found:
                print(" Student not found!")
        except FileNotFoundError:
            print("No records found.")
  def update_student(self):
        roll = input("Enter Roll No to Update: ")
        try:
            with open(self.filename, "r") as f:
                students = list(csv.reader(f))
            updated = False
            for s in students:
                if s and s[0] == roll:
                    print(f"Current: {s}")
                    s[1] = input("Enter New Name (leave blank to keep same): ") or s[1]
                    s[2] = input("Enter New Age (leave blank to keep same): ") or s[2]
                    s[3] = input("Enter New Course (leave blank to keep same): ") or s[3]
                    updated = True
                    break
            if updated:
                with open(self.filename, "w", newline="") as f:
                    csv.writer(f).writerows(students)
                print("✅ Record updated!\n")
            else:
                print(" Student not found!\n")
        except FileNotFoundError:
            print("No records found.\n")
  def delete_student(self):
        roll = input("Enter Roll No to Delete: ")
        try:
            with open(self.filename, "r") as f:
                students = list(csv.reader(f))
            new_students = [s for s in students if s and s[0] != roll]
            if len(new_students) != len(students):
                with open(self.filename, "w", newline="") as f:
                    csv.writer(f).writerows(new_students)
                print("Student deleted!\n")
            else:
                print("Student not found!\n")
        except FileNotFoundError:
            print("No records found.\n")
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
        self.search_student()
      elif c== 3:
        self.update_student()
      elif c== 4:
        self.view_students()
      elif c== 5:
        self.delete_student()
      elif c== 6:
        print("\n Exiting........")
        break
      else:
        print("\n Invaild Choice")
if __name__ == "__main__":
  manager= StudentManager()
  manager.menu()

