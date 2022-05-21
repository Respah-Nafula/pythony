x=1
y=20
while x<y :
    x+=1
    print(x)
    if x%3 ==0:
        continue
    print(x)

    w=1
    r=50
    while w<r :
        w+=1
        if w%5!=0:
            continue
        print(w)