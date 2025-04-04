import numpy as np
from scipy.stats import f, levene


def levene_test(*groups, center='median'):
    center = getattr(np, center)
    k = len(groups)
    N = sum(len(group) for group in groups)
    Z = [[abs(x-center(group)) for x in group] for group in groups]
    Zmean = np.mean(Z)

    num = (N-k) * sum(len(group)*(np.mean(z)-Zmean)**2 for z, group in zip(Z, groups))
    denum = (k-1) * sum((x-np.mean(z))**2 for z in Z for x in z)
    W = num/denum

    return W, f.sf(W, k-1, N-k)


if __name__=='__main__':
    from inputlib import input_table
    data = input_table(ragged=True)
    method = input('Enter the method to calculate the deviations: ')

    results = levene_test(*data, center=method)
    print(results)
    results = levene(*data, center=method)
    print('statistic={0.statistic}, pvalue={0.pvalue}'.format(results))
