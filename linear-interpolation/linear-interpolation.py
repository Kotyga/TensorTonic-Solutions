def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    filling_values = []
    left = []
    right = []
    
    for i in range(len(values)-1):
        if values[i + 1] is None and values[i] is not None:
           left.append(i)
        if values[i] is None and values[i + 1] is not None:
            right.append(i + 1)

    if len(left) * len(right) == 0:
      return values

    else:
      left_idx = next(iter(left))
      right_idx = next(iter(right))

      for i in range(len(values)):
          if values[i] is not None:
            filling_values.append(values[i]) 
          else:
              if i < left_idx and i > right_idx:
                left_idx = next(iter(left))
                right_idx = next(iter(right))
              
              exp = values[left_idx] + (i - left_idx) / (right_idx - left_idx) * (values[right_idx] - values[left_idx])
              filling_values.append(exp) 
      return filling_values