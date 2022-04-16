from main import Optimize
import matplotlib.pyplot as plt
import numpy as np

test = Optimize()
res = np.array(test.optimize())
labels = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']

plt.plot(res)
plt.savefig('./output.png')