import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df4 = pd.read_csv("14 prog 5ds_salaries.csv")

grouped = df4.groupby('experience_level')['salary_in_usd'].mean()

plt.bar(grouped.index, grouped.values, width=0.5, edgecolor='white', linewidth=0.4)
plt.xlabel("Experience Level")
plt.ylabel("Average Salary (USD)")
plt.title("Average Salary by Experience Level (Matplotlib)")
plt.show()


sns.barplot(x='experience_level', y='salary_in_usd', data=df4)
plt.xlabel("Experience Level")
plt.ylabel("Salary (USD)")
plt.title("Salary vs Experience Level (Seaborn)")
plt.show()
