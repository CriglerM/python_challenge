# Dependancies
import os
import csv

budgetFileInput = input("What is the name of your file? (include extension) : ")

# Define file path
csvPath = os.path.join('raw_data', budgetFileInput)
#csvPath = os.path.join('raw_data', 'budget_data_2.csv')

# Open file
with open(csvPath, newline = '') as csvFile:

# Define reader
    csvReader = csv.reader(csvFile, delimiter = ',')
#Skip the header
    next(csvReader, None)

# Define variables
    totalMonths = 0
    totalRevenue = 0
    priorRevenue = 0
    monthChange = 0
    revenueChange = 0
    avgRevenue = 0
    highChange = 0
    highDate = ''
    lowChange = 0
    lowDate = ''

# Start looping through the data
    for budgetData in csvReader:

        # Set up variable on first loop
        if totalMonths == 0:
            priorRevenue = int(budgetData[1])
            highChange = int(budgetData[1])
            highDate = budgetData[0]
            lowChange = int(budgetData[1])
            lowDate = budgetData[0]

        

        # Calc month change then test for highs and lows
        monthChange = int(budgetData[1]) - priorRevenue

        if monthChange > highChange:
            highChange = monthChange
            highDate = budgetData[0]

        if monthChange < lowChange:
            lowChange = monthChange
            lowDate = budgetData[0]
        
        # aggregate revenue and revnue changes
        totalRevenue = totalRevenue + int(budgetData[1])
        revenueChange = revenueChange + monthChange
        
        # reset priorRevenue and increment month counter
        priorRevenue = int(budgetData[1])
        totalMonths += 1    


    # Calculate average revenue
    avgRevenue = int(revenueChange/totalMonths)

    # Print to terminal
    print("  ")
    print("----------------------------------------------------")
    print("               Financial Analysis                   ")
    print("----------------------------------------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total Revenue: ${totalRevenue} ")
    print(f"Average Revenue Change:  ${avgRevenue}")
    print(f"Greatest Increase in Revenue:  {highDate} - ${highChange}")
    print(f"Greatest Decrease in Revenue: {lowDate} -  ${lowChange}")


    # Setup Output file name
    parseFileName = budgetFileInput.split(".")
    budgetFileOutput = parseFileName[0] + ".txt"
    #print(budgetFileOutput)


    # Write to file
    file = open(budgetFileOutput,"w") 
    file.write("\n  ")
    file.write("\n----------------------------------------------------")
    file.write("\n               Financial Analysis                   ")
    file.write("\n----------------------------------------------------")
    file.write(f"\nTotal Months: {totalMonths}")
    file.write(f"\nTotal Revenue: ${totalRevenue} ")
    file.write(f"\nAverage Revenue Change:  ${avgRevenue}")
    file.write(f"\nGreatest Increase in Revenue:  {highDate} - ${highChange}")
    file.write(f"\nGreatest Decrease in Revenue: {lowDate} -  ${lowChange}")
    
    file.close() 



