num_students = int(input("How many students are in the class? "))

midterm_scores = []
final_scores = []

# Loop through each student and prompt for their exam scores
for i in range(num_students):
    midterm_score = float(input("Enter the midterm score for student " + str(i+1) + ": "))
    final_score = float(input("Enter the final score for student " + str(i+1) + ": "))
    midterm_scores.append(midterm_score)
    final_scores.append(final_score)

# Calculate the average midterm and final exam scores
avg_midterm = sum(midterm_scores) / num_students
avg_final = sum(final_scores) / num_students

# Calculate the average grade for the class
avg_grade = 0.4 * avg_midterm + 0.6 * avg_final

# Determine the letter grade based on the average grade
if avg_grade >= 90:
    letter_grade = "A"
elif avg_grade >= 80:
    letter_grade = "B"
elif avg_grade >= 70:
    letter_grade = "C"
elif avg_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display the average grade and letter grade for the class
print("The average grade for the class is:", round(avg_grade, 2))
print("The letter grade for the class is:", letter_grade)
