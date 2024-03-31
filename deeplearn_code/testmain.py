# 示例用法
# 提取第3行数据
import torch

from second_deeplearn.inputOnceTest import X_test_tensor
from second_deeplearn.inputAndOutput import predict_mental_health

sample_data = torch.tensor(X_test_tensor[2], dtype=torch.float32).unsqueeze(0)  # 添加 batch 维度
print(len(X_test_tensor[2]))
# 进行预测
result = predict_mental_health(sample_data)

if result:
    print('预测结果:  Having mental health disorders')
else:
    print('预测结果:  No mental health disorders')