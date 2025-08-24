import pandas as pd

# Load the XLSX file
file_path = "/Users/mehlulidlamini/Desktop/DSE580S/dse580-cleaned_sorted_by_type.xlsx"
df = pd.read_excel(file_path)

# 1. Remove duplicates
df = df.drop_duplicates()

# 2. Drop rows with any missing values
df = df.dropna()

# 3. Remove rows containing "fixed_line_or_mobile"
df = df[~df.astype(str).apply(lambda x: x.str.contains("fixed_line_or_mobile").any(), axis=1)]

# 4. Drop columns with 90%+ missing values
threshold = 0.9
df = df.loc[:, df.isnull().mean() < threshold]

# 5. Add 'Lead_Potential' column if 'Rating' and 'Reviews' exist
if {'Rating', 'Reviews'}.issubset(df.columns):
    # Ensure 'Reviews' is numeric and positive
    df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce').abs()
    
    # Initialize Lead_Potential with default 'Low'
    df['Lead_Potential'] = 'Low'
    
    # Assign 'High' where rating >= 4.5 and reviews >= 50
    high_mask = (df['Rating'] >= 4.5) & (df['Reviews'] >= 50)
    df.loc[high_mask, 'Lead_Potential'] = 'High'
    
    # Assign 'Medium' where rating >= 4.0 and reviews < 50
    medium_mask = (df['Rating'] >= 4.0) & (df['Reviews'] < 50)
    df.loc[medium_mask, 'Lead_Potential'] = 'Medium'
else:
    print("Warning: 'Rating' or 'Reviews' columns not found. Skipping 'Lead_Potential' calculation.")

# 6. Sort by 'Type' if the column exists
if 'Type' in df.columns:
    df = df.sort_values(by='Type').reset_index(drop=True)
else:
    print("Warning: 'Type' column not found.")

# 7. Save as XLSX
output_path = "MEHLULIdse580-cleaned_sorted_by_type_updated.xlsx"
df.to_excel(output_path, index=False)
print(f"Iteration Four (sorted by Type): {output_path} saved successfully.")