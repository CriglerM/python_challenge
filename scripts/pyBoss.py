# Dependancies
import csv
import os
import glob


# Define variables and dictionary
us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }

all_csv_data = []
new_csv_data = []


# Iterate through the listdir results
print ("Indentifying files ....")
filepaths = glob.glob("raw_data/*.csv")


# Read each csv file and append the contents to the all_csv_data list
print("Merging files ....")
for file in filepaths:
    with open(file, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csvdata = list(csvreader)
        # @NOTE: We use index slicing to skip the header line from each file
        all_csv_data.extend(csvdata[1:])


# Write the merged data to a new file.
csvpath = "merged_records.csv"
with open(csvpath, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Emp ID","Name","DOB","SSN","State"])
    csvwriter.writerows(all_csv_data)


# Define file path
csvPath = os.path.join('merged_records.csv')

# Open file
with open(csvPath, newline = '') as csvFile:
    
# Define reader
    csvReader = csv.reader(csvFile, delimiter = ',')
#Skip the header
    next(csvReader, None)
 
# Transform data and put into new array
    print("Transforming files ...")

    for row in csvReader:
        # Reset transformation variables
        t_empNameParse = []
        t_firstName = ""
        t_lastName = ""
        t_DOBparse = ""
        t_DOB = ""
        t_SSNparse =""
        t_SSN = ""
        t_State = ""
        

        # transform name
        #print("Orig name: " + test)
        t_empNameParse = row[1].split(" ")
        t_firstName = t_empNameParse[0] 
        t_lastName = t_empNameParse[1]
        #print("first: " + t_firstName)
       # print("last: " + t_lastName)

        # transform DOB
        t_DOBparse = row[2].split("-")
        t_DOB = t_DOBparse[1] + "/" + t_DOBparse[2] + "/" + t_DOBparse[0]

        # transform SSN
        t_SSNparse = row[3].split("-")
        t_SSN = "***-**-"+ t_SSNparse[2]

        # transform State
        t_state = us_state_abbrev[row[4]]

        new_csv_data.append([row[0], t_firstName, t_lastName, t_DOB, t_SSN, t_state])



# Write the transformed data to a new file.
print("Writing new file ....")
csvpath = "final_records.csv"
with open(csvpath, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
    csvwriter.writerows(new_csv_data)

print("File processing is complete!")