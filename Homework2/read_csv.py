import csv

# open CSV file and read data
# Automatically closes the csvfile 
with open("presidents.csv", "r", newline='', encoding="utf-8") as csvfile:
    c = csv.reader(csvfile)

    # change the object to a list, I couldn't figure out how to fix the for loop so I made this change
    pres = list(c)
    

# Define column widths
col1_width = 20
col2_width = 35
col3_width = 30

# Create the border
border = f"+{'-' * col1_width}+{'-' * col2_width}+{'-' * col3_width}+"

# Establish the headers and print them
heading1 = "President"
heading2 = "Party"
heading3 = "College"
header_row = f"|{heading1:^{col1_width}}|{heading2:^{col2_width}}|{heading3:^{col3_width}}|"

# Print headers and borders
print(border)
print(header_row)
print(border)

# Skip the first row 
# iterate and print the data
for row in pres[1:]:  
    print(f"|{row[1]:^{col1_width}}|{row[5]:^{col2_width}}|{row[8]:^{col3_width}}|")

print(border)
