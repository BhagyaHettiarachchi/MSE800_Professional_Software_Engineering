import numpy as np

scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

# Calculate and print the average score for each student
average_score_stu = np.mean(scores, axis=1)
print("Average Score For Each Student:",average_score_stu)

# Calculate and print the average score for each subject
average_score_sbj = np.mean(scores, axis=0)
print("Average Score For Each Subject:",average_score_sbj)

# The student with the highest total score
# Get total score for each student
total_score_stu = np.sum(scores, axis=1)

# Get the index of the row with highest total score
highest_total = np.argmax(total_score_stu)
print("The student(row index) with the highest total score:", highest_total)

# Add 5 bonus points to the third subject for all students
scores[:,2] += 5
print("After adding 5 bonus points to the third subject for all students:",scores)