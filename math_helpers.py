def smart_divide(numerator, denominator):
  if numerator in (0, True, False, None) or denominator in (0, True, False,
                                                            None):
    return 0
  else:
    return numerator / denominator

