import pandas as pd

# Read the CSV file into a pandas DataFrame
data = pd.read_csv("sales_data.csv")

# Explore the data
print(data.head())  # Display the first few rows
print(data.shape)  # Check the shape of the DataFrame - tuple (no. rows, no. columns)
data.info()  # Get information about the DataFrame
print(data.describe())  # Compute summary statistics

# Perform analysis
total_sales_per_product = data.groupby("Product")["Total Sales"].sum()
product_with_highest_sales = total_sales_per_product.idxmax()
average_quantity_sold_per_day = data["Quantity Sold"].mean()

# More analysis
january_sales = data[data["Date"].str.startswith("2022-01")]["Total Sales"].sum()
unique_products_sold = data["Product"].nunique()
average_sales_per_product = data.groupby("Product")["Total Sales"].mean()

print("Total sales amount for January:", january_sales)
print("Unique products sold:", unique_products_sold)
print("Average sales amount per product:\n", average_sales_per_product)