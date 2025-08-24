import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load Excel file
# -----------------------------
file_path = "/Users/mehlulidlamini/Desktop/DSE580S/dse580-cleaned_sorted_by_type.xlsx"
df = pd.read_excel(file_path)

# -----------------------------
# 2. Data Cleaning
# -----------------------------
# Remove duplicates
df = df.drop_duplicates()

# Drop rows with any missing values
df = df.dropna()

# Remove rows containing "fixed_line_or_mobile"
df = df[~df.astype(str).apply(lambda x: x.str.contains("fixed_line_or_mobile").any(), axis=1)]

# Drop columns with 90%+ missing values
threshold = 0.9
df = df.loc[:, df.isnull().mean() < threshold]

# -----------------------------
# 3. Add 'Lead_Potential' column if applicable
# -----------------------------
if {'Rating', 'Reviews'}.issubset(df.columns):
    df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce').abs()
    df['Lead_Potential'] = 'Low'
    
    high_mask = (df['Rating'] >= 4.5) & (df['Reviews'] >= 50)
    df.loc[high_mask, 'Lead_Potential'] = 'High'
    
    medium_mask = (df['Rating'] >= 4.0) & (df['Reviews'] < 50)
    df.loc[medium_mask, 'Lead_Potential'] = 'Medium'
else:
    print("Warning: 'Rating' or 'Reviews' columns not found. Skipping 'Lead_Potential' calculation.")

# -----------------------------
# 4. Sort by 'Type' if exists
# -----------------------------
if 'Type' in df.columns:
    df = df.sort_values(by='Type').reset_index(drop=True)
else:
    print("Warning: 'Type' column not found.")

# -----------------------------
# 5. Save cleaned Excel
# -----------------------------
output_path = "MEHLULIdse580-cleaned_sorted_by_type_updated.xlsx"
df.to_excel(output_path, index=False)
print(f"Iteration Four (sorted by Type): {output_path} saved successfully.")

# -----------------------------
# 6. Generate line charts for all numeric columns
# -----------------------------
numeric_cols = df.select_dtypes(include='number').columns.tolist()

if numeric_cols:
    for col in numeric_cols:
        plt.figure(figsize=(10,6))
        plt.plot(df.index, df[col], marker='o', linestyle='-', label=col)
        plt.title(f"{col} Trend")
        plt.xlabel("Index")
        plt.ylabel(col)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()
        
        # Optional: save chart
        plt.savefig(f"{col}_line_chart.png")
else:
    print("No numeric columns found to plot.")

    # -----------------------------
# 7. Pie chart: Lead_Potential by Type
# -----------------------------
if 'Type' in df.columns and 'Lead_Potential' in df.columns:
    # Group by Type and Lead_Potential
    pie_data = df.groupby(['Type', 'Lead_Potential']).size().unstack(fill_value=0)
    
    for type_name, row in pie_data.iterrows():
        plt.figure(figsize=(6,6))
        plt.pie(row, labels=row.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff','#99ff99','#ff9999'])
        plt.title(f"Lead Potential Distribution for Type: {type_name}")
        plt.tight_layout()
        plt.show()
        
        # Optional: save pie chart
        plt.savefig(f"pie_lead_potential_{type_name}.png")
else:
    print("Warning: 'Type' or 'Lead_Potential' column not found. Cannot generate pie chart.")