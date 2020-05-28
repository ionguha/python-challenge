# Let us import the needed modules from library
import os # Allows us to create file paths across directories
import csv # Module for reading csv files
import sys # Module for system-specific parameters and functions
# Let us create the file path where the data resides
filename = 'budget_data.csv'
csvpath = os.path.join('Resources', filename)
# Let us create the file path where the analysis will be stored
outputfile = 'budget_analysis.txt'
output_txt_path = os.path.join('Analysis',outputfile)
# Initialize terminal
print('--------------')
print(f"Initial Check")
print('--------------')
# Check if the file exists
try:
    with open(csvpath, newline='',encoding='utf-8') as f:
        print(f"Found the file: {filename}")
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist")
# Let's create lists to store the data
Dates = [] # List to store the dates
Profit_Loss = [] # List to store Profit/Loss
Increment = [] # List to store incremental change in Profit/Loss
# Let's read the csv file using csv module
with open(csvpath) as csvfile: # Open the file
    # CSV reader reads the contents separated by delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row to see the column names
    csv_header = next(csvreader) # Also the counter is now moved by one
    # Write the header in the output txt file
    with open(output_txt_path,"w+") as txt_file:
        txt_file.write(f"Headers in {filename}: \n{csv_header}\n")
        txt_file.close()
    # Print the header row to show the column names
    print(f"Headers in {filename}: \n {csv_header}\n")
    # Let's read the rest of the rows and extract data
    try:
        for row in csvreader:
            date = row[0] # Date is in 1st column
            profit_or_loss = row[1] # Profit/Loss is in 2nd column
            Dates.append(date) # Save the Date in a list
            Profit_Loss.append(profit_or_loss) # Save Profit/Loss in a list
    except csv.Error as er: # Incase we encounter error in reading the file
        sys.exit('file {}, line {}: {}'.format(filename,csvreader.line_num,er))

print('---------------------')
print(f"Financial Analysis")
print('---------------------')
# Let's see how many items are there in the dataset
print(f"Total Months: {len(Dates)}")
# Let's calculate the total number of items in Profit_Loss
total = sum(int(pl) for pl in Profit_Loss) # Calculate the total 
print(f"Total : ${total}")
# Let's populate the list of incremental change
for n in range(len(Profit_Loss)-1):
    increment = int(Profit_Loss[n+1]) - int(Profit_Loss[n])
    Increment.append(increment)
# Let's calculate the average changes in the Increment list
total = sum(int(pl) for pl in Increment) # Calculate the total
print(f"Average Change : ${round((total/len(Increment)),2)}")
# Let's find the maximum of the Increment list
# max function returns the maximum of the list, .index returns the index of the maximum
# Since Increment list is one less than Dates list, we add 1 to the index value
print(f"Greatest Increase in Profits: {Dates[Increment.index(max(Increment))+1]} (${max(Increment)})")
# Let's find the minimum of the Increment list
# min function returns the minimum of the list, .index returns the index of the minimum
# Since Increment list is one less than Dates list, we add 1 to the index value
print(f"Greatest Decrease in Profits: {Dates[Increment.index(min(Increment))+1]} (${min(Increment)})")
# Write the output to 
with open(output_txt_path,"a") as txt_file:
        txt_file.write('--------------------\n')
        txt_file.write(f"Financial Analysis \n")
        txt_file.write('---------------------\n')
        txt_file.write(f"Total Months: {len(Dates)}\n")
        txt_file.write(f"Total : ${total}\n")
        txt_file.write(f"Average Change : ${round((total/len(Increment)),2)}\n")
        txt_file.write(f"Greatest Increase in Profits: {Dates[Increment.index(max(Increment))+1]} (${max(Increment)})\n")
        txt_file.write(f"Greatest Decrease in Profits: {Dates[Increment.index(min(Increment))+1]} (${min(Increment)})\n")
        txt_file.close()
        
