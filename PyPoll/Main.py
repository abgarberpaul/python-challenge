#PyPoll Code

# Modules
import os
import csv

#set variables
vote_count = 0
#vote = 0

#set empty dictionary
candidatelist = {}

# Set path for file
csvpath = os.path.join("PyPoll", "Resources", "PyPollData.csv")

#Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader: 
        vote_count += 1
        candidate = row[2]    

        if candidate not in candidatelist:
            candidatelist.update({candidate : 1})
        else:
            candidatelist[candidate] += 1
    
    print(candidatelist)
    # find percentage of votes
    #for candidate in candidatelist:
    #    print(candidate)
        #vote_percent = (candidatelist[1]/[vote_count])
    
    # for candidate in candidatelist:
    #    vote_percent = candidatelist({candidate : 2}) / vote_count
    #    candidatelist.update({candidate : 3})

print("Election Results")
print("---------------------------")
print(f"Total Votes: {vote_count}")
print("---------------------------")
winner_votes = 0
winner_candidate = ""
for candidate in candidatelist:
    print(f"{candidate}: {(candidatelist[candidate]/vote_count)*100:.3f}% ({candidatelist[candidate]})")
    if candidatelist[candidate] > winner_votes:
        winner_votes = candidatelist[candidate]
        winner_candidate = candidate
print("---------------------------")

print(f"Winner: {winner_candidate}")


output_path = os.path.join("PyPoll", "Analysis", "PyPoll_HW_Output.csv")

with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(['-----------------------------'])
    csvwriter.writerow([f"Total Votes: {vote_count}"])
    for candidate in candidatelist:
        csvfile.write(f"{candidate}: {(candidatelist[candidate]/vote_count)*100:.3f}% ({candidatelist[candidate]})\n")
    csvfile.write("---------------------------\n")   
    csvfile.write(f"Winner: {winner_candidate}\n")    