import numpy as np

G = np.array([0, 10.0])

class Physics:
    def __init__(self):
        return
    @staticmethod
    def calc_dr(v,dt):
        r = v*dt+G*dt*dt/2
        return(r)
    @staticmethod
    def calc_dv(v,dt):
        v = G*dt
        return(v)