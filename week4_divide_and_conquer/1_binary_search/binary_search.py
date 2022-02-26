def binary(right,keys,q):
    k=keys
    left=0
    while right-left>1:
        n=(right-left)//2
        if k[n+left]<=q:
            left=left+n
        else:
            right=right-n-(right-left)%2
    if k[right-1]==q:
        if right==1:
            final=left
        elif right>=2:
            while k[right-1]==k[right-2] and right>=2:
                  right=right-1
                  left=left-1
            final=left
    else:
        final=-1
    return final
if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary(num_keys,input_keys, q), end=' ')