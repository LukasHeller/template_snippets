N = 100
eps_rel = np.concatenate([np.ones(int(N/3)), 10*np.ones(int(N/30)) - 1j*np.ones(int(N/30)),np.ones(int(N/3)),10*np.ones(int(N/30)),np.ones(int(N/3))])
eps_colors = [cm.gray(256 - int(128*e/max(eps_rel))) for e in eps_rel]

for i in range(len(eps_rel)-1):
   ax.fill_between(x[i:i+2],(1,1),(-1,-1), color = eps_colors[i])
