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
Q1 = q1
if 1.00 <= q1  <= 1.125:
    print("Q1 Grade: 1.00, EXCELLENT") 
elif 1.126 < q1 <= 1.375:
    print("Q1 Grade: 1.25, VERY GOOD")
elif 1.376 < q1 <= 1.625:
    print("Q1 Grade: 1.50, VERY GOOD")
elif 1.626 < q1 <= 1.875:
    print("Q1 Grade: 1.75, GOOD")
elif 1.876 < q1 <= 2.125:
    print("Q1 Grade: 2.00, GOOD")
elif 2.126 < q1 <= 2.375:
    print("Q1 Grade: 2.25, SATISFACTORY")
elif 2.376 < q1 <= 2.625:
    print("Q1 Grade: 2.50, SATISFACTORY")
elif 2.626 < q1 <= 2.875:
    print("Q1 Grade: 2.75, FAIR")
elif 2.876 < q1 <= 3.00:
    print("Q1 Grade: 3.00, FAIR")
elif 3.01 < q1 <= 4.00:
    print("Q1 Grade: 4.00, FAILED ON CONDITION")
elif 4.01 < q1 <= 5.00:
    print("Q1 Grade: 5.00, FAILED")

a_q2 = float(input("Enter your Q2 assessment score: "))
if 100 >= a_q2 >= 96:
    print("Equivalent Q2 Assessment Score: 1.00")
elif 95.99 >= a_q2 >= 90:
    print("Equivalent Q2 Assessment Score: 1.25")
elif 89.99 >= a_q2 >= 84:
    print("Equivalent Q2 Assessment Score: 1.50")
elif 83.99 >= a_q2 >= 78:
    print("Equivalent Q2 Assessment Score: 1.75")
elif 77.99 >= a_q2 >= 72:
    print("Equivalent Q2 Assessment Score: 2.00")
elif 71.99 >= a_q2 >= 66:
    print("Equivalent Q2 Assessment Score: 2.25")
elif 65.99 >= a_q2 >= 60:
    print("Equivalent Q2 Assessment Score: 2.50")
elif 59.99 >= a_q2 >= 55:
    print("Equivalent Q2 Assessment Score: 2.75")
elif 54.99 >= a_q2 >= 50:
    print("Equivalent Q2 Assessment Score: 3.00")
elif 49.99 >= a_q2 >= 40:
    print("Equivalent Q2 Assessment Score: 4.00")
elif 39.99 >= a_q2:
    print("Equivalent Q2 Assessment Score: 5.00")
    
q2 = float(input("Enter the tentative grade for Q2: "))
Q2 = (q1 + (2 * q2)) / 3
if 1.00 <= Q2  <= 1.125:
    print("Q2 Grade: 1.00, EXCELLENT") 
elif 1.126 < Q2 <= 1.375:
    print("Q2 Grade: 1.25, VERY GOOD")
elif 1.376 < Q2 <= 1.625:
    print("Q2 Grade: 1.50, VERY GOOD")
elif 1.626 < Q2 <= 1.875:
    print("Q2 Grade: 1.75, GOOD")
elif 1.876 < Q2 <= 2.125:
    print("Q2 Grade: 2.00, GOOD")
elif 2.126 < Q2 <= 2.375:
    print("Q2 Grade: 2.25, SATISFACTORY")
elif 2.376 < Q2 <= 2.625:
    print("Q2 Grade: 2.50, SATISFACTORY")
elif 2.626 < Q2 <= 2.875:
    print("Q2 Grade: 2.75, FAIR")
elif 2.876 < Q2 <= 3.00:
    print("Q2 Grade: 3.00, FAIR")
elif 3.01 < Q2 <= 4.00:
    print("Q2 Grade: 4.00, FAILED ON CONDITION")
elif 4.01 < Q2 <= 5.00:
    print("Q2 Grade: 5.00, FAILED")

a_q3 = float(input("Enter your Q3 assessment score: "))
if 100 >= a_q3 >= 96:
    print("Equivalent Q3 Assessment Score: 1.00")
elif 95.99 >= a_q3 >= 90:
    print("Equivalent Q3 Assessment Score: 1.25")
elif 89.99 >= a_q3 >= 84:
    print("Equivalent Q3 Assessment Score: 1.50")
elif 83.99 >= a_q3 >= 78:
    print("Equivalent Q3 Assessment Score: 1.75")
elif 77.99 >= a_q3 >= 72:
    print("Equivalent Q3 Assessment Score: 2.00")
elif 71.99 >= a_q3 >= 66:
    print("Equivalent Q3 Assessment Score: 2.25")
elif 65.99 >= a_q3 >= 60:
    print("Equivalent Q3 Assessment Score: 2.50")
elif 59.99 >= a_q3 >= 55:
    print("Equivalent Q3 Assessment Score: 2.75")
elif 54.99 >= a_q3 >= 50:
    print("Equivalent Q3 Assessment Score: 3.00")
elif 49.99 >= a_q3 >= 40:
    print("Equivalent Q3 Assessment Score: 4.00")
elif 39.99 >= a_q3:
    print("Equivalent Q3 Assessment Score: 5.00")

q3 = float(input("Enter the tentative grade for Q3: "))
Q3 = (Q2 + (2 * q3)) /3
if 1.00 <= Q3  <= 1.125:
    print("Q3 Grade: 1.00, EXCELLENT") 
elif 1.126 < Q3 <= 1.375:
    print("Q3 Grade: 1.25, VERY GOOD")
elif 1.376 < Q3 <= 1.625:
    print("Q3 Grade: 1.50, VERY GOOD")
elif 1.626 < Q3 <= 1.875:
    print("Q3 Grade: 1.75, GOOD")
elif 1.876 < Q3 <= 2.125:
    print("Q3 Grade: 2.00, GOOD")
elif 2.126 < Q3 <= 2.375:
    print("Q3 Grade: 2.25, SATISFACTORY")
elif 2.376 < Q3 <= 2.625:
    print("Q3 Grade: 2.50, SATISFACTORY")
elif 2.626 < Q3 <= 2.875:
    print("Q3 Grade: 2.75, FAIR")
elif 2.876 < Q3 <= 3.00:
    print("Q3 Grade: 3.00, FAIR")
elif 3.01 < Q3 <= 4.00:
    print("Q3 Grade: 4.00, FAILED ON CONDITION")
elif 4.01 < Q3 <= 5.00:
    print("Q3 Grade: 5.00, FAILED")
    
a_q4 = float(input("Enter your Q4 assessment score: "))
if 100 >= a_q4 >= 96:
    print("Equivalent Q4 Assessment Score: 1.00")
elif 95.99 >= a_q4 >= 90:
    print("Equivalent Q4 Assessment Score: 1.25")
elif 89.99 >= a_q4 >= 84:
    print("Equivalent Q4 Assessment Score: 1.50")
elif 83.99 >= a_q4 >= 78:
    print("Equivalent Q4 Assessment Score: 1.75")
elif 77.99 >= a_q4 >= 72:
    print("Equivalent Q4 Assessment Score: 2.00")
elif 71.99 >= a_q4 >= 66:
    print("Equivalent Q4 Assessment Score: 2.25")
elif 65.99 >= a_q4 >= 60:
    print("Equivalent Q4 Assessment Score: 2.50")
elif 59.99 >= a_q4 >= 55:
    print("Equivalent Q4 Assessment Score: 2.75")
elif 54.99 >= a_q4 >= 50:
    print("Equivalent Q4 Assessment Score: 3.00")
elif 49.99 >= a_q4 >= 40:
    print("Equivalent Q4 Assessment Score: 4.00")
elif 39.99 >= a_q4:
    print("Equivalent Q4 Assessment Score: 5.00")

q4 = float(input("Enter the tentative grade for Q4: "))
final_grade = (Q3 + (2 * q4)) / 3 
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
