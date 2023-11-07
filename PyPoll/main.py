import os
import csv

# Set the file path
file_path =  r'C:\Repos (UCB)\python_challenge\PyPoll\Resources\election_data.csv'

# Initialize variables
total_votes = 0
candidate_votes = {}

# Read the CSV file
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  # Skip the header row
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

# Calculate the percentage of votes each candidate won
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Find the winner based on the popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Ensure the 'analysis' directory exists
output_directory = r"C:\Repos (UCB)\python_challenge\PyPoll\analysis"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Write the analysis results to a text file
output_path = os.path.join(output_directory, "election_results.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        txtfile.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
