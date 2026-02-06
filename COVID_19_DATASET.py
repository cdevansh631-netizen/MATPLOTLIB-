import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("country_wise_latest.csv")




# #DATA_UNDERSTANDING :-
# # print(df.head())
# # print(df.tail())
# # print(df.info())
# # print(df.describe(include=object))
# # print("(ROW,COLUMN) :",df.shape)
df["Deaths / 100 Recovered"].replace(np.inf,0,inplace=True)

# #DATA HANDLING : -
# print("NAMES OF WHO REGION:-")
# for c in df["WHO Region"].unique():
#     print(c)
# print(df.isnull().sum())
# df.drop_duplicates("Country/Region",inplace=True)
# df.rename(columns={"New cases":"New_Cases","New deaths":"New_Deaths","New recovered":"New_Recovered"})


# # COUNTRY WITH MOST ACTICE CASE :-
# print("COUNTRY WITH MOST ACTICE CASE :-")
# print(df.loc[df["Active"]==df["Active"].max(),"Country/Region"].to_string(index=False),"\n")

# # Country with most death :
# print("COUNTRY WITH MOST DEATH :-")
# print(df.loc[df["Deaths"]==df["Deaths"].max(),"Country/Region"].to_string(index=False),"\n")

# #COUNTRY WITH HIGHEST RECOVERY :-
# print("COUNTRY WITH HIGHEST RECOVERY :-")
# print(df.loc[df["Recovered / 100 Cases"]==df["Recovered / 100 Cases"].max(),"Country/Region"].to_string(index=False),"\n")


# #INDIA PIE CHART :- WHICH TELL USE ABOUT RECOVERY,DEATH,:-
# Death=df.loc[df["Country/Region"]=="India","Deaths"].astype(int).to_string(index=False)
# Recovered=df.loc[df["Country/Region"]=="India","Recovered"].astype(int).to_string(index=False)
# Active=df.loc[df["Country/Region"]=="India","Active"].astype(int).to_string(index=False)
# X=[Death,Recovered,Active]
# plt.pie(X,colors=["pink","red","green"],labels=["Death","Recovered","Active"],explode=[0,0,.1],autopct="%.f")
# plt.title("INDIA COVID DATA")
# plt.show()


# #WHO REGION WITH HIGHEST DEATH RATE:-
# print("REGION WITH HIGHEST DEATH RATE")
# print(df.groupby("WHO Region")["Deaths / 100 Cases"].max().idxmax(),"\n")


#TOP 10 COUNTRIES WITH MOST CONFIRMED CASES :-
# dx=df.sort_values('Confirmed',ascending=False).head(10)
# plt.bar(dx["Country/Region"],dx["Confirmed"],color="magenta",edgecolor="black")
# plt.title("COUNTRUES VS CONFIRMED CASES",fontsize=10)
# plt.xlabel("COUNTRIES")
# plt.ylabel("CONFIRMED CASES")
# plt.legend()
# plt.show()

#DISTRIBUTION OF DEATH RATE :-BY THIS GRAPH WE ANALYZE THAT HOW MANY COUNTRIES FALL IN WHICH REGION OF "Deaths / 100 Recovered :- 
# plt.hist(df["Deaths / 100 Recovered"],bins=20,edgecolor="black",color="pink")
# plt.xlabel("DEATH RATES")
# plt.ylabel("NO OF CONTRIES")
# plt.show()
 

#COUNT OF COUNTRIES PER WHO REGION :-Analyzing which Region carries how many countries :-
# plt.bar(df["WHO Region"].value_counts().index,df["WHO Region"].value_counts().values,color="green",edgecolor="black")
# plt.title("COUNT OF COUNTRIES PER WHO REGION")
# plt.xlabel("COUNTRIES")
# plt.ylabel("NO OF COUNTRIES")
# plt.show()


#Active vs Recovered :-
plt.scatter(df["Active"],df["Recovered"],cmap="pink")
plt.colorbar()
plt.show()