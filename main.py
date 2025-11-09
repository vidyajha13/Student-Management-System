# welcome to project Student Management System
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