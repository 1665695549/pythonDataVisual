import matplotlib.pyplot as plt
#broken line diagram
#import third-part software tool. matplotlib need to be install in advance
input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5)

#set char title and label axes
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#set the scale mark size
plt.tick_params(axis='both',labelsize=14)
plt.show()

