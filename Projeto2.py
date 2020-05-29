import math

def main():
    print("Insert Velocity (m/s):")
    v = int(input(">"))

    print("Insert Angle (Deg):")
    ang = int(input(">"))

    print("Insert Viscosity (Deg):")
    Vis = input(">")
    if Vis == "":
        Vis = 0
    else:
        int(Vis)

    print("Insert Gravity (m/s2):")
    G = input(">")
    if G == "":
        G = -9.8
    else:
        int(G)

    print("Time of Flight = " + str(trajectory(v,ang,Vis,G)))

def trajectory(velocity, angle,viscosity,gravity):
    Vx = math.cos(angle)*velocity
    Vy = math.sin(angle)*velocity
    V0 = (Vx, Vy)
    
    for x in V0:
        t = 2 * x * math.sin(angle) / gravity
        if (t < 0):
            break
        else:
            return t

main()