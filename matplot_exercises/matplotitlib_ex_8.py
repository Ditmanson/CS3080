import pandas as pd
import matplotlib.pyplot as plt

csv_file = pd.read_csv('company_sales_data.csv')
profitList= csv_file ['total_profit'].tolist()
monthList= csv_file['month_number'].tolist()
labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
salesData   = [csv_file ['facecream'].sum(), csv_file ['facewash'].sum(), csv_file ['toothpaste'].sum(), 
        csv_file ['bathingsoap'].sum(), csv_file ['shampoo'].sum(), csv_file ['moisturizer'].sum()]
plt.axis('equal')
plt.pie(salesData, labels=labels, autopct='%1.1f%%')
plt.title('sales data')
plt.legend(loc='lower right')

plt.legend()
#print(csv_file)
plt.show()


