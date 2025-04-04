import numpy as np
from scipy.stats import chi2, bartlett


def bartlett_test(*groups):
    k = len(groups)
    N = sum(len(group) for group in groups)
    pooled_var = sum((len(group)-1)*np.var(group, ddof=1) for group in groups) / (N-k)

    num = (N-k)*np.log(pooled_var) - sum((len(group)-1)*np.log(np.var(group, ddof=1)) for group in groups)
    denum = 1 + 1/(3*(k-1)) * sum(1/(len(group)-1) - 1/(N-k) for group in groups)
    T = num/denum

    return T, chi2.sf(T, k-1)


if __name__=='__main__':
    from inputlib import input_table
    data = input_table(ragged=True)

    results = bartlett_test(*data)
    print(results)
    results = bartlett(*data)
    print('statistic={0.statistic}, pvalue={0.pvalue}'.format(results))
