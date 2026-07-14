def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    N = len(actual_tokens)
    H = 0

    for i in range(N):
        H += np.log(prob_distributions[i][actual_tokens[i]])
    H = -H/N 
    
    return np.exp(H)