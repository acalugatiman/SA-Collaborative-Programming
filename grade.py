q1 = float(input("Enter the tentative grade for Q1: "))
q2 = float(input("Enter the tentative grade for Q2: "))
q3 = float(input("Enter the tentative grade for Q3: "))
q4 = float(input("Enter the tentative grade for Q4: "))

Q1 = q1
Q2 = (q1 + (2 * q2)) / 3
Q3 = (q2 + (2 * q3)) /3
final_grade = (q3 + (2 * q4)) / 3

final_grade = int(final_grade * 100) / 100
print(f"Final Grade: {final_grade:.2f}")

if 1.00 <= final_grade <= 1.25:
    print("EXCELLENT")
elif 1.25 < final_grade <= 1.50:
    print("VERY GOOD")
elif 1.50 < final_grade <= 2.00:
    print("GOOD")
elif 2.00 < final_grade <= 2.50:
    print("SATISFACTORY")
elif 2.50 < final_grade <= 3.00:
    print("FAIR")
elif 3.00 < final_grade <= 4.00:
    print("FAILED ON CONDITION")
elif 4.00 < final_grade <= 5.00:
    print("FAILED")
