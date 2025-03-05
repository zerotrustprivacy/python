import numpy
np = numpy
import matplotlib.pyplot
plt = matplotlib.pyplot

  # create the general format of the function f(x)

def f(x,a,b):
 y = a*x**2+b
 return y
x = np.linspace(-5,5,100) # 100 points between -5 and +5
y = f(x,2,-1) # vector y containing the values of f(x)
y2 = f(x,2,-5) # vector y containing the values of f(x)
plt.figure() # create a new figure
plt.plot(x,y) # plot f(x)
plt.plot(x,y2) # plot f2(x)
plt.xlabel('x') # label of the x axis
plt.ylabel('y') # label of the y axis
plt.legend(['f(x)','f2(x)']) # figure legend
plt.xlim([-5,5]) # change axis limits (x)
plt.ylim([-6,50]) # change axis limits (y)
plt.title('My Matplotlib Static Plot') # figure title
plt.savefig('myfig3.png')
plt.show()
