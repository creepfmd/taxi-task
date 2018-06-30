import math

pD = [0, 0]
pA = [0, 1]
pB = [2, 0]
pH = [2, 1]

# Scalar multiply
scDADH = (pD[0] - pA[0])*(pD[0] - pH[0]) + (pD[1] - pA[1])*(pD[1] - pH[1])
scBHDH = (pB[0] - pH[0])*(pD[0] - pH[0]) + (pB[1] - pH[1])*(pD[1] - pH[1])
# Abs
modDH = math.sqrt((pD[0] - pH[0])**2 + (pD[1] - pH[1])**2)

# Projection of DA on DH
# Not going back for pick-up
prDADH = scDADH / modDH
print(prDADH)

# Projection of BH on DH
# Not going back for drop-out
prBHDH = scBHDH / modDH
print(prBHDH)

# If all projections is posititve than direction is OK
if prDADH >= 0 and prBHDH >= 0:
    print('Direction is OK!!!')
else:
    print('Direction is NOT OK')
