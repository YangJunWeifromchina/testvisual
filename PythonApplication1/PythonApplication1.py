
import sys
import numpy as np     # installed with matplotlib
import matplotlib.pyplot as plt
from math import radians,cos,sin 
def method_name():
    return print("hello visual studio!")

for i in range(360):
    print(cos(i))

def make_dot_string(x):
    return ' ' * int(20 * cos(radians(x)) + 30) + 'o'
for i in range(0,720,20):
    make_dot_string(i)

    from math import radians

def main():
    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.show()

main()