import pandas as pd

# Load the Excel file
file_path = "merged_data.xlsx"  # Replace with your actual file name
xls = pd.ExcelFile(file_path)

# Define categories and types
categories = ["Content", "Geography", "Traffic"]
types = ["Chart", "Table", "Totals"]

# Dictionary to store data categorized properly
data_dict = {category: {data_type: [] for data_type in types} for category in categories}

# Loop through each sheet and classify it
for sheet in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet)
    
    # Determine category
    matched_category = next((cat for cat in categories if cat in sheet), None)
    matched_type = next((typ for typ in types if typ in sheet), None)
    
    # If both category and type are found, store the data
    if matched_category and matched_type:
        data_dict[matched_category][matched_type].append(df)

# Create a new Excel file with categorized sheets
output_file = "categorized_data.xlsx"
with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
    for category, type_dict in data_dict.items():
        for data_type, dfs in type_dict.items():
            if dfs:  # Ensure there is data
                merged_df = pd.concat(dfs, ignore_index=True)
                sheet_name = f"{category}_{data_type}"  # Example: Content_Chart, Geography_Table
                merged_df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Categorized data saved to {output_file}")
