import numpy as np
import torch
from torch.utils.data import DataLoader
from sklearn.metrics import accuracy_score

# 导入自定义的数据预处理函数 'prep_data' 和模型定义 'Net'
from second_deeplearn.data import prep_data
from second_deeplearn.models import Net

# from model_file import Net  # 假设你的模型保存在一个名为 model_file.py 的文件中
# 从数据集中排除非数值列
model_data = prep_data.copy()

# 假设你的目标变量所在的列名是 'mh_disorder_current'
model_data = model_data[model_data['mh_disorder_current'] != 0]

# 选择数值类型的列
col_numeric = [cols for cols in model_data.columns if model_data[cols].dtype in ['int64', 'float64', 'int32', 'float32']]
model_data = model_data[col_numeric]

# 假设你的目标变量所在的列名是 'mh_disorder_current'，并将1映射为0，2映射为1
model_data['mh_disorder_current'] = model_data['mh_disorder_current'].replace({1: 0, 2: 1})

# 获取目标变量 'mh_disorder_current'
y = model_data['mh_disorder_current']

# 从特征中排除目标变量
cols = [col for col in model_data.columns if col not in ['mh_disorder_current']]
X = model_data[cols]

# 将数据转换为PyTorch的张量
X_test_tensor = torch.tensor(X.values, dtype=torch.float32)
y_test_tensor = torch.tensor(y.values.reshape(-1, 1), dtype=torch.float32)
# 加载模型
input_size = X_test_tensor.shape[1]  # 获取输入特征的维度
model = Net(input_size)  # 创建神经网络模型
model.load_state_dict(torch.load('trained_model.pth'))  # 请确保训练好的模型文件 'trained_model.pth' 位于相同目录下

# 设置模型为评估模式
model.eval()

# 创建数据加载器
test_loader = DataLoader(dataset=list(zip(X_test_tensor, y_test_tensor)), batch_size=50, shuffle=False)

# 用于保存测试结果的列表
predictions = []

# 迭代测试集
for images, labels in test_loader:
    # 前向传播得到预测结果
    output = model(images)
    predictions.extend(output.detach().numpy())  # 将预测结果添加到列表中

# 对预测结果进行后处理（如果需要）
predictions = (np.array(predictions) > 0.5).astype(int)  # 二分类问题，将概率值大于0.5的转换为1，否则为0

# 计算准确率
accuracy = accuracy_score(y, predictions)

print(f'准确率: {accuracy}')