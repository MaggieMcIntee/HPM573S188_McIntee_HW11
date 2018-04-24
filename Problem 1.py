print("problem 2 is on parameters and problem 3 & 5 is in RunMarkovModel and RunMarkovModelTreat")

print(" ")
print("Problem 1")
print(" ")

print("Part 1")
print("Rate of stroke-associated mortalitiy events:")
# = 36.2/100,000
print("0.000362 or 0.0362 deaths per 1,000 population (of age 65 and older)")
print("Background (non-stroke associated) mortality:")
# =(18*100)-36.2
#   -------------    ==
#      100,000
print("0.017638 or 1.7638 deaths per 1,000 population (of age 65 and older)")

print(" ")

print("Part 2")
print("Annual rate of stroke events for this population:")
# (15/1000) = 0.015
#1-0.015 = 0.985
# -ln(.985) = 0.01511363
print ("0.01511")

print(" ")

print("Part 3")
print("Annual rate of transition from well to stroke:")
#(1-0.9) = 0.1
#15/0.1 = 150
#150/1000=0.15
#1-.15=0.85
#-ln(0.85) = 0.1625
print("0.1625")
print("Annual rate of transition from well to stroke-death:")
#(1-0.1) = 0.9
#15/0.9 = 16.67
#16.67/1000=0.016667
#1-0.016667=0.9833
#-ln(0.85) = 0.1625
print("0.1681")

print(" ")

print("Part 4")
print("Annual rate of recurrent stroke events:")
#1-.17=0.83
#15/0.83=18.072289
#18.07/1000=0.01807
#1-0.01807 = 0.9819
#-ln(0.9819)
print("0.01827")

print(" ")

print("Part 5")
print("Annual transition rate from Post-Stroke to Stroke:")
#1-.8=0.2
#0.01827/0.2 = 0.091329
#1-0.091329 = 0.908671
#-ln(0.908671) = 0.09577223497
print("0.09577")
print("Annual transition rate from Post-Stroke to Stroke-Death:")
#1-.2=0.8
#0.01827/0.8 = 0.0228375
#1-0.091329 = 0.9771625
#-ln(0.908671) = 0.02310231528
print("0.0231")

print(" ")

print("Part 6")
print("Annual rate of transition from Stroke to Post-Stroke:")
#0.01827/52 = 0.00035072
#1-0.00035072
#-ln(0.9996)=0.00035078151
print("0.0003507 or 35 per 100,000 population")

