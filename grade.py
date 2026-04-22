q1 = float(input("Enter the tentative grade for Q1: "))
q2 = float(input("Enter the tentative grade for Q2: "))
q3 = float(input("Enter the tentative grade for Q3: "))
q4 = float(input("Enter the tentative grade for Q4: "))

Q1 = q1
Q2 = (q1 + 2 * q2) / 3
Q3 = (q2 + 2 * q3) /3
final_grade = (q3 + 2 * q4) / 3

print(f"Final Grade: {final_grade}")
