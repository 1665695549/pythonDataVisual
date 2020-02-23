import csv
from matplotlib import pyplot as plt
from datetime import datetime
filename='sitka_weather_2014.csv'
with open(filename) as f:
	#create a reader instance associated with the file
	reader=csv.reader(f)
	#read the first line
	header_row=next(reader)
	
	#get the highest temperature ,datetime and lowest temperature
	dates,highs,lows=[],[],[]
	for row in reader:
		
		try:
			current_date=datetime.strptime(row[0],"%Y-%m-%d")
			high=int(row[1])
			low=int(row[3])
		except ValueError:
			print(current_date,'missing data')
		else:
			highs.append(high)
			lows.append(low)
		dates.append(current_date)
		

		
#draw the graphical according to the data
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='blue')
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1

)

#set the graphic format
plt.title("Daily high and low temperatures-2014",fontsize=24)
plt.xlabel('',fontsize=16)
#draw slanted dates to avoid overlapping
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=16)
#set the size of tic marks
plt.tick_params(axis='both',which='major',labelsize=10)

plt.show()
