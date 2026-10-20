"""
Week 5 - Hands-On Exercise: Student Grade Analyzer Version 3
Course: Python Programming
Name: Edrian Baladad
Course:BSIT WMT 4-2
"""

raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
    "Fred,90,85",
    "Gina",
    "Henry,90,eighty,85",
    "Ivy,",
]

PASSING_GRADE = 75

student_scores = {}

# PART A & F: Parse and organize records safely with guardian conditions.
for record in raw_records:
    fields = record.split(",")

    if len(fields) != 4:
        print(f"Skipped invalid record: {record}")
        continue

    name = fields[0].strip()

    try:
        scores = [int(score.strip()) for score in fields[1:]]
    except ValueError:
        print(f"Skipped invalid record: {record}")
        continue

    student_scores[name] = scores


# PART B: Display records alphabetically.
print("\nORGANIZED STUDENT RECORDS")

for name, scores in sorted(student_scores.items()):
    print(f"{name}: {scores}")


ranking = []

passed_count = 0
failed_count = 0
sum_of_averages = 0

# PART C: Calculate the student results.
for name, scores in student_scores.items():
    if not scores:
        continue

    total = sum(scores)
    average = total / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)

    if average >= PASSING_GRADE:
        remark = "Passed"
    else:
        remark = "Failed"

    if remark == "Passed":
        passed_count += 1
    else:
        failed_count += 1

    sum_of_averages += average

    ranking.append((average, name, highest_score, lowest_score, remark))


# PART D: Sort and display the ranking.
ranking.sort(reverse=True)

print("\nSTUDENT GRADE REPORT")
print("Rank  Name       Average  Highest  Lowest  Remark")

for rank, (avg, name, highest, lowest, remark) in enumerate(ranking, start=1):
    print(f"{rank:<6}{name:<11}{avg:<9.2f}{highest:<9}{lowest:<8}{remark}")


#PART E: Display the class summary.
student_count = len(ranking)
class_average = (sum_of_averages / student_count) if student_count > 0 else 0.0

if student_count > 0:
    highest_student = ranking[0]   # (average, name, ...)
    lowest_student = ranking[-1]   # (average, name, ...)
else:
    highest_student = (0.0, "N/A")
    lowest_student = (0.0, "N/A")

print("\nCLASS SUMMARY")

# TODO: Display all required summary information.
print(f"Number of Students: {student_count}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Class Average: {class_average:.2f}")
print(f"Highest: {highest_student[1]} - {highest_student[0]:.2f}")
print(f"Lowest: {lowest_student[1]} - {lowest_student[0]:.2f}")