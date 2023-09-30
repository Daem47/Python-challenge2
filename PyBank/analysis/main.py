import os
import csv

input_path = os.path.join("resources", "budget_data.csv")
with open(input_path, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    n_months = 0 # Number of months in the Dataset
    PL_total = 0 # Total amount of Profit/Loose

    next(csvreader,None)
    for row in csvreader:
        n_months = n_months + 1 # Number of months in the Dataset
        PL_total = PL_total + int(row[1]) # Total amount of Profit/Loose

        if n_months == 1:
            first = int(row[1])
            last = int(row[1])
            PL_greatest = 0
            PL_lowest = 0
        else:
            PL_dif = int(row[1]) - last
            last = int(row[1])
            if  PL_dif >= PL_greatest: #The greatest increase in profits (date and amount) over the entire period
                PL_greatest = PL_dif
                Date_greatest = row[0]
            if PL_dif <= PL_lowest: #The greatest decrease in losses (date and amount) over the entire period
                PL_lowest = PL_dif
                Date_lowest = row[0]

    PL_changes = round((last - first)/(n_months-1),2) # changes in "Profit/Losses" over the entire period, then find the average of those changes

    print(f'Total Months: {n_months}')
    print(f'Total: {PL_total}')
    print(f'Average Change: ${PL_changes}')
    print(f'Lowest change is: {Date_lowest} ({PL_lowest})')
    print(f'Highest change is: {Date_greatest} ({PL_greatest})')

output_path = os.path.join("resources", "analisis_results.csv")
with open(output_path, 'w', newline="") as csvfile2:
    csvwriter = csv.writer(csvfile2, delimiter=",")
    csvwriter.writerow(['Total Months:', n_months])
    csvwriter.writerow(['Total:', f'${PL_total}'])
    csvwriter.writerow(['Average Change:', f'${PL_changes}'])
    csvwriter.writerow(['Lowest change is:', f'{Date_lowest} (${PL_lowest})'])
    csvwriter.writerow(['Highest change is:', f'{Date_greatest} (${PL_greatest})'])




