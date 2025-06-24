import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_style("whitegrid")
df = sns.load_dataset('tips')
print("First 5 Rows:\n", df.head())

plt.figure(figsize=(8, 5))
sns.barplot(x='day', y='total_bill', data=df, palette='pastel')
plt.title('Average Total Bill by Day')
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(x='day', data=df, palette='muted')
plt.title('Number of Customers by Day')
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x='day', y='total_bill', data=df, palette='Set2')
plt.title('Total Bill Distribution by Day')
plt.show()

plt.figure(figsize=(8, 5))
sns.violinplot(x='sex', y='total_bill', data=df, palette='Set3')
plt.title('Total Bill Distribution by Gender')
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x='total_bill', y='tip', hue='sex', data=df)
plt.title('Scatter Plot: Tip vs Total Bill')
plt.show()

plt.figure(figsize=(8, 5))
sns.lineplot(x=df.index, y='total_bill', data=df)
plt.title('Line Plot of Total Bill Over Index')
plt.show()

plt.figure(figsize=(8, 5))
correlation_matrix = df.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

sns.pairplot(df, hue='sex', palette='husl')
plt.suptitle('Pairwise Relationships (Pair Plot)', y=1.02)
plt.show()
