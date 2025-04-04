'''
from scipy.stats import f, f_oneway
import numpy as np

def f_Oneway(*groups, unbalanced=True):
    all_factors = [data for factor in groups for data in factor] if unbalanced else groups
    N = len(all_factors) if unbalanced else len(groups)*len(groups[0])

    SST = N*np.var(all_factors)
    SSW = sum(len(groups)*np.var(factor) for factor in groups)
    SSB = SST-SSW

    DFB = len(groups)-1
    DFW = N-len(groups)
    DFT = N-1

    MSW = SSW/DFW
    MSB = SSB/DFB
    
    F_ratio = MSB/MSW
    p_value = f.sf(F_ratio, DFB, DFW)

    print(" Source  |       SS      |     DF        |       MS      |       F-ratio |    P Value    |")
    print(f"Between |   {SSB:.8f}   |   {DFB:.4f}   |   {MSB:.8f}   |   {F_ratio}   |   {p_value}   |")

f_Oneway([1,2,3,4], [5,6,7,8], [9,10,11,12])



def input_data(n=None, dtype=float):
    data = []
    i = 0
    while True:
        if len(data) == n: return data
        inp = input(f'Enter element {i+1} - ')
        if not inp and n is None: return data
        data.append(dtype(inp))
        i += 1
    return data

def input_table(r=None, c=None, ragged=False, dtype=float):
    print("Row 1:")
    row1 = input_data(c, dtype=dtype)
    table = [row1]
    c_new = c if ragged else len(row1)
    while True:
        try:
            if len(table)==r: return table
            print(f'Row {len(table)+1}:')
            row = input_data(c_new, dtype=dtype)
            if not row and c is None: return table
            table.append(row)
        except ValueError as e:
            if r is c is None: return table
            else: raise e

'''
import numpy as np
from scipy.stats import f, levene
def levene_test(*samples, center="median"):
    center = getattr(np, center)
    k = len(samples)
    N = sum(len(sample) for sample in samples)
    Z = [[(abs(x-center(sample))) for x in sample] for sample in samples]
    Zmean = np.mean(Z)

    num = (N-k)*sum(len(sample)*((np.mean(z)-Zmean)**2) for z, sample in zip(Z, samples))
    denom = (k-1)*sum((x-np.mean(z)) for z in Z for x in z)
    W = num/denom

    return W, f.sf(W, k-1, N-k)

