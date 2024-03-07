import math
import matplotlib.pyplot as plt
import sys
import time

def get_plot(values_cos):
    xs = [x for x in range(len(values_cos))]
    plt.plot(xs, values_cos)
    plt.show()


def give_cos(x):
    return math.cos(x)


def sync_cos_task(x):
    values_cos = []
    for i in range(0,200, x):
        values_cos.append(give_cos(i))
    #get_plot(values_cos)



if __name__ == "__main__":
    #print(sys.argv[1])
    #start = time.time()
    sync_cos_task(int(sys.argv[1]))
    #end = time.time()
    #print("Duration (s):", str(end-start))