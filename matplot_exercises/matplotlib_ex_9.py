import pandas as pd
import matplotlib.pyplot as plt

csv_file = pd.read_csv('company_sales_data.csv')

bathingsoap= csv_file ['bathingsoap'].tolist()
monthList= csv_file['month_number'].tolist()
faceWashSalesData   = csv_file ['facewash'].tolist()


f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(monthList, bathingsoap, label= "BathingSoap Sales Data", color='k',marker ='o' , linewidth=3)
axarr[0].set_title('Sales data of bathing soap sales')

axarr[1].plot(monthList, faceWashSalesData, label= "FaceWash Sales Data", color='r',marker ='o' , linewidth=3)
axarr[1].set_title('Sales data of face washing sales')

plt.xticks(monthList)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')

#print(csv_file)
plt.show()
