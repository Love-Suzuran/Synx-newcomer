def get_fibonacci(n):
    a=0;
    b=1;
    print("[",end='');
    if n == 0:
        print("]");
    elif n == 1:
        print("0]");
    elif n == 2:
        print("0,1]");
    else:
        n = n-2;
        print("0, 1",end=', ');
        c = a+b
        a = b
        b = c
        while n>=2:
            print(c,end=', ');
            a = b
            b = c
            c = a+b
            n = n-1
        print(c,end='');
        print("]")

get_fibonacci(10)
