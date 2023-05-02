a1,a2 = map(int,input().split())
c = int(input())
n_ = int(input())
if a1*n_+a2 <= c * n_ and c >= a1:
    print(1)
else :
    print(0)
