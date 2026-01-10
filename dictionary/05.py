# marks of a student in different subjects
marks = {
    "math": 92,
    "science": 88,
    "english": 92,
    "history": 85,
    "geography": 90,
    "math": 95  # duplicate key; this will overwrite the previous "math" entry
}
print(marks)
print("Marks in Math:", marks["math"])  # accessing the value for key "math"