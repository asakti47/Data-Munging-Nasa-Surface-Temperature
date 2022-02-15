
# Place code below to do the analysis part of the assignment.

# Import csv module
import csv

# Create an empty list to store the average for every ten years
annEveryTen = []

# Open the csv file
with open('clean_data.csv', 'r',) as file:

    # Read the csv file
    reader = csv.reader(file, delimiter = ',')

    # Create an empty list to store the average annual temperature for current set of years
    currNums = []

    # Create a counter variable to help loop through the csv file
    counter = 0

    # Loop through the rows in the csv file
    for row in reader:

        # The condition for when it passes the header
        if("Year" in row):
            continue

        # Append the current year's data to currNums list
        currNums.append(float(row[13]))
        counter = counter + 1

        # The condition for when it is the tenth year within the current set of years
        if(counter > 9):
            currAnnMean = (sum(currNums)) / 10
            firstYear = int(row[0]) - 9
            currYear = row[0]
            annEveryTen.append(str(firstYear) + " to " + str(currYear) + ": " + str(currAnnMean))
            counter = 0
            currNums = []

# Print the average for every ten years
print(annEveryTen)




