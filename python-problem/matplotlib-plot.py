import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8-whitegrid')
# This helps charts display nicely inside Jupyter Notebook


# For reproducible random data
np.random.seed(42)

print("Matplotlib is ready!")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

sales = np.array([120, 135, 150, 160, 180, 175, 190, 210, 230, 240, 260, 300])
expenses = np.array([80, 90, 95, 100, 110, 120, 125, 130, 145, 150, 160, 180])
profit = sales - expenses
customers = np.array([300, 330, 350, 370, 420, 410, 455, 480, 510, 530, 560, 610])
marketing_budget = np.array([15, 18, 20, 22, 30, 28, 35, 38, 42, 45, 48, 55])

categories = ["Laptop", "Mobile", "Tablet", "Accessories", "Software"]
category_sales = [350, 500, 220, 180, 300]

exam_scores = np.random.normal(loc=72, scale=10, size=120)
exam_scores = np.clip(exam_scores, 35, 100)

df = pd.DataFrame({
    "months": months,
    "sales": sales,
    "expenses": expenses,
    "profit": profit,
    "customers": customers,
    "marketing_Budget": marketing_budget
})

from matplotlib.patches import ArrowStyle
from matplotlib.lines import lineStyles
fig,ax = plt.subplots(figsize = (10,5))


ax.plot(months , sales , color ='Blue' , linestyle='solid', linewidth= 5 , marker = 'o'  , markersize=15, label='Sales')

ax.plot(months , expenses , color ='Red' , linestyle='solid', linewidth= 5 , marker = 'o'  , markersize=15, label='Expense')

ax.plot(months , profit , color ='Green' , linestyle='solid', linewidth= 5 , marker = 'o'  , markersize=15, label='Profit')




ax.set_title("Monthly Sales Comparison" ,  fontdict={
        "fontsize": 18,
        "color": "Black",
        "fontweight": "bold"
    } , )
ax.set_xlabel('Month Name',fontdict={
        "fontsize": 12,
        "color": "Black",
        "fontweight": "bold"
    })
ax.set_ylabel('Sales amount',fontdict={
        "fontsize": 12,
        "color": "Black",
        "fontweight": "bold"
    })


ax.grid(True , alpha= 0.4)
plt.xticks(rotation=10)
ax.legend()

ax.annotate('Highest Sales', 
            xy=(11, sales[-1]),
            xytext=(8,285),
            arrowprops=dict(arrowstyle= '->', color= 'Black'),
            fontsize=10)


plt.tight_layout()
plt.show()