import csv
import os

#The data we need to retrieve:
#1. The total number of votes cast
#2. A complete list of candidates who received votes. 
#3. The percentage of votes each candidate won. 
#4. The total number of votes each candidate won. 
#5. The winnder of the election based on the popular vote.

#Module notes the following steps (algorithm) for considering an election audit:
#1. Open the data file. 
#2. Write down the names of the candidates
#3. Add a vote for each candidate, when applicable. 
#4. Get the total votes for each candidate
#5. Get total votes cast for the election.

#file_to_load = 'Resources/election_results.csv'
#above, telling computer to open the election_results.csv in the Resources folder, which is in the same directory
#as this .py file.

#open the election_results file and read it:
# election_data = open(file_to_load, "r")

#Perform the analysis here

#Close the file

# election_data.close()

# writing code for the indirect path:

# file_to_load = os.path.join("Resources" , "election_results.csv")

# # here is an example of using a with statement to open, read/write a file wiithout using open() and close() everytime. 
# # The structure of this with statement is very similar to a if-else statement and for-loop re: colon and indent

# with open(file_to_load) as election_data :
# #    perform analysis here

#     print(election_data)

#Here, creating a text file into which we can write and save data:

# file_to_save = os.path.join('analysis' , 'election_analysis.txt')
#Using open() with "w" mdode to write data to the file.
#Note that opening the file and assigning it to outfile
#the .write() method is a part of the os module.
#then closing the file.
# outfile = open(file_to_save, "w")

# outfile.write("Hello World")

# outfile.close()

# with open(file_to_save, "w") as txt_file:
    
    # txt_file.write("Hello World, ")
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson, ")

    #You can re-write the above to get the code to appear on different lines using newline escape sequence \n:

    # txt_file.write("Counties in the Election\n----------------\nArapahoe\nDenver\nJeferson")

#Working on reading election data: 
#assign variable to load file from path:

file_to_load = os.path.join("Resources" , "election_results.csv")

#assign a variable to save the file to a path:

file_to_save = os.path.join('analysis' , 'election_analysis.txt')

#creating the accumulator variable in order to count the total votes:

total_votes = 0

#creating a empty list to hold candidate option names:
candidate_options = []

#creating an empty dictionary to hold candidate votes:
candidate_votes = {}

#creating a var. with empty str to hold winning candidate:
winning_candidate = ""

#creating a var. to hold the winning count
winning_count = 0

#creating a variable to hold the percentage of the winning candidate:
winning_percentage = 0
#Open the election results and read the file:

with open(file_to_load) as election_data:
    #To do: Read and analyze the data here:
    #here, you are assigning the read election_data to the var. file_reader:
    file_reader = csv.reader(election_data)
    # for row in file_reader:
    #     print(row)
    #note that when you print here, each row is printed as a list.
    #this for loop allows you to iterate through every row and print the data.

    #the next() method skips the first row and returns the next itme on the list. Stores in headers var.
    headers = next(file_reader)
    
    for row in file_reader:
        #Adding up the votes:
        total_votes += 1
        #grabbing the candidate name:
        candidate_name = row[2]
        #appending that name to the candidate_options list. using a if-else statement with not in
        #first checks if the name is in the candidate_options list initiated above. 
        #if condition returns True, runs code block.
        if candidate_name not in candidate_options:
            #add candidate name to the candidate_options list

            candidate_options.append(candidate_name)

            #begin tracking candidate's vote count. 
            #as it goes through the for-loop it creates the key in the dictionary as the name
            #it also sets the vote count to 0
            candidate_votes[candidate_name] = 0 

        #then you need to capture each votes:
        #put this outside of the if statement so as to capture every row.
        candidate_votes[candidate_name] += 1

with open(file_to_save , "w") as txt_file:
    election_results = (
        f'\nElection Results\n'
        f'----------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'----------------------------\n')
    print(election_results, end="")
    #the end parameter will print a newline (\n) by default. 
    #The end parameter ensures that nothing will be printed on the last line.

        #Save the final vote count  to the text file:
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        #retrieving the vote count for each candidate
        votes = candidate_votes[candidate_name]
        #calculating the percentage of votes 
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (
            f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")

        print(candidate_results)

        txt_file.write(candidate_results)
        #setting up if statement to determine the winning count and percentage.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        #printing candidate name with vote percentage using an f-string
        # print(f"{candidate_name}: received {vote_percentage: .1f}% of the vote.")

         
    

    #writing a summary:
    winning_candidate_summary = (
        f'--------------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'--------------------------------\n')

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)

# print(winning_candidate_summary)

    