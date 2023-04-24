x,y,w,h = map(int,input().split())
ans = [x,y,w-x,h-y]
print (min(ans))
