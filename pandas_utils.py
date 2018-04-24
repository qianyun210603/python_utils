import pandas as pd
import numpy as np

def count_consecutive(boolseries):
    """
    Count consecutive appearance of True in a pandas Series of bool

    Param:
    boolseries: pandas.Series of type bool

    Return: pandas.Series of type int
    Number of consecutive True if corresponding position is True else 0
    """
    grp = boolseries.groupby((boolseries != boolseries.shift()).cumsum())
    return pd.Series(data=np.where(boolseries, grp.cumcount() + grp.cumcount(ascending=False) + 1, 1),
                     index=boolseries.index
                    )

    
