import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 



#----1-->

# df = pd.DataFrame({
#     "Student": ["A","B","C","D","E","F","G","H","I","J"],
#     "Class": [7,10,7,9,10,8,8,9,10,8],
#     "Gender": ["M","F","M","F","M","F","M","F","M","F"],
#     "Math": [78,88,65,72,90,55,68,82,75,60],
#     "Science": [85,90,70,75,92,60,65,80,78,62],
#     "English": [74,81,60,78,88,58,70,85,72,65],
#     "Attendance": [92,95,80,85,98,70,75,90,88,72]
# })
# df["PERCENTAGE"]=(df["Math"]+df["Science"]+df["English"])/3
##BAR PLOT
#STUDENT V/S ATTENDENCE :-THIS HELP TO UNDERSTAND WHICH HAS HIGHEST ATTENDENCE AND LOWEST ATTENDENCE IMMEDIEATLY :-
# plt.bar(df["Student"],df["Attendance"],color="pink",edgecolor="black")
# plt.title("STUDENT V/S ATTENDANCE :-")
# plt.xlabel("Students")
# plt.ylabel("ATTENDANCE")
# plt.legend()
# plt.show()



##SCATTER PLOT :-
#MATH V/S ATTENDANCE :-THIS HELP TO UNDERSTAND THAT DOES ATTENDENCE AFFECT MATH MARKS:-
# plt.scatter(df["Attendance"],df["Math"],cmap="green")
# plt.xlabel("ATTENDANCE")
# plt.ylabel("MATH MARKS")
# plt.title("MATH V/S ATTENDANCE")
# plt.show()

##PIE CHART :-
# THIS HELP TO GET AVERAGE ATTENDENCE IN CLASSES :-
# gp=df.groupby("Class").agg({"PERCENTAGE":"mean"}).round(2)
# print(gp)
# plt.pie(gp["PERCENTAGE"],labels=gp.index,explode=[0.1,0,0,0],autopct="%.f")
# plt.title("PERCENTAGE")
# plt.show()


##VIOLIN PLOT :
# whch region carry more high percentage :-
# plt.violinplot(df["PERCENTAGE"],showmeans=True,showextrema=True,showmedians=True)
# plt.show()




#------2->

import pandas as pd

df = pd.DataFrame({
    "Employee": ["E1","E2","E3","E4","E5","E6","E7","E8","E9","E10"],
    "Department": ["HR","IT","HR","Sales","IT","Sales","HR","IT","Sales","HR"],
    "Gender": ["M","F","F","M","M","F","M","F","M","F"],
    "Experience_Years": [1,5,2,7,4,6,3,8,5,2],
    "Salary": [25000,60000,28000,75000,55000,70000,30000,85000,65000,27000],
    "Performance_Score": [65,88,70,92,85,90,72,95,89,68],
    "Attendance": [85,95,88,92,90,94,87,96,91,86]
})

#BAR PLOT :-
# gp=df.groupby("Department").agg({"Performance_Score":"sum"})
# plt.bar(gp.index,gp["Performance_Score"],color="red")
# plt.xlabel("DEPARTMENT")
# plt.ylabel("PERFORMANCE_SCORE")
# plt.legend()
# plt.show()


##BOX PLOT :--
# HELP TO UNDESTAND HOW THE SALARY DISTRIBUTED :- 
# plt.boxplot(df["Salary"],showmeans="True")
# plt.show()


##VIOLIN PLOT :-
#Help us to find how attendence distributed hence  we can analyse which attendence comman or mean .
# plt.violinplot(df["Attendance"],showmedians="False",showmeans="True")
# plt.show()

#Scatter plot:-
#By this e can undestand how performance vary with expernce :-
# color=np.random.randint(10,100,10)
# plt.scatter(df["Experience_Years"],df["Performance_Score"],cmap="hot",c=color)
# plt.xlabel("EXPERIENCE_YEAR")
# plt.ylabel("PERFORMANCE_SCORE")
# plt.colorbar()
# plt.show()

##HIST PLOT :-
# plt.hist(df["Performance_Score"],bins=8,color="pink",edgecolor="black")
# plt.ylabel("Performance_Score")
# plt.show()

##STEM PLOT:-
#HELP US TO GET EXACT VALUE OF PERFORMANCE:
# plt.stem(df["Performance_Score"],markerfmt="s",linefmt="--")
# plt.show()


##STACK PLOT MATPLOT :-
# plt.stackplot(df["Experience_Years"],df["Performance_Score"],df["Performance_Score"]*0.2,baseline="sym",labels=["Performance_Score","BONUS"])
# plt.legend()
# plt.show()