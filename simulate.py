from time import time
import time
import pybullet as p

passphysicsClient = p.connect(p.GUI)

for i in range(1000):
    p.stepSimulation()
    print(i)
    time.sleep(0.01)


p.disconnect()
