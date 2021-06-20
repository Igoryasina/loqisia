from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
import pandas as pd

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)

excel = pd.read_excel('Список_курсов_2020_id.xls', index_col=0)  
excel2 = pd.read_excel('Рефлексия_ПЦС-2020.xls', index_col=0)  


# print(excel[:5])
# print(excel2[:5])

common_idx = excel.index.intersection(excel2.index)
excel = excel.loc[common_idx]
excel2 = excel2.loc[common_idx]

verdicts_q1 = model.predict(sentences=excel2['REFLEXION_3'].values, k=2)
v_dict = {'id': []}
for i, d in enumerate(verdicts_q1):
    skipped_ks = [k for k in v_dict.keys() if k not in d and k != 'id']
    for k in skipped_ks:
        v_dict[k].append(0)
    for k in d.keys():
        if k in v_dict:
            v_dict[k].append(d[k])
        else:
            v_dict[k] = [0]*(i + 1)
    v_dict['id'].append(excel2.index[i])
verdicts_q1_df = pd.DataFrame(v_dict)
print(verdicts_q1_df[:5])

excel2 = verdicts_q1_df.groupby('id').agg('mean')
print(excel.columns)
print(excel2.columns)

excel = pd.concat([excel, excel2], axis=1)

print(excel[:5])

excel.loc[:, ['Провайдер', 'neutral', 'skip', 'negative', 'positive', 'speech']].to_csv('university_reviews.csv', sep=',', encoding='utf-8')
