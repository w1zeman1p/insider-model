from sklearn.linear_model import SGDClassifier
import numpy as np
import cPickle
import pandas as pd
import db

'''
id
cik
title
link
term
date
created_at
updated_at
ticker
document // this is a json blob see README for more deets
day_traded_price
plus_3_months_price
plus_6_months_price
plus_12_months_price
day_traded_volume
day_traded_market_cap
insider_id
file_id
company_id
'''
def train():
    model = SGDClassifier()
    all_classes = np.array([0, 1])
    for batch_no, batch in enumerate(db.mini_batches(100)):
        X, y = vectorize_batch(batch)
        model.partial_fit(X, y, classes = all_classes)
        if sampling and batch_no == 1000:
            break
    return model

def vectorize(raw):
    datum = [
      raw['sum_shares'],
      raw['sum_shares_after'],
      raw['day_traded_volume'],
      raw['day_traded_price'],
      raw['is_officer'],
      raw['is_director'],
      raw['is_ten_percent_owner'],
      raw['is_other'],
      raw['per_code_p'],
      raw['per_code_s'],
      raw['per_code_v'],
      raw['per_code_a'],
      raw['per_code_d'],
      raw['per_code_f'],
      raw['per_code_i'],
      raw['per_code_m'],
      raw['per_code_c'],
      raw['per_code_e'],
      raw['per_code_h'],
      raw['per_code_o'],
      raw['per_code_x'],
      raw['per_code_g'],
      raw['per_code_l'],
      raw['per_code_w'],
      raw['per_code_z'],
      raw['per_code_j'],
      raw['per_code_k'],
      raw['per_code_u']
    ]
    return datum

def vectorize_batch(batch):
    df = pd.DataFrame(data = batch, columns = [
        "price_change",
        "sum_shares",
        "sum_shares_after",
        "day_traded_volume",
        "day_traded_price",
        "is_officer",
        "is_director",
        "is_ten_percent_owner",
        "is_other",
        "per_code_p",
        "per_code_s",
        "per_code_v",
        "per_code_a",
        "per_code_d",
        "per_code_f",
        "per_code_i",
        "per_code_m",
        "per_code_c",
        "per_code_e",
        "per_code_h",
        "per_code_o",
        "per_code_x",
        "per_code_g",
        "per_code_l",
        "per_code_w",
        "per_code_z",
        "per_code_j",
        "per_code_k",
        "per_code_u"
    ])
    return (df.drop(['price_change'], axis = 1).values, df['price_change'].values)

def pickle(model):
    with open('trained_model.pickle', 'w') as f:
        cPickle.dump(model, f)

if __name__ == '__main__':
    sampling = True
    model = train()
    pickle(model)
