import matplotlib.pyplot as plt
#scatter diagram
#import third-part software tool. matplotlib need to be install in advance
x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=10)

#set char title and label axes
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#set the scale mark size
plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()
