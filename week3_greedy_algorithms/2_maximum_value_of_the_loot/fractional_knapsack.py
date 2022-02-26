import sys
import numpy as np

def get_optimal_value(capacity, weights, values):
    n=len(weights)
    value=0
    vpw=[]
    for i in range(n):
        vpw.append(values[i]/weights[i])
    while capacity!=0 and len(weights)!=0:
        max_index=vpw.index(max(vpw))
        if weights[max_index]<=capacity:
            capacity=capacity-weights[max_index]
            value=value+values[max_index]
            vpw.pop(max_index)
            weights.pop(max_index)
            values.pop(max_index)
        else:
            value=value+capacity*vpw[max_index]
            capacity=0

    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))