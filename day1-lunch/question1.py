import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots( nrows=2 )

x=[1, 2, 3, 4 ,5]
x2=[2, 5, 6]
y=[1, 4, 9, 16, 25]
y2=[8, 125, 216]

ax[0].plot( x, y, '.' )
ax[1].plot( x2, y2 )

# setting limits to the axes 
# do not know what the plot looks like, have to run in Jupyter
ax[0].set_xlim(0,max(x + x2))
ax[0].set_ylim(0,max(y + y2))
ax[1].set_xlim(0,max(x + x2))
ax[1].set_ylim(0,max(y + y2))

fig.savefig('question1.png')
plt.close('question1')
