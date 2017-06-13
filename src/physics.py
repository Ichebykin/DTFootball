import numpy as np

G = np.array([0, 500.0])
dt = 0.01

class Physics:
    def __init__(self):
        return
    @staticmethod
    def calc_dr(v):
        dr = v * dt + G * dt * dt / 2
        return(dr)
    @staticmethod
    def calc_dv(v):
        a = -0.5 * v #дополнительное уменьшение скорости из-за вязких сил 
        dv = (G + a) * dt
        return(dv)
