#this makes the code work across operating systems
import os

#this mod reads the CSV file
import csv
from datetime import date

text_output = ""
def load_data(budget_data):
    mylist = []
    with open(budget_data) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        diff = 0
        total_diff = 0
        net = 0
        previous_row = 0 
        greatest_increase = 0
        greatest_increase_month = ''
        greatest_decrease = 0
        greatest_decrease_month = ''
    
        #Counting total months
        for row in csv_reader:
            profit_loss = int(row['Profit/Losses'])
            net = net + profit_loss
            diff = profit_loss - previous_row
            previous_row = profit_loss

            if diff > greatest_increase:
                greatest_increase = diff
                greatest_increase_month = row['Date']

            if diff < greatest_decrease:
                greatest_decrease = diff
                greatest_decrease_month = row['Date'] 
            
            if len(mylist) > 0:
                total_diff = total_diff + diff

            mylist.append(row)
    
    #finding average change
    average_change = round(total_diff / (len(mylist) -1), 2)

    #text ouput component
    text_output = ('Financial Analysis\n'
    
    #\n ends the line
    f'Months {len(mylist)}\n' 
    f'Net Profit/Loss: {net}\n'
    f'Avg. Change: {average_change}\n'
    f'Greatest Increase: {greatest_increase_month}  ${greatest_increase}\n'
    f'Greatest Decrease: {greatest_decrease_month}  ${greatest_decrease}')

    return(text_output)

#resources component
text_out = load_data("Resources/budget_data.csv")
print(text_out)
output_file = "analysis/budget_analysis.txt"
with open(output_file, "w") as textfile:
   textfile.write(text_out)

   


