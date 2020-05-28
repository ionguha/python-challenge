# Let us import the needed modules from library
import os # Allows us to create file paths across directories
import csv # Module for reading csv files
import sys # Module for system-specific parameters and functions
# Let us create the file path where the election data resides
filename = 'election_data.csv'
csvpath = os.path.join('Resources', filename)
# Let us create the file path where the analysis will be stored
outputfile = 'election_analysis.txt'
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
Voter_ID = [] # List to store the voter i.d.
County = [] # List to store name of the county
Candidate = [] # List to store name of the candidate
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
    print(f"Headers in {filename}: \n {csv_header}")
    # Let's read the rest of the rows and extract data
    try:
        for row in csvreader:
            voter_id = row[0] # Voter ID is in 1st column
            county = row[1] # County name is in 2nd column
            candidate = row[2] # Candidate name is in 3rd column
            Voter_ID.append(voter_id) # Save Voter I.D. in the list
            County.append(county) # Save the County name in the list
            Candidate.append(candidate) # Save Candidate name in the list
    except csv.Error as er: # Incase we encounter error in reading the file
        sys.exit('file {}, line {}: {}'.format(filename,csvreader.line_num,er))
print('---------------------------------')
print(f"Worksheet : Tallying the votes")
print('---------------------------------')
# Let's see how many unique candidates are there in the election
# We shall make a list of candidates (only unique candidate names)
Candidate_list = list(set(Candidate))
print(f"Number of unique candidates: {len(Candidate_list)}")
print('---------------------------------')
print(f"Candidates in this election are:")
print('---------------------------------')
# Let's print the unique candidate names
for candidate in Candidate_list:
    print(candidate)
# Let's see how many unique counties are there in the election
# We shall make a list of counties (only unique county names)
County_list = list(set(County))
print('-------------------------------')
print(f"Number of unique counties: {len(County_list)}")
print('-------------------------------')
print(f"Counties in this election are:")
print('-------------------------------')
# Let's print the unique candidate names
for county in County_list:
    print(county)
Vote_Tally = [] # List to keep the total votes won by each candidate
County_Tally = [] # List to keep the total votes from each county
# Let's populate the Vote_tally with total votes won by each candidate
for candidate in Candidate_list:
    votes = Candidate.count(candidate)
    Vote_Tally.append(votes)
# Let's populate the County_tally with total votes from each county
for county in County_list:
    votes = County.count(county)
    County_Tally.append(votes)
# Let's print the Vote_tally grouped by candidates
print('---------------------------------')
print(f"Votes won by each candidate")
print('---------------------------------')
for (name, total_vote) in zip(Candidate_list,Vote_Tally):
    print(f"{name} : {total_vote}")
# Let's print the Vote_tally grouped by counties
print('------------------------------------')
print(f"Votes reported by each county")
print('------------------------------------')
for (name, total_vote) in zip(County_list,County_Tally):
    print(f"{name} : {total_vote}")
print('----------------------------')
print(f"    Election Results       ")
print('----------------------------')
# Let's make sure we have unique voter_ids, i.e. one vote per voter_id
if (len(Voter_ID) == len(set(Voter_ID))):
    # Voter_id is correct representation of votes
    print(f"Total votes: {len(Voter_ID)}")
    total_votes = len(Voter_ID)
else:
    print(f"Error in Voter_ID list: Not correct vote-count")
print('----------------------------')
# Let's print election results for each candidate
winner_name = ''
for (name, vote) in zip(Candidate_list,Vote_Tally):
        percent_vote = format((100* (vote / total_votes)),'.3f')
        print(f"{name} : {percent_vote}% ({vote})")
        if (vote == max(Vote_Tally)):
                winner_name = name
                winner_votes = vote
print('----------------------------')
# Before declaring the winner let's check if there is a draw
# Let's copy the Candidate_list and Vote_Tally to new lists for manipulations
Candidate_list2 = Candidate_list.copy()
Vote_Tally2 = Vote_Tally.copy()
runner_up_name = ''
Vote_Tally2.remove(max(Vote_Tally))
Candidate_list2.remove(winner_name)
for (name, vote) in zip(Candidate_list2,Vote_Tally2):
        if (vote == max(Vote_Tally2)):
                runner_up_name = name
                runner_up_votes = vote
# Difference in number of votes between winner and runner up
vote_diff = winner_votes - runner_up_votes
vote_diff_percent = format((100* (vote_diff / total_votes)),'.2f')
# Let's find the winner of this election
if(winner_name == runner_up_name):
    print(f"We have a draw between {winner_name} & {runner_up_name}")
else:
    print(f"Winner    : {winner_name}")
print('----------------------------')
print(f"Runner-up : {runner_up_name}")
print('--------------------------------------')
print(f"{runner_up_name} got {vote_diff_percent}% ({vote_diff}) less votes")
print('--------------------------------------')
# Writing the output to a file in Analysis folder
with open(output_txt_path,"a") as txt_file:
        txt_file.write('-------------------------------\n')
        txt_file.write(f"Worksheet : Tallying the votes \n")
        txt_file.write('--------------------------------\n')
        txt_file.write(f"Number of Candidates: {len(Candidate_list)}\n")
        txt_file.write('--------------------------------\n')
        txt_file.write(f"Candidate Names \n")
        txt_file.write('--------------------------------\n')
        for candidate in Candidate_list:
                txt_file.write(f"{candidate}\n")
        txt_file.write('--------------------------------\n')
        txt_file.write(f"Number of Counties: {len(County_list)}\n")
        txt_file.write('--------------------------------\n')
        txt_file.write(f"County Names \n")
        txt_file.write('--------------------------------\n')
        for county in County_list:
                    txt_file.write(f"{county}\n")
        txt_file.write('--------------------------------\n')
        txt_file.write(f"Votes won by each candidate \n")
        txt_file.write('--------------------------------\n')
        for (name, total_vote) in zip(Candidate_list,Vote_Tally):
                   txt_file.write(f"{name} : {total_vote}\n") 
        txt_file.write('--------------------------------\n')
        txt_file.write(f"Votes reported by each county \n")
        txt_file.write('--------------------------------\n')
        for (county, total_vote) in zip(County_list,County_Tally):
                   txt_file.write(f"{county} : {total_vote}\n")
        txt_file.write('--------------------------------\n')
        if (len(Voter_ID) == len(set(Voter_ID))):
            txt_file.write('Voter_ID Check : Passed \n')
        else:
            txt_file.write('Voter_ID Check : Failed !! \n')
        txt_file.write('--------------------------------\n')
        txt_file.write(f"    Election Results \n")
        txt_file.write('--------------------------------\n')        
        txt_file.write(f"Total votes: {len(Voter_ID)}\n")
        txt_file.write('--------------------------------\n')
        for (name, vote) in zip(Candidate_list,Vote_Tally):
                percent_vote = format((100* (vote / total_votes)),'.3f')
                txt_file.write(f"{name} : {percent_vote}% ({vote})\n")
        txt_file.write('--------------------------------\n')
        if(winner_name == runner_up_name):
                txt_file.write(f"We have a draw between {winner_name} & {runner_up_name}\n")
        else:
                txt_file.write(f"Winner    : {winner_name}\n")
        txt_file.write('--------------------------------\n')
        txt_file.write(f"Runner-up : {runner_up_name}\n")
        txt_file.write('--------------------------------------\n')
        txt_file.write(f"{runner_up_name} got {vote_diff_percent}% ({vote_diff}) less votes\n")
        txt_file.write('--------------------------------------\n')
        txt_file.write(f"End of Report\n")
        txt_file.close()
