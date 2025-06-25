import os
import pandas as pd

# Define the parent directory containing the company folders
parent_directory = "."  # Change this to your actual path

# Define the output Excel file
output_excel = "merged_data.xlsx"

# Create an Excel writer
with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
    # Loop through each company folder
    for company_folder in os.listdir(parent_directory):
        folder_path = os.path.join(parent_directory, company_folder)
        
        # Check if it's a directory
        if os.path.isdir(folder_path):
            # Extract the company name (last word from the folder name)
            company_name = company_folder.split()[-1]  
            type = company_folder.split(" ")[0]
            # Loop through each file in the company folder
            for file_name in os.listdir(folder_path):
                if file_name.endswith(".csv"):  # Process only CSV files
                    file_path = os.path.join(folder_path, file_name)
                    
                    # Read the CSV file
                    df = pd.read_csv(file_path)
                    
                    #adding column as company name
                    df["Company"] = company_name
                    # Use the base name (without .csv) as the sheet name
                    sheet_name = type+"_"+file_name.split(".")[0] + "_" + company_name
                    
                    # Save to the same Excel file as a new sheet
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
                    print(f"Added data from {file_name} → Sheet: {sheet_name}")

print(f"All data merged into {output_excel} successfully.")
