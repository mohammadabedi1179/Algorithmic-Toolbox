
def binary(keys,q):
    k=keys
    while len(k)>1:
        n=len(k)//2
        if k[n]<=q:
            k=k[n:]
        else:
            k=k[0:n]
    
    if k[0]==q:
        final=keys.index(q)
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
        print(binary(input_keys, q), end=' ')
