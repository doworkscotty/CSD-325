



import json

# Load the JSON file
def load_students(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

# Print function
def print_students(student_list, message):
    print(message)
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")
    print()

# Save the updated list to the JSON file
def save_students(file_path, student_list):
    with open(file_path, "w") as f:
        json.dump(student_list, f, indent=2)
    print("The JSON file has been updated.\n")

def main():
    file_path = "student.json"

    # Load original students
    students = load_students(file_path)

    # Print original list
    print_students(students, "Original Student List:")

    # Append your student info
    new_student = {
        "F_Name": "Scott",
        "L_Name": "Anderson",
        "Student_ID": 99999,
        "Email": "scotanderson@my365.bellevue.edu"
    }
    students.append(new_student)

    # Print updated list
    print_students(students, "Updated Student List:")

    # Save back to JSON file
    save_students(file_path, students)

if __name__ == "__main__":
    main()
