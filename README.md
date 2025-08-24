# Business Data Visualization – Data Science Life Cycle

**Author:** Mehluli Dlamini (219105359)

This project demonstrates how to apply the **Data Science Life Cycle** to analyze and visualize business data from an Excel file. It focuses on generating insights from business characteristics such as type, lead potential, and other attributes.

---

## ✅ Data Science Life Cycle in This Project

### **1. Data Collection**
- The dataset is sourced from an Excel file: `dse580-cleaned_sorted_by_type.xlsx`.

### **2. Data Preparation**
- Removed duplicate rows.
- Dropped rows with missing values.
- Removed invalid entries such as `fixed_line_or_mobile`.
- Dropped columns with **90%+ missing values**.
- Converted `Reviews` to numeric values.
- Created a derived column `Lead_Potential` based on:
  - **High:** Rating ≥ 4.5 and Reviews ≥ 50
  - **Medium:** Rating ≥ 4.0 and Reviews < 50
  - **Low:** Otherwise

### **3. Data Analysis**
- Grouped businesses by `Type` and `Lead_Potential`.
- Computed distributions for different attributes.

### **4. Data Visualization**
The script generates:
- **Line Charts**: For all numeric columns (e.g., Rating, Reviews).
- **Pie Charts**: Lead Potential distribution by business type.
- **Additional Recommended Charts**:
  - Bar charts for top addresses with highest-reviewed businesses.
  - Heatmaps for business type vs location.

### **5. Interpretation & Insight**
- Visualizations help answer:
  - Which business types dominate specific locations?
  - Where do Low/Medium potential businesses cluster?
  - What are possible market gaps and opportunities?

---

## 📂 Files
- `charts-script.py` → Main script for data cleaning and visualization.
- `MEHLULIdse580-cleaned_sorted_by_type_updated.xlsx` → Cleaned data after processing.
- `*_line_chart.png` → Line charts for numeric columns.
- `pie_lead_potential_*.png` → Pie charts per business type.

---

## ⚙️ Installation

Install required dependencies:

```bash
pip install pandas matplotlib openpyxl
