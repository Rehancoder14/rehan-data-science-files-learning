def remove_outliers(df, x):
    q25, q75 = np.percentile(df[x],25), np.percentile(df[x],75)
    iqr = q75 - q25
    cut_off= iqr  *1.5
    lower, upper = 1, (q75+cut_off)
    df = (df[x] < upper) and (df[x] > lower)
    print("outliers of '{}' are removed\n".format(x))
    return df 