students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]


#  Calculate average
def calculate_average(marks):
    if len(marks) == 0:
        return None

    for mark in marks:
        if mark < 0 or mark > 100:
            return None

    return sum(marks) / len(marks)


#  Classify performance
def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


#  Display student report
def display_report(students):
    for s in students:
        student_id = s[0]
        name = s[1]
        marks = s[2]

        average = calculate_average(marks)

        if average is None:
            print(student_id, name, "Invalid or missing marks")
        else:
            result = classify_performance(average)
            print(student_id, name, average, result)


# Test
display_report(students)

# Test invalid marks
print(calculate_average([80, 110, 90]))

# Test missing marks
print(calculate_average([]))
