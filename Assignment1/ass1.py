# Assignment 1

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import norm

# Part 1

#labels = ['unknown', 'prices', '']
real_estate_prices = pd.read_csv("./houses.csv")
rep_values = real_estate_prices.iloc[:,1]
rep_mean = rep_values.mean()
rep_median = rep_values.median()
rep_std = rep_values.std()
rep_min = rep_values.min()
rep_max = rep_values.max()
#real_estate_prices
print(f'{rep_mean}, {rep_median}, {rep_std}, {rep_min}, {rep_max}')
#real_estate_prices
#rep_values.to_numpy()

# Plot of the distribution of the prices
# The plot is initially weird looking because the values are discrete, 
# if we convert them to "continuous" values, the histogram will be a good visualisation tool

n_bins = rep_values.size
#bins = [i for i in range(0, rep_max, int(rep_max/6))]
#print(rep_values.values.size)
rep_valuesf = rep_values.values.astype(np.float32)/256
plt.hist(rep_values, bins=np.arange(rep_min, rep_max), log=True)
plt.ylabel('Frequency')
plt.xlabel('Price')
plt.title('Prices of real estates in England')
plt.show()