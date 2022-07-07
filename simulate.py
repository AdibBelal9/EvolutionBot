from time import time
import time
import pybullet as p
import pybullet_data

passphysicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")

p.loadSDF("boxes.sdf")

for i in range(1000):
    p.stepSimulation()
    print(i)
    time.sleep(0.05)
    
p.disconnect()
# testing 