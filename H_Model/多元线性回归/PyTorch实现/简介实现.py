import torch
from torch import nn
import torch.utils.data as Data
from torch.nn import init
import torch.optim as optim
torch.manual_seed(1) # 随机数种子


num_inputs = 2
num_examples = 1000
true_w = [2, -3.4]
true_b = 4.2
features = torch.normal(0, 1, size=(num_examples, num_inputs))
labels = true_w[0] * features[:, 0] + true_w[1] * features[:, 1] + true_b
labels += torch.normal(0, 0.01, size=labels.size()) # 添加噪音

batch_size = 10
dataset = Data.TensorDataset(features, labels) # 包装数据集

# 把 dataset 放入 DataLoader
data_iter = Data.DataLoader(
    dataset=dataset,
    batch_size=batch_size,
    shuffle=True,
    num_workers=2 # how many subprocesses to use for data loading. 0 means that the data will be loaded in the main process. (default: 0)
)


class LinearNet(nn.Module):
    def __init__(self, n_feature):
        super(LinearNet, self).__init__()
        self.linear = nn.Linear(n_feature, 1)

    def forward(self, x):
        y = self.linear(x)
        return y


net = LinearNet(num_inputs)

# 初始化模型参数
init.normal_(net.linear.weight, mean=0.0, std=0.01)
init.constant_(net.linear.bias, val=0.0)

loss = nn.MSELoss() # 损失函数为均方误差


optimizer = optim.SGD(net.parameters(), lr=0.03) # 优化器
num_epochs = 20 # 最大训练轮数


if __name__ == '__main__':
    for epoch in range(1, num_epochs + 1):
        l = 0
        for X, y in data_iter: # 多进程需要在main函数中运行
            output = net(X)
            l = loss(output, y.view(-1, 1))
            optimizer.zero_grad()
            l.backward()
            optimizer.step()
        print('epoch %d, loss: %f' % (epoch, l.item()))

        if l < 0.0001:
            break


    # 预测参数与真实参数对比
    print(true_w, net.linear.weight.data)
    print(true_b, net.linear.bias.data)