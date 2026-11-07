#import pandas as pd

#test = pd.read_csv("D:/download new/house-prices-advanced-regression-techniques/test.csv")
#train = pd.read_csv("D:/download new/house-prices-advanced-regression-techniques/train.csv")
#print(test.head())
#print(train.head())
#print(train.info()) ## meriksa tipe data
#print(train.describe(include="all")) ## analisis deskriptif
# Memeriksa jumlah nilai yang hilang di setiap kolom
#missing_values = train.isnull().sum()
#missing_values[missing_values > 0]
#print(missing_values)

# BAR CHART
import matplotlib.pyplot as plt
import pandas as pd

cities = ('Bogor', 'Bandung', 'Jakarta', 'Semarang', 'Yograkarta', 'Surakarta', 'Surabaya', 'Medan', 'Makassar')

populations = (45076704, 11626410, 212162757, 19109619, 50819826, 17579085, 3481, 287750, 785409)

df = pd.DataFrame({
    'Cities' : cities,
    'Population' : populations
})

df.sort_values(by='Population', inplace=True)

plt.barh(y=df["Cities"], width=df["Population"])
plt.xlabel("Population (Millions)")
plt.title("Population of Cities in Indonesia")
plt.show()