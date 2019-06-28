import pandas as pd
import numpy as np
import time

def test_join_2level_few_combinations():
    dates = pd.date_range(start='1990-1-1', end='2030-1-1')
    strings = np.array(
        [
        'apple', 'grape', 'orange'
    ])

    start = time.time()
    idx = pd.MultiIndex.from_product([dates,strings], names=['date', 'fruit'])
    end = time.time()
    print("MultiIndex execution time:", end-start)

    lenght = idx.shape[0]
    df_1 = pd.DataFrame({'col_A':np.random.randn(lenght),
                  'col_2':np.arange(lenght),
                  'col_b' : np.random.choice(a=[False, True], size=(lenght)),
                  'col_i' : np.random.random_integers(low=0,high=100, size=lenght),
            }, index=idx)

    df_2 = pd.DataFrame({'col_x':np.arange(lenght)} ,
                        index=idx)

    assert df_1.shape == (43833, 4)

    start = time.time()
    df_1 = df_1.join(df_2, how='left')
    end = time.time()
    print("Join execution time:", end - start)
    assert df_1.shape == (43833, 5)

def test_join_2level_more_combinations():
    dates = pd.date_range(start='1980-1-1', end='2050-1-1')
    strings = np.array(
        [
            'apple', 'grape', 'orange' ,'pear', 'melon', 'banana',
            'watermelon', 'lemon', 'strawberry', 'berry', 'blackberry',
            'cherry','pineapple' , 'mango', 'papaya', 'peach', 'coffee',
            'planes', 'cars', 'houses', 'dogs', 'cats', 'computers',
            'servers', 'sun', 'moon', 'chairs', 'tables', 'screens',
            'keyboards', 'shoes', 't-shirts', 'tv', 'radio', 'door', 'windows',
            'bed', 'spoon', 'key', 'paper', 'foot', 'bee', 'ants' ,'worm',
            'pack', 'phone', 'boat', 'hair', 'yellow', 'disc'
    ])
    start = time.time()
    idx = pd.MultiIndex.from_product([dates,strings], names=['date', 'words'])
    end = time.time()
    print("MultiIndex execution time:", end-start)
    lenght = idx.shape[0]
    start = time.time()
    df_1 = pd.DataFrame({'col_A':np.random.randn(lenght),
                  'col_2':np.arange(lenght),
                  'col_b' : np.random.choice(a=[False, True], size=(lenght)),
                  'col_i' : np.random.random_integers(low=0,high=100, size=lenght),
            }, index=idx)
    end = time.time()
    print("data frame creation execution time:", end-start)
    df_2 = pd.DataFrame({'col_x':np.arange(lenght)},
                        index=idx)

    assert df_1.shape == (1278450, 4)

    start = time.time()
    df_1 = df_1.join(df_2, how='left')
    end = time.time()
    print("Join execution time:", end - start)
    assert df_1.shape == (1278450, 5)

if __name__ == '__main__':
    test_join_2level_few_combinations()
    test_join_2level_more_combinations()

