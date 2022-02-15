# Place code below to do the munging part of this assignment.

# Open the data file in read mode
file = open('data.txt', 'r')

# Create a list of all lines of the data file
allLines = file.readlines()

# Create a file to save the structured data into
returnFile = open('clean_data.csv', 'w')

# Create a boolean variable to determine whether we have passed the first header of "Year"
lineFirstInst = True

# Create a boolean variable to determine whether the program should write to the csv file
canWrite = False

# Loop through the data file
for rows in allLines:

    # Create a boolean variable to determine if the character is a space
    isPrevSpace = False

    # The condition for when we encounter a row with no data
    if(rows == "\n"):
        continue

    # The condition for when we encounter the year header
    if("Year" in rows):

        # If it is not the first instance of header, we go to the next row
        if(lineFirstInst == False):
            continue
        canWrite = True

    # Loop through the columns
    for columns in rows:

        # The condition if current character is in the alphabet
        if (columns.isalpha() and lineFirstInst == False):
            canWrite = False
            break

        # The condition if we are not supposed to write into the csv file
        if(canWrite == False):
            continue

        # The condition when we encounter a space
        if(columns.isspace() and columns != rows[len(rows)-1]):
            if(isPrevSpace == False):
                returnFile.write(",")
                isPrevSpace = True
            continue

        # The condition when we encounter a character in the relevant data
        if(columns.isdigit() or columns == "*" or columns == "-" or columns == "\n" or ("Year" in rows)):

            # The condition when the character is a line break
            if(rows == "\n"):
                continue

            # The condition when the character is part of the data
            if(all(chr.isdigit() or chr.isspace() or chr == "*" or chr == "-" for chr in rows)):
                returnFile.write(columns)
                isPrevSpace = False

            # The condition when we encounter the first header
            if("Year" in rows and lineFirstInst == True):
                returnFile.write(columns)
                isPrevSpace = False

    # Check to see if we pass the first header and ensure that we do not write any more headers
    if("Year" in rows and lineFirstInst == True):
        lineFirstInst = False

# Close the new csv file containing the clean data in celcius
returnFile.close()

# Open the csv file we created in read mode
structuredFile = open('clean_data.csv', 'r')

# Read the lines in the new csv file
allLinesStruc = structuredFile.readlines()

# Create an empty list to contain all modified rows in the dataset
returnAllList = []

# Create an empty list to store the current data in the csv file
splitList = []

# Loop through the rows in the csv file and store the data in splitList
for newRows in allLinesStruc:
    splitList.append(newRows.split(','))

# Loop through the list containing the data
for splitRows in splitList:

    # Create an empty list to store the current row
    returnList = []

    # Loop through the characters in a corresponding row within the list containing the data
    i = 0
    while i < len(splitRows):

        # If we encounter the header
        if ("Year" in splitRows):
            returnList.append(splitRows[i])
            i = i+1
            continue

        # If we encounter missing the data
        if(splitRows[i] == "***" or splitRows[i] == "****"):
            returnList.append(splitRows[i])
            i = i+1
            continue

        # If we encounter the first or last column in the row
        if(i == 0 or i == len(splitRows) - 1):
            returnList.append(splitRows[i])
            i = i+1
            continue

        # Convert the temperature data from 0.01 Celcius to Fahrenheit
        currCelcius = float(splitRows[i])
        fahrenConv = format(((currCelcius / 100) * 1.8), '.1f')
        returnList.append(fahrenConv)
        i = i+1

    # Append the current row into the list containing all the rows
    returnAllList.append(returnList)

# Close the csv file
structuredFile.close()

# Open the csv file in write mode
testFile = open('clean_data.csv', 'w')

# Write the new temperature data in Fahrenheit from the list into the csv file
for lastRows in returnAllList:
    colCount = 0
    while colCount < len(lastRows):
        if(lastRows[colCount].__contains__("\n")):
            testFile.write(lastRows[colCount])
            colCount = colCount + 1
            continue
        testFile.write(lastRows[colCount]+ ",")
        colCount = colCount + 1

# Close the modified csv file
testFile.close()






















