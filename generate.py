from ctypes import sizeof
import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")

    # Box dimensions
    length = 1
    width = 1
    height = 1

    # Box position
    x = 0
    y = 2
    z = 0.5
    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
    pyrosim.End()

Create_World()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    length = 1
    width = 1
    height = 1
    x = 0
    y = 0
    z = 0.5
    pyrosim.Send_Cube(name="Link0", pos=[x,y,z] , size=[length,width,height])
    pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0,0,1])
    pyrosim.Send_Cube(name="Link1", pos=[0,0,0.5] , size=[1,1,1])
    pyrosim.End()

Create_Robot()


# for loops for multiple links:
    #for s in range(10):
    #   pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
    #    if z == z:
    #        z = z + 1
    #    print(s)