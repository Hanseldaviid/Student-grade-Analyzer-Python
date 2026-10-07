
# Degrees
def name_user():
    name = input("Insert name of student: ").strip()
    return name
    
def ask_note():
    while True:
        try:
            note = float(input("Insert note of student: (0.0 - 5.0) "))
            if note < 0.0 or note > 5.0:
                print("Insert something valid")
            else:
                print("Note added successfully ")
            return note
        except ValueError:
            print("Insert only numbers")  
        
def calculate_avarage(students): # Calculate the note of all the students
    if not students:
        return 0
    else:
        total = 0
        for s in students:
            total += s['grade']
    return total / len(students)        
            

def get_best_student(students):        
    best = students[0]
    for s in students:
        if s['grade'] > best['grade']:
            best = s
    return best               

def dictionarie():
    name = name_user()
    grade = ask_note()
    
    student = {
        "name" : name,
        "grade": grade
    } 
    return student      

# List
students = []
while True: 
    print("\n = = M E N U = = \n")
    print("1) Register student \n")
    print("2) Show all students \n")
    print("3) Show class statistic \n")
    print("4) Exit \n")
    try:
        choice = int(input("Enter a choice (1 - 4): "))
        match choice:
            case 1:
                info = dictionarie()
                students.append(info)
                print("✅ Student registered \n")
            
            case 2:
                if not students:
                    print("There's not students registered \n")   
                else:
                    for student in students:
                        print("Students registered: \t ") 
                        print(f"Name: {student['name']} °|° Grade: {student['grade']} \n")
            
            case 3:
                if not students:
                    print("There's not students registered \n")
                else:
                    avg = calculate_avarage(students)
                    best = get_best_student(students)   
                    print(f"Class avarage: {avg}")
                    print(f"Best student: {best['name']} with {best['grade']}")
            
            case 4:
                print("Exiting of the program . . . ")
                break
            
            case _:
                print("Invalid option")
    except ValueError:
        print("Only numbers ")        
                                   

        
            
        
    
            
