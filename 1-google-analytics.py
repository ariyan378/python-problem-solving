import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

team = [('Marta', 20, 'center'),
        ('Ana', 22, 'point guard'),
        ('Gabi', 22, 'shooting guard'),
        ('Luz', 21, 'power forward'),
        ('Lorena', 19, 'small forward')]


def player_position(player_list):
    result = []
    for name, age, position in player_list:

        result.append(f"Name : {name:>7}\nPosition : {position:>5}")
    return result

for p in player_position(team):
    print(p)
    print("-" * 20)


data = []   
for name, age, position in team:
    data.append([name, age]) 

df = pd.DataFrame(data, columns=['Name', 'Age'])

print("\n--- Team DataFrame ---")

print(df.to_string(index=False))


plt.figure(figsize=(8, 4))
plt.plot(df['Name'], df['Age'], marker='o', linestyle='-', color='b')

plt.title("Player Ages")
plt.xlabel("Player Name")
plt.ylabel("Age")
plt.grid(True)

plt.show() 