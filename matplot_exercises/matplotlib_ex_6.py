import pandas as pd
import matplotlib.pyplot as plt

csv_file = pd.read_csv('company_sales_data.csv')
profitList= csv_file ['total_profit'].tolist
monthList= csv_file['month_number'].tolist()
bathingsoapSalesData   = csv_file ['bathingsoap'].tolist()
plt.bar(monthList, bathingsoapSalesData)

plt.xlabel('Month number')
plt.ylabel('Sales units in Number')
plt.xticks(monthList)
plt.title('Sales data')
plt.legend(loc='upper left')

plt.grid(True, linewidth=1, linestyle='--')

plt.legend()
#print(csv_file)
plt.show()


