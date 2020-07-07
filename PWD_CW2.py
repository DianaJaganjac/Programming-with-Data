# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:17:03 2019

@author: Diana Jaganjac
"""

import random as rand 
import matplotlib.pyplot as plt  
import time

#Phase 1

def myHealthcare(n):
    rand.seed(404)
    records = [] #I append the generated records to a list to create a 2D array/ matrix
    ts = 100
    for i in range(n): #n is the number of records to generate
        ts += 1
        temp = rand.randint(36,39) #rand.randint is used to generate the values I need
        hr = rand.randint(55, 100)
        pulse = rand.randint(55, 100)
        bloodpr = rand.randint(120, 121)
        resrate = rand.randint(11, 17)
        oxsat = rand.randint(93, 100)
        ph = round(rand.uniform(7.1,7.6),1)
        records.append([ts] +[temp] + [hr] + [pulse] + [bloodpr] + [resrate] + [oxsat] +[ph])
    
    return records  
        
#x = myHealthcare(1000)
#print(x)
    
#Phase 2
    
def abnormalSignAnalytics(n):
    rand.seed(404)
    choice = input('Please choose to view Abnormal rates for Blood Pressure or Pulse')
    #I give a choice of either results for Pulse or Blood Pressure as user input to seperate these
    abpulsehist = []
    abpulse = []
    abbloodpr = []
    abbloodprhist = []
    countpulse = 0
    countbloodpr = 0
    for i in range(n):
       records = myHealthcare(n) #generate records according to n in function abnormalSignAnalytics
       if choice == 'Pulse':
           if records[i][3] >= 55 and records[i][3]  <= 59 or records[i][3] == 100: #these are abnormal values
               abpulsehist.append(records[i][3]) #append abnormal records to a list for the histogram
               abpulse.append((records[i][0], records[i][3])) #append abnormal records as a tuple to a list
               countpulse += 1 #keep track of count for output 
               
               plt.style.use('ggplot')
               plt.xlabel('Abnormal Pulse Rates')
               plt.ylabel('Count')
               plt.title('Frequency Histogram of Abnormal Pulse Rates') #The titles and labels are specific to each graph so are not a redundant repetition of code
               plt.hist(abpulsehist, bins=50) #I set bins to 50 through this function so that each value has its own bin/ bar and is easy to identify and visualise 
               # I include the histogram code within the function to automatically generate the histogram with the results 
               
        
               
       if choice == 'Blood Pressure':    
           if records[i][4] == 121: #there is only one abnormal value for Blood Pressure
               abbloodprhist.append(records[i][4]) #append abnormal records to a list for the histogram
               abbloodpr.append((records[i][0], records[i][4])) #append abnormal records as a tuple to a list
               countbloodpr += 1
               
               plt.style.use('ggplot')
               plt.xlabel('Abnormal Blood Pressure Rates')
               plt.ylabel('Count')
               plt.title('Frequency Histogram of Abnormal Blood Pressure Rates') #The titles and labels are specific to each graph so are not a redundant repetition of code
               plt.hist(abbloodprhist, bins=50)
    
    # I return the selected results as a list, and the histogram for the selected vital sign, either Blood Pressure or Pulse           
    return ['pulse, ' + str(countpulse) + ' ' + str(abpulse)], ['blood pressure, ' + str(countbloodpr) + ' ' + str(abbloodpr)]
    return plt.show       
         


#x= abnormalSignAnalytics(50)
#print(x)
    
def abnormalSignAnalyticsbin(mat):
    # I take the already generated matrix as input and do not generate within the function
    rand.seed(404)
    choice = input('Please choose to view Abnormal rates for Blood Pressure or Pulse')
    #I give a choice of either results for Pulse or Blood Pressure as user input to seperate these
    abpulsehist = []
    abpulse = []
    abbloodpr = []
    abbloodprhist = []
    countpulse = 0
    countbloodpr = 0
    for row in mat: 
       mid = ((len(row)-1)//2) #I set the value of mid of the matrix for binary search
       for mid in row: #I evaluate every row individually by binary search
           if choice == 'Pulse':
               if mid >= 55 and mid <= 59 or mid == 100:
                   abpulsehist.append(mid) # I append results to a list for the histogram
                   abpulse.append((row[0], mid)) #I append results as a tuple to a list
                   countpulse += 1 #I only count the relevant values, i.e when mid equals an abnormal value 
               elif mid < 55:
                   mid += 1 #if mid is < 55 I increase the index of mid until mid fits the criteria for the abnormal values
               else:
                   if mid > 59 or mid > 100:
                       mid -= 1 # if mid > 59 or 100 I decrease the index of mid until mid fits the criteria for the abnormal values
 
               
               plt.style.use('ggplot')
               plt.xlabel('Abnormal Pulse Rates')
               plt.ylabel('Count')
               plt.title('Frequency Histogram of Abnormal Pulse Rates') #The titles and labels are specific to each graph so are not a redundant repetition of code
               plt.hist(abpulsehist, bins=50)
               
        
               
           if choice == 'Blood Pressure':    
               if mid == 121: 
                   abbloodprhist.append(mid) #I append the relevant results to the relevant lists 
                   abbloodpr.append((row[0], mid))
                   countbloodpr += 1 #I only keep track of when mid equals an abnormal value
               else:
                   if mid < 121:
                       mid += 1 
                #As there are only 2 options for Blood Pressure, 120 or 121, I only include mid < 121 as the only other value it can be is 120. 
                # If mid is 120, I increase the index of mid by 1 to 121 which is an abnormal value 
                       
               
               plt.style.use('ggplot')
               plt.xlabel('Abnormal Blood Pressure Rates')
               plt.ylabel('Count')
               plt.title('Frequency Histogram of Abnormal Blood Pressure Rates')
               plt.hist(abbloodprhist, bins=50)
               
    # I return the selected results as a list, and the histogram for the selected vital sign, either Blood Pressure or Pulse            
    return ['pulse, ' + str(countpulse) + ' ' + str(abpulse)], ['blood pressure, ' + str(countbloodpr) + ' ' + str(abbloodpr)]
    return plt.show       
         

#mat = myHealthcare(50)
#x= abnormalSignAnalyticsbin(mat)
#print(x)

    
def frequencyAnalytics(n):
    rand.seed(404)
    total = [] # I use a list to append all my results for pulse rates
    count = {} # I use a dictionary to count repeated values for pulse rates
    
    
    for i in range(n):
        records = myHealthcare(n) # I generate records according to the value of n in the frequencyAnalytics function 
        total.append(records[i][3]) # I append the records for pulse rates to the list total
        
    for i in total: 
        if i not in count:
            count[i] = 1 
            # if the values in total are not in the dictionary count, I append them to the dictionary as a key and set 1 as the value for each key 
        else:
            count[i] = count[i] + 1
            # for repeated values in total, I increase the value by 1 therefore keeping count of how many of each key there are
            
    plt.style.use('ggplot')     
    plt.xlabel('Pulse')
    plt.ylabel('Count')
    plt.title('Frequency Histogram of Pulse Rates') 
    # I plot a histogram with relevant titles and labels
    
    plt.hist(total, bins = 45) #I set the bins value to 45 so that the y-axis count reflects the number of values generated and is easily visualised 
    
    return count   
    return plt.show       
           
#x = frequencyAnalytics(50)  
#print(x)
    
#Phase 3

def HealthAnalyser(n, x):
    rand.seed(404)
    alist = []
    heartrate = []
    for i in range(n):
        records = myHealthcare(n) #I generate the number of records according to n in HealthAnalyser
    
        if records[i][3] == x: # x is the value I am looking for, i.e 56 and is an argument of HealthAnalyser
            alist.append(records[i][0:8]) #if the pulse rate value equals x, I append the entire list to alist
            heartrate.append(records[i][2]) #I also append the values for heartrate when pulse equals x to another list called heartrate for the histogram 
            
            plt.style.use('ggplot')
            plt.xlabel('Heart Rate Values')
            plt.ylabel('Count')
            plt.title('Frequency Histogram of Heart Rate Values')
            plt.hist(heartrate, bins= 45) #I set bins to 45 so that each value for heartrate can have its own bar, and count is easily represented and visualised. 
        
    return alist
    return plt.show  

#x = HealthAnalyser(1000, 56)
#print(x)

def binsearch(mat, x): #mat is the matrix and x is the value we are looking for, i.e. 56 
    rand.seed(404)
    alist = []
    blist = []
    for row in mat:
        mid = ((len(row)-1)//2) #I assign a mid value to every row in the matrix
        for mid in row: # I use mid as an index to search in each row
            if mid == x: 
                alist.append(row) #if mid equals x then I append to alist 
            elif mid < x:
                mid += 1 #if mid is < x I increase the index of mid by 1
            else:
                if mid > x: #if mid is > x I decrease the index of mid by 1
                    mid -= 1
    for r in alist:
        if r[3] == x: #as heart rate values can also be 56, I filter these out and append the pulse rate values of 56 to blist 
            blist.append(r)
    return blist

#mat =  myHealthcare(1000)
#x = 56       
#res = binsearch(mat, x)
#print(res) 
    
def intersearch(mat, x): #mat is the matrix and x is the value we are looking for, i.e. 56 
    rand.seed(404)
    alist = []
    blist = []
    low = 0 #low is the lowest index in each row
    high = 7 #high is the highest value in each row 
    for row in mat: #I use a for loop to iterate through the rows in the matrix
        L = row[0] #I assign the lowest index value in each row to L
        H = row[7] #I assign the highest index value in each row to H
        pos = low + (((high - low)/(H - L))*(x - L)) #I assign pos and apply to it the formula for interpolation search 
        for pos in row:
            if pos == x:
                alist.append(row) #if the first generated index position is x then I append this to alist
            elif pos < x:
                low += 1 #if pos is < x I increase the index of pos by 1
            else:
                if pos > x:
                    high -= 1 #if pos is > x I decrease the index of pos by 1
    for r in alist:
        if r[3] == x: #I filter out the heart rate values which could also be 56, and append only pulse rate values of 56 to blist 
            blist.append(r)
    return blist

#mat =  myHealthcare(1000)
#x = 56       
#res = intersearch(mat, x)
#print(res)

#Phase 4  
  
def benchmarking(n):
    rand.seed(404)
    start = time.time() #record start time
    myHealthcare(n) #run myHealthcare function 
    end = time.time() #record end time
    return (end-start) #return the total time it took to run the function 


reps = [1000, 2500, 5000, 7500, 10000]
ls = []
for n in reps:
    ls.append(benchmarking(n))
#I use the list reps to iterate through each value of n and run the benchmarking function

names = ['1000', '2500', '5000', '7500', '10000']

plt.style.use('ggplot')
plt.xlabel('Repetitions')
plt.ylabel('Time Taken')
plt.title('MyHealthcare Device Benchmarking')
plt.plot(names, ls) #I set the x-axis as names, and the y-axis as the results from the benchmarking(n) function
plt.show()
    
print(ls)
