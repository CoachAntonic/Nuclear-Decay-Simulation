import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def Decay_comparison(elements,t_max,nb_points) :
    
    time_s = np.linspace(0,t_max,nb_points)
    plt.style.use('dark_background')
    fig, axis = plt.subplots()
    N_t_list = []
    curves = []
    N0_list = []
    colors = ['r', 'g', 'c']
    
    for (name, N0 ,λ), color in zip(elements, colors):
        N_t = N0*np.exp(-λ*time_s)
        N_t_list.append(N_t)
        animated_plot, = axis.plot([], [], color=color, label=f'{name}')
        curves.append(animated_plot)
        N0_list.append(N0)
        
    axis.set_ylim([0, max(N0_list)])
    axis.set_xlim([0, t_max])
    plt.title('Decay of different elements')
    plt.xlabel('Time in sec')
    plt.ylabel('N (atoms)')
    plt.grid(True)       
    
    
    def update_data(frame) :
        
        for N_t, updated_data in zip(N_t_list, curves) : 
            updated_data.set_data(time_s[:frame*8], N_t[:frame*8])
            
        return curves,
    
    animation = FuncAnimation(fig=fig,
                              func=update_data,
                              frames=len(time_s),
                              interval = 2,
                )
    plt.legend()
    plt.show()
    
    return N_t, time_s, animation,
        
        
    
    
    
 #test  
elements = [
    ('Iodine-131', 10000, np.log(2)/692928),
    ('Barium-140', 10000, np.log(2)/1101600),
    ('Cerium-141', 10000, np.log(2)/2808000)
]


result = Decay_comparison(elements,2*10**7, 1000)
        
    
    
