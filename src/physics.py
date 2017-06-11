import numpy as np

G = np.array([0, 500.0])
dt = 0.01

class Physics:
    def __init__(self):
        return
    @staticmethod
    def calc_dr(v):
        r = v*dt+G*dt*dt/2
        return(r)
    @staticmethod
    def calc_dv(v):
        a = -0.5 * v 
        v = (G+a)*dt
        return(v)