"""
Ashu and Shanu are best buddies. One day Shanu gives Ashu a problem to test his intelligence.He gives him an array of N natural numbers and asks him to solve the following queries:-

Query 0:- modify the element present at index i to x.
Query 1:- count the number of even numbers in range l to r inclusive.
Query 2:- count the number of odd numbers in range l to r inclusive.

input:
First line of the input contains the number N. Next line contains N natural numbers.
Next line contains an integer Q followed by Q queries.
0 x y - modify the number at index x to y.
1 x y - count the number of even numbers in range l to r inclusive.
2 x y - count the number of odd numbers in range l to r inclusive.

Constraints:
1<=N,Q<=10^5
1<=l<=r<=N
0<=Ai<=10^9
1<=x<=N
0<=y<=10^9

Note:- indexing starts from 1.

This Problem is solved using Fenwick Tree.
Here we are only calculating the occurences of even numbers in the given range from l to r.

"""


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
