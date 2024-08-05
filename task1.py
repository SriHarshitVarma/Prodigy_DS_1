import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("your_dataset.csv")
data.plot(x='Country', y='Population', kind='bar')
plt.title("Population by Country")
plt.xlabel("Country")
plt.ylabel("Population")
plt.xticks(rotation=45)
plt.savefig("population_bar_chart.png")
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('population_data.csv')
