from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier, XGBRFClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, roc_curve
from sklearn import preprocessing

from second_deeplearn.data import prep_data

# 从数据集中排除非数值列
model_data = prep_data.copy()

# 选择数值类型的列
col_numeric = [cols for cols in model_data.columns if model_data[cols].dtype in ['int64', 'float64', 'int32', 'float32']]
model_data = model_data[col_numeric]
# 'model_data' 是用于预测变量 'mh_disorder_current' 的新数据集
# 特征变量和目标变量
y = model_data['mh_disorder_current']
# 从特征中排除目标变量
cols = [col for col in model_data.columns if col not in ['mh_disorder_current']]
X = model_data[cols]

# 数据验证
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 预定义函数
def model_assess(model, name='默认'):
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print('---', name, '---', '\n',
          confusion_matrix(y_test, preds), '\n',
          '准确率:', round(accuracy_score(y_test, preds), 5), '\n')

# 神经网络
nn = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(150, 10), random_state=1)
model_assess(nn, '神经网络')