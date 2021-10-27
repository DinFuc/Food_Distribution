def distributeFood(food,n):
    b = [0] * n
    for i in food:
        b[i[0]] += i[2]
        if i[1] + 1 < n:
            b[i[1] + 1] -= i[2];
    c = [0] * n
    x = 0;
    for i in range(n):  
        x += b[i]
        c[i] = x;
    return c;
