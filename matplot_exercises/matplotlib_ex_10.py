import pandas as pd
import matplotlib.pyplot as plt

csv_file = pd.read_csv('company_sales_data.csv')

monthList  = csv_file ['month_number'].tolist()
faceCremSalesData   = csv_file ['facecream'].tolist()
faceWashSalesData   = csv_file ['facewash'].tolist()
toothPasteSalesData =csv_file ['toothpaste'].tolist()
bathingsoapSalesData   =csv_file ['bathingsoap'].tolist()
shampooSalesData   = csv_file ['shampoo'].tolist()
moisturizerSalesData = csv_file ['moisturizer'].tolist()


plt.plot([],[],color='m', label='face Cream', linewidth=5)
plt.plot([],[],color='c', label='Face wash', linewidth=5)
plt.plot([],[],color='r', label='Tooth paste', linewidth=5)
plt.plot([],[],color='k', label='Bathing soap', linewidth=5)
plt.plot([],[],color='g', label='Shampoo', linewidth=5)
plt.plot([],[],color='y', label='Moisturizer', linewidth=5)

plt.stackplot(monthList, faceCremSalesData, faceWashSalesData, toothPasteSalesData, 
            bathingsoapSalesData, shampooSalesData, moisturizerSalesData, 
            colors=['m','c','r','k','g','y'])
plt.title('Alll product sales data using stack plot')
plt.legend(loc='upper left')
#plt.legend()
plt.xticks(monthList)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')

print(csv_file)
plt.show()
