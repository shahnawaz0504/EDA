import numpy as np
from scipy.stats import t, spearmanr


def get_ranks(data):
    accum_idx = []
    indices = np.argsort(data)
    ranks = np.argsort(indices).astype(type) + 1

    for i in range(len(indices)):
        accum_idx.append(indices[i])
        if i!=(len(indices)-1) and data[indices[i]]==data[indices[i+1]]:
            continue
        ranks[accum_idx] = np.mean(ranks[accum_idx])
        accum_idx.clear()

    return ranks


def spearman_test(data1, data2, alternative='two-sided'):
    n = len(data1)
    ranks1 = get_ranks(data1)
    ranks2 = get_ranks(data2)
    covariance = sum((x-np.mean(ranks1))*(y-np.mean(ranks2))
        for x, y in zip(ranks1, ranks2, strict=True)) / n

    r = covariance/(np.std(ranks1)*np.std(ranks2))
    T = r * ((n-2)/(1-r**2))**(1/2)

    if alternative=='two-sided':
        return r, 2*min(t.cdf(T, n-2), t.sf(T, n-2))
    elif alternative=='greater':
        return r, t.sf(T, n-2)
    elif alternative=='less':
        return r, t.cdf(T, n-2)
    else:
        raise ValueError("alternative must be 'less', 'greater' or 'two-sided'")


if __name__=='__main__':
    from inputlib import input_data
    print('Sample 1:')
    data1 = input_data()
    print('Sample 1:')
    data2 = input_data()
    alt = alt if (alt:=input('Enter the type of test: ')) else 'two-sided'

    results = spearman_test(data1, data2, alternative=alt)
    print(results)
    results = spearmanr(data1, data2, alternative=alt)
    print('statistic={0.statistic}, pvalue={0.pvalue}'.format(results))
