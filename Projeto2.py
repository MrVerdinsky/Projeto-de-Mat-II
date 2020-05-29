import math

def main():
    print("Hello")

def trajectory(velocity, angle,viscosity,gravity):
    Vx = math.cos(angle)*velocity
    Vy = math.sin(angle)*velocity
    V0 = (Vx, Vy)
    t = 
