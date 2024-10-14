import csv
import os

# Ask the user for the input file path
input_file = input("Please enter the input file path (e.g., /path/to/checks.csv[/home/optit/Documents/Big_Data_analysis_and_sortings/csv_python_sort/checks.csv]# Replace with your file ): ").strip()

# Check if the file exists
if not os.path.isfile(input_file):
    print("File not found. Please check the path and try again.")
else:
    # Ask the user if they want to convert the file to CSV
    convert_to_csv = input("Do you want your file to get converted to CSV? (yes/no): ").strip().lower()

    if convert_to_csv == 'yes':
        # Ask for the output filename (full path)
        output_file = input("Please enter the output filename (with .csv extension): ").strip()
    else:
        print("Skipping CSV conversion.")
        output_file = input("Please enter the output filename (with .csv extension): ").strip()

    # Open the input file and process it line by line
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)

        for line in infile:
            # Split the line by tabs
            row = line.strip().split('\t')  # Split by tab character
            csv_writer.writerow(row)

    print("Conversion to CSV completed.")
