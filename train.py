from sklearn.linear_model import SGDClassifier
import numpy as np
import cPickle

import db

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
    return (df.drop('price_change').values, df['price_change'].values)

def pickle(model):
    with open('trained_model.pickle', 'w') as f:
        cPickle.dump(model, f)

if __name__ == '__main__':
    sampling = True
    model = train()
    pickle(model)


