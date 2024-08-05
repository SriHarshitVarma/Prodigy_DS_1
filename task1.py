import requests
import zipfile
import io
import pandas as pd
import matplotlib.pyplot as plt
url = "http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv"
response = requests.get(url)
zip_file = zipfile.ZipFile(io.BytesIO(response.content))
zip_file.extractall("world_bank_data")
df = pd.read_csv('world_bank_data/API_SP.POP.TOTL_DS2_en_csv_v2_4701373.csv', skiprows=4)
most_recent_year = df.columns[-1]
population_data = df[['Country Name', most_recent_year]].dropna()
population_data.columns = ['Country', 'Population']
plt.figure(figsize=(15, 10))
plt.bar(population_data['Country'], population_data['Population'])
plt.xlabel('Country')
plt.ylabel('Population')
plt.title('Population Distribution by Country')
plt.xticks(rotation=90)
plt.savefig('population_distribution_by_country.png')
plt.show()
