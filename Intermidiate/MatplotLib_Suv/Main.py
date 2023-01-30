from matplotlib import pyplot as plt 
from matplotlib import style as s

s.use('ggplot')

# plot simple line 
plt.plot([10,20,3],[40,5,90],label='first')
plt.plot([1,2,3],[4,5,9],label='second')

# include title 
plt.title('This is simple Heading')

# use for removing ticks x and y axis 
# plt.xticks([])
# plt.yticks([])

# include labels 
plt.xlabel('This is x')
plt.ylabel('This is y')

plt.legend()
# show plot 
plt.show()