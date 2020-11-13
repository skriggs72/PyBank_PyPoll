# Import Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Set the output of the text file
text_path = ('Analysis/finanalysis.txt')

#Set variables
sum_profit = 0
sum_loss = 0
revenue = 0
profit = 0
monthly_profit_change = []
revenue_change = 0
previous_revenue = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]
revenue_average = 0
total_profit = []
listofdates = []

# Open the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
               
# Count the number of months in dataset
    months = sum(1 for row in csvreader)
    
    print("Financial Analysis")
    print("-----------------------------------------------")
    print(f"Total Months: {months}")
    
# Calculate the total net Profit/Losses
    csvfile.seek(0)
    next(csvreader)
    for row in csvreader:
        profit = int(row[1])
        date = row[0]
        listofdates.append(date)
        if profit > 0:
            sum_profit = sum_profit + profit
        elif profit < 0:
            sum_loss = sum_loss - profit
        total_profit.append(profit)
    revenue = sum_profit - sum_loss
    print(f"Total Revenue: ${revenue}")

# Calculate the changes in Profit/Losses then find the average of changes
    
    for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        average_change = {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}
    print(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")    

# Find the greatest increase and decrease in profits
    budget_data_max = max(monthly_profit_change)
    budget_data_min = min(monthly_profit_change)
    maxdate = (monthly_profit_change.index(budget_data_max))
    mindate = (monthly_profit_change.index(budget_data_min))
    budget_data_maxdate = (listofdates[maxdate+1])
    budget_data_mindate = (listofdates[mindate+1])
    print(f"Maximum Increase = {budget_data_maxdate}, ${budget_data_max}")
    print(f"Minimum Decrease = {budget_data_mindate}, ${budget_data_min}")
    
# Create a text file with the results
with open(text_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write("Total Months: %d\n" % months)
    file.write("Total Revenue: $%d\n" % revenue)
    file.write("Average Change: $%s\n" % round(sum(monthly_profit_change)/len(monthly_profit_change),2))
    file.write("Greatest Increase in Profits: %s ($%s)\n" % (budget_data_maxdate, budget_data_max))
    file.write("Greatest Decrease in Profits: %s ($%s)\n" % (budget_data_mindate, budget_data_min))


