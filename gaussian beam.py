import numpy as np
import matplotlib.pyplot as plt

wavelen = 780e-9

r,z = np.meshgrid(np.linspace(-6,6,300)*800e-9,np.linspace(-10,10,300)*800e-9, indexing = 'ij')
dr = wavelen/25
w_0 = wavelen*1.5
zr = np.pi*w_0**2/wavelen
w = w_0*np.sqrt(1+(z/zr)**2)
k = 2*np.pi/wavelen
            
R = z*(1+(zr/z)**2)
jz = np.exp(-((r)**2)/w**2)

phasefactor = k*((r)**2)/2/R + k*z - np.arctan(z/zr)
plt.figure(4)
plt.pcolormesh(z,r,(jz*np.sin(phasefactor))**2,
               cmap = plt.get_cmap('bwr'),
               shading='gouraud')


    

