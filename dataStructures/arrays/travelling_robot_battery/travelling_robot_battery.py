# A robot uses 1 joule of battery by going up per joule of gravitational energy and recharges the same when going down

# E = F * d = 9.8 * d

gravForce = 9.8

def heightClimbedToEnergyNeeded(deltaHeight):
    return max(deltaHeight * gravForce, 0)

def minimumEnergyNeededForPath(posArray):
    maxDelta = 0
    prevZ = posArray[0][2]
    for z in (pos[2] for pos in posArray):
        if z - prevZ > maxDelta:
            maxDelta = z - prevZ
        prevZ = z

    return heightClimbedToEnergyNeeded(maxDelta)
