import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    param = np.asarray(param)
    grad = np.asarray(grad)
    m = np.asarray(m)
    v = np.asarray(v)
    t = np.asarray(t)
    lr = np.asarray(lr)
    beta1 = np.asarray(beta1)
    beta2 = np.asarray(beta2)
    eps = np.asarray(eps)

    m_next = beta1 * m + (1 - beta1) * grad
    v_next = beta2 * v + (1 - beta2) * grad ** 2
    m_corr = m_next / (1 - beta1 ** t)
    v_corr = v_next / (1 - beta2 ** t)
    param_next = param - lr * m_corr / (v_corr ** 0.5 + eps) 
    return param_next, m_next, v_next