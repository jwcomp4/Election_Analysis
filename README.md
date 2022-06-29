# Module 3 Challenge: Election Analysis

## Overview of the Election Audit

- This election audit helps to certify the results for a congressional election in Colorado. While Excel is capable of anlyzing tabular data such as this voting data, using Python will allow us to automate the process and use a refactored version of this code to audit and certify other elections. 

- In this challenge, I am developing a Python script that will print the following data to the terminal:
    - Total Votes
    - Amount of votes per county and the percentage of the vote each county represents
    - County with the largest voter turnout
    - How many votes each candidate received and their respective percentage of the vote
    - Name of the winning candidate, the amount of votes they received, and percentage of the vote

- The same data noted above will be printed and saved to a .txt file entitled "election_analysis.txt" in to the "Resources directory.

## Election Audit Results

- Number of votes cast in this congressional election: 369,711

    - After loading in dataset, reading the file, and declaring the variables, this calculation was performed with a simple for-loop:

    ```python
      for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

- County vote data:

    - Denver County had the largest voter turnout.
        - Jefferson County: 38,855 votes (10.5% of total votes)
        - Denver County: 306,055 votes (82.8% of total votes)
        - Jefferson County: 24,801 votes (6.7% of total votes)

    - Producing the County vote data required a for-loop that iterates through the county_votes dictionary with a nested if-statement that evaluates the data to determine what county has the highest voter turnout:

    ```python 

        for cname in county_votes:

        # 6b: Retrieve the county vote count.
        cvotes = county_votes.get(cname)

        # 6c: Calculate the percentage of votes for the county.
        county_percentage = float(cvotes) / float(total_votes) *100

         # 6d: Print the county results to the terminal.
        county_results = (
            f"{cname}: {county_percentage:.1f}% ({cvotes:,})\n")
         
        print(county_results)

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if cvotes > county_turnout:
            county_turnout = cvotes
            largest_county = cname
    
- Candidate vote data:

    - Diana DeGette won the election receiving 272,892 votes (73.8% of the total votes).
        - Charles Casper Stockham received 85,213 votes (23.0% of the total votes).
        - Diana DeGette received 272,892 votes (73.8%% of the total votes).
        - Raymon Anthony Doane received 11,606 votes (3.1% of the total votes).

    - Determining who one the election and the results for each candidate required a for-loop that iterated through candidate_votes dictionary with a nested if-statement to determine the winning candidate:

    ```python

        for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

## Election Audit Summary

- This Python script effectively uses variables to enhance its versatility and applicability for other elections beyond this Congressional race. 
    - Refactoring the variables in the code would make the code more readable for any election.
        - For example, changing the county-related variables to capture state district-related data could make this same script work for a gubernatorial elction. 
        - Likewise, these variables could be changed to reprsente city districts for a mayorial election    
- Refactoring the code in this manner is simple and still produces an accurate election audit efficiently, regardless of the election type. 



