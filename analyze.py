from turtle import color
import matplotlib.pyplot
import numpy 

b = numpy.load("data/backLegSensorValues.npy", mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII')
a = print(numpy.load("data/backLegSensorValues.npy", mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII'))

d = numpy.load("data/frontLegSensorValues.npy", mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII')
c = print(numpy.load("data/frontLegSensorValues.npy", mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII'))

matplotlib.pyplot.plot(b, linewidth=3, color='green')
matplotlib.pyplot.plot(d, color='purple')

matplotlib.pyplot.legend()
matplotlib.pyplot.show()

