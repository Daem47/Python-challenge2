import os
import csv

input_path = os.path.join("resources", "election_data.csv")
with open(input_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    list = ["NAMES"]
    list2 = ["VOTES"]
    list3 = ["PERCENTAGE"]
    number_votes = 1
    new_candidate = True

    next(csvreader, None)
    for row in csvreader:
            
            #The total number of votes cast
            number_votes = number_votes + 1 
            candidate = row[2]
            lenght = len(list) 

            for x in range(0,lenght):
                new_candidate = True  

                #Validates if candidate is new or not on our Database
                if candidate == list[x]: 
                    new_candidate = False

                    #If is already registered sum a vote
                    list2[x] = list2[x] + 1 
                    break
            
            #If candidate is new, we will register on our Databse
            if new_candidate == True: 
                list.append(candidate) 
                list2.append(int("1"))     
                       
    print("Election Results")
    print("------------------------")
    print(f'Total Votes: {number_votes - 1}')
    print("------------------------")
    
    last = 0
    for x in range(1,lenght):
         
         #Make a new list for the percentages of each candidate
         list3.append(f'{round((list2[x])*100/number_votes,2)}%') 
         print(f'{list[x]}: {list3[x]}% ({list2[x]})')

         #Search for the candidate with most votes on the vote list
         if last <= list2[x]:
              last = list2[x]
              winner = list[x] 
    final = zip(list, list3, list2)

    print("------------------------")
    print(f'Winner: {winner}')
    print("------------------------")

#Exports data to CSV file
output_path = os.path.join("resources", "analysis_results.csv") 
with open(output_path, 'w', newline = "") as csvfile2:
    csvwriter = csv.writer(csvfile2, delimiter = ',')
    csvwriter.writerows(final)
    