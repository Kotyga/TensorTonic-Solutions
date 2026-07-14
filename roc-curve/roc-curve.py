import numpy as np

def roc_curve(y_true, y_score):
    """
    Compute ROC curve from binary labels and scores.
    """
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)

    thresholds = [np.inf]
    TPR = [0.0]
    FPR = [0.0]

    unique_scores = np.sort(np.unique(y_score))[::-1]

    for threshold in unique_scores:
        y_pred = np.where(y_score >= threshold, 1, 0)

        TP = np.sum((y_pred == 1) & (y_true == 1))
        TN = np.sum((y_pred == 0) & (y_true == 0))
        FP = np.sum((y_pred == 1) & (y_true == 0))
        FN = np.sum((y_pred == 0) & (y_true == 1))

        TPR.append(TP / (TP + FN))
        FPR.append(FP / (FP + TN))
        thresholds.append(threshold)

    return np.array(FPR), np.array(TPR), np.array(thresholds)