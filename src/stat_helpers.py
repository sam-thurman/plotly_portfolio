import numpy as np
import pandas as pd
import sklearn

def get_high_target_corrs(correlation):
    t = correlation.target
    ti = t.index
    high_corr = []
    for i in range(len(t)):
        if (abs(t[i]) > 0.5) and (ti[i] != 'target'):
            high_corr.append((ti[i], t[i]))
    return high_corr