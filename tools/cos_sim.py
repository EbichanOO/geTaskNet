import numpy as np

def cos_sim(x, y):
    return np.dot(x, y) / (np.linalg.norm(x)*np.linalg.norm(y))