# 导入所需的库
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tqdm import tqdm

# 导入自定义的数据预处理函数 'prep_data'，这里假设它是可用的
from second_deeplearn.data import prep_data
from second_deeplearn.models import Net

# 从数据集中排除非数值列
model_data = prep_data.copy()

# 假设你的目标变量所在的列名是 'mh_disorder_current'
model_data = model_data[model_data['mh_disorder_current'] != 0]

# 选择数值类型的列
col_numeric = [cols for cols in model_data.columns if model_data[cols].dtype in ['int64', 'float64', 'int32', 'float32']]
model_data = model_data[col_numeric]

# 假设你的目标变量所在的列名是 'mh_disorder_current'，并将1映射为0，2映射为1
model_data['mh_disorder_current'] = model_data['mh_disorder_current'].replace({1: 0, 2: 1})

# 'model_data' 是用于预测变量 'mh_disorder_current' 的新数据集
# 特征变量和目标变量

# 获取目标变量 'mh_disorder_current'
y = model_data['mh_disorder_current']

# 从特征中排除目标变量
cols = [col for col in model_data.columns if col not in ['mh_disorder_current']]
X = model_data[cols]

# 数据验证，将数据集分成训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 将数据转换为PyTorch的张量
X_train_tensor = torch.tensor(X_train.values, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train.values.reshape(-1, 1), dtype=torch.float32)

# 创建数据加载器
train_loader = torch.utils.data.DataLoader(dataset=list(zip(X_train_tensor, y_train_tensor)), batch_size=50, shuffle=True)


# 实例化模型、定义损失函数和优化器
input_size = X_train_tensor.shape[1]  # 获取输入特征的维度
model = Net(input_size)  # 创建神经网络模型
criterion = nn.BCELoss()  # 二分类交叉熵损失
optimizer = optim.Adam(model.parameters(), lr=0.001)  # Adam优化器，学习率为0.001

# 训练模型
total_step = len(train_loader)  # 计算训练集数据加载器的总步数

for epoch in range(100):
    for i, (images, labels) in enumerate(train_loader):
        optimizer.zero_grad()  # 重置梯度
        output = model(images)  # 通过模型前向传播得到预测结果
        loss = criterion(output, labels)  # 计算损失
        loss.backward()  # 反向传播计算梯度
        optimizer.step()  # 更新模型参数

        if ((epoch+1)%20==0) and ((i+1) % 4 == 0):
            print ('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}'.format(epoch+1, 100, i+1, total_step, loss.item()))

# 在训练完成后，添加以下代码以保存模型
torch.save(model.state_dict(), 'trained_model.pth')


# 在测试集上评估模型
with torch.no_grad():
    X_test_tensor = torch.tensor(X_test.values, dtype=torch.float32)
    y_test_tensor = torch.tensor(y_test.values.reshape(-1, 1), dtype=torch.float32)
    predictions = model(X_test_tensor)  # 使用训练好的模型进行预测
    predictions = (predictions > 0.5).float()  # 将概率值大于0.5的转换为1，否则为0
    accuracy = (predictions == y_test_tensor).sum().item() / len(y_test)  # 计算准确率

print(f'准确率: {accuracy}')  # 打印测试集上的准确率
# 准确率: 0.8408304498269896
