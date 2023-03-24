import pandas as pd
import matplotlib.pyplot as plt

csv_file = pd.read_csv('company_sales_data.csv')
profitList= csv_file ['total_profit'].tolist()
monthList= csv_file['month_number'].tolist()
labels = ['low', 'average', 'Good', 'Best']
profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
plt.hist(profitList, profit_range, label = 'Profit data')
plt.xlabel('profit range in dollar')
plt.ylabel('Actual Profit in dollar')
plt.xticks(profit_range)
plt.title('Profit data')
plt.legend(loc='upper left')


plt.legend()
#print(csv_file)
plt.show()


