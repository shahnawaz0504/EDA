import numpy as np
from scipy.stats import norm, kendalltau


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


def kendalls_tau(data1, data2, alternative='two-sided'):
    n = len(data1)
    indices = np.argsort(data1)
    ranks = get_ranks(np.take(data2, indices))

    C = D = 0
    for i in range(len(ranks)):
        for j in range(i+1, len(ranks)):
            if ranks[i]<ranks[j]:
                C += 1
            elif ranks[i]>ranks[j]:
                D += 1
            else:
                C += 0.5
                D += 0.5

    tau = (C-D) / (C+D)
    dist = norm(0, ((2*(2*n+5))/(9*n*(n-1)))**(1/2))

    if alternative=='two-sided':
        return tau, 2*min(dist.cdf(tau), dist.sf(tau))
    elif alternative=='greater':
        return tau, dist.sf(tau)
    elif alternative=='less':
        return tau, dist.cdf(tau)
    else:
        raise ValueError("alternative must be 'less', 'greater' or 'two-sided'")


if __name__=='__main__':
    from inputlib import input_data
    print('Sample 1:')
    data1 = input_data()
    print('Sample 1:')
    data2 = input_data()
    alt = alt if (alt:=input('Enter the type of test: ')) else 'two-sided'

    results = kendalls_tau(data1, data2, alternative=alt)
    print(results)
    results = kendalltau(data1, data2, method='asymptotic', alternative=alt)
    print('statistic={0.statistic}, pvalue={0.pvalue}'.format(results))
