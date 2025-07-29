# 🧾 Tip Analysis Dashboard (Seaborn + Matplotlib)

This dashboard explores **tipping behavior** using Seaborn's `tips` dataset. It analyzes how tips vary by **total bill**, **day of the week**, **gender**, and **time of day** using clean and informative visualizations.

---

## 📊 Dataset

- **Source**: Seaborn built-in `tips` dataset
- **Key Columns**:
  - `total_bill`: Meal cost
  - `tip`: Tip amount
  - `sex`, `day`, `time`, `smoker` : Customer demographics and visit time
  - `size`: Party size

---

## 🔧 Requirements

Install the required packages:

```bash
pip install pandas seaborn matplotlib scipy

```
---
## 🧠 Questions & Visualizations

### 1. 💡 Q1: What's the relationship between Total Bill and Tip?
Chart: 
- Scatter Plot Based On Gender With Pearson Correlation
- Line Plot

Code:

``` python
#Data Preparation

sns.set_theme(style = 'whitegrid')
fig, ax = plt.subplots(1,2, figsize = (12,5))

hue_colors = {
    'Female':'Red',
    'Male':'Black'
}
total_bill = tips['total_bill']
tip = tips['tip']
male_total_bill = tips[tips['sex'] == 'Male']['total_bill']
male_tip = tips[tips['sex'] == 'Male']['tip']
female_total_bill = tips[tips['sex'] == 'Female']['total_bill']
female_tip = tips[tips['sex'] == 'Female']['tip']

#Person Correlation
overall_corr,_ = pearsonr(total_bill,tip)
male_corr,_ = pearsonr(male_total_bill,male_tip)
female_corr,_ = pearsonr(female_total_bill,female_tip)

#Scatter Plot
sns.scatterplot(
    data = tips, 
    x = 'total_bill',
    y = 'tip',
    hue = 'sex',
    hue_order=['Female','Male'],
    palette= hue_colors, 
    ax = ax[0]
)
ax[0].set_title('Total Bill vs Tip Amount by Gender', fontsize = 12)
ax[0].set_xlabel('Total_Bill', fontsize = 11)
ax[0].set_ylabel('Tip', fontsize = 11)
ax[0].tick_params(axis='x',labelsize = 11)
ax[0].tick_params(axis ='y', labelsize = 11)

correlations = [
    ('Overall',overall_corr),
    ('Male',male_corr),
    ('Female',female_corr)
]

start_y = 9.5
for i,(x,y) in enumerate(correlations):
    next_y = start_y - i*0.5
    start_x = ax[0].get_xlim()[1]*0.65 
    ax[0].text(
        start_x,
        next_y,
        f"{x} r = {y:.2f}",
        fontsize = 10,
        color = 'black',
        alpha = 0.6,
        bbox = dict(facecolor = 'white', alpha = 0.9)
    )

#LinePlot

sns.lineplot(
    data = tips,
    x = tips['total_bill'].round(0),
    y = 'tip',
    estimator='mean',
    markers='o',
    ax= ax[1]
)
ax[1].set_title('Average Tip over Total Bill', fontsize = 12)
ax[1].set_xlabel('Total_Bill', fontsize = 11)
ax[1].set_ylabel('Tip', fontsize = 11)
ax[1].tick_params(axis = 'x', labelsize = 11)
ax[1].tick_params(axis = 'y', labelsize = 11)

plt.tight_layout()
plt.savefig(r"C:\Users\Randy V\Tips_Dashboard\docs\relationship_total_bill_and_tip.png", dpi=300, bbox_inches='tight')
plt.show()
```

![Chart_1](docs/relationship_total_bill_and_tip.png)

Insights: 
- **Line Plot:** Tips generally increase with bill size.
- **Scatter Plot**: 
  - Based on overall score pearson correlation of **0.68**, there is **a moderate positive correlation** between **tips growth and total bill**. 
  - Breaking it down by **gender**, the results for both male and female show similarly **a moderate positive correlation.** 

### 2. 💡 How does tipping differ by day of the week?
Chart: Relplot (kind = Line)

Code: 

```python
a = sns.relplot(
    data = tips,
    kind = 'line',
    x = tips['total_bill'].round(0),
    y = 'tip',
    col = 'day',
    col_wrap= 2,
    col_order=['Thur','Fri','Sat','Sun'],
    markers = True
)

a.fig.suptitle('Average Tip over Total Bill across Days',
               y = 1.03)

a.set_axis_labels('Total_Bill','Tip')
plt.tight_layout()
plt.savefig(r"C:\Users\Randy V\Tips_Dashboard\docs\relationship_total_bill_and_tip_across_days.png", dpi=300, bbox_inches='tight')
plt.show()

```
![Chart_2](docs/relationship_total_bill_and_tip_across_days.png)

Insights:
- Across days of the week, the overall trend of the increase of total bill followed by tips is still continuing except for **Sunday** that shows more **dynamic trend** between total bill and tips. 

### 3. 💡 Do customers tip differently at lunch vs dinner?
Chart: Relplot(kind = Scatter )

Code:
```python
a = sns.relplot(
    data = tips,
    kind = 'scatter',
    x = 'total_bill',
    y = 'tip',
    col = 'time',
    size= 'size',
    hue = 'size',
    markers = 'o'
)

a.fig.suptitle('Total Bill vs Tip across Time and Size',
               y = 1.03)

a.set_axis_labels('Total_Bill','Tip')
plt.savefig(r"C:\Users\Randy V\Tips_Dashboard\docs\relationship_total_bill_and_tip_across_time_size.png",dpi=300,bbox_inches='tight')
plt.tight_layout()
plt.show()
```

![Chart_3](docs/relationship_total_bill_and_tip_across_time_size.png)

Insights:
- The overall trend of the increase of total bill followed by tips is still applicable in both lunch and dinner time.
- People not only tend to **tip more on dinner** but also **the size of more than 2 people in a table are higher** compared to lunch time.
