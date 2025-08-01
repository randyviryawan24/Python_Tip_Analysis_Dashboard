#%% 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import pearsonr

tips = sns.load_dataset('tips')
tips.head()
#%% 1. Scatter Plot
#💡 Is there a relationship between the total bill and the tip amount? Does this vary by gender?
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

#%% 2. Line Plot
#💡 How does the average tip change as the total bill increases?
sns.lineplot(
    data = tips,
    x = 'total_bill',
    y = 'tip',
    markers=True
)
plt.title('Average Tip over Total Bill', fontsize = 12)
plt.xlabel('Total_bill', fontsize = 11)
plt.ylabel('Tip', fontsize = 11)
plt.xticks(fontsize = 11)
plt.yticks(fontsize = 11)
plt.tight_layout()
plt.show()

#%% 3. 3. Relplot (Faceted Relational Plot)
#💡 Does the relationship between total bill and tip change across different times of day or days of the week?

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

#%% 4. Relplot (Faceted Relational Plot)
#💡 Does the relationship between total bill and tip change across different times of day or days of the week?

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

#%%
tips.query('day=="Thur" & time =="Dinner"')


#B. Categorical Plot (Catplot)
#4. Count Plot
#💡 How many customers came in on each day of the week? Does gender play a role?
#Plot idea:
hue_colors = {
    'Male':'Black',
    'Female':'Red'
}
hue_orders = ['Female','Male']
a = sns.countplot(
    data = tips,
    #kind='count',
    x = 'day',
    hue = 'sex',
    palette=hue_colors,
    hue_order=hue_orders
)
for i in a.patches:
    width = i.get_x() + i.get_width()/2
    height = i.get_height()
    a.text(
     width,
     height,
     f"{height:.0f}",
     fontsize = 10,
     ha = 'center',
     va = 'bottom'   
    )
a.set_title('Number of Customers Across Days by Gender')
a.set(xlabel = 'Day', ylabel='Count')
plt.tight_layout()
#plt.savefig(r"C:\Users\Randy V\Tips_Dashboard\docs\num_customers_across_days_gender.png",dpi=300, bbox_inches = 'tight')
plt.show()

#%%

tips.value_counts(subset='sex',normalize=True)
#%%5. Box Plot
#💡 What’s the distribution of total bills per day? Are there any outliers?
#Plot idea:
#Use sns.catplot(kind="box", x="day", y="total_bill", data=tips).

sns.set_theme(style='whitegrid')
fig,ax = plt.subplots(1,2, figsize=(12,5))

hue_colors = {
    'Male':'Green',
    'Female':'Red'
}
sns.boxplot(
    data = tips,
    x = 'day',
    y = 'total_bill',
    hue = 'sex',
    whis = [5,95],
    order=['Thur','Fri','Sat','Sun'],
    hue_order=['Female','Male'],
    palette=hue_colors,
    ax = ax[0]
)
ax[0].set_title('Box Plot Total Bill across Days by Gender')
ax[0].set_xlabel('Day')
ax[0].set_ylabel('Total Bill')

#6. Box Plot (again for practice)
#💡 Do men and women tip differently?
#Plot idea:
#Use sns.catplot(kind="box", x="sex", y="tip", data=tips).

sns.boxplot(
    data=tips,
    x = 'day',
    y = 'tip',
    hue ='sex',
    whis = [5,95],
    order=['Thur','Fri','Sat','Sun'],
    hue_order=['Female','Male'],
    palette=hue_colors,
    ax = ax[1]
)
ax[1].set_title('Box Plot Tip across Day by Gender')
ax[1].set_xlabel('Day')
ax[1].set_ylabel('Tip')
plt.tight_layout()
#plt.savefig(r"C:\Users\Randy V\Tips_Dashboard\docs\box_plot_total_bill_tip.png", dpi = 300, bbox_inches = 'tight')
plt.show()

#%%7. Point Plot
#💡 What is the average tip given by smokers vs. non-smokers across different meal times?
#Plot idea:
#Use sns.catplot(kind="point", x="time", y="tip", hue="smoker", data=tips).

a = sns.catplot(
    data=tips,
    kind='point',
    x = 'smoker',
    y = 'tip',
    col = 'time',
    estimator='mean',.
    linestyle = 'none',
    errorbar= ('ci',95),
    capsize = 0.2
)

a.fig.suptitle('Point Plot Tip across Smoker by Day', y = 1.03)
a.set_xlabels('Smoker')
a.set_ylabels('Tip')
plt.tight_layout()
plt.savefig(r"C:\Users\Randy V\Tips_Dashboard\docs\point_plot_smoker_time.png", dpi = 300, bbox_inches = 'tight')
plt.show()

## Futher Analysis

#%% Tips Percentage Analysis

tips['tips_pct'] = tips['tip']/tips['total_bill']

#%%Box Plot Tips' Percentage across Day by Gender
sns.set_theme(style='whitegrid')

hue_colors={
    'Male':'Green',
    'Female':'Red'
}
#Box plot
a = sns.catplot(
    data= tips,
    kind= 'box',
    x = 'day',
    y = 'tips_pct',
    hue='sex',
    hue_order=['Female','Male'],
    palette=hue_colors
)
a.fig.suptitle("Box Plot Tips' Percentage across Day by Gender")
a.set_xlabels('Day')
a.set_ylabels('Tips(%)')
plt.tight_layout()
plt.savefig(r"C:\Users\Randy V\Python_Tips_Analysis_Dashboard\docs\box_tips_pct_day_gender.png", dpi = 300, bbox_inches = 'tight')
plt.show()

#%% Box plot Tips' Percentage across Time by Smoker
sns.set_theme(style='whitegrid')

hue_colors_smokers ={
    'Yes':'Red',
    'No':'Green'
}
a = sns.catplot(
    data= tips,
    kind= 'box',
    x = 'time',
    y = 'tips_pct',
    hue = 'smoker',
    palette=hue_colors_smokers
)
a.fig.suptitle("Box Plot Tips' Percentage across Time by Smoker Status")
a.set_xlabels('Time')
a.set_ylabels('Tips(%)')
plt.tight_layout()
plt.savefig(r"C:\Users\Randy V\Python_Tips_Analysis_Dashboard\docs\box_tips_pct_time_smoker.png",dpi = 300, bbox_inches = 'tight')

#%% Heatmap of Tip% by Day and Time
pivot = tips.pivot_table(
    index = 'day',
    columns='time',
    values='tips_pct',
    aggfunc='median',
    fill_value=0
)
sns.heatmap(
    pivot,
    cmap='coolwarm',
    annot=True,
    annot_kws={'size':10}
)
plt.title('Heatmap Tips(%) by Day and Time')
plt.xlabel('Time')
plt.ylabel('Day')
plt.tight_layout()
plt.savefig(r"C:\Users\Randy V\Python_Tips_Analysis_Dashboard\docs\heatmap_tips_pct_time_day.png", dpi = 300, bbox_inches='tight')
plt.show()

#%% Statistical Testing (T-test)
# 🎯 Purpose of a t-test:
# To compare the means of two groups and decide whether the observed difference is real (statistically significant) or just random noise in the data.

#%% T-test between Male and Female on Tipping Pct
# importing t-test
from scipy.stats import ttest_ind

# Preparing the data
male = tips[tips['sex']=='Male']['tips_pct']
female = tips[tips['sex']=='Female']['tips_pct']

# Calculating the mean and number of samples
male_mean = round(male.mean()*100,2)
male_sample = male.count()
female_mean = round(female.mean()*100,2)
female_sample = female.count()

# implementing t-test
stats_test = ttest_ind(
    male,
    female,
    equal_var=False
)

print(f"male_mean = (n = {male_sample}) {male_mean}")
print(f"female_mean = (n = {female_sample}) {female_mean}")
print(f"T-statistic result = {stats_test.statistic}")
print(f"p-value = {stats_test.pvalue}")
print(f"Test type = Welch’s t-test")


#%% T-test between Lunch and Dinner on Tipping Pct

# importing t-test
from scipy.stats import ttest_ind

# Preparing the data
dinner = tips[tips['time'] =='Dinner']['tips_pct']
lunch = tips[tips['time'] =='Lunch']['tips_pct']

# Calculating the mean and number of samples
dinner_mean = round(dinner.mean()*100,2)
dinner_sample = dinner.count()
lunch_mean = round(lunch.mean()*100,2)
lunch_sample = lunch.count()

# implementing t-test
stats_test = ttest_ind(
    dinner,
    lunch,
    equal_var=False
)

print(f"dinner_mean = (n = {dinner_sample}) {dinner_mean}")
print(f"lunch_mean = (n = {lunch_sample}) {lunch_mean}")
print(f"T-statistic result = {stats_test.statistic}")
print(f"p-value = {stats_test.pvalue}")
print(f"Test type = Welch’s t-test")

#%% T-test between weekday and weekend on Tipping Pct

# importing t-test
from scipy.stats import ttest_ind

# Preparing the data
weekday = tips[np.logical_or(tips['day'] =='Thur',tips['day'] =='Fri')]['tips_pct']
weekend = tips[np.logical_or(tips['day'] =='Sat',tips['day'] =='Sun')]['tips_pct']

# Calculating the mean and number of samples
weekday_mean = round(weekday.mean()*100,2)
weekday_sample = weekday.count()
weekend_mean = round(weekend.mean()*100,2)
weekend_sample = weekend.count()

# implementing t-test
stats_test = ttest_ind(
    weekday,
    weekend,
    equal_var=False
)

print(f"weekday_mean = (n = {weekday_sample}) {weekday_mean}")
print(f"weekend_mean = (n = {weekend_sample}) {weekend_mean}")
print(f"T-statistic result = {stats_test.statistic}")
print(f"p-value = {stats_test.pvalue}")
print(f"Test type = Welch’s t-test")


#%% T-test between smoker and non smoker on Tipping Pct

# importing t-test
from scipy.stats import ttest_ind

# Preparing the data
smoker = tips[tips['smoker'] =='Yes']['tips_pct']
non_smoker = tips[tips['smoker'] =='No']['tips_pct']

# Calculating the mean and number of samples
smoker_mean = round(smoker.mean()*100,2)
smoker_sample = smoker.count()
non_smoker_mean = round(non_smoker.mean()*100,2)
non_smoker_sample = non_smoker.count()

# implementing t-test
stats_test = ttest_ind(
    smoker,
    non_smoker,
    equal_var=False
)

print(f"smoker_mean = (n = {smoker_sample}) {smoker_mean}")
print(f"non_smoker_mean = (n = {non_smoker_sample}) {non_smoker_mean}")
print(f"T-statistic result = {stats_test.statistic}")
print(f"p-value = {stats_test.pvalue}")
print(f"Test type = Welch’s t-test")
#%% T-test between Friday-Lunch and other day-time Tipping Pct

# importing t-test
from scipy.stats import ttest_ind

# Preparing the data
friday_lunch = tips[(tips['day']=='Fri') & (tips['time']=='Lunch')]['tips_pct']
not_friday_lunch = tips[~((tips['day'] == 'Fri') & (tips['time'] =='Lunch'))]['tips_pct']

# Calculating the mean and number of samples
friday_lunch_mean = round(friday_lunch.mean()*100,2)
friday_lunch_sample = friday_lunch.count()
not_friday_lunch_mean = round(not_friday_lunch.mean()*100,2)
not_friday_lunch_sample = not_friday_lunch.count()

# implementing t-test
stats_test = ttest_ind(
    friday_lunch,
    not_friday_lunch,
    equal_var=False
)

print(f"friday_lunch_mean = (n = {friday_lunch_sample}) {friday_lunch_mean}")
print(f"not_friday_lunch_mean = (n = {not_friday_lunch_sample}) {not_friday_lunch_mean}")
print(f"T-statistic result = {stats_test.statistic}")
print(f"p-value = {stats_test.pvalue}")
print(f"Test type = Welch’s t-test")

#%% T-test between Female and Male Tipping Pct on Friday
# importing t-test
from scipy.stats import ttest_ind

# Preparing the data
female_fri = tips[(tips['sex'] == 'Female') & (tips['day'] == 'Fri')]['tips_pct']
male_fri = tips[(tips['sex'] == 'Male') & (tips['day'] == 'Fri')]['tips_pct']

# Calculating the mean and number of samples
female_fri_mean = round(female_fri.mean()*100,2)
female_fri_sample = female_fri.count()
male_fri_mean = round(male_fri.mean()*100,2)
male_fri_sample = male_fri.count()

# implementing t-test
stats_test = ttest_ind(
    female_fri,
    male_fri,
    equal_var=False
)

print(f"female_fri_mean = (n = {female_fri_sample}) {female_fri_mean}")
print(f"male_fri_mean = (n = {male_fri_sample}) {male_fri_mean}")
print(f"T-statistic result = {stats_test.statistic}")
print(f"p-value = {stats_test.pvalue}")
print(f"Test type = Welch’s t-test")
###Takeaways Summary

#%% avg total bill and tips pct by gender
tips.groupby('sex').agg(
    avg_total_bill = ('total_bill','mean'),
    avg_tips_pct = ('tips_pct','mean'),
    median_tips_pct = ('tips_pct','median')
)

tips.groupby(['sex','day']).agg(
    avg_total_bill = ('total_bill','mean'),
    avg_tips_pct = ('tips_pct','mean'),
    median_tips_pct = ('tips_pct','median')
)
#%% avg total bill and tips pct by day & time
tips.groupby(['day','time']).agg(
    avg_total_bill = ('total_bill','mean'),
    avg_tips_pct = ('tips_pct','mean'),
    median_tips_pct = ('tips_pct','median')
)

#%% avg total bill and tips pct by smokers & time
tips.groupby(['smoker','time'])['tips_pct'].median()