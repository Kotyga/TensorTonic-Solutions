def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    
    len_rel = len(relevant)
    top_k = recommended[:k]
    union = 0
    for i in range(len(top_k)):
      if top_k[i] in relevant:
        union += 1
    
    precision = union / k
    recall = union / len_rel
    return [precision, recall]