#用了埃氏筛，会有加分吗AWA

is_pri =[1]*(1000005)
get_pri=[1]*(1000005);
p=0;
def get_primes(n):
    global p;
    n=min(n,1000000);
    if n<2:
        print("[]");
    else:
        for i in range(1,n):
            is_pri[i]=1;
        is_pri[0]=is_pri[1]=0;
        for i in range(2,n):
            if is_pri[i]==1 :
                p+=1;
                get_pri[p]=i;
                for j in range(2*i,n,i):
                    is_pri[j]=0;

get_primes(10000);
print("[",end="");
for i in range(1,10):
    print(get_pri[i],end=",")
print(get_pri[10],end="");
print("]",end="");
