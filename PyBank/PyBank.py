#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

# Find csv file for the project on computer
import os
import csv

# Define variables in PyBank csv - what are we solving for
months = []
profit_loss_changes = []

month_count = 0
total_profit_loss = 0
previous_profit_loss = 0
current_profit_loss = 0
profit_loss_change = 0

# Change directory to match the current python code
os.chdir(os.path.dirname(__file__))

# make sure CSV files have the correct path to the CSV file
budget_data_csv_path = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_data_csv_path, newline="") as csvfile:

    #tell python that csv data is differentiated by a comma (delimiter)
    csv_reader = csv.reader(csvfile, delimiter=",")

    # tell python there is a header - read the header (Date, Profit/Losses)
    csv_header = next(csvfile)
             
    # Read rows after the header
    for row in csv_reader:

        # calculate how many months there are in the csv
        month_count += 1

        # count months of "Profit/Losses" through csv
        current_profit_loss = int(row[1])
        total_profit_loss += current_profit_loss

        # make sure the value of the previous month is equal to the current month
        if (month_count == 1):
            previous_profit_loss = current_profit_loss
            continue

        else:

            # mark down all changes in the profit loss 
            profit_loss_change = current_profit_loss - previous_profit_loss

            # make sure all months are noted
            #append function to list out all information being called
            months.append(row[0])

            # find the profit loss changes and add them to a list
            profit_loss_changes.append(profit_loss_change)

            # for the next loop, we need the current month profit/loss to move to next
            previous_profit_loss = current_profit_loss

    #calculate the total changes per month and average them for the entire csv
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(month_count - 1), 2)

    # find the greatest increase (highest) and greatest decrease (lowest) changes - min and max calculations
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # find greatest increase and decrease - use index function 
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    # Assign greatest increase and decrease to calculate values
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

# show results of the challenge
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_profit_loss}")
print(f"Greatest Increase in Profits: {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses: {worst_month} (${lowest_change})")


# create new .txt document with results
budget_file = os.path.join("Output", "budget_data.txt")
with open("budget_file", "w") as text:

    text.write("Financial Analysis\n")
    text.write("------------------------------\n")
    text.write(f"Total Months: {month_count}\n")
    text.write(f"Total: ${total_profit_loss}\n")
    text.write(f"Average Change: ${average_profit_loss}\n")
    text.write(f"Greatest Increase in Profits: {best_month} (${highest_change})\n")
    text.write(f"Greatest Decrease in Losses: {worst_month} (${lowest_change})\n")