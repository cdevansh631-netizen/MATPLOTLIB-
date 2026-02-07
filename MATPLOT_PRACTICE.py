import pandas as pd
import matplotlib.pyplot as plt 

df = pd.DataFrame({
    "Student": ["A","B","C","D","E","F","G","H","I","J"],
    "Class": [10,10,9,9,10,8,8,9,10,8],
    "Gender": ["M","F","M","F","M","F","M","F","M","F"],
    "Math": [78,88,65,72,90,55,68,82,75,60],
    "Science": [85,90,70,75,92,60,65,80,78,62],
    "English": [74,81,60,78,88,58,70,85,72,65],
    "Attendance": [92,95,80,85,98,70,75,90,88,72]
})

#STUDENT V/S ATTENDENCE :-THIS HELP TO UNDERSTAND WHICH HAS HIGHEST ATTENDENCE AND LOWEST ATTENDENCE IMMEDIEATLY :-
plt.bar(df["Student"],df["Attendance"],color="pink",edgecolor="black")
plt.title("STUDENT V/S ATTENDANCE :-")
plt.xlabel("Students")
plt.ylabel("ATTENDANCE")
plt.legend()
plt.show()