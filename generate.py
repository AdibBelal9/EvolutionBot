from ctypes import sizeof
import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

# Box dimensions
length = 1
width = 1
height = 1
# Box position
x = 0
y = 0
z = 0.5
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])


pyrosim.End()





# for loops for multiple links:
    #for s in range(10):
    #   pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
    #    if z == z:
    #        z = z + 1
    #    print(s)