import pandas as pd

# Load CSV
file_path = "/Users/mehlulidlamini/Desktop/DSE580S/Indiana_Leads_Cleaned_appended_clearoutphone_results.csv"  
df = pd.read_csv(file_path)

# 1. Remove duplicates
df = df.drop_duplicates()

# 2. Handle missing values (drop rows with any NaN values)
df = df.dropna(how='all')  # Drop rows where all values are NaN
df = df.dropna(axis=0)      # Drop rows with any NaN values

# 3. Remove rows containing the string "fixed_line_or_mobile"
df = df[~df.apply(lambda row: row.astype(str).str.contains("fixed_line_or_mobile").any(), axis=1)]

# 4. Drop unnecessary columns (those with 90%+ missing values)
threshold = 0.9
df = df.loc[:, df.isnull().mean() < threshold]

# 5. Sort by 'Type' while keeping all other columns intact
if 'Type' in df.columns:
    df = df.sort_values(by='Type').reset_index(drop=True)
else:
    print("Warning: 'Type' column not found.")

# 6. Save as Excel
output_path = "dse580-cleaned_sorted_by_type.xlsx"
df.to_excel(output_path, index=False)

print(f"Iteration Three (sorted by Type): {output_path}")