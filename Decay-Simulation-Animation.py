import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

rng = np.random.default_rng()

def N(N0,λ,t_max,nb_points,element):
    time_s = np.linspace(0,t_max,nb_points)
    N_t = N0*np.exp(-λ*time_s)
    plt.style.use('dark_background')
    fig, axis = plt.subplots()
    animated_plot, = axis.plot([], [],linewidth=2, color='red', label=f'{element}')
    axis.set_xlim([0, t_max])
    axis.set_ylim([0, N0])
    plt.title(f'Decay of the {element} vs time')
    plt.xlabel('Time in sec')
    plt.ylabel('N (atoms)')

    def update_data(frame):
        animated_plot.set_data(time_s[:frame*10], N_t[:frame*10]) #faire attention au bug
        return animated_plot,

    animation = FuncAnimation(fig=fig,
                                  func=update_data,
                                  frames=len(time_s),
                                  interval = 2,
                                  )
    plt.legend()
    plt.show()
    
    return N_t, time_s, animation,
        
#iodine 131
result = N(10000,np.log(2)/692928,1*10**7,1000,'Iodine 131')


