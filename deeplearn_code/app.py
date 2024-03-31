from flask import Flask, request, jsonify
from flask_cors import CORS
import torch

from second_deeplearn.inputAndOutput import predict_mental_health
app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Replace this with the path to your trained Python model
# You may need to adapt this depending on the type of model you have
# and how it is serialized or loaded.
# For example, if it's a machine learning model, you might use a library like joblib or pickle to load it.
# If it's a deep learning model, you might use a library like TensorFlow or PyTorch.
# Import and load your model here.

@app.route('/predict', methods=['POST'])
def predict():
    try:
        json_data = request.get_json(force=True)
        # Extract the numeric values from the JSON data
        numeric_values = [float(value) if '.' in value else int(value) for value in json_data.values() if
                          value and (value.replace('.', '', 1).isdigit() or (value[0] == '-' and value[1:].isdigit()))]
        # 删掉mh_disorder_current列，因为这个应该是预测值
        del numeric_values[-8]
        # 这里因为teach_flag数据还没有传过来，先给它一个假的值
        numeric_values[-2]=1
        # Convert the numeric values to PyTorch tensor
        tensor_data = torch.tensor([numeric_values], dtype=torch.float32)
        # 将 tensor_data 重新形状为所需形式（一维张量）
        tensor_data = tensor_data.view(-1)
        # 暂时输入用的excel表格的第三行数据
        # print(X_test_tensor[2])
        # print(len(X_test_tensor[2]))
        # print(tensor_data)
        # print(len(tensor_data))
        sample_data = torch.tensor(tensor_data, dtype=torch.float32).unsqueeze(0)  # 添加 batch 维度
        # 进行预测
        result = predict_mental_health(sample_data)
        if(result):
            print("yes")
        else:
            print("no")

        # Replace this with your actual model prediction logic
        # Make sure to adapt this to how you've loaded or trained your model
        # predict_with_your_model(text_data)
        response = {
            'result': result
        }
        return jsonify(response)
    except Exception as e:
        print(str(e))  # 添加调试语句
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
