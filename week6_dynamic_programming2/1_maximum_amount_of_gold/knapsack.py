import sys

def optimal_weight(total,weights):
    hamechi = cansum(total,weights)
    if hamechi[1]:
        return total
    else:
        return total - min(hamechi[0].keys())

def cansum(target,numbers,memo={}):
    if target in memo:
            return (memo,memo[target])

    if target == 0:
        return (memo,True)

    if target < 0:
        return (memo,False)

    for number in numbers:

        subtarget = target - number
        new_numbers = [i for i in numbers]
        new_numbers.remove(number)

        if cansum(subtarget,new_numbers,memo)[1]:               
            memo[target] = True
            return(memo,True) 

    memo[target]= False
    return (memo,False)
    

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
#print(optimal_weight(20,[5,7,12]))
            
        

