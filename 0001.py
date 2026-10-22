students = {
    "Rahul" : 95,
    "Ayush" : 87,
    "Preet" : 70,
    "Soham" : 89,
    "Aayan" : 76,
}

marks = list(students.values())

def averageMarks(marks): 
    return sum(marks) / len(marks) 

def maximumMarks(marks):
    return max(marks)

def minimumMarks(marks):
    return min(marks)

print("Student Marks:")
for name, mark in students.items():
    print(name, ":", marks)

print("Average Marks = ", averageMarks(marks))
print("Maximum Marks = ", maximumMarks(marks))
print("Minimum Marks = ", minimumMarks(marks))