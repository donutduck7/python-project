import os
import csv

# Set the file path
file_path =  r'C:\Repos (UCB)\python_challenge\PyBank\Resources\budget_data.csv'

# Initialize lists to store data
months = []
profit_losses = []

# Read the CSV file
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  # Skip the header row
    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))

# Calculate the total number of months
total_months = len(months)

# Calculate the net total amount of profit/losses
net_total = sum(profit_losses)

# Calculate the changes in profit/losses over the entire period
profit_changes = [profit_losses[i + 1] - profit_losses[i] for i in range(len(profit_losses) - 1)]

# Calculate the average of those changes
average_change = sum(profit_changes) / len(profit_changes)

# Find the greatest increase in profits (date and amount)
max_increase = max(profit_changes)
max_increase_date = months[profit_changes.index(max_increase) + 1]

# Find the greatest decrease in profits (date and amount)
max_decrease = min(profit_changes)
max_decrease_date = months[profit_changes.index(max_decrease) + 1]

# Print the analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")

# Ensure the 'analysis' directory exists
output_directory = r"C:\Repos (UCB)\python_challenge\PyBank\analysis"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Write the analysis results to a text file
output_path = os.path.join(output_directory, "financial_analysis.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n")