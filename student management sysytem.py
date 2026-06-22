students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update student")
    print("6. exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        student = {
            "Roll No": roll_no,
            "Name": name,
            "Marks": marks
        }

        students.append(student)
        with open("student.txt","a")as file:
            file.write(f"{roll_no},{name},{marks}\n")
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for student in students:
                print("----------------------")
                print("Roll No:", student["Roll No"])
                print("Name:", student["Name"])
                print("Marks:", student["Marks"])

    elif choice == "3":
        search_roll = input("Enter Roll Number to search: ")

        found = False
        for student in students:
            if student["Roll No"] == search_roll:
                print("\nStudent Found")
                print("Roll No:", student["Roll No"])
                print("Name:", student["Name"])
                print("Marks:", student["Marks"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        delete_roll = input("Enter Roll Number to delete: ")

        found = False
        for student in students:
            if student["Roll No"] == delete_roll:
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "5":
        update_roll =input("enter roll number to update:")      
        found=False
        for i in students:
            if i["Roll No"] == update_roll:
                new_name=input("enter new name:")
                new_marks=input("enter new marks:")

                i["Name"]=new_name
                i["Marks"]=new_marks

                print("student record updated successfully!")
                found=True
                break
            if not found:
                print("student not found.")

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")