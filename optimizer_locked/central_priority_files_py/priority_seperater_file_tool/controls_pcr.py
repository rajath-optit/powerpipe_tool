import os
import pandas as pd
from tabulate import tabulate

def generate_unique_filename(filename, extension):
    """
    Generates a unique filename by appending _1, _2, etc. if the file already exists.
    """
    base, ext = os.path.splitext(filename)
    if ext != extension:
        filename += extension
    
    counter = 1
    unique_filename = filename
    while os.path.exists(unique_filename):
        unique_filename = f"{base}_{counter}{extension}"
        counter += 1
    
    return unique_filename

def filter_checks_by_priority(file_path, priority):
    # Attempt to read the CSV file with different encodings
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='ISO-8859-1')  # Try ISO-8859-1 if UTF-8 fails

    # Clean up whitespace in the relevant columns
    df['title'] = df['title'].str.strip()
    df['control_title'] = df['control_title'].str.strip()  # Adjust column name based on actual CSV
    df['priority'] = df['priority'].str.strip()

    # Filter the DataFrame based on the selected priority
    filtered_df = df[df['priority'] == f'p{priority}']

    # Print the output with the desired columns including 'Recommendation Steps/Approach' and 'COST'
    table_output = tabulate(
        filtered_df[['title', 'control_title', 'priority', 'Recommendation Steps/Approach', 'COST']], 
        headers='keys', 
        tablefmt='pretty', 
        showindex=False
    )
    print(table_output)

    # Ask if the user wants to save the output to a file
    save_file = input("Do you want to save the filtered table results to a new file? (yes/no): ").strip().lower()

    if save_file == 'yes':
        # Get the file name for CSV, ensure extension is added and uniqueness
        csv_filename = input("Enter the name of the CSV file (e.g., 'filtered_output.csv'): ").strip()
        csv_filename = generate_unique_filename(csv_filename, '.csv')
        # Save CSV file
        filtered_df.to_csv(csv_filename, index=False)
        print(f"Filtered results have been saved to {csv_filename}")

        # Ask if the user wants to save a clear formatted table file
        save_table = input("Do you want to save a clear formatted table file as well? (yes/no): ").strip().lower()
        if save_table == 'yes':
            # Get the file name for the table format, ensure uniqueness
            table_filename = input("Enter the name of the table file (e.g., 'filtered_output.txt'): ").strip()
            table_filename = generate_unique_filename(table_filename, '.txt')
            # Save the table format to a file
            with open(table_filename, 'w') as f:
                f.write(table_output)
            print(f"Formatted table has been saved to {table_filename}")
    else:
        print("No files were saved.")

if __name__ == "__main__":
    # Get the file name from the user
    file_path = input("Enter the name of the CSV file (e.g., 'centralfile.csv' or 'input_file_priority.csv'): ").strip()

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
    else:
        # Get user input for priority level
        priority = input("Enter the priority level you want to filter by (1, 2, or 3): ")

        # Call the filtering function
        filter_checks_by_priority(file_path, priority)
    