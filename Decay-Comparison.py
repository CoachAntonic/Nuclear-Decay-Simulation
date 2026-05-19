import numpy as np
import matplotlib.pyplot as plt

def Decay_comparison(elements,t_max,nb_points) :
    plt.figure(figsize=(10,6))
    time_s = np.linspace(0,t_max,nb_points)
    for name, N0 ,λ in elements:
        plt.plot(time_s,N0 * np.exp(-λ*time_s),linestyle='-',markersize=2,label=f'{name}')
    plt.title('Decay of different elements')
    plt.xlabel('Time in sec')
    plt.ylabel('N (atoms)')
    plt.grid(True)
    plt.legend()
    plt.show()        
    
elements = [
    ('Iodine-131', 10000, np.log(2)/692928),
    ('Barium-140', 10000, np.log(2)/1101600),
    ('Cerium-141', 10000, np.log(2)/2808000)
]


Decay_comparison(elements,2*10**7, 1000)
        
    
    
