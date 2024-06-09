import numpy as np

def calculate(list):
    arr = np.array(list).reshape(3,3)
    calculations = {'mean':[arr.mean(axis=0), arr.mean(axis=1), arr.mean()],
                    'variance':[arr.var(axis=0), arr.var(axis=1), arr.var()],
                    'standard deviation':[arr.std(axis=0), arr.std(axis=1), arr.std()],
                    'max':[arr.max(axis=0), arr.max(axis=1), arr.max()],
                    'min':[arr.min(axis=0), arr.min(axis=1), arr.min()],
                    'sum':[arr.sum(axis=0), arr.sum(axis=1), arr.sum()]}
    return calculations


data = calculate([0,1,2,3,4,5,6,7,8])
print(data)
