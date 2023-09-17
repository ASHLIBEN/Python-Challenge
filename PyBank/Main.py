#importing os and csv file to read csv files
import os
import csv

#Set path for csv file to a variable
csvpath = os.path.join("Resources","budget_data.csv")

#Variable declaration and initialization
total_months=[]
total_profits=[]
profit_changes=[]
monthly_changes=[]

#Open CSV file

with open(csvpath,newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    #skipping header to be counted 
    csv_header= next(csvfile)
  #  print(f"Header:{csv_header}")

#read each row of data after the header
    for rows in csvreader:
        total_profits.append(int(rows[1]))
        total_months.append(rows[0])
    for x in range(1,len(total_profits)):
        profit_changes.append((int(total_profits[x])-int(total_profits[x-1])))
        #To find average changes
        monthly_changes=sum(profit_changes)/len(profit_changes)

    #Calculate number of months
    months=len(total_months)
#To find greatest increase in profit
greatest_increase = max(profit_changes)
#To find greatest decrease in profit
greatest_decrease = min(profit_changes)
#To print results
print("Financial Analysis")
print(".....................................")
print("  ")
print("Total Months:"+str(months))
print("  ")
print("Total:"+"$" + str(sum(total_profits)))
print("  ")
print("Average change:" + "$" +str(monthly_changes))
print("  ")
print("Greatest increase in profits:" + str(total_months[profit_changes.index(max(profit_changes))+1])+""+"$"+ str(greatest_increase))
print("  ")
print("Greatest decrease in profits:" + str(total_months[profit_changes.index(min(profit_changes))+1])+""+"$"+ str(greatest_decrease))
print(".....................................")

print("  ")  
