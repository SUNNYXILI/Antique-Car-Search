#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 23:55:13 2019

@author: lixi
"""

import pandas as pd
df=pd.read_csv("cars.csv")
df=df[["Model","MPG","Origin","Horsepower"]]


while True:
    print("Welcome to Antique Car Search")
    print("===============================")
    print("1-Search Car")
    print("2-Green Best/Worst Report")
    print("3-Car Origin Report")
    print("0-Exit")
    
    selectFeature=input("What do you want to do?")
    
    if selectFeature=="1":
        MinMpg=int(input("Required:"))
        MinHorsepower=int(input("Required Min.Horsepower:"))
        fdf=df[(df["MPG"]>=MinMpg)&(df["Horsepower"]>=MinHorsepower)]
        index = fdf.index
        number_of_rows = len(index)
        print("Found", number_of_rows ,"cars matching the criteria.")
        print(fdf["Model"])
    if selectFeature=="2":
        AveMpg=df.MPG.mean()
        Greenest=df.MPG.idxmax()
        print(Greenest)
       
        Worstcar=df[df["MPG"]==df["MPG"].min()]
        print(Worstcar)
        print("Ave.MPG of all cars is : ",AveMpg)
        print("Greenest car is ",df.loc[Greenest,"Model"] )
        print("Worst Car is ",Worstcar["Model"])
    if selectFeature=="3":
        
        org = df[["Origin", "MPG"]]  
        ret = org.groupby("Origin").count()
        print(ret)
        
    
            
    if selectFeature=="4":
        break