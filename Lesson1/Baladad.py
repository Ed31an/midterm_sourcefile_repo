import sys
scores = [85, 72, 91, 64, 78]

print("Student Scores:")
for score in scores:
    print(score)

print() 


passed = 0
failed = 0

for i, score in enumerate(scores, start=1):
    if score >= 90:
        status = "Excellent - Passed"
        passed += 1
    elif score >= 80:
        status = "Very Good - Passed"
        passed += 1
    elif score >= 75:
        status = "Good - Passed"
        passed += 1
    else:
        status = "Failed"
        failed += 1

    print(f"Student {i}: {score} - {status}")

print()

total = sum(scores)
average = int(total / len(scores))
highest = max(scores)
lowest = min(scores)

print(f"Total Score: {total}")
print(f"Average Score: {average}")
print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")