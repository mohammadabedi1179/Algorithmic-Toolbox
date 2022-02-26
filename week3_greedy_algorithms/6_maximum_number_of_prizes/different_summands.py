# Uses python3
import sys
from numpy import sqrt as sq

def optimal_summands(n):
    summands = []
    k=(-1+sq(1+8*n))/2
    k=int(k)
    for i in range(1,k+1):
        summands.append(i)
    s=int(n-k*(k+1)/2)
    summands[k-1]=summands[k-1]+s
    return summands
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
