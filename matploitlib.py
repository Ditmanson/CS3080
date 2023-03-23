import pandas as pd
import matplotlib.pyplot as plt

csv_file = pd.read_csv('company_sales_data.csv')
profitList = csv_file ['total_profit'].tolist()
monthList= csv_file['month_number'].tolist()
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.xticks(monthList)
plt.title('Company profit per month')
plt.yticks([100000,200000,300000,400000,500000])
plt.plot(monthList, profitList, label='MonthWise profit data of last year',
         color ='r')
#print(csv_file)
plt.show()

