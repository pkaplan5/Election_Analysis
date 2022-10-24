
import csv
from importlib.resources import path
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis","election_analysis.txt")

#declare variables, lists, and dict.
total_votes = 0 
candidate_options = []
candidate_votes = {}


#winning variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0


with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    
  #loop to get candidate results
    for row in file_reader:
        total_votes += 1

        candidate_name = row[2]

#enter name of candidate in dict.
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

#add votes of candidate
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:

    election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)


    print(candidate_votes)

    #vote counter to get results
    for candidate_name in candidate_votes:

        #individual candidate vote talley.
        votes = candidate_votes[candidate_name]

        # individual vote %
        vote_percentage = float(votes)/ float(total_votes) * 100

        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
          

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
        
    txt_file.write(winning_candidate_summary)




  
  
