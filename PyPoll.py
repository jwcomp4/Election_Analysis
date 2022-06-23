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

#election_data.close()

#writing code for the indirect path:

# file_to_load = os.path.join("Resources" , "election_results.csv")

#here is an example of using a with statement to open, read/write a file wiithout using open() and close() everytime. 
#The structure of this with statement is very similar to a if-else statement and for-loop re: colon and indent

# with open(file_to_load) as election_data :
    #perform analysis here

    # print(election_data)

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

#Open the election results and read the file:

with open(file_to_load) as election_data:
    #To do: Read and analyze the data here:
    #here, you are assigning the read election_data to the var. file_reader:
    file_reader = csv.reader(election_data)
    # for row in file_reader:
    #     print(row)
    #note that when you print here, each row is printed as a list.
    #this for loop allows you to iterate through every row and print the data.

    #the next() method skips the first row and returns the next itme on the list.
    headers = next(file_reader)
    #this will print the headers.
    print(headers)
