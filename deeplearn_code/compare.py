# ----------- ENCODING -----------
# Split data into 2 datasets: one that needs to be encoded, one that doesnt need to
cols = [x for x in imp_data.columns if x not in ['age', 'why/why_not', 'why/why_not2', 'country_live',
                                                 'live_us_teritory', 'country_work', 'work_us_teritory',
                                                 'work_position']]

data_to_encode = imp_data[cols]
data_not_encode = imp_data[['why/why_not', 'why/why_not2', 'country_live',
                            'live_us_teritory', 'country_work', 'work_us_teritory', 'work_position']]

# Importing OneHotEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder


def encode(data):
    cat_columns = list(data.select_dtypes(include=['category', 'object']))
    column_mask = []

    for column_name in list(data.columns.values):
        column_mask.append(column_name in cat_columns)

    le = LabelEncoder()
    for col in cat_columns:
        data[col] = le.fit_transform(data[col])

    # ohe = OneHotEncoder(categorical_features=column_mask)
    # data = ohe.fit_transform(data)
    # 创建一个用于编码分类变量的OneHotEncoder对象。
    ohe = OneHotEncoder(drop=None, sparse=False)
    # 创建一个ColumnTransformer，它将OneHotEncoder应用于分类列，并保持非分类列不变。
    ct = ColumnTransformer(
        transformers=[
            ('encoder', ohe, column_mask)
        ],
        remainder='passthrough'
    )
    # 将列转换器应用于数据，对分类列进行编码，保持其余列不变。
    data_encoded = ct.fit_transform(data)

    return data


encode(data_to_encode)
matrix = encode(data_to_encode)
encoded_data = pd.DataFrame(matrix)  # to dataframe
encoded_data.columns = data_to_encode.columns

# Preprocessed data
prep_data = pd.concat(objs=[encoded_data, data_not_encode], axis=1)