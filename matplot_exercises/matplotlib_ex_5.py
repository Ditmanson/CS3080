import pandas as pd
import matplotlib.pyplot as plt

csv_file = pd.read_csv('company_sales_data.csv')
monthList= csv_file['month_number'].tolist()
faceCreamSalesData = csv_file['facecream'].tolist()
faceWashSalesData   = csv_file ['facewash'].tolist()

plt.xlabel('Month number')
plt.ylabel('Sales units in Number')
plt.xticks(monthList)
plt.title('Sales data')
plt.legend(loc='upper left')

plt.bar([a-0.25 for a in monthList],  faceCreamSalesData, width= 0.25, label= 'Face Cream sales data', align='edge')
plt.bar([a+0.25 for a in monthList],  faceWashSalesData, width= -0.25, label= 'Face Cream sales data', align='edge')


plt.legend()
#print(csv_file)
plt.show()

