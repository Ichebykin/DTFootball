import numpy as np
import numpy.linalg as la
import math

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
        a = -0.5 * v 
        dv = (G + a) * dt
        return(dv)
    @staticmethod
    def interact(ball,player):
        v = ball.v - player.v
        r = player.r - ball.r
        tau = np.array([-r[1], r[0]])
        alpha = math.acos(np.dot(v, r) / la.norm(v) / la.norm(r))
        v_r = la.norm(v) * math.cos(alpha) * r / la.norm(r)
        v_tau = la.norm(v) * math.sin(alpha) * tau / la.norm(tau)
        if np.dot(v, tau)<0:
            v_tau = - v_tau
        ball.v = v_tau + player.v - 0.5*v_r
        #player.v =player.v
        #player.r = ball.r + r/la.norm(r)*(ball.radius+player.radius)