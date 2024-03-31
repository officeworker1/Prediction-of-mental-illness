import torch
from second_deeplearn.data import prep_data
from second_deeplearn.models import Net
def predict_mental_health(sample_data, model_path='trained_model.pth'):
    # 加载模型
    input_size = sample_data.shape[1]  # 获取输入特征的维度
    model = Net(input_size)  # 创建神经网络模型
    model.load_state_dict(torch.load(model_path))  # 请确保训练好的模型文件 'trained_model.pth' 位于相同目录下

    # 设置模型为评估模式
    model.eval()
    # 进行预测
    with torch.no_grad():
        output = model(sample_data)
        prediction = (output > 0.5).item()  # 将概率值大于0.5的转换为1，否则为0，并获取预测结果

    return prediction