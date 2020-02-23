import matplotlib.pyplot as plt
#import third-part software tool. matplotlib need to be install in advance
from random_walk import RandomWalk

#create an RandomWalk instance and draw all point in the instance
rw=RandomWalk()
rw.fill_walk()

point_numbers=list(range(rw.num_points))

plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)

#highlight start and end points
plt.scatter(0,0,c='green',edgecolors='none',s=30)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=30)

#hide axis
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()
