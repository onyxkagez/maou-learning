students = []
grades = []

while True:
    print("\n--- Grade Manager ---")
    print("1. Add student")
    print("2. Show students")
    print("3. Exit")

    option = input("Choose an option: ")

    if option == "1":
        name = input("Student name: ")

        try:
            grade = float(input("Student grade: "))

            if grade < 0 or grade > 10:
                print("Grade must be between 0 and 10.")
                continue

            students.append(name)
            grades.append(grade)

            print("Student added successfully.")

        except ValueError:
            print("Please enter a valid number.")

    elif option == "2":
        if len(students) == 0:
            print("No students registered.")
        else:
            for i in range(len(students)):
                status = "Passed" if grades[i] >= 6 else "Failed"
                print(f"{students[i]} - {grades[i]} - {status}")

            average = sum(grades) / len(grades)
            print(f"Class average: {average:.2f}")

    elif option == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
