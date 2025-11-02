# NAME - SHOURYA AWASTHI
# DATE - 2024-06-15
#Roll No. - 2501350073
# DESCRIPTION - This module defines a Gradebook class to manage student grades.
print ("Welcome to the Gradebook Management System")
print("Enter 1 for manual input or 2 for csv file input")
if_choice = int(input("Your choice: "))
if if_choice == 2:
    import csv
    def csv_input_of_students():
        name = []
        marks = []
        file_name = input("Enter the CSV file name (with .csv extension): ")
        try:
            with open(file_name, mode ='r')as file:
                csvFile = csv.reader(file)
                for lines in csvFile:
                    name.append(lines[0])
                    marks.append(int(lines[1]))                                              #csv file input of names and marks input
        except FileNotFoundError:
            print("File not found. Please check the file name and try again.")
            return [], []
        return name, marks
    name, marks = csv_input_of_students()
elif if_choice == 1:
 def manual_input_of_students():
    name = []
    marks = []
    no_of_students = int(input("Enter the number of students: "))
    print(" ")
    for i in range(no_of_students):                                                          #manual input of names and marks
        student_name = input(f"Enter the name of student {i + 1}: ")
        student_marks = int(input(f"Enter the marks of student {i + 1}: "))
        name.append(student_name)
        marks.append(student_marks)
        print(" ")
    return name, marks
 def calculate_average(marks):
    for mark in marks:
        if mark < 0 or mark > 100:
            print("Invalid marks entered. Marks should be between 0 and 100.")                     #calculating average of marks
            return None
    total = 0
    for i in range(len(marks)):
        total += marks[i]
    average = total / len(marks)
    return average
 name, marks = manual_input_of_students()
 average= calculate_average(marks)
 print(f"The average marks are: {average}")
 print(" ")
 def median_of_Marks(marks):
    median_marks = sorted(marks)
    if len(median_marks) % 2 == 0:                                                                        #calculating median of marks
        i = len(median_marks) // 2
        return (median_marks[i - 1] + median_marks[i]) / 2
    else:
        i = len(median_marks) // 2
        return median_marks[i]
 print(f"The median marks are:{median_of_Marks(marks)}")
 def grade_of_marksof_all_students(marks):
    grades = []                                                                                       #Giving grades based on marks
    for mark in marks:
        if 100>= mark >= 90:
            grades.append('A')
        elif mark >= 80: 
            grades.append('B')
        elif mark >= 70:
            grades.append('C')
        elif mark >= 60:
            grades.append('D')
        elif mark >= 40:
            grades.append('F')
        elif mark < 40:
            grades.append('Student has failed')
    return grades
 def printing_name_marks_grades(name, marks, grades):
    print("\n------------------------------------------")                                  #printing names, marks and grades of all students
    print (f"{'name':<20} {'marks':<10} {'grades':<10}")
    print("-----------------------------------------")
    for i in range(len(name)):
        print(f"{name[i]:<20} {marks[i]:<10} {grades[i]:<10}")
    print("-----------------------------------------")
    print(" ")
 printing_name_marks_grades(name, marks, grade_of_marksof_all_students(marks))
 def Comparing_highest_lowest_marks(marks,name):
    if marks:
        highest = max(marks)
        lowest = min(marks)
        highest_student = name[marks.index(highest)]                                   #finding highest and lowest marks along with student names
        lowest_student = name[marks.index(lowest)]
        print(f"Highest marks are {highest} from {highest_student}")
        print(f"Lowest marks are {lowest} from {lowest_student}")
    else:
        print("No marks available for comparison.")
 Comparing_highest_lowest_marks(marks,name)
 def Passed_Failed_students_Details(marks,name):                                
    passed_students = []
    failed_students = []
    for i in range(len(marks)):
        if marks[i] >= 40:                                                              #separated passed and failed students
            passed_students.append((name[i]  , marks[i]))
        else:
            failed_students.append((name[i]  , marks[i]))
    print("\nPassed Students:")
    if passed_students:
        for name, marks in passed_students:
            print(f"  {name:<20} {marks}")
    else:
        print("  None")
    print("\nFailed Students:")
    if failed_students:                                                                     #printing details of passed and failed students
        for name, marks in failed_students:
            print(f"  {name:<20} {marks}")
    else:
        print("  None")
 Passed_Failed_students_Details(marks,name)
else:
    print("Invalid choice. Please enter 1 or 2.")
print("Thank you for using the Gradebook Management System")                   

        