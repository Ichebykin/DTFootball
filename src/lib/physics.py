import numpy as np
import numpy.linalg as la
import math

G = np.array([0, 500.0])
#dt = 0.01

class Physics:
    def __init__(self):
        return
    @staticmethod
    def calc_dr(v,dt):
        dr = v * dt + G * dt * dt / 2
        return(dr)
    @staticmethod
    def calc_dv(v,dt):
        a = -1 * v 
        dv = (G + a) * dt
        return(dv)
    @staticmethod
    def interact(ball,player):
        v = ball.v - player.v
        if la.norm(v) > 1:
            r = player.r - ball.r
            r[0]+=(player.rect.w - ball.rect.w)/2#width correction
            r[1]+=(player.rect.h - ball.rect.h)/2
            tau = np.array([-r[1], r[0]])
            alpha = math.acos(np.dot(v, r) / la.norm(v) / la.norm(r))
            v_r = la.norm(v) * math.cos(alpha) * r / la.norm(r)
            v_tau = la.norm(v) * math.sin(alpha) * tau / la.norm(tau)
            if np.dot(v, tau)<0:
                v_tau = - v_tau
            ball.v = v_tau + player.v - 0*v_r
            ball.r = ball.r - r/la.norm(r)*3