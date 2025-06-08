# The combined effect of sleep and exercise on adolescent patients recovering from concussion
Wingerson, MJ  
mat.wingerson@gmail.com

# Description 
Transparency of source code and results for a manuscript submitted to [journal tbd]. 

[Add citation when accepted]

---

# Overview

## Background:

The primary focus of concussion rehabilitation and clinical management is to facilitate a timely resolution of symptoms, particularly among adolescent patients.[[ref]](https://bjsm.bmj.com/content/57/11/695) Evidence-based rehabilitation protocols designed to aid in symptom resolution have been previously established,[[ref]](https://bjsm.bmj.com/content/57/12/771) with the most common approach being engagement in early post-injury aerobic exercise as symptoms allow.[[ref]](https://bjsm.bmj.com/content/57/12/762). However, emerging evidence suggests other lifestyle factors may similarly affect post-concussion symptoms. For example, sleep disturbances are common among adolescents after concussion, and those who sleep better post-injury recover faster.[[ref]](https://pubmed.ncbi.nlm.nih.gov/34145161/).

Although past work has established the role of exercise and sleep in recovery, independent of each other, no research has explored the potential combined effect of sleep and exercise on post-concussion symptom resolution. 

## Objectives: 

Our primary objective was to compare symptom resolution time between adolescents with concussion who reported engaging in exercise *and* sleeping well after injury to those who reported one or neither of these pro-recovery behaviors. 

Our secondary objective was to identify demographic, medical history, and injury characteristics that predict which patients are most likely to engage in both early exercise and quality sleep post-concussion. 

---

## Statistical methods

We grouped patients based on their self-reported sleep and exercise behaviors at the patient's initial post-injury clinical visit (within 21 days of concussion). Patients indicated whether they had engaged in aerobic exercise since their injury (yes or no), and also reported whether they experienced sleep problems during the same timeframe (yes = sleeping poorly; no = sleeping well). Based on these responses, we grouped participants as exercising and sleeping well (+Ex/+Sleep), not exercising and sleeping well (-Ex/+Sleep), exercising and sleeping poorly (+Ex/-Sleep), and not exercising and sleeping poorly (-Ex/-Sleep). 

We first compared the demographic, clinical, and injury characteristics of these four groups univariately using Analysis of Variance (ANOVA) and Chi-Squared tests. We then used Cox Proportional Hazards (Cox PH) models to compare symptom resolution time between the four groups in a time-to-event analysis. The first Cox PH model was unadjusted and included only the four groups as predictors of time to symptom resolution. The second model was adjusted and included covariates that univariably differed between groups. To avoid multicollinearity between predictors in the adjusted model, only one variable representing acute symptom severity was included (i.e., the adjusted model would not include headache severity and HBI score, given the strong correlation between these variables and risk of variance inflation if both are included as predictors). 

---

# Results

**Table 1:** Demographics and injury characteristics for patients enrolled in the study. 
|                               |           | Missing   | Overall       | +Ex/+Sleep    | +Ex/-Sleep    | -Ex/+Sleep    | -Ex/-Sleep    | P-Value |
|-------------------------------|-----------|-----------|---------------|---------------|---------------|---------------|---------------|---------|
| n                             |           |           | 335           | 46            | 9             | 184           | 96            |         | 
| Days since injury, mean (SD)  |           | 0         | 8.64 (5.27)   | 10.59 (5.21)  | 12.78 (5.43)  | 7.97 (4.98)   | 8.61 (5.51)   | 0.0018  |
| Sex, n (%)                    | female    |           | 208 (62.09)   | 25 (54.35)    | 4 (44.44)     | 124 (67.39)   | 55 (57.29)    | 0.1388  |
|                               | male      |           | 127 (37.91)   | 21 (45.65)    | 5 (55.56)     | 60 (32.61)    | 41 (42.71)    |         | 
| age, mean (SD)                |           | 1         | 14.48 (2.26)  | 14.32 (2.28)  | 14.27 (2.92)  | 14.56 (2.30)  | 14.41 (2.14)  | 0.8800  |
| concussion history, n (%)     | No        |           | 190 (56.72)   | 24 (52.17)    | 7 (77.78)     | 101 (54.89)   | 58 (60.42)    | 0.4238  |
|                               | Yes       |           | 145 (43.28)   | 22 (47.83)    | 2 (22.22)     | 83 (45.11)    | 38 (39.58)    |         | 
| Time to symptom resolution, mean (SD)|    | 0         | 21.46 (23.47) | 12.85 (10.51) | 58.33 (89.40) | 21.02 (20.49) | 22.96 (15.34) | <0.0001 |   
| Presisting Sytmptoms, n (%)   | No        |           | 268 (80.00)   | 44 (95.65)    | 4 (44.44)     | 148 (80.43)   | 72 (75.00)    | 0.0013  |   
|                               | Yes       |           | 67 (20.00)    | 2 (4.35)      | 5 (55.56)     | 36 (19.57)    | 24 (25.00)    |         |  
| Time to RTP, mean (SD)        |           | 39        | 31.04 (26.41) | 22.87 (12.31) | 71.44 (89.90) | 30.16 (20.13) | 32.19 (24.88) | <0.0001 |   
| anxiety hx, n (%)             | No        |           | 309 (92.24)   | 45 (97.83)    | 9 (100.00)    | 174 (94.57)   | 81 (84.38)    | 0.0060  | 
|                               | Yes       |           | 26 (7.76)     | 1 (2.17)      | 0 (0.00)      | 10 (5.43)     | 15 (15.62)    |         | 
| depression hx, n (%)          | No        |           | 321 (95.82)   | 44 (95.65)    | 9 (100.00)    | 178 (96.74)   | 90 (93.75)    | 0.6125  |
|                               | Yes       |           | 14 (4.18)     | 2 (4.35)      | 0 (0.00)      | 6 (3.26)      | 6 (6.25)      |         | 
| headaches, n (%)              | No        |           | 70 (20.90)    | 27 (58.70)    | 1 (11.11)     | 36 (19.57)    | 6 (6.25)      | <0.0001 |   
|                               | Yes       |           | 265 (79.10)   | 19 (41.30)    | 8 (88.89)     | 148 (80.43)   | 90 (93.75)    |         |  
| headache_severity (0 to 10), mean (SD)|   | 0         | 2.95 (2.61)   | 1.22 (1.97)   | 3.89 (3.22)   | 2.73 (2.52)   | 4.10 (2.46)   | <0.0001 |   
| history of sleep problems, n (%) | No     |           | 306 (91.34)   | 44 (95.65)    | 6 (66.67)     | 179 (97.28)   | 77 (80.21)    | <0.0001 |
|                               | Yes       |           | 28 (8.36)     | 2 (4.35)      | 2 (22.22)     | 5 (2.72)      | 19 (19.79)    |         |  
|                               | Missing   |           | 1 (0.30)      | 0 (0.00)      | 1 (11.11)     | 0 (0.00)      | 0 (0.00)      |         | 
| HBI_total, mean (SD)          |           | 4         | 19.58 (12.94) | 10.95 (10.79) | 26.11 (11.37) | 17.84 (11.94) | 26.23 (12.55) | <0.0001 | 
| hbi_somatic, mean (SD)        |           | 4         | 8.91 (5.89)   | 5.11 (4.91)   | 12.89 (5.13)  | 7.99 (5.31)   | 12.02 (5.85)  |         |
| hbi_cognitive, mean (SD)      |           | 4         | 10.67 (8.14)  | 5.84 (6.63)   | 13.22 (7.48)  | 9.85 (7.78)   | 14.21 (8.07)  |         |


    0: '-Ex/+Sleep',
    1: '+Ex/+Sleep',
    2: '-Ex/-Sleep',
    3: '+Ex/-Sleep'


    

PPCS:
  Group 0 vs 1: p = 0.0236
  Group 0 vs 3: p = 0.0308
  Group 0 vs 2: p = 0.3689
  Group 1 vs 3: p = 0.0002
  Group 1 vs 2: p = 0.0060
  Group 3 vs 2: p = 0.1163


anxiety:
  Group 0 vs 1: p = 0.5887
  Group 0 vs 3: p = 1.0000
  Group 0 vs 2: p = 0.0089
  Group 1 vs 3: p = 1.0000
  Group 1 vs 2: p = 0.0367
  Group 3 vs 2: p = 0.4338


headaches:
  Group 0 vs 1: p = 0.0000
  Group 0 vs 3: p = 0.8450
  Group 0 vs 2: p = 0.0053
  Group 1 vs 3: p = 0.0246
  Group 1 vs 2: p = 0.0000
  Group 3 vs 2: p = 1.0000


history_sleep_problems:
  Group 0 vs 1: p = 0.9236
  Group 0 vs 3: p = 0.0000
  Group 0 vs 2: p = 0.0000
  Group 1 vs 3: p = 0.0105
  Group 1 vs 2: p = 0.0297
  Group 3 vs 2: p = 0.0043




time_since_injury: ANOVA F = 5.12, p = 0.0018
Multiple Comparison of Means - Tukey HSD, FWER=0.05
===================================================
group1 group2 meandiff p-adj   lower  upper  reject
---------------------------------------------------
     0      1   2.6196 0.0124  0.4157 4.8234   True
     0      2   0.6472 0.7536  -1.036 2.3304  False
     0      3   4.8104 0.0344  0.2463 9.3745   True
     1      2  -1.9724 0.1475 -4.3697  0.425  False
     1      3   2.1908 0.6519 -2.6821 7.0637  False
     2      3   4.1632 0.0986 -0.4974 8.8238  False
---------------------------------------------------

age: ANOVA F = 0.22, p = 0.8800
number_prior_conc: ANOVA F = 0.23, p = 0.8749
time_sx: ANOVA F = 10.43, p = 0.0000
Multiple Comparison of Means - Tukey HSD, FWER=0.05 
====================================================
group1 group2 meandiff p-adj   lower   upper  reject
----------------------------------------------------
     0      1  -8.1739 0.1253 -17.767  1.4192  False
     0      2   1.9366 0.9037 -5.3903  9.2635  False
     0      3  37.3116    0.0 17.4446 57.1786   True
     1      2  10.1105 0.0615  -0.325  20.546  False
     1      3  45.4855    0.0 24.2743 66.6967   True
     2      3   35.375 0.0001 15.0878 55.6622   True
----------------------------------------------------

time_rtp: ANOVA F = 9.06, p = 0.0000
 Multiple Comparison of Means - Tukey HSD, FWER=0.05 
=====================================================
group1 group2 meandiff p-adj   lower    upper  reject
-----------------------------------------------------
     0      1  -7.2887 0.3749 -18.9914   4.414  False
     0      2   2.0256 0.9326  -6.7282 10.7793  False
     0      3   41.284    0.0  18.8143 63.7536   True
     1      2   9.3143 0.2302  -3.3521 21.9806  False
     1      3  48.5726    0.0  24.3097 72.8356   True
     2      3  39.2584 0.0001  16.2722 62.2446   True
-----------------------------------------------------

headache_severity: ANOVA F = 15.62, p = 0.0000
Multiple Comparison of Means - Tukey HSD, FWER=0.05 
====================================================
group1 group2 meandiff p-adj   lower   upper  reject
----------------------------------------------------
     0      1  -1.5163 0.0012 -2.5615 -0.4712   True
     0      2   1.3705 0.0001  0.5722  2.1687   True
     0      3   1.1552  0.514 -1.0093  3.3197  False
     1      2   2.8868    0.0  1.7498  4.0237   True
     1      3   2.6715  0.016  0.3606  4.9824   True
     2      3  -0.2153 0.9944 -2.4255   1.995  False
----------------------------------------------------

bess_hard1: ANOVA F = 1.83, p = 0.1424
bess_hard2: ANOVA F = 4.62, p = 0.0035
Multiple Comparison of Means - Tukey HSD, FWER=0.05
===================================================
group1 group2 meandiff p-adj   lower  upper  reject
---------------------------------------------------
     0      1  -1.1634 0.1071 -2.4865 0.1597  False
     0      2   0.7921  0.179 -0.2154 1.7997  False
     0      3   1.2366 0.6407 -1.4727 3.9458  False
     1      2   1.9556 0.0028  0.5206 3.3906   True
     1      3      2.4 0.1426 -0.4955 5.2955  False
     2      3   0.4444 0.9759 -2.3212 3.2101  False
---------------------------------------------------

bess_hard3: ANOVA F = 5.97, p = 0.0006
Multiple Comparison of Means - Tukey HSD, FWER=0.05
===================================================
group1 group2 meandiff p-adj   lower  upper  reject
---------------------------------------------------
     0      1     -1.1 0.0568 -2.2215 0.0215  False
     0      2   0.8617 0.0485   0.004 1.7194   True
     0      3   0.0556 0.9999 -2.2389 2.3501  False
     1      2   1.9617 0.0002  0.7446 3.1788   True
     1      3   1.1556 0.6163  -1.296 3.6072  False
     2      3  -0.8061 0.8107 -3.1488 1.5365  False
---------------------------------------------------

BESS_total: ANOVA F = 6.64, p = 0.0002
Multiple Comparison of Means - Tukey HSD, FWER=0.05 
====================================================
group1 group2 meandiff p-adj   lower   upper  reject
----------------------------------------------------
     0      1  -2.5219 0.0321 -4.8934 -0.1505   True
     0      2   1.8243 0.0454  0.0253  3.6232   True
     0      3   1.1801 0.9209 -3.6241  5.9842  False
     1      2   4.3462 0.0001  1.7792  6.9133   True
     1      3    3.702 0.2477 -1.4393  8.8434  False
     2      3  -0.6442 0.9865 -5.5479  4.2595  False
----------------------------------------------------

HBI_total: ANOVA F = 19.69, p = 0.0000
 Multiple Comparison of Means - Tukey HSD, FWER=0.05 
=====================================================
group1 group2 meandiff p-adj   lower    upper  reject
-----------------------------------------------------
     0      1  -6.8861 0.0038 -12.0754 -1.6968   True
     0      2   8.3885    0.0   4.4921  12.285   True
     0      3   8.2705  0.181  -2.2777 18.8186  False
     1      2  15.2746    0.0    9.651 20.8983   True
     1      3  15.1566 0.0034   3.8558 26.4573   True
     2      3  -0.1181    1.0 -10.8866 10.6504  False
-----------------------------------------------------

HBI_total_parent: ANOVA F = 18.31, p = 0.0000
 Multiple Comparison of Means - Tukey HSD, FWER=0.05 
=====================================================
group1 group2 meandiff p-adj   lower    upper  reject
-----------------------------------------------------
     0      1   -6.702  0.002 -11.4873 -1.9168   True
     0      2   6.2681 0.0001   2.5825  9.9536   True
     0      3  14.4408 0.0031   3.7668 25.1149   True
     1      2  12.9701    0.0   7.7644 18.1758   True
     1      3  21.1429    0.0   9.8534 32.4323   True
     2      3   8.1728 0.2125  -2.6963 19.0418  False
-----------------------------------------------------

hbi_attention: ANOVA F = 17.49, p = 0.0000
Multiple Comparison of Means - Tukey HSD, FWER=0.05 
====================================================
group1 group2 meandiff p-adj   lower   upper  reject
----------------------------------------------------
     0      1   -0.547 0.0058 -0.9743 -0.1197   True
     0      2   0.6567    0.0  0.3388  0.9746   True
     0      3   0.3755 0.6733 -0.4851   1.236  False
     1      2   1.2037    0.0  0.7413  1.6662   True
     1      3   0.9225 0.0505 -0.0013  1.8463  False
     2      3  -0.2812 0.8418 -1.1598  0.5973  False
----------------------------------------------------



---










|                               |           | Missing   | Overall       | +Ex/+Sleep    | +Ex/-Sleep    | -Ex/+Sleep    | -Ex/-Sleep    | 
|-------------------------------|-----------|-----------|---------------|---------------|---------------|---------------|---------------|
| n                             |           |           | 335           | 46            | 9             | 184           | 96            |           
| month, n (%)                  | April     |           | 26 (7.76)     | 5 (10.87)     | 1 (11.11)     | 13 (7.07)     | 7 (7.29)      |  
|                               | August    |           | 25 (7.46)     | 2 (4.35)      | 0 (0.00)      | 15 (8.15)     | 8 (8.33)      |           
|                               | December  |           | 23 (6.87)     | 3 (6.52)      | 0 (0.00)      | 14 (7.61)     | 6 (6.25)      |           
|                               | February  |           | 21 (6.27)     | 2 (4.35)      | 1 (11.11)     | 14 (7.61)     | 4 (4.17)      |           
|                               | January   |           | 44 (13.13)    | 8 (17.39)     | 0 (0.00)      | 19 (10.33)    | 17 (17.71)    |           
|                               | July      |           | 20 (5.97)     | 5 (10.87)     | 0 (0.00)      | 10 (5.43)     | 5 (5.21)      |           
|                               | June      |           | 31 (9.25)     | 3 (6.52)      | 1 (11.11)     | 18 (9.78)     | 9 (9.38)      |           
|                               | March     |           | 25 (7.46)     | 4 (8.70)      | 0 (0.00)      | 14 (7.61)     | 7 (7.29)      |           
|                               | May       |           | 35 (10.45)    | 7 (15.22)     | 0 (0.00)      | 21 (11.41)    | 7 (7.29)      |           
|                               | November  |           | 16 (4.78)     | 1 (2.17)      | 1 (11.11)     | 8 (4.35)      | 6 (6.25)      |           
|                               | October   |           | 32 (9.55)     | 2 (4.35)      | 4 (44.44)     | 17 (9.24)     | 9 (9.38)      |           
|                               | September |           | 37 (11.04)    | 4 (8.70)      | 1 (11.11)     | 21 (11.41)    | 11 (11.46)    |           
| summer, n (%)                 | 0         |           | 259 (77.31)   | 36 (78.26)    | 8 (88.89)     | 141 (76.63)   | 74 (77.08)    |   
|                               | 1         |           | 76 (22.69)    | 10 (21.74)    | 1 (11.11)     | 43 (23.37)    | 22 (22.92)    |           
| sport, n (%)                  | 1         |           | 69 (20.60)    | 10 (21.74)    | 0 (0.00)      | 40 (21.74)    | 19 (19.79)    |    
|                               | 11        |           | 2 (0.60)      | 1 (2.17)      | 0 (0.00)      | 1 (0.54)      | 0 (0.00)      |           
|                               | 12        |           | 10 (2.99)     | 2 (4.35)      | 1 (11.11)     | 4 (2.17)      | 3 (3.12)      |           
|                               | 13        |           | 7 (2.09)      | 0 (0.00)      | 0 (0.00)      | 1 (0.54)      | 6 (6.25)      |           
|                               | 14        |           | 10 (2.99)     | 2 (4.35)      | 0 (0.00)      | 6 (3.26)      | 2 (2.08)      |           
|                               | 17        |           | 2 (0.60)      | 0 (0.00)      | 0 (0.00)      | 1 (0.54)      | 1 (1.04)      |           
|                               | 18        |           | 32 (9.55)     | 3 (6.52)      | 0 (0.00)      | 19 (10.33)    | 10 (10.42)    |           
|                               | 19        |           | 1 (0.30)      | 0 (0.00)      | 0 (0.00)      | 1 (0.54)      | 0 (0.00)      |           
|                               | 2         |           | 83 (24.78)    | 12 (26.09)    | 1 (11.11)     | 51 (27.72)    | 19 (19.79)    |           
|                               | 20        |           | 14 (4.18)     | 1 (2.17)      | 0 (0.00)      | 11 (5.98)     | 2 (2.08)      |           
|                               | 23        |           | 1 (0.30)      | 0 (0.00)      | 0 (0.00)      | 0 (0.00)      | 1 (1.04)      |           
|                               | 24        |           | 11 (3.28)     | 2 (4.35)      | 3 (33.33)     | 3 (1.63)      | 3 (3.12)      |           
|                               | 25        |           | 3 (0.90)      | 0 (0.00)      | 0 (0.00)      | 1 (0.54)      | 2 (2.08)      |           
|                               | 27        |           | 6 (1.79)      | 2 (4.35)      | 0 (0.00)      | 3 (1.63)      | 1 (1.04)      |           
|                               | 28        |           | 18 (5.37)     | 3 (6.52)      | 1 (11.11)     | 9 (4.89)      | 5 (5.21)      |           
|                               | 29        |           | 12 (3.58)     | 1 (2.17)      | 2 (22.22)     | 6 (3.26)      | 3 (3.12)      |           
|                               | 3         |           | 3 (0.90)      | 0 (0.00)      | 0 (0.00)      | 1 (0.54)      | 2 (2.08)      |           
|                               | 30        |           | 3 (0.90)      | 0 (0.00)      | 0 (0.00)      | 2 (1.09)      | 1 (1.04)      |           
|                               | 31        |           | 1 (0.30)      | 0 (0.00)      | 0 (0.00)      | 1 (0.54)      | 0 (0.00)      |           
|                               | 32        |           | 3 (0.90)      | 0 (0.00)      | 0 (0.00)      | 3 (1.63)      | 0 (0.00)      |           
|                               | 33        |           | 3 (0.90)      | 0 (0.00)      | 0 (0.00)      | 2 (1.09)      | 1 (1.04)      |           
|                               | 35        |           | 3 (0.90)      | 1 (2.17)      | 0 (0.00)      | 1 (0.54)      | 1 (1.04)      |           
|                               | 4         |           | 5 (1.49)      | 0 (0.00)      | 0 (0.00)      | 2 (1.09)      | 3 (3.12)      |           
|                               | 5         |           | 7 (2.09)      | 4 (8.70)      | 0 (0.00)      | 0 (0.00)      | 3 (3.12)      |           
|                               | 6         |           | 8 (2.39)      | 0 (0.00)      | 0 (0.00)      | 6 (3.26)      | 2 (2.08)      |           
|                               | 7         |           | 17 (5.07)     | 2 (4.35)      | 1 (11.11)     | 9 (4.89)      | 5 (5.21)      |           
|                               | 8         |           | 1 (0.30)      | 0 (0.00)      | 0 (0.00)      | 0 (0.00)      | 1 (1.04)      |           
| add_adhd, n (%)               | 0.0       |           | 300 (89.55)   | 41 (89.13)    | 7 (77.78)     | 166 (90.22)   | 86 (89.58)    |   
|                               | 1.0       |           | 32 (9.55)     | 4 (8.70)      | 1 (11.11)     | 18 (9.78)     | 9 (9.38)      |           
|                               | None      |           | 3 (0.90)      | 1 (2.17)      | 1 (11.11)     | 0 (0.00)      | 1 (1.04)      |           
| ld_dyslexia, n (%)            | 0.0       |           | 311 (92.84)   | 43 (93.48)    | 8 (88.89)     | 173 (94.02)   | 87 (90.62)    |   
|                               | 1.0       |           | 23 (6.87)     | 3 (6.52)      | 1 (11.11)     | 10 (5.43)     | 9 (9.38)      |           
|                               | None      |           | 1 (0.30)      | 0 (0.00)      | 0 (0.00)      | 1 (0.54)      | 0 (0.00)      |           
| exercise_since_injury, n (%)  | 0         |           | 280 (83.58)   | 0 (0.00)      | 0 (0.00)      | 184 (100.00)  | 96 (100.00)   |   
|                               | 1         |           | 55 (16.42)    | 46 (100.00)   | 9 (100.00)    | 0 (0.00)      | 0 (0.00)      |           
| current_sleep_problems, n (%) | 0         |           | 230 (68.66)   | 46 (100.00)   | 0 (0.00)      | 184 (100.00)  | 0 (0.00)      |   
|                               | 1         |           | 105 (31.34)   | 0 (0.00)      | 9 (100.00)    | 0 (0.00)      | 96 (100.00)   |           



1, Football | 2, Soccer | 3, Gymnastics | 4, Volleyball | 5, Softball | 6, Baseball | 7, Lacrosse | 8, Swimming | 9, Diving | 10, Rock Climbing | 11, Biking (extreme/dirt bike/motor cross) | 12, Skiing | 13, Snowboarding | 14, Cheerleading | 15, Track & Field | 16, Cross Country | 17, Ultimate Frisbee | 18, Basketball | 19, Tennis | 20, Ice Hocky | 21, Field Hockey | 22, Ski Jumping | 23, Water Polo | 24, Wrestling | 25, Martial Arts | 26, Rodeo | 27, Rugby | 28, Not playing sport/MVA/Fall from height | 29, Other | 30, Equestrian | 31, Trampoline | 32, Ripstick/scooter/skateboard | 33, Gym Class-nonspecific physical activity | 34, Ice skating | 35, Dodgeball









--- 


<lifelines.CoxPHFitter: fitted with 335 total observations, 0 right-censored observations>
             duration col = 'time_sx'
                event col = 'failure'
      baseline estimation = breslow
   number of observations = 335
number of events observed = 335
   partial log-likelihood = -1605.85
         time fit was run = 2025-06-08 15:03:06 UTC
           decimal_places = 4

---
            coef exp(coef)  se(coef)  coef lower 95%  coef upper 95% exp(coef) lower 95% exp(coef) upper 95%
covariate                                                                                                   
grouping_0 -0.59      0.56      0.17           -0.92           -0.26                0.40                0.77
grouping_2 -0.73      0.48      0.18           -1.08           -0.37                0.34                0.69
grouping_3 -1.40      0.25      0.39           -2.16           -0.63                0.12                0.53

            cmp to     z      p  -log2(p)
covariate                                
grouping_0    0.00 -3.52 <0.005     11.17
grouping_2    0.00 -4.01 <0.005     14.03
grouping_3    0.00 -3.59 <0.005     11.57
---
Concordance = 0.58
Partial AIC = 3217.69
log-likelihood ratio test = 21.43 on 3 df
-log2(p) of ll-ratio test = 13.51

              coef  exp(coef)  se(coef)  coef lower 95%  coef upper 95%  exp(coef) lower 95%  exp(coef) upper 95%  cmp to       z       p  -log2(p)
covariate                                                                                                                                          
grouping_0 -0.5882     0.5553    0.1672         -0.9159         -0.2605               0.4002               0.7706     0.0 -3.5184  0.0004   11.1694
grouping_2 -0.7262     0.4837    0.1810         -1.0809         -0.3715               0.3393               0.6897     0.0 -4.0131  0.0001   14.0267
grouping_3 -1.3974     0.2472    0.3892         -2.1602         -0.6346               0.1153               0.5301     0.0 -3.5907  0.0003   11.5662





--- 


<lifelines.CoxPHFitter: fitted with 334 total observations, 0 right-censored observations>
             duration col = 'time_sx'
                event col = 'failure'
      baseline estimation = breslow
   number of observations = 334
number of events observed = 334
   partial log-likelihood = -1576.34
         time fit was run = 2025-06-08 15:11:10 UTC
           decimal_places = 4

---
                        coef exp(coef)  se(coef)  coef lower 95%  coef upper 95% exp(coef) lower 95% exp(coef) upper 95%
covariate                                                                                                               
grouping_0             -0.80      0.45      0.17           -1.14           -0.47                0.32                0.63
grouping_2             -0.92      0.40      0.19           -1.29           -0.55                0.28                0.58
grouping_3             -1.49      0.23      0.42           -2.32           -0.66                0.10                0.52
anxiety                -0.01      0.99      0.21           -0.42            0.40                0.66                1.49
history_sleep_problems  0.14      1.15      0.21           -0.28            0.55                0.76                1.74
time_since_injury      -0.08      0.93      0.01           -0.10           -0.05                0.91                0.95

                        cmp to     z      p  -log2(p)
covariate                                            
grouping_0                0.00 -4.71 <0.005     18.62
grouping_2                0.00 -4.83 <0.005     19.48
grouping_3                0.00 -3.52 <0.005     11.19
anxiety                   0.00 -0.06   0.96      0.07
history_sleep_problems    0.00  0.66   0.51      0.97
time_since_injury         0.00 -6.66 <0.005     35.08
---
Concordance = 0.67
Partial AIC = 3164.67
log-likelihood ratio test = 68.82 on 6 df
-log2(p) of ll-ratio test = 40.35

                          coef  exp(coef)  se(coef)  coef lower 95%  coef upper 95%  exp(coef) lower 95%  exp(coef) upper 95%  cmp to       z       p  -log2(p)
covariate                                                                                                                                                      
grouping_0             -0.8041     0.4475    0.1707         -1.1388         -0.4695               0.3202               0.6253     0.0 -4.7098  0.0000   18.6212
grouping_2             -0.9173     0.3996    0.1899         -1.2896         -0.5450               0.2754               0.5798     0.0 -4.8296  0.0000   19.4797
grouping_3             -1.4876     0.2259    0.4223         -2.3154         -0.6598               0.0987               0.5169     0.0 -3.5223  0.0004   11.1907
anxiety                -0.0118     0.9883    0.2096         -0.4226          0.3990               0.6553               1.4903     0.0 -0.0563  0.9551    0.0663
history_sleep_problems  0.1393     1.1494    0.2115         -0.2752          0.5537               0.7594               1.7397     0.0  0.6587  0.5101    0.9711
time_since_injury      -0.0762     0.9266    0.0114         -0.0986         -0.0538               0.9061               0.9476     0.0 -6.6592  0.0000   35.0804






