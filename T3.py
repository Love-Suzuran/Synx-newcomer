import torch
import numpy as np
import random
def synthetic_data(w, b, num_examples):#真实w，真实b，生成数量
    x = torch.normal(0, 1, (num_examples, len(w)))
    # 从均值为0，标准差为1的正态分布中生成数据
    y = torch.matmul(x, w) + b
    # 2. 计算真实的标签值（无噪声）
    y += torch.normal(0, 0.01, y.shape)
    # 3. 添加噪声
    return x, y.reshape((-1, 1))
    # 确保y是列向量的形式

def linreg(x, w, b):#应该使用矩阵乘法，改这里找了很久才找到问题
    return torch.matmul(x, w.reshape(-1, 1)) + b
def squared_loss(y_hat, y):
    return (y_hat-y)**2
def count_gradient(pre_y,true_y,lenn):
    return  (pre_y-true_y)/lenn*2
def data_iter(batch_size, features, labels):
    num_len=len(features)
    choose=list(range(num_len))
    random.shuffle(choose)
    for i in range(0, num_len, batch_size):
        batch_indices = choose[i:min(i + batch_size, num_len)]#批次起始点到批次终止点
        batch_features = features[batch_indices]
        batch_labels = labels[batch_indices]
        yield batch_features, batch_labels#每次返回一次批次，所以用yield
def sgd(params, lr, batch_size):
    with torch.no_grad():
        for param in params:
            param -= lr * param.grad
            param.grad.zero_()
def train():
    true_w = torch.tensor([11.0,4.0,5.0])
    true_b = 1.4
    w= torch.tensor([0.0,0.0,0.0],requires_grad=True)
    b= torch.tensor(0.0,requires_grad=True)       
#  114514你发现了吗awa
    features, labels = synthetic_data(true_w, true_b, 1000)
    steps=100
    lr=0.01
    print("请输入您想要的batch_size:")
    siz=int(input())
    for j in range(steps):
        epoch_loss=0.0
        counts=0
        for batch_x,batch_y in data_iter(siz,features,labels):#每次获取一组，每一组分别计算awa
            pre_y=linreg(batch_x,w,b)
            true_y=batch_y
            loss=squared_loss(pre_y,true_y)
            loss.sum().backward()
            epoch_loss+=loss.mean().item()
            counts+=1
            sgd([w,b],lr,siz)
        #avg_loss = epoch_loss / batch_count
        #rain_losses.append(avg_loss)可视化，先不写
        print(f"训练损失:{epoch_loss / counts:.4f}")
    print(f"最后训练函数：w1={w[0]:.4f},w2={w[1]:.4f},w3={w[2]:.4f},b={b:.4f}")
train()
    
        
        
        



    




