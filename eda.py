import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis


data = np.random.normal(loc=50, scale=15, size=100)
data[np.random.choice(100, 10, replace=False)] = np.nan

data_clean = data[~np.isnan(data)]
data_filled = np.where(np.isnan(data), np.nanmean(data), data)

Q1 = np.percentile(data_clean, 25)
Q2 = np.percentile(data_clean, 50)
Q3 = np.percentile(data_clean, 75)
IQR = Q3-Q1
print(f'{Q1 = }, {Q2 = }, {Q3 = }, {IQR = }')

plt.boxplot(data_clean)
plt.title('Boxplot')
plt.show()

print('Skewness:', skew(data_clean))
print('Kurtosis:', kurtosis(data_clean))

plt.hist(data_clean, bins=20, edgecolor='black')
plt.axvline(np.mean(data_clean), color='red', linestyle='dashed', label='Mean')
plt.title('Histogram')
plt.legend()
plt.show()
