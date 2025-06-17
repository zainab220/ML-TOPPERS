name = input("enter your name: ")
age = input("enter your age: ")

subjects = ['maths', 'english', 'urdu']
marks = {}
for subject in subjects:
    score = float(input(f"Enter your marks for {subject}: "))
    marks[subject] = score

def average(marks):
    return sum(marks.values()) / len(marks)

avg = average(marks)
print("your average is:  ", avg)

if avg >= 80:
    print("\ngrade = 'A'")
elif 60 < avg < 79:
    print("\ngrade = 'B'")
elif 40 < avg < 59:
    print("\ngrade = 'C'")
else:
    print("\ngrade = 'F'")

bonus = {subject: marks[subject] + 5 for subject in marks}

print("\nMarks after adding bonus:")
for subject in bonus:
    print(f"{subject}: {bonus[subject]}")

with open("data.txt", "w") as file:
    for subject in subjects:
        file.write(f"\nSubject: {subject}")
        file.write(f"\nMarks: {marks[subject]}")

with open("data.txt", "r") as file:
    content = file.read()
    print(content)
