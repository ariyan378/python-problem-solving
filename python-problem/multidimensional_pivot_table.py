import numpy as np
import pandas as pd 
import matplotlib.pylab as plt
import seaborn as sns

df = sns.load_dataset('tips')

table = df.pivot_table(index=['sex','smoker'],columns=['day','time'],aggfunc={
    'size':'mean',
    'tip':'max','total_bill':'sum'},margins=True)

print(table)