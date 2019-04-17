#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:24:27 2019

@author: alyssa
"""

#Parsing code:
import numpy as np
import csv

def ReadDataFile():
    csv_file = open('BattingLineUpData.csv')
    total_row = sum(1 for row in csv_file) - 1
    csv_file.seek(0)
    csv_reader = csv.reader(csv_file, delimiter=',')     
    global Blood_Glucose
    Blood_Glucose = np.zeros((total_row,))
    global Hemoglobin
    Hemoglobin = np.zeros((total_row,))
    Class = np.zeros((total_row,))
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(str(row))
        else:
            Blood_Glucose[line_count-1] = (int(row[0])-70)/420
            Hemoglobin[line_count-1] = (float(row[1])-3.1)/14.7
            Class[line_count-1] = int(row[2])
        line_count += 1
    print("Data Proccessed")
    csv_file.close()
    return Class, Hemoglobin, Blood_Glucose