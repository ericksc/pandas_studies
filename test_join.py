import pandas as pd
import numpy as np

def test_join_2level_few_combinations():
    pd.show_versions()
    dates = pd.date_range(start='2000-1-1', end='2010-1-1')
    strings = np.array(
        [
        'apple', 'grape', 'orange'
    ])
    idx = pd.MultiIndex.from_product([dates,strings], names=['date', 'fruit'])
    lenght = idx.shape[0]
    df_1 = pd.DataFrame({'col_A':np.random.randn(lenght),
                  'col_2':np.arange(lenght),
                  'col_b' : np.random.choice(a=[False, True], size=(lenght)),
                  'col_i' : np.random.random_integers(low=0,high=100, size=lenght),
            }, index=idx)

    df_2 = pd.DataFrame({'col_x':np.arange(lenght)} ,
                        index=idx)

    assert df_1.shape == (10962, 4)
    df_1 = df_1.join(df_2, how='left')
    assert df_1.shape == (10962, 5)

def test_join_2level_more_combinations():
    pd.show_versions()
    dates = pd.date_range(start='2000-1-1', end='2010-1-1')
    strings = np.array(
        [
        'apple', 'grape', 'orange',
        'pear', 'melon', 'banana',
        'watermelon', 'lemon' , 'strawberry',
        'berry', 'blackberry' , 'cherry',
        'pineapple' , 'mango', 'papaya', 'peach', 'coffee'
    ])
    idx = pd.MultiIndex.from_product([dates,strings], names=['date', 'fruit'])
    lenght = idx.shape[0]
    df_1 = pd.DataFrame({'col_A':np.random.randn(lenght),
                  'col_2':np.arange(lenght),
                  'col_b' : np.random.choice(a=[False, True], size=(lenght)),
                  'col_i' : np.random.random_integers(low=0,high=100, size=lenght),
            }, index=idx)

    df_2 = pd.DataFrame({'col_x':np.arange(lenght)},
                        index=idx)

    assert df_1.shape == (62118, 4)
    df_1 = df_1.join(df_2, how='left')
    assert df_1.shape == (62118, 5)

if __name__ == '__main__':
    test_join_2level_few_combinations()
    test_join_2level_more_combinations()

