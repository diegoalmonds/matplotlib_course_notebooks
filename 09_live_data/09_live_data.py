import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

index = count()

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']
    
    plt.cla() # stops the problem of getting different line colors each iteration
    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')
    
    plt.legend(loc='upper left')
    plt.tight_layout()


# animation is stored in a variable that lives as long as the animatino should run
ani = FuncAnimation(plt.gcf(), # plotted on the current figure
                    animate,  # animate is passed as the function that will be called
                    interval=1000) # 1000ms interval between each call

plt.show()