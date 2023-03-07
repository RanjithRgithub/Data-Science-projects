# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 14:27:01 2022

@author: DELL
"""

import pandas as pd
df = pd.read_csv('weatherAUS.csv')

#print(df.duplicated().sum())
#print(df.isnull().sum())

#-----Finding the unique characters present in column fpr assigning values to them
print(df.WindDir3pm.unique())
print(df.WindDir9am.unique())
print(df.WindGustDir.unique())

df = df.fillna(0)

#---- Assigning values to the characters
df.loc[df['WindGustDir']=='NA',  'WindGustDir'] == 0
df.loc[df['WindGustDir']=='E',   'WindGustDir'] = 1
df.loc[df['WindGustDir']=='W',   'WindGustDir'] = 2
df.loc[df['WindGustDir']=='N',   'WindGustDir'] = 3
df.loc[df['WindGustDir']=='S',   'WindGustDir'] = 4
df.loc[df['WindGustDir']=='NE',  'WindGustDir'] = 5
df.loc[df['WindGustDir']=='SW',  'WindGustDir'] = 6
df.loc[df['WindGustDir']=='NW',  'WindGustDir'] = 7
df.loc[df['WindGustDir']=='SE',  'WindGustDir'] = 8
df.loc[df['WindGustDir']=='WNW', 'WindGustDir'] = 9
df.loc[df['WindGustDir']=='WSW', 'WindGustDir'] = 10
df.loc[df['WindGustDir']=='NNW', 'WindGustDir'] = 11
df.loc[df['WindGustDir']=='NNE', 'WindGustDir'] = 12
df.loc[df['WindGustDir']=='ENE', 'WindGustDir'] = 13
df.loc[df['WindGustDir']=='SSE', 'WindGustDir'] = 14
df.loc[df['WindGustDir']=='SSW', 'WindGustDir'] = 15
df.loc[df['WindGustDir']=='ESE', 'WindGustDir'] = 16

df.loc[df['WindDir9am']=='NA',  'WindDir9am'] == 0
df.loc[df['WindDir9am']=='E',   'WindDir9am'] = 1
df.loc[df['WindDir9am']=='W',   'WindDir9am'] = 2
df.loc[df['WindDir9am']=='N',   'WindDir9am'] = 3
df.loc[df['WindDir9am']=='S',   'WindDir9am'] = 4
df.loc[df['WindDir9am']=='NE',  'WindDir9am'] = 5
df.loc[df['WindDir9am']=='SW',  'WindDir9am'] = 6
df.loc[df['WindDir9am']=='NW',  'WindDir9am'] = 7
df.loc[df['WindDir9am']=='SE',  'WindDir9am'] = 8
df.loc[df['WindDir9am']=='WNW', 'WindDir9am'] = 9
df.loc[df['WindDir9am']=='WSW', 'WindDir9am'] = 10
df.loc[df['WindDir9am']=='NNW', 'WindDir9am'] = 11
df.loc[df['WindDir9am']=='NNE', 'WindDir9am'] = 12
df.loc[df['WindDir9am']=='ENE', 'WindDir9am'] = 13
df.loc[df['WindDir9am']=='SSE', 'WindDir9am'] = 14
df.loc[df['WindDir9am']=='SSW', 'WindDir9am'] = 15
df.loc[df['WindDir9am']=='ESE', 'WindDir9am'] = 16

df.loc[df['WindDir3pm']=='NA',  'WindDir3pm'] == 0
df.loc[df['WindDir3pm']=='E',   'WindDir3pm'] = 1
df.loc[df['WindDir3pm']=='W',   'WindDir3pm'] = 2
df.loc[df['WindDir3pm']=='N',   'WindDir3pm'] = 3
df.loc[df['WindDir3pm']=='S',   'WindDir3pm'] = 4
df.loc[df['WindDir3pm']=='NE',  'WindDir3pm'] = 5
df.loc[df['WindDir3pm']=='SW',  'WindDir3pm'] = 6
df.loc[df['WindDir3pm']=='NW',  'WindDir3pm'] = 7
df.loc[df['WindDir3pm']=='SE',  'WindDir3pm'] = 8
df.loc[df['WindDir3pm']=='WNW', 'WindDir3pm'] = 9
df.loc[df['WindDir3pm']=='WSW', 'WindDir3pm'] = 10
df.loc[df['WindDir3pm']=='NNW', 'WindDir3pm'] = 11
df.loc[df['WindDir3pm']=='NNE', 'WindDir3pm'] = 12
df.loc[df['WindDir3pm']=='ENE', 'WindDir3pm'] = 13
df.loc[df['WindDir3pm']=='SSE', 'WindDir3pm'] = 14
df.loc[df['WindDir3pm']=='SSW', 'WindDir3pm'] = 15
df.loc[df['WindDir3pm']=='ESE', 'WindDir3pm'] = 16

 
df.loc[df['RainToday']=='No',     'RainToday'] = 0
df.loc[df['RainToday']=='Yes',    'RainToday'] = 1
df.loc[df['RainTomorrow']=='Yes', 'RainTomorrow'] = 1
df.loc[df['RainTomorrow']=='No',  'RainTomorrow'] = 0

print(df.WindDir3pm.unique())
print(df.WindDir9am.unique())
print(df.WindGustDir.unique())
print(df.RainToday.unique())
print(df.RainTomorrow.unique())


x = df.drop(['Date','Location','RainToday','RainTomorrow'], axis=1)
y = df['RainToday'].astype('int')
z = df['RainTomorrow'].astype('int')
 

from sklearn.neighbors import KNeighborsClassifier
alg = KNeighborsClassifier(n_neighbors=3)
alg1 = KNeighborsClassifier(n_neighbors=3)
# Training the dataset for Rain Today
alg.fit(x,y)
# Training the dataset for Rain Tomorrow
alg1.fit(x,z)

var0 =  input("Ënter the MinTemp value")
var1 =  input("Ënter the MaxTemp value")
var2 =  input("Ënter the Rainfall value")
var3 =  input("Ënter the Evaporation value")
var4 =  input("Ënter the Sunshine value")
var5 =  input("Ënter the Wind Gust Direction")
var6 =  input("Ënter the Wind Gust Speed")
var7 =  input("Ënter the Wind Direction at 9am")
var8 =  input("Ënter the Wind Direction at 3pm")
var9 =  input("Ënter the Wind Speed at 9am")
var10 = input("Ënter the Wind Speed at 3pm")
var11 = input("Ënter the Humidity at 9am")
var12 = input("Ënter the Humidity at 3pm")
var13 = input("Ënter the Pressure at 9am")
var14 = input("Ënter the Pressure at 3pm")
var15 = input("Ënter the Cloud at 9am")
var16 = input("Ënter the Cloud at 3pm")
var17 = input("Ënter the Temperature at 9am")
var18 = input("Ënter the Temperature at 3pm")
 
#if var0 or var1 or var3 or var4 or var5 or var6 or var7 | var8 | var9 | var10 | var11 | var12 | var13 | var14 | var15 | var16 | var17 | var18 == 'NA':
#--- If the input variable is NA then convert to 0
if var0 == 'NA':
    var0 = 0
if var1 == 'NA':
    var1 = 0
if var2 == 'NA':
    var2 = 0
if var3 == "NA":
    var3 = 0
if var4 == 'NA':
    var4 = 0
if var5 == 'NA':
    var5 = 0
if var6 == 'NA':
    var6 = 0
if var7 == "NA":
    var7 = 0
if var8 == 'W':
    var8 = 3
if var9 == 'NA':
    var9 = 0
if var10 == 'NA':
    var10 = 0
if var11 == 'NA':
    var11 = 0
if var12 == 'NA':
    var12 = 0
if var13 == "NA":
    var13 = 0
if var14 == 'NA':
    var14 = 0
if var15 == 'NA':
    var15 = 0
if var16 == 'NA':
    var16 = 0
if var17 == "NA":
    var17 = 0
if var18 == 'NA':
    var18 = 0

# Assigning values to input characters
if var5 == 'E':
    var5 = 1
if var5 == 'W':
    var5 = 2
if var5 == 'N':
    var5 = 3
if var5 == 'S':
    var5 = 4
if var5 == 'NE':
    var5 = 5
if var5 == 'SW':
    var5 = 6
if var5 == 'NW':
    var5 = 7
if var5 == 'SE':
    var5 = 8
if var5 == 'WNW':
    var5 = 9
if var5 == 'WSW':
    var5 = 10
if var5 == 'NNW':
    var5 = 11
if var5 == 'NNE':
    var5 = 12
if var5 == 'ENE':
    var5 = 13
if var5 == 'SSE':
    var5 = 14
if var5 == 'SSW':
    var5 = 15
if var5 == 'ESE':
    var5 = 16
    
if var7 == 'E':
    var7 = 1
if var7 == 'W':
    var7 = 2
if var7 == 'N':
    var7 = 3
if var7 == 'S':
    var7 = 4
if var7 == 'NE':
    var7 = 5
if var7 == 'SW':
    var7 = 6
if var7 == 'NW':
    var7 = 7
if var7 == 'SE':
    var7 = 8
if var7 == 'WNW':
    var7 = 9
if var7 == 'WSW':
    var7 = 10
if var7 == 'NNW':
    var7 = 11
if var7 == 'NNE':
    var7 = 12
if var7 == 'ENE':
    var7 = 13
if var7 == 'SSE':
    var7 = 14
if var7 == 'SSW':
    var7 = 15
if var7 == 'ESE':
    var7 = 16

if var8 == 'E':
    var8 = 1
if var8 == 'W':
    var8 = 2
if var8 == 'N':
    var8 = 3
if var8 == 'S':
    var8 = 4
if var8 == 'NE':
    var8 = 5
if var8 == 'SW':
    var8 = 6
if var8 == 'NW':
    var8 = 7
if var8 == 'SE':
    var8 = 8
if var8 == 'WNW':
    var8 = 9
if var8 == 'WSW':
    var8 = 10
if var8 == 'NNW':
    var8 = 11
if var8 == 'NNE':
    var8 = 12
if var8 == 'ENE':
    var8 = 13
if var8 == 'SSE':
    var8 = 14
if var8 == 'SSW':
    var8 = 15
if var8 == 'ESE':
    var8 = 16


inp = [var0,var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18]
a = inp
print(inp)
ypred = alg.predict([inp])
ypred1 = alg1.predict([a])

print(ypred)
print(ypred1)
'''
if ypred[0]==1:
    print('-------Rain falls Today---------')
else:
    print('----------NO Rainfall for today-----------')

if ypred1[0]==1:
    print('--------Rain falls for tomorrow------------')
else:
    print('------No Rainfall for tomorrow-------')

'''
if ypred[0]==0 and ypred1[0] == 0:
    print('---------Rain does not falls for both Today & Tomorrow----------')
elif ypred[0]==1 and ypred1[0]==1:
    print('-----Rain falls for both today and tomorrow-----')
elif ypred[0]==1 or ypred[0]==0:
    print('-----Rain falls for today  but not for tomorrow--------')
elif ypred[0]==0 or ypred[0]==1:
    print('-----Rain does not fall for todays but falls for tomorrow--')

else:
    print('----------------------------')
 

#13.1	30.1	1.4	NA	NA	W	28	S	SSE	15	11	58	27	1007	1005.7	NA	NA	20.1	28.2


    