from scipy.stats import norm


def runs_test(data, cutoff):
    prev = None
    R = n1 = n2 = 0
    for elem in data:
        if elem>=cutoff:
            n1 += 1
        else:
            n2 += 1

        if elem!=prev:
            R += 1
        prev = elem

    dist = norm(((2*n1*n2)/(n1+n2)) + 1,
        ((2*n1*n2*(2*n1*n2-n1-n2))/((n1+n2-1)*(n1+n2)**2))**(1/2))

    return R, 2*min(dist.cdf(R), dist.sf(R))


if __name__=='__main__':
    from inputlib import input_data
    data = input_data()
    cutoff = float(input('Enter the median: '))

    results = runs_test(data, cutoff)
    print(results)
