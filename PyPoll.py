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

file_to_load = 'Resources/election_results.csv'
#above, telling computer to open the election_results.csv in the Resources folder, which is in the same directory
#as this .py file.

#open the election_results file and read it:
election_data = open(file_to_load, "r")

#Perform the analysis here

#Close the file

election_data.close()