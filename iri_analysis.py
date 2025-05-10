import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set style for plots
sns.set(style="whitegrid")

# Loading and exploring the Iris dataset
try:
    iris = load_iris(as_frame=True)
    df = iris.frame
    df['species'] = df['target'].map(dict(enumerate(iris.target_names)))

    print("First 5 rows of the dataset:")
    print(df.head())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    # Cleaning dataset (no missing values in Iris dataset, but general practice)
    df.dropna(inplace=True)

    # Basic Statistics
    print("\nSummary Statistics:")
    print(df.describe())

    # Grouped statistics
    grouped = df.groupby('species').mean()
    print("\nAverage Measurements by Species:")
    print(grouped)

    # 1. Line chart (using index as pseudo time)
    plt.figure(figsize=(8, 4))
    plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
    plt.plot(df.index, df['sepal width (cm)'], label='Sepal Width')
    plt.title('Sepal Measurements Over Index')
    plt.xlabel('Index')
    plt.ylabel('Length (cm)')
    plt.legend()
    plt.tight_layout()
    plt.show()

    # 2. Bar chart: Average Petal Length per Species
    plt.figure(figsize=(6, 4))
    sns.barplot(x='species', y='petal length (cm)', data=df, palette="muted")
    plt.title('Average Petal Length per Species')
    plt.xlabel('Species')
    plt.ylabel('Petal Length (cm)')
    plt.tight_layout()
    plt.show()

    # 3. Histogram: Distribution of Petal Width
    plt.figure(figsize=(6, 4))
    sns.histplot(df['petal width (cm)'], bins=15, kde=True, color="skyblue")
    plt.title('Distribution of Petal Width')
    plt.xlabel('Petal Width (cm)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

    # 4. Scatter Plot: Sepal Length vs Petal Length
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
    plt.title('Sepal vs Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.tight_layout()
    plt.show()

except Exception as e:
    print("An error occurred:", e)
  
