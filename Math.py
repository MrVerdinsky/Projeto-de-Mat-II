import string

def main():
    printMenu()
    playerInput = input(">")
    while(playerInput != "0"):
        if playerInput == "1":
            FluidImersion()
            printMenu()
            playerInput = input(">")
        elif playerInput ==  "2":
            SpringLength() 
            printMenu()
            playerInput = input(">")
        else:
            playerInput = input(">")
            print("Input Unknown")
            printMenu()
    print("Goodbye")
    quit()
        
def printMenu():
    print("Please choose a problem to solve\n")
    print("1. Flutuation")
    print("2. Springs")
    print("0. Exit" )





def FluidImersion():
    Gravity = -9.81
    fluidDensity = 1000
    objectDensity = 450
    objectVolume = 0.269
    objectMass = objectDensity*objectVolume
    run = True
    result = FluidImersionMath(Gravity,fluidDensity, objectVolume, objectDensity, objectMass)

    while(run):
        print(f"Gravity set to: {Gravity}(m/s2)")
        print(f"Object Mass set to: {round(objectMass, 3)}(Kg)")
        print(f"Object Density set to: {round(objectDensity, 3)}(Kg/m3)")
        print(f"Object Volume set to: {objectVolume}(m3)")
        print(f"Fluid Density set to: {fluidDensity}(Kg/m3)\n")
        print(result)
        print("""Use commad "set" followed by the parameter and a value to change it,\n0 to return to the main menu or "help" for parameter commands""")

        playerInput = input(">")
        playerInput = playerInput.lower()
        playerInput = str.split(playerInput)

       
        if (playerInput[0] == "0"):
            run = False
             
        
        elif (playerInput[0] == "set"):
            if (playerInput[1] == "gravity"):
                Gravity = float(playerInput[2])

            elif (playerInput[1] == "density"):
                objectDensity = float(playerInput[2])
            
            elif (playerInput[1] == "mass"):
                objectMass = float(playerInput[2])
                objectVolume = objectDensity*objectMass
                objectDensity = objectMass/objectVolume

            elif (playerInput[1] == "volume"):
                objectVolume = float(playerInput[2])
                objectDensity = objectMass/objectVolume
            
            elif (playerInput[1] == "fluid"):
                fluidDensity = float(playerInput[2])

        elif(playerInput[0] == "help"):
            Commands()
        else:
            print("Unknown Command\n")

        result = FluidImersionMath(Gravity,fluidDensity, objectVolume, objectDensity, objectMass)

def SpringLength():
    Gravity = 9.81
    objectMass = 0.5
    restLength = 0.25
    springConstant = 25
    run = True
    result = SpringLengthMath(Gravity, objectMass, restLength, springConstant)
    while (run):
        print(f"Gravity set to: {Gravity}(m/s2)")
        print(f"Object Mass set to: {objectMass}(Kg)")
        print(f"Spring Length in Resting position set to: {restLength}(m)")
        print(f"Spring Constant set to: {springConstant}(N/m)\n")
        print(f"Spring would stretch at: {result}(m)\n")
        print("""Use commad "set" followed by the parameter and a value to change it,\n0 to return to the main menu or "help" for parameter commands""")
        
        playerInput = input(">")
        playerInput = playerInput.lower()
        playerInput = str.split(playerInput)
        
       
        if (playerInput[0] == "0"):
            run == False
            
        
        elif (playerInput[0] == "set"):
            if (playerInput[1] == "gravity"):
                Gravity = float(playerInput[2])

            elif (playerInput[1] == "mass"): 
                objectMass = float(playerInput[2])
            
            elif (playerInput[1] == "length"):
                restLength = float(playerInput[2])

            elif (playerInput[1] == "constant"):
                springConstant = float(playerInput[2])
        elif(playerInput[0] == "help"):
            Commands()
        else:
            print("Unknown Command\n")

        steadyStretch = SpringLengthMath(Gravity, objectMass, restLength, springConstant)
        
        result = f"Spring would stretch at: {round(steadyStretch, 3)}"

        return result
def SpringLengthMath(g, oM, r, k):
    # Calculates Gravitational Force
    Fg = oM * -g

    #According to Hook's Law F = -k(L - r), solve for L
    #Knowing that Fg + Fm = 0

    #Calculates the Springs Max Length
    L = (Fg-(-k*-r))/-k
    L = round(L, 3)
    return L

def FluidImersionMath(g, fD,oD, oV, oM):
    #Calculates object side size
    objectSide = oV**(1/3)

    #Calculates Gravitational Force
    gravityForce = oM * g

    #Calculates volume of the object that is submerged
    volumeSubmerged = gravityForce/(fD*g)

    sideSubmerged = volumeSubmerged**(1/3)

    #Calculates Force of impulsion
    fI = fD*g*oV

    if (gravityForce > fI):
        result = "Object sinks!"
        return result

    else:
        #Calculates the size of the submerged part of the object
        floatLevel = volumeSubmerged/(objectSide*objectSide)
        floatLevel = round(floatLevel, 3)

        objectCenterLevel = (sideSubmerged/2) + floatLevel
        result = f"Object's Center of Mass is at:{round(objectCenterLevel, 3)}(m) from the surface\n"
        return result


def Commands():
    print(" ________________________________________________________")
    print("|                          Commands                      |")
    print("|________________________________________________________|")
    print("|For the Flutuation problem, use set <paramater> <value>:|")
    print("""|"gravity" to change the gravity value                   |""")
    print("""|"density" to change the Object's Density                |""")
    print("""|"mass" to change the Object's Mass value                |""")
    print("""|"volume" to change the Object's Volume value            |""")
    print("""|"fluid" to change the Fluid's Density value             |""")
    print("|--------------------------------------------------------|")
    print("|For the Spring problem, use set <paramater> <value>:    |")
    print("""|"gravity" to change the gravity value                   |""")
    print("""|"mass" to change the Object's Mass value                |""")
    print("""|"length" to change the Spring's Resting Length value    |""")
    print("""|"constant" to change the Spring's Constant value        |""")
    print("|________________________________________________________|\n")


main()