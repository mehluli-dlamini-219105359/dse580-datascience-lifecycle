import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned Excel file
file_path = "MEHLULIdse580-cleaned_sorted_by_type_updated.xlsx"
df = pd.read_excel(file_path)

# Clean column names
df.columns = df.columns.str.strip()

# Filter for Lead_Potential = Low or Medium
filtered_df = df[df['Lead_Potential'].isin(['Low', 'Medium'])]

# Create pivot table: Type vs ClearoutPhone Location
heatmap_data = filtered_df.pivot_table(
    index='Type',
    columns='ClearoutPhone Location',
    values='Company Name',
    aggfunc='count',
    fill_value=0
)

# Plot heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='Blues', linewidths=.5)
plt.title("Heatmap of Business Types vs Locations (Low & Medium Leads)", fontsize=14)
plt.xlabel("ClearoutPhone Location", fontsize=12)
plt.ylabel("Business Type", fontsize=12)
plt.tight_layout()
plt.show()

# Optional: save heatmap
plt.savefig("heatmap_business_type_vs_location.png")