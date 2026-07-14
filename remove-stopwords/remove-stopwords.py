def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    filtered_list = []
    for i in range(len(tokens)):
        if tokens[i] not in stopwords:
            filtered_list.append(tokens[i])
    
    return filtered_list
    