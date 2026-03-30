

def register_student (students, id, name, age, program, state):
    
    students.append({
        'Id': id,
        'Name': name,
        'Age': age,
        'Program': program,
        'State': state
    })
    
    return "The student recorded successfully ✅"

def display(students):
    print("\n Students List")
    print("="*20)
    for student in students:
        print(f" Name: {student['Name']} | Age: {student['Age']} | Program: {student['Program']} | state: {student['State']}")


def search(students,id) :
    for student in students:
        if student['Id']==id:
            print("aqui")
            return student
    return None


def update(student, name, age, program, state: True):
    student['Name'] = name
    student['Age'] = age
    student['Program'] = program
    student['State'] = state
    
    return "The student update successfully ✅"

def delete(students, id):
    for student in students:
        if student['Id']==id:
            students.remove(student)
            return "The student was deleted "
    return "Any student was found with this identification number"