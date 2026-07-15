def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    len_x1 = 0
    len_x2 = 0
    s = 0
    for i in range(len(x1)):
        s += x1[i] * x2[i]
        len_x1 += x1[i] ** 2
        len_x2 += x2[i] ** 2
    cos = s / ((len_x1 ** 0.5) * (len_x2 ** 0.5))

    if label == 1:
        return 1 - cos
    elif label == -1:
        return max(0, cos - margin)