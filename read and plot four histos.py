import numpy as np
import matplotlib.pyplot as plt
import fittingToolbox as fitt
import pandas as pd
from scipy.optimize import least_squares # Levenberg-Marquadt Algorithm #
import pathlib

nano = 10**-9
save = True

#%% Set up Histogram parameters + read data file
start = np.array([-20, 400, 400,-20])*nano
interval_time = np.array([81.92, 2.56, 2.56, 2.56])*nano

datafile = '20180618 - Data006'
pathlib.Path(datafile).mkdir(parents=True, exist_ok=True) 

data = pd.read_csv(datafile+'.txt', delim_whitespace=True, 
                   header=None, index_col = 0, usecols = range(0,18), 
                   names = ['','fname','CH0','CH1','CH2','CH3','g2','dg2','eff',
                            'deff','pw','dpw','pr','dpr','cwr','acci','tr','mots'])

data['pr'] = data['pr'] - data['pr'].iloc[0]
data['pw'] = data['pw'] - data['pw'].iloc[0]
data['freq'] = data.index*2*100
data[['fname', 'CH1', 'CH2','CH3','cwr','acci','tr','mots','freq']] = data[['fname', 'CH1', 'CH2','CH3','cwr','acci','tr','mots','freq']].astype(int)

#%% Read all Hists (Histogram 1-4) for and plot
for j,take in enumerate(data['fname'].iloc[0:]):
    fig = plt.figure(j*100)
    for i in range(0,4):
        file = 'Histo{:1d}{:03d}.his'.format(i,take)
        print(file)
        hist = fitt.read_histo(file)
        
        fig.suptitle('Histograms from take ' + str(take))
        plt.subplot(2,2,i+1)
        plt.title('Histogram' + str(i))
    #    plt.bar((start[i] + np.array(range(0,991))*interval_time[i])/nano,hist, interval_time[i]/nano,  align='center')
        plt.plot((start[i] + np.array(range(0,991))*interval_time[i])/nano,hist)
    if save:
        plt.savefig('{0}/{1:02d}Histograms_1234_{2}'.format(datafile,j,take))
        plt.close()