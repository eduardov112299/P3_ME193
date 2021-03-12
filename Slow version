import math 

import numpy as np

import matplotlib.pyplot as plt

import time

 

start = time.time()

#Preallocating space for variables - don't know if python needs this but this should make things quicker I think

timeConstant = 2*math.sqrt(3)*math.pi/3;

N = 1000;

dt = timeConstant/N;

t = np.zeros(N);

x1 = np.zeros(N);

x2 = np.zeros(N);

x3 = np.zeros(N);

x3dot = np.zeros(N);

 
#Setting up initial conditions

t[0] = 0;

x1[0] = 1;

x2[0] = -1;

x3[0] = 0;

 
 
#Doing forward Euler to approximate ODE

for n in range(1,N):

    x3dot[n] = np.exp(-t[n-1]/2) - 3*x2[n-1];

    t[n] = t[n-1] + dt;

    x3[n] = x3[n-1] + x3dot[n]*dt;

    x2[n] = x2[n-1] + x3[n]*dt;

    x1[n] = x1[n-1] + x2[n]*dt;



end = time.time()

print('Time for code run (not including the plot):',end-start, 'sec')

plt.plot(t,x1)

plt.xlabel('Time [s]');

plt.title('Solution to ODE');
