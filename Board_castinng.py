import numpy as np

budget = np.array([10000, 8000, 12000, 9500])  


actual = np.array([
    [9800,  8200, 11500, 9000],   # Month 1
    [10200, 7900, 12400, 9800],   # Month 2
    [9500,  8100, 11800, 9300],   # Month 3
    [10500, 8300, 12100, 9700],   # Month 4
    [9900,  7800, 11600, 9100],   # Month 5
    [10100, 8050, 12300, 9600],   # Month 6
]) 


variance  = actual - budget

print("variance_from_buget")
print(variance)
print('Overspend')
overspend = np.any(variance>0 , axis=1)
print(overspend)