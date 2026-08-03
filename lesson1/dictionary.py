students = {
    "s1": {"name": "Eyosi", "age": 22, "salary": 500},
    "s2": {"name": "Efrem", "age": 23, "salary": 9000},
    "s3": {"name": "Esru", "age": 13, "salary": 900}
}

print(f"Type of students variable: {type(students)}")

for key, values in students.items():
    if values["salary"] <= 500:
        print(f"{key}: Your salary ({values['salary']}) is 500 or less.")
        continue
    print(f"ID: {key}")
    print(f"Info: {values}")
