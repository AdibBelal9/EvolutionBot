import matplotlib.pyplot
import numpy 

b = numpy.load("data/Store.npy", mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII')
a = print(numpy.load("data/Store.npy", mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII'))

matplotlib.pyplot.plot(b)
# , **kwargs

matplotlib.pyplot.show()

