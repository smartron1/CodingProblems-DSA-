def update(i, num):
    previous = arr[i-1]
    index = i-1
    mod2 = num%2
    mod1 = previous%2
    while(i < len(fenwick)):
        if mod1 == 0 and mod2 == 0:
            break
        elif mod1 == 1 and mod2 == 1:
            break
        elif mod1 == 0 and mod2 == 1:
            fenwick[i]-=1
        elif mod1 == 1 and mod2 == 0:
            fenwick[i]+=1
        
        i += (i&(-i))
    arr[index] = num

def getSum(i):
    ans = 0
    while (i > 0):
        ans+=fenwick[i]
        i -= (i&(-i))
    return ans

n = int(input())
arr = list(map(int, input().split()))
fenwick = [0]*(n+1)
for i in range(n):
    j = i+1
    mod1 = arr[i]%2
    while(j < len(fenwick)):
        if mod1 == 0:
            fenwick[j]+=1
        j += (j&(-j))
        
q = int(input())
for _ in range(q):
    query, x, y = map(int, input().split())
    if query == 0:
        update(x, y)
    elif query == 2:
        print((y-x+1) - (getSum(y) - getSum(x-1)))
    else:
        print(getSum(y) - getSum(x-1))
