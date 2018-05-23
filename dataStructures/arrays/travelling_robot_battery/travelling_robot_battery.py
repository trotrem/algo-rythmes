# A robot uses 1 joule of battery by going up per joule of gravitational energy and recharges the same when going down

# E = F * d = 9.8 * d

gravForce = 9.8

def heightClimbedToEnergyNeeded(deltaHeight):
    return max(deltaHeight * gravForce, 0)

def minimumEnergyNeededForPath(posArray):
    climb = 0
    maxClimb = 0
    prevZ = posArray[0][2]
    for z in (pos[2] for pos in posArray):
        climb = max(climb + (z - prevZ), 0)
        if climb > maxClimb:
            maxClimb = climb
        prevZ = z

    return heightClimbedToEnergyNeeded(maxClimb)
