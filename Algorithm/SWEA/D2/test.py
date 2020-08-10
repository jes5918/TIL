for t in range(int(input())):
    n=int(input())
    b=[[0]*n for i in range(n)]
    dy=[0,1,0,-1]
    dx=[1,0,-1,0]
    d=r=c=0
    l=1
    while(l<=n*n):
        b[r][c]=l
        l+=1
        nr=r+dy[d]
        nc=c+dx[d]
        if 0<=nr<n and 0<=nc<n and b[nr][nc]==0:
            r,c=nr,nc
        else:
            d=(d+1)%4
            r+=dy[d]
            c+=dx[d]
    print(f'#{t+1}')
    for i in range(n):
        for j in range(n):print(b[i][j],end=' ')
        print()