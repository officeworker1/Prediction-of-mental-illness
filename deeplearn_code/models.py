import torch
import torch.nn as nn

class Net(nn.Module):
    def __init__(self, input_size):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)  # 输入层到隐藏层，使用64个神经元
        self.fc2 = nn.Linear(64, 1)  # 隐藏层到输出层，输出1个值
        self.sigmoid = nn.Sigmoid()  # 使用Sigmoid激活函数

    def forward(self, x):
        x = torch.relu(self.fc1(x))  # 使用ReLU激活函数
        x = self.fc2(x)
        x = self.sigmoid(x)
        return x
