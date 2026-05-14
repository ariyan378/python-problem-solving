# Multiindex df in terms of both cols and index

import numpy as np
import pandas as pd

multi_index = pd.MultiIndex.from_product([['himu' , 'hridoy'] , [2020,2021,2022]])

df = pd.DataFrame(
    [
        [1,2,3,4],
        [1,2,3,4],
        [1,2,3,4],
        [1,2,3,4],
        [1,2,3,4],
        [1,2,3,4],
    ],
    index=multi_index,
    columns=pd.MultiIndex.from_product([['cse', 'eee'] , ['Number', 'cg']])
    
)
print(df)