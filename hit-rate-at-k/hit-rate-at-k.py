def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    N = len(ground_truth)
    target = 0

    for i in range(N):
        if ground_truth[i][0] in recommendations[i][:k]:
            target += 1
    return target/N