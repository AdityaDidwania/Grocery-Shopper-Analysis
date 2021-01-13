# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:31:10 2019

@author: Aditya Didwania
"""

import pymysql
import pandas as pd
from sqlalchemy import create_engine
db = pymysql.connect(host='localhost',
user='root',
password='Aditya.02',
db='db_consumer_panel2',
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor)
engine = create_engine('mysql+pymysql://root:Aditya.02@localhost/db_consumer_panel2')


dta_at_hh = pd.read_csv("C:\\Users\\Aditya Didwania\\Desktop\\Brandeis\\Sem I\\Bus 211f Analyzing Big Data I\\Final Project\\dta_at_hh.csv")
b1=dta_at_hh.drop('Unnamed: 0', axis=1)
pd.io.sql.to_sql(b1,'households', con=engine, index=False, if_exists='append')

dta_at_prod_id = pd.read_csv("C:\\Users\\Aditya Didwania\\Desktop\\Brandeis\\Sem I\\Bus 211f Analyzing Big Data I\\Final Project\\dta_at_prod_id.csv")
b2=dta_at_prod_id.drop('Unnamed: 0', axis=1)
pd.io.sql.to_sql(b2,'products', con=engine, index=False, if_exists='append')

dta_at_TC = pd.read_csv("C:\\Users\\Aditya Didwania\\Desktop\\Brandeis\\Sem I\\Bus 211f Analyzing Big Data I\\Final Project\\dta_at_TC.csv")
b3=dta_at_TC.drop('Unnamed: 0', axis=1)
b3_1=b3[0:5000000]
b3_2=b3[5000000:10000000]
b3_3=b3[10000000:15000000]
b3_4=b3[15000000:20000000]
b3_5=b3[20000000:25000000]
b3_6=b3[25000000:30000000]
b3_7=b3[30000000:35000000]
b3_8=b3[35000000:40000000]
pd.io.sql.to_sql(b3_1,'purchases', con=engine, index=False, if_exists='append')
pd.io.sql.to_sql(b3_2,'purchases', con=engine, index=False, if_exists='append')
pd.io.sql.to_sql(b3_3,'purchases', con=engine, index=False, if_exists='append')
pd.io.sql.to_sql(b3_4,'purchases', con=engine, index=False, if_exists='append')
pd.io.sql.to_sql(b3_5,'purchases', con=engine, index=False, if_exists='append')
pd.io.sql.to_sql(b3_6,'purchases', con=engine, index=False, if_exists='append')
pd.io.sql.to_sql(b3_7,'purchases', con=engine, index=False, if_exists='append')
pd.io.sql.to_sql(b3_8,'purchases', con=engine, index=False, if_exists='append')


dta_at_tc_upc = pd.read_csv("C:\\Users\\Aditya Didwania\\Desktop\\Brandeis\\Sem I\\Bus 211f Analyzing Big Data I\\Final Project\\dta_at_tc_upc.csv")
b4=dta_at_tc_upc.drop('Unnamed: 0', axis=1)
dta_at_TC = pd.read_csv("C:\\Users\\Aditya Didwania\\Desktop\\Brandeis\\Sem I\\Bus 211f Analyzing Big Data I\\Final Project\\dta_at_TC.csv")
b4=dta_at_TC.drop('Unnamed: 0', axis=1)
b4_1=b4[0:5000000]
b4_2=b4[5000000:10000000]
pd.io.sql.to_sql(b4_1,'trips', con=engine, index=False, if_exists='append')
pd.io.sql.to_sql(b4_2,'trips', con=engine, index=False, if_exists='append')



