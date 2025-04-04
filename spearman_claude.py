import numpy as np
from scipy.stats import t, spearmanr, rankdata

data_x = [56, 75,45,	71,	62,	64,	58,	80,	76,	61]
data_y = [66, 70,40,	60,	65,	56,	59,	77,	67,	63]

def spearman_rank_corr_test(x, y, alternative='two-sided'):

    x = np.array(x)
    y = np.array(y)
    if len(x) != len(y):
        raise ValueError("Input arrays must have the same length")

    rank_x = rankdata(x)
    rank_y = rankdata(y)
    d = rank_x - rank_y
    n = len(x)
    r = 1 - (6 * np.sum(d**2)) / (n * (n**2 - 1))

    T = r * ((n-2)/(1-r**2))**(1/2)

    if alternative=='two-sided':
        return r, 2*min(t.cdf(T, n-2), t.sf(T, n-2))
    elif alternative=='greater':
        return r, t.sf(T, n-2)
    elif alternative=='less':
        return r, t.cdf(T, n-2)
    else:
        raise ValueError("alternative must be 'less', 'greater' or 'two-sided'")
    

if __name__ == "__main__":
    correlation = spearman_rank_corr_test(data_x, data_y)
    print(f"Spearman rank correlation coefficient: {correlation}")
    scipy_corr = spearmanr(data_x, data_y)
    print(f"Scipy's spearmanr result: {scipy_corr}")
