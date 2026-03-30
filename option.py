from processes import register_student,search, delete, update, display
from validation import get_non_empty_text, get_positive_number
from csv_manager import save_csv

# option : Register
def option_1(students):
    id=get_positive_number("Enter the Student identification: ")
    name=get_non_empty_text("Enter the name of the student: ")
    age=get_positive_number("Enter the age of the student: ")
    program=get_non_empty_text("Enter the program name: ")
    state=True
    
    result=register_student(students, id, name, age, program, state)
    print(result)

# option : Viw Students list 
def option_2 (students):
    if students:
        display(students)
    else:
        print("No information has been saved")

# option : Search Student
def option_3(students):
    id=get_positive_number("which students are you looking? write the Id: ")
    result=search(students, id)
    
    if result!= None:
        print(f"Student: {result['Name']} | Program: {result['Program']}")
    else :
        print("Any student was found with this identification number")
        
# option : Update student Information
def option_4(students):
    id=get_positive_number("Enter the Student identification: ")
    result="Any student was found with this identification number"
    for student in students:
        if student['Id']==id:
            name=get_non_empty_text("Enter the name of the student: ")
            age=get_positive_number("Enter the age of the student: ")
            program=get_non_empty_text("Enter the program name: ")
            validate = True
            while validate:
                option = input("\n If the student is Active enter T if, on the other hand, enter F "
                ).strip().upper()
                if option in ["T", "F"]:
                    validate=False
                else:
                    print("\n Please enter T or F")
            if option == "T":
                   state=True
            else : state=False
            
            result=update(student, name, age, program, state)
            
    print(result)

# option : Delete a student
def option_5(students):
    id=get_positive_number("which students do you want to delete? Write the Id: ")
    result=delete(students, id)
    print(result)

# option : Save CSV"
def option_6(students):
      # By default, The inventory.csv file is where I store the information when the user selects the option 
      print(save_csv(students, "students.csv"))