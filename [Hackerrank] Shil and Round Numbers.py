"""
Shil likes Round numbers very much . A number is called Round number if its non-negative and its first and last digits are same. For example 0 , 3 , 343 and 50005 are round numbers whereas 1000 is not a round number.
Shil has an array A1 , A2 .. AN . He wants to answer Q queries of following two type :
1 l r : Find total number of round numbers in range [l, r]
2 i K : Update ith element of array A to K i.e perform the operation Ai = K.
Since you are the friend of Shil , he asks for your help .

INPUT:
First line consists of two integers N and Q. Next line consists of N integers A1 , A2 .. AN. Next line consists of Q queries. Each query consists of three integers as mentioned in the problem.

OUTPUT:
For each query of type 2 , output total number of round numbers in range [l,r].

CONSTRAINTS:
1 ≤ N , Q ≤ 2*105
-1018 ≤ Ai ≤ 1018
1 ≤ l,r ≤ N
-1018 ≤ K ≤ 1018

Solved using Fenwick Tree
"""

def update(i, num):
    index = i-1
    if str(arr[index])[0] == str(arr[index])[-1] and str(num)[0] != str(num)[-1]:
        while i < len(fenwick):
            fenwick[i] -= 1
            i += (i&-(i))
    elif str(arr[index])[0] != str(arr[index])[-1] and str(num)[0] == str(num)[-1]:
        while i < len(fenwick):
            fenwick[i] += 1
            i += (i&-(i))
    arr[index] = num

def getSum(i):
    ans = 0
    while i > 0:
        ans+=fenwick[i]
        i-=(i&(-i))
    return ans


n, q = map(int, input().split())
arr = list(map(int, input().split()))
fenwick = [0]*(n+1)
for i in range(n):
    j = i+1
    x = str(arr[i])
    while j < len(fenwick):
        if x[0] == x[-1]:
            fenwick[j]+=1
        j += (j&(-j))
for _ in range(q):
    query, l, r = map(int, input().split())
    if query == 1:
        print(getSum(r)-getSum(l-1))
    else:
        update(l,r)
