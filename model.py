# Used in production to predict on new examples
# Should only use `predict` method

import cPickle
import numpy as np
import train

def __load_model__():
    # Ensure model is only unpickled once
    __load_model__.counter += 1
    assert __load_model__.counter <= 1

    with open('trained_model.pickle', 'r') as f:
        model = cPickle.load(f)

    print "Loaded model"

    return model
__load_model__.counter = 0

class __Model__(object):
    model = __load_model__()

    def vectorize(self, raw_data):
        return train.vectorize(raw_data)

    def predict(self, data):
        return self.model.predict(data)

# Global model
model = __Model__()

def predict(data):
    vectorized = train.vectorize(data)
    return model.predict(vectorized)

