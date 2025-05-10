import pandas as pd

# Step 1: Create a sample sales_data.csv
sales_data = {
    'Date': ['2025-05-01', '2025-05-01', '2025-05-02', '2025-05-02', '2025-05-03'],
    'Product': ['Laptop', 'Phone', 'Laptop', 'Tablet', 'Phone'],
    'Quantity Sold': [3, 5, 2, 4, 6],
    'Revenue ($)': [3000, 2500, 2000, 1600, 3000]
}
df = pd.DataFrame(sales_data)
df.to_csv('sales_data.csv', index=False)

# Step 2: Load the CSV file
df = pd.read_csv('sales_data.csv')

# Step 3: Calculate total revenue
total_revenue = df['Revenue ($)'].sum()

# Step 4: Find best-selling product
best_selling = df.groupby('Product')['Quantity Sold'].sum().idxmax()
best_selling_quantity = df.groupby('Product')['Quantity Sold'].sum().max()

# Step 5: Identify the day with the highest sales
daily_sales = df.groupby('Date')['Revenue ($)'].sum()
top_sales_day = daily_sales.idxmax()
top_sales_amount = daily_sales.max()

# Step 6: Save results to a text file
summary = (
    f"Sales Summary Report\n"
    f"----------------------\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Best-Selling Product: {best_selling} (Quantity Sold: {best_selling_quantity})\n"
    f"Day with Highest Sales: {top_sales_day} (${top_sales_amount})\n"
)

with open("sales_summary.txt", "w") as file:
    file.write(summary)

# Step 7: Print insights
print(summary)
