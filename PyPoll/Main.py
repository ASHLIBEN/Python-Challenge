#importing os and csv file to read csv files
import csv
import os

#Set path for csv file to a variable
csvpath = os.path.join("/Users/ashliben/Desktop/Python-Challenge/Python-Challenge/PyPoll/Resources","election_data.csv")


#Variable declaration and initialization
total_votes = 0
candidate_options = []
candidate_votes = {}
county_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(csvpath) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    print("\nElection Results")
    print("............................................\n")
    
    print("Total Votes:"+str(total_votes)+"\n")

    
    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve candidate name, vote percentage and vote count
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage 
        print(candidate_results)
      
     
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"---------------------------------------------\n"
        f"Winner: {winning_candidate}\n"
    
        f"--------------------------------------------\n")
    print(winning_candidate_summary)

 
