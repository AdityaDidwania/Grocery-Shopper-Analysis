# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:33:46 2019

@author: Aditya Didwania
"""

import numpy as np
import pymysql
import pandas as pd
from pandas import read_csv
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns


db = pymysql.connect(host='localhost',
user='root',
password='3p2a1o2333',
db='big data mid',
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor)
engine = create_engine('mysql+pymysql://root:3p2a1o2333@localhost/big data mid')



#a(4)ii
sql_select_Query = "select * from department"
cursor = db.cursor()
cursor.execute(sql_select_Query)
department = cursor.fetchall()


df3 = pd.DataFrame(list(department),columns=["department","products"])
ax = df3.plot.bar(rot=0)


ax.set_ylabel("Number")
plt.show()

df3 = pd.DataFrame(list(department),columns=["department","module"])
ax = df3.plot.bar(rot=0,color="y")
ax.set_xticklabels(df3["department"],rotation=90)
ax.set_ylabel("Number")
plt.show()



#b(2)iii
single=read_csv("E:\\Big data\\final project\\b(2).csv")
double=read_csv("E:\\Big data\\final project\\b(2)ii.csv")
single["hh_state"].hist(bins=20, grid=True, xlabelsize=8, ylabelsize=10,figsize=(12,11))
double["hh_state"].hist(bins=20, grid=True, xlabelsize=8, ylabelsize=10,figsize=(12,11))
import pylab as pl
pl.xticks(rotation=90)


#b(3)i

df1 = read_csv("/Users/tmh/Desktop/bdm/b(3)i.csv")

x1 = df1.month
y1 = df1.num_items
fig, ax = plt.subplots()
ax.plot(x1, y1)
plt.title("Average Number of Items Purchased")
plt.xlabel("month")
plt.ylabel("nummer of items")
plt.show()

#b(3)ii
df2 = read_csv("/Users/tmh/Desktop/bdm/b(3)ii.csv")

x2 = df2.month
y2 = df2.num_trips
fig, ax = plt.subplots()
ax.plot(x2, y2)
plt.title("Average Number of Shopping Trips")
plt.xlabel("month")
plt.ylabel("nummer of trips")
plt.show()

#b(3)iii


data1 = read_csv("/Users/tmh/Desktop/bdm/b(3)iii.csv")
ax1 = sns.distplot(data1["TIME_GAP"],bins=500,rug=False, hist=True, kde=False)

plt.xlim(xmax = 16)
plt.ylabel("Nummer of trips")

# c(1)

data1 = read_csv("/Users/tmh/Desktop/bdm/c(1).csv")
## scatterplot
fig, ax = plt.subplots()
ax.scatter(data1["num_items"], data1["num_trips"])
ax.set_xlabel("Shoppng trips per month")
ax.set_ylabel("Avg number of item purchased")
plt.show()
## correlation
data1.corr()
#####0.048186 



# c(2)
data2 = read_csv("/Users/tmh/Desktop/bdm/c(2).csv")
## scatterplot
fig, ax = plt.subplots()
ax.scatter(data2["avg_price_paid_per_item"], data2["quantity_at_TC_prod_id"])
ax.set_xlabel("AVG price paid per item")
ax.set_ylabel("Quantity")
plt.show()
## correlation
data2.corr()
####-0.090335


#c(3)i
df4 = read_csv("/Users/tmh/Desktop/bdm/c(3)i.csv")

x4 = df4.group_at_prod_id
y4 = df4.proportion
fig, ax = plt.subplots()
plt.figure(figsize = (20,5))
plt.xticks(fontsize = 10)
plt.bar(x4, y4)

plt.title("categories_CTL_BR")

plt.xlabel("Category")
plt.xticks(rotation=90)
plt.ylabel("Proportion")

plt.show()




#c(3)ii

df5 = read_csv("/Users/tmh/Desktop/bdm/c(3)ii.csv")
x5 = df5.month1
y5 = df5.share
fig, ax = plt.subplots()
plt.figure(figsize = (20,5))
plt.xticks(fontsize = 10)
plt.bar(x5, y5)

plt.title("Expenditure share in Private Labeled products")

plt.xlabel("Month")
plt.xticks()
plt.ylabel("Share")

plt.show()




#c(3)iii

data1 = read_csv("/Users/tmh/Desktop/bdm/c(3)iii.csv")
ax1 = sns.distplot(data1["percentage"],rug=False, hist=True, kde=False)

plt.xlim(xmax = 16)
plt.ylabel("Nummer of trips")
plt.title("Income")
plt.xlabel("Group")
plt.xticks()
plt.ylabel("Percentage")
plt.show()