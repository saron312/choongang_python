# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:04:02 2022

@author: user
"""

import csv
import matplotlib.pyplot as plt
f = open('c:\\backup\card.csv', encoding='utf8')
data = csv.reader(f)
next(data)
data=list(data)
#print(data)
s_mon=[0,0,0]
for row in data:
    if row[-1] =='전표매입':
        mon,payment=int(row[0].split('-')[1]),int(row[-3])
        #print(mon,payment)
        idx = mon-10
        #print(idx)
        s_mon[idx] += payment
plt.rc('font',family='malgun gothic')
plt.title('10~12월 지출현황')
plt.bar(['10월','11월','12월'], s_mon, color='royalblue')
plt.show()