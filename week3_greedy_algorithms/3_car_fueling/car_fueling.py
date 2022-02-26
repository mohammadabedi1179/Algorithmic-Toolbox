import sys


def compute_min_refills(distance, tank, stops):
    num=0
    start=0
    stops.append(distance)
    for j in range(len(stops)):
        if stops[j]-start>tank:
            start=stops[j-1]
            num=num+1
    stops.insert(0,0)
    for i in range(len(stops)-1):
        if stops[i+1]-stops[i]>m:
           num=-1
    return num
if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))