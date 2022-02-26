# Uses python3
import sys
import itertools

def howsum(target,numbers,memo={},subs=[]):
    if target in memo.keys():
        return memo[target]

    if target == 0:
        return []
    
    if target < 0:
        return None
    
    for number in numbers:

        subtarget = target - number
        new_numbers = [n for n in numbers]
        new_numbers.remove(number)
        list = howsum(subtarget,new_numbers,memo)

        if list != None:
            newlist = [i for i in list]
            newlist.append(number)

            memo[target] = newlist
            return memo[target]
    memo[target] = None
    return memo[target]
def partition3(list_of_numbers):
    list_of_numbers.sort(reverse=True)
    summation = 0
    for i in list_of_numbers:
        summation += i
    summation = summation/3 
    for i in range(3):
        memo ={}
        split = howsum(summation,list_of_numbers,memo)
        if split == None:
            return 0
        else:
            for n in split:
                list_of_numbers.remove(n)
    return 1




"""def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0
"""
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

#print(partition3([17, 59, 34, 57, 17, 23, 67, 1 ,18, 2 ,59]))