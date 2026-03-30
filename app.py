from validation import get_positive_number
from System import menu
to_continue=True
students=[]

while to_continue:
    
    print("\nStudent Register System")
    print("*"*30)
    print("1. Register new Students")
    print("2. Display Student List")
    print("3. Search a Student")
    print("4. Update the Information Student")
    print("5. Delete a student")
    print("6. Save CSV")
    print("7. Close the System ")
    
    try:
     opcion = int(get_positive_number("\n Select a menu option: "))
     if opcion in menu:
        menu[opcion](students)
     elif opcion==7:
        print("\nClosing section... ")
        to_continue=False
     else: 
        print("The option is invalid ")
     
    except ValueError :
       print("Invalid value")