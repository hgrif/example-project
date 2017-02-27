import numpy as np
import pandas as pd


def generate(n):
    noise = np.random.randn(n)
    df = pd.DataFrame({
        'time': range(0, n),
    })
    df['profit'] = (df['time'] ** 2) + noise
    return df
