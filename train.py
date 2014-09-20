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
    for batch_no, batch in enumerate(db.mini_batches(100)):
        X, y = vectorize_batch(batch)
        model.partial_fit(X, y)
        if sampling and batch_no == 10:
            break
    return model

def vectorize(raw):
    return vectorize_batch([raw])

def vectorize_batch(batch):
    df = pd.DataFrame(batch)
    print df
    return (df.drop('price_change').values, df['price_change'].values)

def pickle(model):
    with open('trained_model.pickle', 'w') as f:
        cPickle.dump(model, f)

if __name__ == '__main__':
    sampling = True
    model = train()
    pickle(model)


