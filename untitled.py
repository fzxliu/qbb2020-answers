

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
print(type(x))
print(len(x))
print(x[1])
y=[1,4,9,16,25]
fig, ax = plt.subplots()
ax.plot( x, y )
fig.savefig('testfig.png')
plt.close('fig')

# for command, open figure using:
# cmd.exe /C start testfig.png 