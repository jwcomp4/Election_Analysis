print("Hello World")
counties = ["Arapahoe" , "Denver" , "Jefferson"]

#if counties[1] == "Denver" :
    #print(counties[1])

#using membership operator in:
if "El Paso" in counties:
    print("El Paso is in the list of counties.")

else:
    print("El Paso is not in the list of counties.")

#combining membership and logical operators:
if "Arapahoe" and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else: 
    print("Arapahoe or El Paso is not in the list of counties.")

 #Setting up if-else decision statement:
temperature = int(input("What is the temperature outside? "))
#using input() to get data from user and passing it through int() because input() returns str
#assigns value from user to temperature variable

if temperature > 80 :
    print("Turn on the AC")
    #this condition evaluates user input data, if true, runs print statement
    #if false, skils the print statement and goes to else.
else :
    print("Open the windows.")  
    #if the above condition is false, runs this print statement. 

#getting your grade, setting up if-elif-if statements:

score = int(input("What is your grade? "))

if score >= 90 :
    print("Your grade is an A.")
#using the elif syntax allows you to have multiple conditions.
#if above returns false, go to the next else, if (elif)
elif score >= 80 :
    print("Your grade is a B.")

elif score >= 70 :
    print("Your grade is a C.")

elif score >= 60 :
    print("Your grade is a D.")
#the code after the else only runs if all of the other elifs return False
else: 
    print("Your grade is an F.")
#This if-elif-else construction is much easier to read/write than multiple nested if-else statements.

#example of a while loop

x = 0
while x <= 5:
#while initiates the loop and sets the condition
#as long as the condition is True, this code runs:
    print(x)
    x = x + 1
#stops when it's no longer true. If you forget to put the code that can make the condition false:
#the code will run indefinitely, an infinite loop

#example of a for-loop iterating through counties list above.
#for county in counties:
    #print(county)

counties_dict =  {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}

#Getting the keys for counties_dict

#for county in counties_dict:
    #print(county)

#you can do the same as above by adding the keys() to counties_dict

for county in counties_dict.keys():
    print(county)

#you can retrieve the values using the values() method:
#note the more appropriate iterator variable

for voters in counties_dict.values():
    print(voters)

#you can also use the format dictionary_name[key] to get the value:
#here, note where you are using the iterator variable in the print statement.
#this will only print the values.

for county in counties:
    print(counties_dict[county])

#it is also possible to use the get() method to retrieve the values in the dict

for county in counties:
    print(counties_dict.get(county))

#to get the key-value pairs, you can use the item() method
#the first variable declared in the for loop is the key
#the second variable declared in teh for loop is the value

for county, voters in counties_dict.items():
    print(county, voters)

#doing the same as above with better print statement

for county, voters in counties_dict.items():
    print(county + " has " + str(voters) + " registered voters.")

#now working on using a for-loop to iterate through a list of dictionaries.

#creating list of dictionaries: 
voting_data = [{"county" : "Arapahoe", "registered_voters": 4228229}, {"county": "Denver", "registered_voters": 463353},
{"county": "Jefferson", "registered_voters": 432438}]

#to print each dictionary on a separate line:

for county_dict in voting_data:
    print(county_dict)

#because this is a list, you can use the range() function to print just the counties:
#assume that here, you tell the program to print the "county" key at the i index.
voting_data = [{"county" : "Arapahoe", "registered_voters": 4228229}, {"county": "Denver", "registered_voters": 463353},
{"county": "Jefferson", "registered_voters": 432438}]
for i in range(len(voting_data)):
    print(voting_data[i]["county"])

#getting values from list of dictionaries
#requires a nested for-loop
#need to think through this one a bit..
voting_data = [{"county" : "Arapahoe", "registered_voters": 4228229}, {"county": "Denver", "registered_voters": 463353},
{"county": "Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)



#Playing with f-strings

my_votes = int(input("How many votes did you get in the election? "))

total_votes = int(input("What is the total number of votes in the election? "))

print(f"I received {my_votes / total_votes * 100}% of the total")
    #here  the f-string calculates the value in the {} and formats to a str

#F-Strings with Dictionaries
#Here using f-strings to get print statement from previous code, cf line 108-109
#This makes it a lot easier to read. 
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#Multi-Line F-Strings

#this looks really interesting - basically creating a variable to hold the multi-line string
#curious if this is considered a tuple?

candidate_votes = int(input("How many votes did the candidate get in the election? "))

total_votes = int(input("What is the total number of votes in the election? "))

message_to_candidate = (
    f"You received {candidate_votes: ,} number of votes. "
    f"The total number of votes in the election was {total_votes: ,}. "
    f"You received {candidate_votes / total_votes * 100: .2f}% of the total votes. ")

print(message_to_candidate)

#a few things to note here about formating floating point. 
#general format is f"{value: {width} . {precision}}
#width specifies the number of char used, but if more is needed, they will appear
#precision is the number of decimal places. 
#note that in line 162 and 163 there is a : after candidate_votes followed by space and then ,
#this means that you can use thousands comma delimiter
#in 164 you see the . after the : followed by .2f noting the precision of 2 "floating point decimal places" f is impt

#skill drill of printing everything in counties_dict using f-strings
#this is iterating through a dictionary

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#skill drill of printing everything in voting_data using f-strings
#this is retrieving data in a list of dictionaries
voting_data = [{"county" : "Arapahoe", "registered_voters": 4228229}, {"county": "Denver", "registered_voters": 463353},
{"county": "Jefferson", "registered_voters": 432438}]

for county_data in voting_data:
    for county, voters in county_data:
        print(f"{county} county has {voters: ,} registered voters")

