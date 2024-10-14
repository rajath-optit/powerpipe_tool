import pandas as pd
import os
import shutil  # Import the shutil module

def load_priority_data(priority_file):
    """Load priority data from a given CSV file."""
    if os.path.exists(priority_file):
        return pd.read_csv(priority_file)
    else:
        print(f"Error: The file {priority_file} does not exist.")
        return None

def create_priority_files(report_df, reports_folder):
    """Create separate files for each priority level and move them to the reports folder."""
    for priority in [1, 2, 3]:
        priority_df = report_df[report_df['priority'] == priority]
        if not priority_df.empty:
            # Create a new file name based on priority
            new_file_name = f"{report_file.split('.')[0]}_priority_{priority}.csv"
            priority_df.to_csv(new_file_name, index=False)
            print(f"Created file: {new_file_name}")
            # Move the created file to the reports folder
            shutil.move(new_file_name, os.path.join(reports_folder, new_file_name))
            print(f"Moved file to: {os.path.join(reports_folder, new_file_name)}")

def move_report_to_folder(report_file, reports_folder):
    """Move the generated report to the reports folder."""
    shutil.move(report_file, os.path.join(reports_folder, report_file))
    print(f"Moved report to: {os.path.join(reports_folder, report_file)}")

def main(report_file):
    # Define the reports folder
    reports_folder = 'reports'
    os.makedirs(reports_folder, exist_ok=True)  # Create the reports folder if it doesn't exist

    # Load priority data
    priority1_file = 'optimizer_locked/ex1/1_priority_expe.csv'
    priority2_file = 'optimizer_locked/ex1/2_priority_expe.csv'  # Corrected name
    priority3_file = 'optimizer_locked/ex1/3_priority_expe.csv'

    priority1_data = load_priority_data(priority1_file)
    priority2_data = load_priority_data(priority2_file)
    priority3_data = load_priority_data(priority3_file)

    # Check if any priority data is None
    if priority1_data is None or priority2_data is None or priority3_data is None:
        print("One or more priority data files could not be loaded. Exiting.")
        return

    # Load report data
    report_df = pd.read_csv(report_file)

    # Initialize new columns for priorities, recommendations, and cost
    report_df['priority'] = None
    report_df['Recommendation Steps/Approach'] = None
    report_df['COST'] = None

    # Assign priorities, recommendations, and costs based on control titles
    for priority_data, priority in zip([priority1_data, priority2_data, priority3_data], [1, 2, 3]):
        for index, row in priority_data.iterrows():
            control_title = row['control_title']
            recommendation = row['Recommendation Steps/Approach']
            cost = row['COST']
            
            # Check if control_title exists in the report DataFrame
            if control_title in report_df['control_title'].values:
                report_df.loc[report_df['control_title'] == control_title, 
                              ['priority', 'Recommendation Steps/Approach', 'COST']] = [priority, recommendation, cost]

    # Save the updated report
    updated_report_file = f"{report_file.split('.')[0]}_with_priorities.csv"
    report_df.to_csv(updated_report_file, index=False)
    print(f"Report saved as {updated_report_file}")

    # Move the report file to the reports folder
    move_report_to_folder(updated_report_file, reports_folder)

    # Prompt for additional file creation
    create_files = input("Do you want to create separate files for priorities 1, 2, and 3? (yes/no): ").strip().lower()
    if create_files == 'yes':
        create_priority_files(report_df, reports_folder)

if __name__ == "__main__":
    report_file = input("Enter the report file name: ").strip()
    main(report_file)
