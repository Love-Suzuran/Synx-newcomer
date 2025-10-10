##  C语言（第四大题）

###  一、ascii码

####  T1：

输出为97，因为录入的是字符a，输出的是a的ascii码97

####  T2：

```c
   #include <stdio.h>
   
   int main(){
       char a = '1';
       //预期输出结果 1
       //请在这里补全代码
   	   int k = a;
       k-=48;
       a=k;
       //
       printf("%d",a);
       return 0;
   }
```

区别：一个是字符，一个是数字。

###  二、数组

####  T1：

```c
#include<stdio.h>
int a[105];
int main(){
    double sum=0;
    for(int i=1;i<=5;i++){
        printf("请输入第%d个学生的成绩：",i);
        scanf("%d",&a[i]);
        sum +=a[i];
    }
    printf("5个学生平均分为：%.2lf",sum/5.0);
}
```

####  T2 :

```c
#include<stdio.h>
int a[105];
int main(){
    int n;
    printf("请输入学生人数：");
    scanf("%d",&n);
    double sum=0;
    for(int i=1;i<=n;i++){
        printf("请输入第%d个学生的成绩：",i);
        scanf("%d",&a[i]);
        sum +=a[i];
    }
    printf("%d个学生平均分为：%.2lf",n,sum/(n*1.0));
}
```

####  T3:

```c
#include<stdio.h>
int a[105];
int mark[105];
int main(){
    int n;
    printf("请输入学生人数：");
    scanf("%d",&n);
    double sum=0;
    for(int i=0;i<=101;i++){
        mark[i]=0;
    }
    printf("请输入学生分数（0-100）：\n");
    for(int i=1;i<=n;i++){
        printf("请输入第%d个学生的成绩：",i);
        scanf("%d",&a[i]);
        sum +=a[i];
        mark[a[i]]++;
    }
    printf("%d个学生平均分为：%.2lf\n",n,sum/(n*1.0));
    printf("分数分布统计：\n");
    printf("分数       人数\n");
    printf("===============\n");
    for(int i=0;i<=100;i++){
        if(mark[i]!=0){
            printf("%d       %d\n",i,mark[i]);
        }
    }
}
```

###  循环：

####  T1：

```c
#include<stdio.h>
long long a=1;
int main(){
    printf("请输入一个非负整数：\n");
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        a*=i;
    }
    printf("%d!=%lld",n,a);
}
```

####  T2:

```c
#include<stdio.h>
int get_fibonacci(int n){
    int a=0;
    int b=1;
    if(n == 0) {
        printf("无");
        return 0;
    }
        
    else if( n == 1){
        printf("0");
        return 0;
    }

    else if (n == 2){
        printf("0 1");
        return 0;
    }
    else{
        n = n-2;
        printf("0 1 ");
        int c = a+b;
        a = b;
        b = c;
        while (n>=1){
            printf("%d ",c);
            a = b;
            b = c;
            c = a+b;
            n = n-1;
        }
            
    }
        
}
int main(){
    printf("请输入打印项数：");
    int nn;
    scanf("%d",&nn);
    printf("斐波那契数列前%d项为: ",nn);
    get_fibonacci(nn);
    
}

```

####  T3:（使用递归）

```c
#include <stdio.h>
long long factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    else {
        return n * factorial(n - 1);
    }
}
int main() {
    int num;
    printf("请输入一个非负整数: ");
    scanf("%d", &num);
    long long result = factorial(num);
    printf("%d! = %lld\n", num, result);
    return 0;
}
```

###  指针：

####  T1

```c
#include<stdio.h>
int main(){
    int num=10;
    int *ptr=&num;
    printf("num的值: %d\n",*ptr);
    printf("num的地址: %p\n",ptr);
    *ptr=20;
    printf("修改后num的值: %d\n",num);
    return 0;
}
```

####  T2:

```c
#include<stdio.h>
int main(){
    int arr[5]={1,2,3,4,5};
    int *ptr=arr;
    for(int i=0;i<5;i++){
        printf("arr[%d]=%d",i,*ptr);
        printf(",地址:%p\n",ptr);
        ptr++;
    }
return 0;
}
```

####  T3：

```
10
20
11
20
```