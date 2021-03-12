import numpy as np
from scipy.integrate import odeint
import matplotlib
import matplotlib.pyplot as pl

# define the ODE as a first order system
def ODE3(x,t):
    return [ 
        x[1], 
        x[2], 
        np.exp(-t/2) - (3*t)
        ]  

# initial values
x0=[ 10.6, -3.6, 31.2]
#y0 = [1, -1, 0]
# points at which the solution value is requested
t = np.linspace(0,10,501)
# numerical integration
y=odeint(ODE3, x0, t)
# y[-1,:] contains the value at x=10

# plot the solution with subplots for each component
plt.plot(t,y)
