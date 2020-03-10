w,h,x,y= map(int,input().split())

centerx = w/2
centery = h/2

if(centerx == x and centery == y):
    print((w*h)/2)
    print("1")
else:
    print((w*h)/2)
    print("0")
