import pandas as pd
import numpy as np

def test_groupby():
    my_df = pd.DataFrame({'DOG#3M': {'1/1/1999': 0.04825, '1/4/1999': 0.0476, '1/5/1999': 0.0474, '1/6/1999': 0.0476, '1/7/1999': 0.0474},
     'DOG#6M': {'1/1/1999': 0.04751, '1/4/1999': 0.0469, '1/5/1999': 0.0471, '1/6/1999': 0.0473, '1/7/1999': 0.0468,},
     'CAT#3M': {'1/1/1999': 0.05072, '1/4/1999': 0.0501, '1/5/1999': 0.0501, '1/6/1999': 0.0498, '1/7/1999': 0.0497,},
     'FISH#3M': {'1/1/1999': np.nan, '1/4/1999': 0.0161, '1/5/1999': 0.0155, '1/6/1999': 0.01495, '1/7/1999': 0.015, },
     'FISH#6M': {'1/1/1999': 0.0323, '1/4/1999': 0.03223, '1/5/1999': 0.03204, '1/6/1999': 0.03197, '1/7/1999': 0.03179,}})

    def getTenorInMos(tenor):
        """
        tenor (string) of the format: \d+[Y|M]
        """

        tenor = tenor.upper()
        if tenor[-1] == 'Y':
            mult = 12
            pass
        elif tenor[-1] == 'M':
            mult = 1
            pass
        else:
            raise KeyError("tenorType[%s] not supported" % tenor[-1])

        return int(tenor[:-1])*mult

    import sys
    print('Python version',sys.version)
    print('pandas version', pd.__version__)
    result = my_df.groupby(by=lambda c: c.split('#')[0], axis='columns').apply(
        lambda df:
        pd.DataFrame(df.values, index=df.index,
                         columns=[getTenorInMos(c.split('#', )[-1]) for c in df.columns]).stack()
    )
