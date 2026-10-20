"""Student Grade Analyzer - Starter Code

Complete every section marked TODO. Keep this file and grades.txt in the
same folder. Rename the completed file to student_grade_analyzer_.py.
"""


def classify_grade(grade):
    """Return the classification and status of a grade."""
    if 90 <= grade <= 100:
        return "Excellent", "Passed"
    elif 85 <= grade < 90:
        return "Very Good", "Passed"
    elif 80 <= grade < 85:
        return "Satisfactory", "Passed"
    elif 75 <= grade < 80:
        return "Needs Improvement", "Passed"
    else:
        return "Unsatisfactory", "Failed"
    # TODO: Use if/elif/else and return (classification, status).
    pass


def load_students(filename):
    """Read valid student records from a text file and return them as a list."""
    students = []

    # TODO: Open filename safely by using with open(...) and try/except.
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()

                if not clean_line or clean_line.startswith("#"):
                    continue  # Skip blank lines and comments

                parts = clean_line.split(",")

                if len(parts) != 3:
                    continue  # Skip lines that don't have exactly 3 fields

                student_id = parts[0].strip()
                name = parts[1].strip()
                try:
                    grade = float(parts[2].strip())
                except ValueError:
                    continue  # Skip lines where grade is not a valid float 
                if 0 <= grade <= 100:
                    students.append({
                        "student_id": student_id,
                        "name": name,
                        "grade": grade
                    })
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except OSError as error:
        print(f"Error: An OS error occurred while reading '{filename}': {error}")
    # TODO: Loop through the file, clean each line, and skip blank lines.
    # TODO: Split each record and check that it contains three fields.
    # TODO: Convert and validate the grade.
    # TODO: Append a dictionary for every valid record.

    return students


def calculate_statistics(students):
    """Calculate and return the class statistics."""
    if not students:
        return None

    total_grade = 0
    passed_count = 0
    failed_count = 0
    highest_student = students[0]
    lowest_student = students[0]

    for student in students:
        grade = student["grade"]
        total_grade += grade

        if grade >= 75:
            passed_count += 1
        else:
            failed_count += 1

        if grade > highest_student["grade"]:
            highest_student = student
        elif grade < lowest_student["grade"]:
            lowest_student = student

    total_students = len(students)
    average_grade = total_grade / total_students if total_students > 0 else 0.0

    return {
        "total_students": total_students,
        "passed_count": passed_count,
        "failed_count": failed_count,
        "highest_student": highest_student,
        "lowest_student": lowest_student,
        "average_grade": average_grade
    }

    # TODO: Use one loop to update the accumulator, counters, highest, and lowest.
    # Do not use sum(), max(), or min() for this part.

    # TODO: Calculate the average and return all results in a dictionary.
    pass


def display_students(students):
    """Display all student records in a formatted table."""
    if not students:
        print("No student records to display.")
        return

    print("\n" + "-" * 70)
    print(f"{'Student ID':<12} {'Name':<22} {'Grade':<6} {'Classification':<18} {'Status':<8}")
    print("-" * 70)

    for student in students:
        classification, status = classify_grade(student["grade"])
        print(f"{student['student_id']:<12} {student['name']:<22} {student['grade']:<6.2f} {classification:<18} {status:<8}")

    print("-" * 70)
    # TODO: Print column headings.
    # TODO: Loop through students and call classify_grade for each record.
    pass


def display_statistics(statistics):
    """Display the calculated class statistics."""
    if not statistics:
        print("No statistics to display.")
        return

    high  = statistics["highest_student"]
    low  = statistics["lowest_student"]

    print("\nCLASS STATISTICS")
    print(f"Total Students: {statistics['total_students']}")
    print (f"Class Average: {statistics['average_grade']:.2f}")
    print(f"Passed: {statistics['passed_count']}")
    print(f"Failed: {statistics['failed_count']}")
    print(f"Highest Grade: {high['name']} - {high['grade']:.2f}")
    print(f"Lowest Grade: {low['name']} - {low['grade']:.2f}")
    # TODO: Display every value in statistics clearly.
    pass


def search_student(students, keyword):
    """Return records whose student number or name matches the keyword."""
    matches = []

    clean_keyword = keyword.strip().lower()

    if not clean_keyword:
        return matches

    for student in students:
        if (clean_keyword in student["student_id"].lower() or
                clean_keyword in student["name"].lower()):
            matches.append(student)
    # TODO: Make keyword lowercase and remove extra whitespace.
    # TODO: Use a loop and partial, case-insensitive matching.
    return matches


def save_report(students, statistics, filename):
    """Write the student results and class statistics to a report file."""
    if not students or not statistics:
        print("No data to save or No valid student data or statistics available.")
        return

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("-" * 70 + "\n")
            file.write("STUDENT GRADE REPORT\n")
            file.write("-" * 70 + "\n")

            file.write("Student RESULTS:\n")
            file.write("-" * 70 + "\n")
            file.write(f"{'Student ID':<12} {'Name':<22} {'Grade':<6} {'Classification':<18} {'Status':<8}\n")
            file.write("-" * 70 + "\n")
            for student in students:
                classification, status = classify_grade(student["grade"])
                name_display = student['name'][:22]  # Truncate name to 22 characters
                file.write(f"{student['student_id']:<12} {name_display:<22} {student['grade']:<6.2f} {classification:<18} {status:<8}\n")
            file.write("-" * 70 + "\n")

            file.write("CLASS STATISTICS:\n")
            file.write("-" * 70 + "\n")
            file.write(f"Total Students: {statistics['total_students']}\n")
            file.write(f"Class Average: {statistics['average_grade']:.2f}\n")
            file.write(f"Passed: {statistics['passed_count']}\n")
            file.write(f"Failed: {statistics['failed_count']}\n")
            high = statistics["highest_student"]
            low = statistics["lowest_student"]
            file.write(f"Highest Grade: {high['name']} - {high['grade']:.2f}\n")
            file.write(f"Lowest Grade: {low['name']} - {low['grade']:.2f}\n")
            file.write("-" * 70 + "\n")

        print(f"Report saved successfully to '{filename}'.")
    except OSError as error:
        print(f"Error: An OS error occurred while writing to '{filename}': {error}")

    # TODO: Safely open filename in write mode.
    # TODO: Write all student results and statistics.
    # TODO: Handle a possible OSError.
    pass


def main():
    """Run the menu-driven Student Grade Analyzer."""
    students = load_students("grades.txt")

    if not students:
        print("No valid student records were loaded.")
        return

    statistics = calculate_statistics(students)

    while True:
        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_students(students)
        elif choice == "2":
            display_statistics(statistics)
        elif choice == "3":
            keyword = input("Enter student ID or name to search: ")
            matches = search_student(students, keyword)
            if matches:
                print(f"Found {len(matches)} matching student(s):")
                display_students(matches)
            else:
                print("No matching student records found.")
        elif choice == "4":
            save_report(students, statistics, "grade_report.txt")
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue
            

        # TODO: Call the appropriate function for choices 1 to 4.
        # TODO: For choice 3, ask for a keyword and display every match.
        # TODO: Use break for choice 5.
        # TODO: Use continue after an invalid choice.


if __name__ == "__main__":
    main()

