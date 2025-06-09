import numpy as np
import pandas as pd 
from tableone import TableOne

import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, ScalarFormatter

from lifelines import CoxPHFitter
from lifelines import KaplanMeierFitter
import statsmodels.api as sm

import scipy.stats as stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import itertools

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 100)  
pd.set_option('display.width', None)

print('done')

# load data 
file_path = "C:\\Users\\wingersm\\OneDrive - The University of Colorado Denver\\Desktop\\Python Projects\\8.0 Salfi Four Groups\\Data\\Salfi_fourGroups.csv"
df = pd.read_csv(file_path)

# Grouping var
conditions = [
    (df['exercise_since_injury'] == 0) & (df['current_sleep_problems'] == 0),
    (df['exercise_since_injury'] == 1) & (df['current_sleep_problems'] == 0),
    (df['exercise_since_injury'] == 0) & (df['current_sleep_problems'] == 1),
    (df['exercise_since_injury'] == 1) & (df['current_sleep_problems'] == 1),
]
choices = [0, 1, 2, 3]

df['grouping'] = np.select(conditions, choices)

df['grouping'].value_counts() 

df['grouping_label'] = df['grouping'].map({
    0: '-Ex/+Sleep',
    1: '+Ex/+Sleep',
    2: '-Ex/-Sleep',
    3: '+Ex/-Sleep'
})

df['grouping_label'].value_counts() 


# Table 1
table_columns = {
    'variables': ['record_id', 'doi', 'month', 'month_numeric', 'summer', 'time_since_injury',
                    'sex1f', 'age', 'failure', 'sport', 'loc', 'conc_hx',
                    'number_prior_conc', 'time_sx', 'PPCS', 'time_rtp', 'add_adhd',
                    'ld_dyslexia', 'anxiety', 'depression', 'migraines',
                    'exercise_since_injury', 'headaches', 'headache_severity',
                    'current_sleep_problems', 'history_sleep_problems', 'bess_hard1',
                    'bess_hard2', 'bess_hard3', 'BESS_total', 'HBI_total',
                    'HBI_total_parent', 'hbi_attention', 'hbi_distract', 'hbi_concentrate',
                    'hbi_remembering', 'hbi_directions', 'hbi_daydream', 'hbi_confused',
                    'hbi_forgetthings', 'hbi_finishthings', 'hbi_figurethings',
                    'hbi_learnthings', 'hbi_headache', 'hbi_dizzy', 'hbi_roomspin',
                    'hbi_faint', 'hbi_blurry', 'hbi_double', 'hbi_sick', 'hbi_tired',
                    'hbi_tiredeasily', 'hbi_somatic', 'hbi_cognitive', 'grouping',
                    'grouping_label'],
    'categorical': ['month', 'sex1f', 'sport', 'loc', 'conc_hx', 'PPCS', 'add_adhd', 'ld_dyslexia', 
                    'anxiety', 'depression', 'migraines', 'exercise_since_injury', 'headaches', 'summer',
                    'current_sleep_problems', 'history_sleep_problems'],
    'continuous': ['time_since_injury', 'age', 'number_prior_conc', 'time_sx', 'time_rtp', 
                    'headache_severity', 'bess_hard1', 'bess_hard2', 'bess_hard3', 'BESS_total', 'HBI_total',
                    'HBI_total_parent', 'hbi_attention', 'hbi_distract', 'hbi_concentrate',
                    'hbi_remembering', 'hbi_directions', 'hbi_daydream', 'hbi_confused',
                    'hbi_forgetthings', 'hbi_finishthings', 'hbi_figurethings',
                    'hbi_learnthings', 'hbi_headache', 'hbi_dizzy', 'hbi_roomspin',
                    'hbi_faint', 'hbi_blurry', 'hbi_double', 'hbi_sick', 'hbi_tired',
                    'hbi_tiredeasily', 'hbi_somatic', 'hbi_cognitive']
}

overview = TableOne(
    data=df,
    columns=table_columns['variables'],
    categorical=table_columns['categorical'],
    continuous=table_columns['continuous'],
    groupby='grouping_label',
    pval=False,
    decimals=2,
    min_max=['continuous']
)
print(overview.tabulate(tablefmt='github'))



################


# Univariable comparisons
categorical = [
    'month', 'sex1f', 'sport', 'loc', 'conc_hx', 'PPCS', 'add_adhd', 'ld_dyslexia',
    'anxiety', 'depression', 'migraines', 'exercise_since_injury', 'headaches', 'summer',
    'current_sleep_problems', 'history_sleep_problems'
]

continuous = [
    'time_since_injury', 'age', 'number_prior_conc', 'time_sx', 'time_rtp',
    'headache_severity', 'bess_hard1', 'bess_hard2', 'bess_hard3', 'BESS_total',
    'HBI_total', 'HBI_total_parent', 'hbi_attention'
]

for var in categorical:
    ct = pd.crosstab(df['grouping'], df[var])
    chi2, p, dof, ex = stats.chi2_contingency(ct)
    print(f"{var}: Chi2 = {chi2:.2f}, p = {p:.4f}")

## Post-hoc test
vars = [
    'sport', 'PPCS', 'add_adhd', 'anxiety', 'migraines', 'exercise_since_injury', 'headaches', 'history_sleep_problems'
]

for var in vars:
    print(f"\n{var}:")
    groups = df['grouping'].unique()
    for g1, g2 in itertools.combinations(groups, 2):
        subset = df[df['grouping'].isin([g1, g2])]
        ct = pd.crosstab(subset['grouping'], subset[var])
        if ct.shape[0] == 2 and ct.shape[1] > 1:
            chi2, p, _, _ = stats.chi2_contingency(ct)
            print(f"  Group {g1} vs {g2}: p = {p:.4f}")


## Continuous vars
for var in continuous:
    groups = [df[df['grouping'] == g][var].dropna() for g in df['grouping'].unique()]
    fstat, pval = stats.f_oneway(*groups)
    print(f"{var}: ANOVA F = {fstat:.2f}, p = {pval:.4f}")

    # Post-hoc
    if pval < 0.05:
        tukey = pairwise_tukeyhsd(df[var].dropna(), df['grouping'][df[var].notna()])
        print(tukey.summary())
        print()


###################


# Cox PH - unadjusted
df['grouping'] = pd.Categorical(df['grouping'], categories=[1, 0, 2, 3], ordered=False)
df_dummies = pd.get_dummies(df, columns=['grouping'], drop_first=True)

cph = CoxPHFitter()
cph.fit(df_dummies[['time_sx', 'failure', 'grouping_0', 'grouping_2', 'grouping_3']], duration_col='time_sx', event_col='failure')
cph.print_summary(decimal_places=4)

summary_df = cph.summary.round(4)
print(summary_df)

# Cox PH - adjusted for HBI, days since injury, and sleep problems
df_dummies_temp = df_dummies[df_dummies['history_sleep_problems'] != 'None']
cph2 = CoxPHFitter()
cph2.fit(df_dummies_temp[['time_sx', 'failure', 'grouping_0', 'grouping_2', 'grouping_3', 'anxiety', 'history_sleep_problems', 'time_since_injury']], duration_col='time_sx', event_col='failure')
cph2.print_summary(decimal_places=4)

summary_df2 = cph2.summary.round(4)
print(summary_df2)


######################


# KM Curve
kmf = KaplanMeierFitter()
plt.figure(figsize=(8, 6))
n = len(df)
kmf.fit(durations=df['time_sx'], event_observed=df['failure'], label=f"All Participants (n={n})")
kmf.plot_survival_function(ci_show=True)
plt.xlabel('Time to Event (i.e., Symptom Resolution)')
plt.ylabel('Survival Probability')
plt.legend()
plt.tight_layout()
plt.savefig(
    "C:\\Users\\wingersm\\OneDrive - The University of Colorado Denver\\Desktop\\Python Projects\\8.0 Salfi Four Groups\\figs\\Survivial_curve.png", 
    dpi=300, bbox_inches='tight')
plt.show()


kmf = KaplanMeierFitter()
plt.figure(figsize=(8, 6))
for group_value in sorted(df['grouping_label'].unique()):
    mask = df['grouping_label'] == group_value
    n = mask.sum()
    kmf.fit(df.loc[mask, 'time_sx'], event_observed=df.loc[mask, 'failure'], label=f"{group_value} (n={n})")
    kmf.plot_survival_function(ci_show=False)
plt.xlabel('Time to Event (i.e., Symptom Resolution)')
plt.ylabel('Survival Probability')
plt.legend()
plt.tight_layout()
plt.savefig(
    "C:\\Users\\wingersm\\OneDrive - The University of Colorado Denver\\Desktop\\Python Projects\\8.0 Salfi Four Groups\\figs\\Figure1.png", 
    dpi=300, bbox_inches='tight')
plt.show()


## Plot Hazard Ratios
summary_df2['HR'] = summary_df2['exp(coef)']
summary_df2['HR_lower'] = summary_df2['exp(coef) lower 95%']
summary_df2['HR_upper'] = summary_df2['exp(coef) upper 95%']

ref_row = pd.DataFrame({
    'HR': [1.0],
    'HR_lower': [1.0],
    'HR_upper': [1.0]
}, index=['group_ref']) 

cph_plot_df = pd.concat([summary_df2[['HR', 'HR_lower', 'HR_upper']], ref_row])

custom_labels = {
    'grouping_0': '-Ex/+Sleep',
    'grouping_2': '-Ex/-Sleep',
    'grouping_3': '+Ex/-Sleep',
    'group_ref': '+Ex/+Sleep (reference group)',
    'anxiety': 'History of Anxiety',
    'history_sleep_problems': 'History of Sleep Problems',
    'time_since_injury': 'Days since injury'
}

custom_order = [
    '+Ex/+Sleep (reference group)',
    '-Ex/+Sleep',
    '-Ex/-Sleep',
    '+Ex/-Sleep',
    'History of Anxiety',
    'History of Sleep Problems',
    'Days since injury'
]

cph_plot_df['label'] = cph_plot_df.index.map(custom_labels.get)

cph_plot_df['label'] = pd.Categorical(cph_plot_df['label'], categories=custom_order[::-1], ordered=True)

cph_plot_df = cph_plot_df.sort_values('label')

plt.figure(figsize=(8, 6))
plt.errorbar(
    cph_plot_df['HR'],
    cph_plot_df['label'],
    xerr=[cph_plot_df['HR'] - cph_plot_df['HR_lower'],
          cph_plot_df['HR_upper'] - cph_plot_df['HR']],
    fmt='o', color='black', ecolor='black', capsize=4, markerfacecolor='lightgray'
)
plt.axvline(x=1, color='black', linestyle='--')
plt.xlabel('Hazard Ratio', color='black', fontweight='bold')
ticks = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 2]
ax = plt.gca()
ax.xaxis.set_major_locator(FixedLocator(ticks))
ax.xaxis.set_major_formatter(ScalarFormatter())
plt.ticklabel_format(style='plain', axis='x') 
plt.tight_layout()
plt.savefig(
    "C:\\Users\\wingersm\\OneDrive - The University of Colorado Denver\\Desktop\\Python Projects\\8.0 Salfi Four Groups\\figs\\Figure2.png", 
    dpi=300, bbox_inches='tight')
plt.show()