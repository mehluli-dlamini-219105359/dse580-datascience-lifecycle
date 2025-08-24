import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned Excel file
file_path = "MEHLULIdse580-cleaned_sorted_by_type_updated.xlsx"
df = pd.read_excel(file_path)

# Clean column names
df.columns = df.columns.str.strip()

# Filter for Lead_Potential = Low or Medium
filtered_df = df[df['Lead_Potential'].isin(['Low', 'Medium'])]

# Count unique company names per Type
# Adjust 'Company Name' if the column name is different
company_count = filtered_df.groupby('Type')['Company Name'].nunique()

# Sort descending for better visualization
company_count = company_count.sort_values(ascending=False)

# Plot horizontal bar chart
plt.figure(figsize=(12,8))
ax = company_count.plot(kind='barh', color='#ff7f0e')
plt.title("Number of Companies by Type with Low or Medium Lead Potential", fontsize=14)
plt.xlabel("Number of Companies", fontsize=12)
plt.ylabel("Type of Business", fontsize=12)
plt.gca().invert_yaxis()  # Highest values on top

# Add counts on the bars
for i, v in enumerate(company_count):
    ax.text(v + 0.1, i, str(v), color='black', va='center', fontsize=10)

plt.tight_layout()
plt.show()
import seaborn as sns

heatmap_data = filtered_df.pivot_table(index='Type', columns='ClearoutPhone Location', values='Company Name', aggfunc='count', fill_value=0)

plt.figure(figsize=(12,8))
sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='Blues')
plt.title("Heatmap of Business Types vs Locations (Low & Medium Leads)")
plt.tight_layout()
plt.show()

# Optional: save chart
plt.savefig("low_medium_lead_potential_by_type.png")