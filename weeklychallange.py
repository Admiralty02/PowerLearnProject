import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# 1. NumPy array from 1 to 10 and calculate the mean
array = np.arange(1, 11)
mean_value = np.mean(array)
print("NumPy Array:", array)
print("Mean of array:", mean_value)

# 2. Load a small dataset into a pandas DataFrame and display summary statistics
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
    'Age': [23, 30, 25, 22, 28],
    'Score': [85, 90, 88, 95, 80]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:\n", df)
print("\nSummary Statistics:\n", df.describe())

# 3. Fetch data from a public API using requests
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
if response.status_code == 200:
    bitcoin_data = response.json()
    usd_price = bitcoin_data['bpi']['USD']['rate']
    print("\nCurrent Bitcoin Price in USD:", usd_price)
else:
    print("\nFailed to fetch data from API.")

# 4. Plot a simple line graph using matplotlib
numbers = [1, 3, 5, 7, 9]
plt.plot(numbers, marker='o', linestyle='-', color='green')
plt.title("Simple Line Graph")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.tight_layout()
plt.show()
