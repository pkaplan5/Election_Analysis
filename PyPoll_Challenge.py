

import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0


# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}



# 2: Track the largest county and county voter turnout.
winning_county = ""
county_count = 0
county_winning_percentage = 0 


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # 3: Extract the county name from each row.
        county_name = row[1]
      # If the candidate does not match any existing candidate add it to


        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)
            
            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
        
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

        #Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results)
    txt_file.write(election_results)
   


    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        votes = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        county_vote_percentage = float(votes) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        
        county_results = (
            f"{county_name} {county_vote_percentage:.1f}% ({votes:,})\n"
            )
        print(county_results)
        txt_file.write(county_results)
      

         # 6e: Save the county votes to a text file.
        
        
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > county_count) and (county_vote_percentage > county_winning_percentage):

            # 7: Print the county with the largest turnout to the terminal.
            county_count = votes
            winning_county = county_name
            county_winning_percentage = county_vote_percentage
        # 8: Save the county with the largest turnout to a text file.
        winning_county_summary = (
        f"                            \n"
        f"----------------------------\n"
        f"Largest County Turn-Out: {winning_county}\n"
        f"----------------------------\n"
        f"                            \n")
        
    print(winning_county_summary)
    txt_file.write(winning_county_summary)
    # Save the winning candidate's name to the text file
    


 #####candiate portion


#declare variables, lists, and dict. from former file
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

with open(file_to_save, "a") as txt_file:

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
        txt_file.write(candidate_results)
        #  Save the candidate results to our text file.
 
        
          

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name



    winning_candidate_summary = (
        f"                         \n"
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    txt_file.write(winning_candidate_summary)
    print(winning_candidate_summary)
    
    
  
   

   

    
    
    
