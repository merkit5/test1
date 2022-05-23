import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df1 = pd.read_csv("../zillow.csv")
pd.read_csv('../zillow.csv', names=['ID', 'Girth', 'Height', 'Volume'], index_col=False)
sort = df1.sort_values(by='Height').head(31)
df = pd.DataFrame(sort)
#Здесь сортировка
print(df)
#Здесь построение графика
#x = np.arange(31)
#plt.plot(x,df['Height'],label='Height',color='g')
#plt.legend()
#Здесь первая диаграмма
plt.hist(df['Height'], bins=31)
plt.savefig('Height.png')
#Здесь вторая диаграмма
#plt.clf()
#plt.bar(df['ID'],df['Height'])
plt.show()