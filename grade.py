a = float(input("Enter your assessment score: "))

if 100 >= a >= 96:
    print("Equivalent Assessment Score: 1.00")
elif 95.99 >= a >= 90:
    print("Equivalent Assessment Score: 1.25")
elif 89.99 >= a >= 84:
    print("Equivalent Assessment Score: 1.50")
elif 83.99 >= a >= 78:
    print("Equivalent Assessment Score: 1.75")
elif 77.99 >= a >= 72:
    print("Equivalent Assessment Score: 2.00")
elif 71.99 >= a >= 66:
    print("Equivalent Assessment Score: 2.25")
elif 65.99 >= a >= 60:
    print("Equivalent Assessment Score: 2.50")
elif 59.99 >= a >= 55:
    print("Equivalent Assessment Score: 2.75")
elif 54.99 >= a >= 50:
    print("Equivalent Assessment Score: 3.00")
elif 49.99 >= a >= 40:
    print("Equivalent Assessment Score: 4.00")
elif 39.99 >= a:
    print("Equivalent Assessment Score: 5.00")
    
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

if 1.00 <= final_grade <= 1.125:
    print("Final Grade: 1.00, EXCELLENT") 
elif 1.126 < final_grade <= 1.375:
    print("Final Grade: 1.25, VERY GOOD")
elif 1.376 < final_grade <= 1.625:
    print("Final Grade: 1.50, VERY GOOD")
elif 1.626 < final_grade <= 1.875:
    print("Final Grade: 1.75, GOOD")
elif 1.876 < final_grade <= 2.125:
    print("Final Grade: 2.00, GOOD")
elif 2.126 < final_grade <= 2.375:
    print("Final Grade: 2.25, SATISFACTORY")
elif 2.376 < final_grade <= 2.625:
    print("Final Grade: 2.50, SATISFACTORY")
elif 2.626 < final_grade <= 2.875:
    print("Final Grade: 2.75, FAIR")
elif 2.876 < final_grade <= 3.00:
    print("Final Grade: 3.00, FAIR")
elif 3.01 < final_grade <= 4.00:
    print("Final Grade: 4.00, FAILED ON CONDITION")
elif 4.01 < final_grade <= 5.00:
    print("Final Grade: 5.00, FAILED")
