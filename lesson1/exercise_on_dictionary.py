students = {
    "Fahmi": [85, 90, 78],
    "Eyoba": [72, 68, 75],
    "Gech": [45, 52, 48],
    "Deva": [95, 92, 98],
    "Manish": [60, 65, 70]
}

print("Student Data:", students)

for name, scores in students.items():
    average = sum(scores) / len(scores)
    
    if average >= 90:
        grade = "Very Good"
    elif average >= 80:
        grade = "Good"
    else:
        grade = "Needs Improvement"
        
    print(f"Name: {name} | Average: {average:.2f} | Grade: {grade}")
    print(f"  Last Score: {scores[-1]}")