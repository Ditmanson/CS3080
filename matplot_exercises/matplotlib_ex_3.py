import pandas as pd
import matplotlib.pyplot as plt

csv_file = pd.read_csv('company_sales_data.csv')
profitList = csv_file ['total_profit'].tolist()
monthList= csv_file['month_number'].tolist()
faceCreamSalesData = csv_file['facecream'].tolist()
faceWashSalesData   = csv_file ['facewash'].tolist()
toothPasteSalesData = csv_file ['toothpaste'].tolist()
bathingsoapSalesData   = csv_file ['bathingsoap'].tolist()
shampooSalesData   = csv_file ['shampoo'].tolist()
moisturizerSalesData = csv_file ['moisturizer'].tolist()
plt.xlabel('Month number')
plt.ylabel('Sales')
plt.xticks(monthList)
plt.title('Company profit per month')
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.title('Sales data')
plt.legend(loc='upper left')


plt.plot(monthList, faceCreamSalesData, label='MonthWise profit data of last year', marker='o', linewidth=3)
plt.plot(monthList, faceWashSalesData,   label = 'Face Wash Sales Data',  marker='o', linewidth=3)
plt.plot(monthList, toothPasteSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, bathingsoapSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, shampooSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, moisturizerSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)

plt.legend()
#print(csv_file)
plt.show()

