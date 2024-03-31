import numpy as np
import torch
from second_deeplearn.data import prep_data
from second_deeplearn.models import Net
# 从数据集中排除非数值列
model_data = prep_data.copy()
# model_data.to_excel('model_data.xlsx', index=False)
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

# 提取第3行数据
sample_data = torch.tensor(X_test_tensor[2], dtype=torch.float32).unsqueeze(0)  # 添加 batch 维度

# 进行预测
with torch.no_grad():
    output = model(sample_data)
    prediction = (output > 0.5).item()  # 将概率值大于0.5的转换为1，否则为0，并获取预测结果

if prediction:
    print('预测结果:  Having mental health disorders')
else:
    print('预测结果:  No mental health disorders')
# True为预测有精神疾病
