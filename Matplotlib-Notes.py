# MATPLOTLIB NOTES :-

# 1-> SCATTER PLOT .
# 2-> STEP PLOT .
# 3-> BAR PLOT .
# 4-> FILL BETWEEN .
# 5-> TIME SERIES .
# 6-> BOX PLOT .
# 7-> HISTOGRAM .

import pandas as pd
import matplotlib.pyplot as plt


# 1-> BAR PLOT .

# X=[94,95,81,86,97]
# Y=["MATH","CHEMISTRY","PHYSICS","ENGLISH","IP"]
# plt.bar(Y,X,color="blue",edgecolor="black")
# plt.title("RESULT",fontsize=20)
# plt.xlabel("SUBJECT",fontsize=20)
# plt.ylabel("MARKS",fontsize=20)
# plt.show()



data=pd.read_csv(r"C:\Users\cdeva\Downloads\sample_expenses.csv")
df=pd.DataFrame(data)
grp=df.groupby("Payment_Mode")["Amount"].sum()
plt.bar(grp.index,grp.values)
plt.show()