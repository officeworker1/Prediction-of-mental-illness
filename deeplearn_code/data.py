# 导入必要的库
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
import warnings

from sklearn.preprocessing import OneHotEncoder, LabelEncoder

warnings.filterwarnings('ignore')

# 导入数据
survey_2016 = pd.read_csv("mental-heath-in-tech-2016_20161114.csv")

# ----------- 数据清理 -----------
# 对列名进行修改
# 原列名列表
renamed_columns = ['self_empl_flag', 'comp_no_empl', 'tech_comp_flag', 'tech_role_flag', 'mh_coverage_flag',
                  'mh_coverage_awareness_flag', 'mh_employer_discussion', 'mh_resources_provided', 'mh_anonimity_flag',
                  'mh_medical_leave', 'mh_discussion_neg_impact', 'ph_discussion_neg_impact', 'mh_discussion_cowork',
                  'mh_discussion_supervis', 'mh_eq_ph_employer', 'mh_conseq_coworkers', 'mh_coverage_flag2', 'mh_online_res_flag',
                  'mh_diagnosed&reveal_clients_flag', 'mh_diagnosed&reveal_clients_impact', 'mh_diagnosed&reveal_cowork_flag', 'mh_cowork_reveal_neg_impact',
                  'mh_prod_impact', 'mh_prod_impact_perc', 'prev_employers_flag', 'prev_mh_benefits', 'prev_mh_benefits_awareness',
                  'prev_mh_discussion', 'prev_mh_resources', 'prev_mh_anonimity', 'prev_mh_discuss_neg_conseq', 'prev_ph_discuss_neg_conseq',
                  'prev_mh_discussion_cowork', 'prev_mh_discussion_supervisor', 'prev_mh_importance_employer', 'prev_mh_conseq_coworkers',
                  'future_ph_specification', 'why/why_not', 'future_mh_specification', 'why/why_not2', 'mh_hurt_on_career', 'mh_neg_view_cowork',
                  'mh_sharing_friends/fam_flag', 'mh_bad_response_workplace', 'mh_for_others_bad_response_workplace', 'mh_family_hist',
                  'mh_disorder_past', 'mh_disorder_current', 'yes:what_diagnosis?', 'maybe:whats_your_diag', 'mh_diagnos_proffesional',
                  'yes:condition_diagnosed', 'mh_sought_proffes_treatm', 'mh_eff_treat_impact_on_work', 'mh_not_eff_treat_impact_on_work',
                  'age', 'sex', 'country_live', 'live_us_teritory', 'country_work', 'work_us_teritory', 'work_position', 'remote_flag']
survey_2016.columns = renamed_columns

# 性别列重新编码
survey_2016['sex'].replace(to_replace = ['Male', 'male', 'Male ', 'M', 'm',
       'man', 'Cis male', 'Male.', 'male 9:1 female, roughly', 'Male (cis)', 'Man', 'Sex is male',
       'cis male', 'Malr', 'Dude', "I'm a man why didn't you make this a drop down question. You should of asked sex? And I would of answered yes please. Seriously how much text can this take? ",
       'mail', 'M|', 'Male/genderqueer', 'male ',
       'Cis Male', 'Male (trans, FtM)',
       'cisdude', 'cis man', 'MALE'], value = 1, inplace = True)

survey_2016['sex'].replace(to_replace = ['Female', 'female', 'I identify as female.', 'female ',
       'Female assigned at birth ', 'F', 'Woman', 'fm', 'f', 'Cis female ', 'Transitioned, M2F',
       'Genderfluid (born female)', 'Female or Multi-Gender Femme', 'Female ', 'woman', 'female/woman',
       'Cisgender Female', 'fem', 'Female (props for making this a freeform field, though)',
       ' Female', 'Cis-woman', 'female-bodied; no feelings about gender',
       'AFAB'], value = 2, inplace = True)

survey_2016['sex'].replace(to_replace = ['Bigender', 'non-binary', 'Other/Transfeminine',
       'Androgynous', 'Other', 'nb masculine',
       'none of your business', 'genderqueer', 'Human', 'Genderfluid',
       'Enby', 'genderqueer woman', 'mtf', 'Queer', 'Agender', 'Fluid',
       'Nonbinary', 'human', 'Unicorn', 'Genderqueer',
       'Genderflux demi-girl', 'Transgender woman'], value = 3, inplace = True)

# 重新简化和更改一些标签
survey_2016['comp_no_empl'].replace(to_replace = ['More than 1000'], value = '>1000', inplace = True)
survey_2016['country_live'].replace(to_replace = ['United States of America'], value = 'USA', inplace = True)
survey_2016['country_live'].replace(to_replace = ['United Kingdom'], value = 'UK', inplace = True)
survey_2016['country_work'].replace(to_replace = ['United States of America'], value = 'USA', inplace = True)
survey_2016['country_work'].replace(to_replace = ['United Kingdom'], value = 'UK', inplace = True)

# 最大年龄323岁，最小年龄3岁。
# 处理异常值：(3岁、15岁、99岁、323岁)。
# 取平均值作为他们的年龄
mean_age = survey_2016[(survey_2016['age'] >= 18) | (survey_2016['age'] <= 75)]['age'].mean()
survey_2016['age'].replace(to_replace = survey_2016[(survey_2016['age'] < 18) | (survey_2016['age'] > 75)]['age'].tolist(),
                          value = mean_age, inplace = True)

# ----------- 处理缺失值 -----------
# 绘制缺失值热力图
plt.figure(figsize = (16,4))
sns.heatmap(data = survey_2016.isna());

# 由于问卷有 1433 行数据，我们首先将删除超过一半观测值为缺失的所有列
cols = (survey_2016.isna().sum() >= survey_2016.shape[0]/2).tolist()
to_drop = survey_2016.columns[cols]
survey_2016.drop(labels = to_drop, axis = 1, inplace = True)

# 处理其他缺失值
from sklearn.impute import SimpleImputer

# 使用众数填充缺失值
imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imp.fit(survey_2016)
imp_data = pd.DataFrame(data = imp.transform(survey_2016), columns = survey_2016.columns)

# ----------- 编码 -----------
# 将数据分为需要编码和不需要编码的两个数据集
cols = [x for x in imp_data.columns if x not in ['age', 'why/why_not', 'why/why_not2', 'country_live',
       'live_us_teritory', 'country_work', 'work_us_teritory', 'work_position']]

data_to_encode = imp_data[cols]
data_not_encode = imp_data[['why/why_not', 'why/why_not2', 'country_live',
       'live_us_teritory', 'country_work', 'work_us_teritory', 'work_position']]

# 引入
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
    data = ct.fit_transform(data)

    return data


encode(data_to_encode)
matrix = encode(data_to_encode)
encoded_data = pd.DataFrame(matrix)  # to dataframe
encoded_data.columns = data_to_encode.columns

# Preprocessed data
prep_data = pd.concat(objs=[encoded_data, data_not_encode], axis=1)

# ----------- 其他变更 -----------
# 一共有 53 个国家
# 其中大多数受访者来自美国、英国、加拿大、德国、荷兰和澳大利亚
# 通常情况下，为了样本能够足够代表总体，样本大小需要按照惯例>30。
# 由于受访者在回答时不能被平等对待（不同的背景、文化等），我们将排除所有受访者数小于30的国家。
# 因为受访者数>30的国家都比较相似（经济发达、生活水准相似），所以某些分析将把所有国家视为一个整体。

# 保留只有受访者数>30的国家
imp_data = imp_data[imp_data['country_work'].isin(['USA', 'UK', 'Canada', 'Germany', 'Netherlands', 'Australia'])]
imp_data = imp_data[imp_data['country_live'].isin(['USA', 'UK', 'Canada', 'Germany', 'Netherlands', 'Australia'])]

prep_data = prep_data[prep_data['country_work'].isin(['USA', 'UK', 'Canada', 'Germany', 'Netherlands', 'Australia'])]
prep_data = prep_data[prep_data['country_live'].isin(['USA', 'UK', 'Canada', 'Germany', 'Netherlands', 'Australia'])]

# 这段代码大概功能就是把work_position列含有Back-end,Front-end等等这样的词的标记为1，其余的标记为0，并且这个列叫做tech-flag列
# 由于 tech_flag 列中有大量缺失值，我们将需要映射 'work_position' 列（最初没有任何缺失值）
# 创建包含技术类职位的列表
tech_list = []
tech_list.append(imp_data[imp_data['work_position'].str.contains('Back-end')]['work_position'].tolist())
tech_list.append(imp_data[imp_data['work_position'].str.contains('Front-end')]['work_position'].tolist())
tech_list.append(imp_data[imp_data['work_position'].str.contains('Dev')]['work_position'].tolist())
tech_list.append(imp_data[imp_data['work_position'].str.contains('DevOps')]['work_position'].tolist())

# 一维化列表嵌套列表结构（它是一个嵌套列表），然后删除重复值
flat_list = [item for sublist in tech_list for item in sublist]
flat_list = list(dict.fromkeys(flat_list))

# 创建一个新列并对其重新编码
imp_data['tech_flag'] = imp_data['work_position']
imp_data['tech_flag'].replace(to_replace=flat_list, value=1, inplace=True)

# 其他条目 - 非技术类
remain_list = imp_data['tech_flag'].unique()[1:].tolist()

imp_data['tech_flag'].replace(to_replace=remain_list, value=0, inplace=True)

# 对 prep_data 做同样的处理
# 创建一个新列并对其重新编码
prep_data['tech_flag'] = prep_data['work_position']
prep_data['tech_flag'].replace(to_replace=flat_list, value=1, inplace=True)

# 其他条目 - 非技术类
prep_data['tech_flag'].replace(to_replace=remain_list, value=0, inplace=True)
# prep_data.to_excel("processed_data.xlsx", index=False)

# y = prep_data['mh_disorder_current']
# print(y)