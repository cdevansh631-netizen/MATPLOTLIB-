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
# brand=["MARUTI","TOYOTA","AUDI","MERCEDES","LANDROVER"]
# X=[456,233,56,76,189]
# ex=[0,0,0,.1,0]
# #explode :- keep out slice of that portion little outside .
# #autopct :- give % on each slice of portion.
# #startangle :- start with angle 90.
# plt.pie(X,colors=["magenta","pink","red","orange","purple"],
#         labels=brand,explode=ex,shadow=True,autopct="%.f",startangle=90)
# plt.show()


# da=pd.read_csv(r"C:\Users\cdeva\Downloads\sample_expenses.csv")
# df=pd.DataFrame(da)
# drp=df.groupby("Payment_Mode")["Amount"].sum()
# ex=[0,.1,0]
# plt.pie(drp.values,autopct="%.f",labels=drp.index,explode=ex,shadow=True)
# plt.show()

# 5-> BOX PLOT :-[--THEORY IN NOTEBOOK--]

# l=[1,3,4,7,12,2,8,9,24]
# l1=[2,3,6,8,9,1,13,4,1]
# plt.boxplot([l,l1])
# plt.show()

# da=pd.read_csv(r"C:\Users\cdeva\Downloads\sample_expenses.csv")
# df=pd.DataFrame(da)
# plt.boxplot(df["Amount"])
# plt.show()


#6-> HISTOGRAM :-
# x=[12,14,17,56,34,67,89,98,94,91]
# plt.hist(x,bins=20,edgecolor="black",color="pink")
# plt.show()


# da=pd.read_csv(r"C:\Users\cdeva\Downloads\sample_expenses.csv")
# df=pd.DataFrame(da)
# plt.hist(df["Amount"],color="orange",edgecolor="black")
# plt.show()




# 7 ->VIOLIN PLOT :-
# X=[1,10,99,22,35,90,42,97,98,99,84,88,96,83]
# plt.violinplot(X,widths=10,showmedians=False,showmeans=False,showextrema=True)
# plt.show()


# da=pd.read_csv(r"C:\Users\cdeva\Downloads\sample_expenses.csv")
# df=pd.DataFrame(da)
# plt.violinplot(df["Amount"],showmeans=True)
# plt.show()


# 8 -> STEAM PLOT :-
# X=[12,45,65,34,13,15,17,19,56,77]
# plt.stem(X,linefmt="--",markerfmt="s",)
# plt.plot(X,color="magenta")
# plt.show()
#Same For DataFrame :--


# 9 -> STACK PLOT MATPLOTLIB :--

# Days=[1,2,3,4,5,6,7]

# NOP1=[56,95,44,49,38,34,55]
# NOP2=[95,99,97,88,97,66,44]
# #baseline-how it look/design.
# NOP3=[34,54,64,90,88,94,88]
# plt.stackplot(Days,NOP1,NOP2,NOP3,baseline="sym",labels=["WEEK 1","WEEK 2","WEEK 3","WEEK 4","WEEK 5","WEEK 6","WEEK 7"])
# plt.legend()
# plt.show()



# da=pd.read_csv(r"C:\Users\cdeva\Downloads\food_nutrition.csv")
# df=pd.DataFrame(da)
# gp=df.groupby("Food").agg({"Calories":"mean","Protein_g":"mean","Fat_g":"mean"})
# plt.stackplot(df["Food"],df["Calories"],df["Protein_g"],df["Fat_g"],labels=["CALORIES","PROTEIN","FAT"])
# plt.legend()
# plt.show()


# 10 -> STEP PLOT :-
# x=["DAY 1","DAT 2","DAY 3","DAY 4"]
# y=[30,50,10,70]
# plt.step(x,y,marker="s",where="mid")
# plt.show()

# da=pd.read_csv(r"C:\Users\cdeva\Downloads\sample_expenses.csv")
# df=pd.DataFrame(da)
# gp=df.groupby("Category").agg({"Amount":"sum"})
# plt.step(df["Category"].unique(),gp["Amount"],marker="s",where="mid")
# plt.show()