def split_data(dt): 
    """
    Function to split dates ("MM/DD/YYYY", etc.) into multiple columns
    Input: DF column, output - 1x3 data frame 

    """
    import pandas as pd

    assert type(dt)==pd.Series, 'argument should be a pandas Series'
    dt=pd.to_datetime(dt)
    year=dt.td.year
    month=dt.td.month
    day=dt.td.day
    result = pd.DataFrame({'year': year, 
                      'month':month,
                        'day':day})


    return result


def train_val_test_split(df, pct_val=0.2, pct_test=0.2):
    """
Train/validate/test split function for a dataframe
Takes a non-empty DF as an input, returns 3 dataframes -- train, test, and validation 

    """
    import pandas as pd 
    assert type(df)==pd.DataFrame, 'first argument needs to be a dataframe'
    assert df.shape[0]>1, 'df should not be empty'
    assert (pct_test+pct_val) < 1, 'check percentages, sum should be <1'
    n_rows=df.shape[0]
    test=df.sample(n=pct_test*n_rows)
    df=df.drop(test)
    val=df.sample(n=pct_val*n_rows)
    train=df.drop(val)
    return train, test, val

