
#ps这一道题的学习率太大了，导致我调试1000次时w和b的偏差极其大，检查了很久
#搞成0.01时是非常接近2,0的。
import random
from typing import List, Any

data = [
    (1, 2),
    (2, 4),
    (3, 6),
    (4, 8),
    (5, 10)
]
def count_cost(pre_y,true_y,lenn):
    return ((pre_y-true_y)**2)/lenn
def count_gradient(pre_y,true_y,lenn):
    return  (pre_y-true_y)/lenn*2
# //要求实现的函数

def gradient_descent(data:List[Any], w_init:float, b_init:float, lr:float, steps:int,mode):#定义mode1为随机，mode2为batch
    
    datalen=len(data)
    if mode == 2:
        print("请输入想要的size:(请不要超过5)")
        batch_size=int(input())
    
    for j in range(steps):
        sum_loss=0
        gw=0
        bw=0
        if mode == 1:#随机
            choose=[random.randint(0,datalen-1)]
        else:#batch
            choose=random.sample(range(datalen), batch_size)
        lenn=len(choose)    
        for i in choose:
            y_pre=w_init*data[i][0]+b_init
            y_true=data[i][1]
            loss=count_cost(y_pre,y_true,lenn)
            sum_loss+=loss
            gw+=count_gradient(y_pre,y_true,lenn)*data[i][0]
            bw+=count_gradient(y_pre,y_true,lenn)
        w_init-=lr*gw
        b_init-=lr*bw
        print(f"第{j}次，损失为{sum_loss:.4f}，w为{w_init:.4f},b为{b_init:.4f}")
    return w_init,b_init
gradient_descent(data,0.0,0.0,0.1,5,2)

            



   