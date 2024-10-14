import pandas as pd
import os

def create_final_optimized_report(report_file, final_report_file):
    # Load the report data
    report_df = pd.read_csv(report_file)
    
    # Standard columns that should always be included
    standard_columns = ['title', 'control_title', 'description', 'control_description', 'priority', 
                        'Recommendation Steps/Approach', 'COST', 'reason', 'resource', 'status', 
                        'account_id', 'region']
    
    # Additional columns to check for
    additional_columns = ['acsc_essential_eight', 'cis_controls_v8_ig1', 'gxp_21_cfr_part_11', 'nist_800_53_rev_5', 
                          'nist_csf', 'cisa_cyber_essentials', 'fedramp_low_rev_4', 'fedramp_moderate_rev_4', 
                          'ffiec', 'gdpr', 'hipaa_final_omnibus_security_rule_2013', 
                          'hipaa_security_rule_2003', 'nist_800_171_rev_2', 'nist_800_53_rev_4', 'pci_dss_v321', 
                          'rbi_cyber_security', 'soc_2', 'rbi_itf_nbfc', 'gxp_eu_annex_11', 
                          'acsc_essential_eight_ml_3', 'audit_manager_control_tower', 'aws_foundational_security']

    # Find additional columns that are present in the report file
    present_additional_columns = [col for col in additional_columns if col in report_df.columns]

    # Combine the standard columns with the additional ones that are present
    final_columns = standard_columns + present_additional_columns
    
    # Create the final DataFrame with only the necessary columns
    final_report_df = report_df[final_columns]
    
    # Save the final optimized report
    final_report_df.to_csv(final_report_file, index=False)
    print(f"Final optimized report saved as {final_report_file}")

def main():
    # Ask the user to input the report file name
    report_file = input("Enter the report file name (e.g., aws_compliance_benchmark_all_controls_benchmark_vested_with_priorities.csv): ").strip()
    
    # Set the output path to the reports directory
    reports_directory = os.path.dirname(os.path.abspath(__file__))  # Get the current script's directory
    final_report_file = os.path.join(reports_directory, 'aws_compliance_benchmark_all_controls_benchmark_final_optimized_report.csv')

    # Ask if the user wants to create the final report
    create_report = input("Do you want to create the final optimized report? (yes/no): ").strip().lower()
    if create_report == 'yes':
        create_final_optimized_report(report_file, final_report_file)
    else:
        print("Final report creation skipped.")

if __name__ == "__main__":
    main()
