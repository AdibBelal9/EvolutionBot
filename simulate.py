from time import time
import time
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy 

passphysicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")


# p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(10000)

for i in range(100):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    print(backLegSensorValues[i])
    time.sleep(0.05)
    # print(i)

print(backLegSensorValues)

p.disconnect()
# testing 