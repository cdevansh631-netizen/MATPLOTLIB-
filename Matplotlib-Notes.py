# MATPLOTLIB NOTES :-

# 1-> SCATTER PLOT .
# 2-> STEP PLOT .
# 3-> BAR PLOT .
# 4-> FILL BETWEEN .
# 5-> TIME SERIES .
# 6-> BOX PLOT .
# 7-> HISTOGRAM .

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1-> BAR PLOT .

# X=[94,95,81,86,97]
# Y=["MATH","CHEMISTRY","PHYSICS","ENGLISH","IP"]
# plt.bar(Y,X,color="blue",edgecolor="black")
# plt.title("RESULT",fontsize=20)
# plt.xlabel("SUBJECT",fontsize=20)
# plt.ylabel("MARKS",fontsize=20)
# plt.show()

# data=pd.read_csv(r"C:\Users\cdeva\Downloads\sample_expenses.csv")
# df=pd.DataFrame(data)
# grp=df.groupby("Payment_Mode")["Amount"].sum()
# plt.bar(grp.index,grp.values)
# plt.show()



# 2-> LINE PLOT :-
# x=["Day 1","Day 2","Day 3","Day 4","Day 5"]
# y=[200,456,345,222,300]
# z=[178,346,389,300,478]
# plt.plot(x,y,marker="*",ls="--",color="black",label="Week 1",alpha=0.3,linewidth=2)
# plt.plot(x,z,marker="*",ls="--",color="red",label="Week 2",alpha=1,linewidth=2)
# plt.legend(loc="upper left")
# plt.show()


# data=pd.read_csv(r"C:\Users\cdeva\Downloads\sample_expenses.csv")
# df=pd.DataFrame(data)
# grp=df.groupby("Category")["Amount"].sum()
# plt.plot(grp.index,grp.values,ls="--",marker="^",label="INFLAMATION",linewidth=2.44)
# plt.show()



# 3-> SCATTER PLOT :-

# X=np.random.randint(1,10,50)
# Y=np.random.randint(10,100,50)
# color=np.random.randint(10,100,50)
# plt.scatter(X,Y,marker="+",cmap="winter_r",c=color)
# plt.colorbar()
# plt.show()



# data=pd.read_csv(r"C:\Users\cdeva\Downloads\sample_expenses.csv")
# df=pd.DataFrame(data)
# plt.scatter(df["Category"],df["Amount"],color="black",alpha=0.6,s=77)
# plt.show()



# 4-> PIE CHART :-
