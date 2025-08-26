marks = [45, 78, 65, 98, 35, 66, 89, 54, 32, 47,
         21, 76, 58, 92, 84, 73, 62, 55, 41, 69]

total_students = len(marks)
highest = max(marks)
lowest = min(marks)
average = sum(marks) / total_students


passed = len([m for m in marks if m >= 40])
failed = total_students - passed
pass_percentage = (passed / total_students) * 100

sorted_marks = sorted(marks)


grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
for m in marks:
    if m >= 85:
        grades["A"] += 1
    elif m >= 70:
        grades["B"] += 1
    elif m >= 55:
        grades["C"] += 1
    elif m >= 40:
        grades["D"] += 1
    else:
        grades["F"] += 1


print(f"Total Students: {total_students}")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")
print(f"Average Marks: {average:.1f}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Pass Percentage: {pass_percentage:.1f}%")
print(f"Sorted Marks: {sorted_marks}")
print(f"Grade A: {grades['A']} Students")
print(f"Grade B: {grades['B']} Students")
print(f"Grade C: {grades['C']} Students")
print(f"Grade D: {grades['D']} Students")
print(f"Grade F: {grades['F']} Students")