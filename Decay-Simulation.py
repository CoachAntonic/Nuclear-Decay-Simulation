import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

def N(N0,λ,t_max,nb_points,element):
    plt.figure(figsize=(10,6))
    time_s = np.linspace(0,t_max,nb_points)
    N = N0*np.exp(-λ*time_s)
    plt.plot(time_s , N , 'r-', markersize=1,label="N")
    Noisy_signal = rng.normal(0,N*0.05,nb_points) + N
    plt.plot(time_s, Noisy_signal , 'gp',markersize=2,label="Noisy signal")
    plt.ylabel('N (atoms)')
    plt.xlabel('Time (sec)')
    plt.title(f'Decay of {element} vs time')
    plt.grid(True)
    plt.legend()
    plt.show()

#iodine 131
N(10000,np.log(2)/692928,1*10**7,1000,'Iodine 131')

#to zoom plt.xlim(0,1000000)
