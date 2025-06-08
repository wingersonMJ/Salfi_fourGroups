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

We first compared the demographic, clinical, and injury characteristics of these four groups univariately using Analysis of Variance (ANOVA) and Chi-Squared tests. Post-hoc tests were used to evaluate differences between individual groups, with p-values adjusted for multiple comparisons using Tukey's HSD. We then used Cox Proportional Hazards (Cox PH) models to compare symptom resolution time between the four groups in a time-to-event analysis. The first Cox PH model was unadjusted and included only the four groups as predictors of time to symptom resolution. The second model was adjusted and included covariates that univariably differed between groups. To avoid multicollinearity between predictors in the adjusted model, only one variable representing acute symptom severity was included (i.e., the adjusted model would not include headache severity and HBI score, given the strong correlation between these variables and risk of variance inflation if both are included as predictors). 

All statistical tests were two-sided and evaluated at an alpha level of 0.05. Analysis was conducted in Python.

---

# Results

**Table 1:** Demographics and injury characteristics for patients enrolled in the study. 
|                               |           | Missing   | Overall       | +Ex/+Sleep    | +Ex/-Sleep    | -Ex/+Sleep    | -Ex/-Sleep    | P-Value |
|-------------------------------|-----------|-----------|---------------|---------------|---------------|---------------|---------------|---------|
| n                             |           |           | 335           | 46            | 9             | 184           | 96            |         | 
| Days since injury, mean (SD)  |           | 0         | 8.64 (5.27)   | 10.59 (5.21)  | 12.78 (5.43)  | 7.97 (4.98)   | 8.61 (5.51)   | 0.0018  |
| Sex, n (%)                    | female    |           | 208 (62.09)   | 25 (54.35)    | 4 (44.44)     | 124 (67.39)   | 55 (57.29)    | 0.1388  |
|                               | male      |           | 127 (37.91)   | 21 (45.65)    | 5 (55.56)     | 60 (32.61)    | 41 (42.71)    |         | 
| Age, mean (SD)                |           | 1         | 14.48 (2.26)  | 14.32 (2.28)  | 14.27 (2.92)  | 14.56 (2.30)  | 14.41 (2.14)  | 0.8800  |
| Concussion history, n (%)     | No        |           | 190 (56.72)   | 24 (52.17)    | 7 (77.78)     | 101 (54.89)   | 58 (60.42)    | 0.4238  |
|                               | Yes       |           | 145 (43.28)   | 22 (47.83)    | 2 (22.22)     | 83 (45.11)    | 38 (39.58)    |         | 
| Time to symptom resolution, mean (SD)|    | 0         | 21.46 (23.47) | 12.85 (10.51) | 58.33 (89.40) | 21.02 (20.49) | 22.96 (15.34) | <0.0001 |   
| Presisting Symptoms, n (%)    | No        |           | 268 (80.00)   | 44 (95.65)    | 4 (44.44)     | 148 (80.43)   | 72 (75.00)    | 0.0013  |   
|                               | Yes       |           | 67 (20.00)    | 2 (4.35)      | 5 (55.56)     | 36 (19.57)    | 24 (25.00)    |         |  
| Time to RTP, mean (SD)        |           | 39        | 31.04 (26.41) | 22.87 (12.31) | 71.44 (89.90) | 30.16 (20.13) | 32.19 (24.88) | <0.0001 |   
| Anxiety history, n (%)        | No        |           | 309 (92.24)   | 45 (97.83)    | 9 (100.00)    | 174 (94.57)   | 81 (84.38)    | 0.0060  | 
|                               | Yes       |           | 26 (7.76)     | 1 (2.17)      | 0 (0.00)      | 10 (5.43)     | 15 (15.62)    |         | 
| Depression history, n (%)     | No        |           | 321 (95.82)   | 44 (95.65)    | 9 (100.00)    | 178 (96.74)   | 90 (93.75)    | 0.6125  |
|                               | Yes       |           | 14 (4.18)     | 2 (4.35)      | 0 (0.00)      | 6 (3.26)      | 6 (6.25)      |         | 
| Proportion with headache, n (%)| No       |           | 70 (20.90)    | 27 (58.70)    | 1 (11.11)     | 36 (19.57)    | 6 (6.25)      | <0.0001 |   
|                               | Yes       |           | 265 (79.10)   | 19 (41.30)    | 8 (88.89)     | 148 (80.43)   | 90 (93.75)    |         |  
| Headache severity (0 to 10 scale), mean (SD)|| 0      | 2.95 (2.61)   | 1.22 (1.97)   | 3.89 (3.22)   | 2.73 (2.52)   | 4.10 (2.46)   | <0.0001 |   
| History of sleep problems, n (%) | No     |           | 306 (91.34)   | 44 (95.65)    | 6 (66.67)     | 179 (97.28)   | 77 (80.21)    | <0.0001 |
|                               | Yes       |           | 28 (8.36)     | 2 (4.35)      | 2 (22.22)     | 5 (2.72)      | 19 (19.79)    |         |  
|                               | Missing   |           | 1 (0.30)      | 0 (0.00)      | 1 (11.11)     | 0 (0.00)      | 0 (0.00)      |         | 
| HBI total, mean (SD)          |           | 4         | 19.58 (12.94) | 10.95 (10.79) | 26.11 (11.37) | 17.84 (11.94) | 26.23 (12.55) | <0.0001 | 


**Group codes**
0: '-Ex/+Sleep',
1: '+Ex/+Sleep',
2: '-Ex/-Sleep',
3: '+Ex/-Sleep'

Presisting Symptoms:
  Group 0 vs 1: p = 0.0236
  Group 0 vs 3: p = 0.0308
  Group 0 vs 2: p = 0.3689
  Group 1 vs 3: p = 0.0002
  Group 1 vs 2: p = 0.0060
  Group 3 vs 2: p = 0.1163

Anxiety history:
  Group 0 vs 1: p = 0.5887
  Group 0 vs 3: p = 1.0000
  Group 0 vs 2: p = 0.0089
  Group 1 vs 3: p = 1.0000
  Group 1 vs 2: p = 0.0367
  Group 3 vs 2: p = 0.4338

Proportion with headache:
  Group 0 vs 1: p = 0.0000
  Group 0 vs 3: p = 0.8450
  Group 0 vs 2: p = 0.0053
  Group 1 vs 3: p = 0.0246
  Group 1 vs 2: p = 0.0000
  Group 3 vs 2: p = 1.0000

History of sleep problems:
  Group 0 vs 1: p = 0.9236
  Group 0 vs 3: p = 0.0000
  Group 0 vs 2: p = 0.0000
  Group 1 vs 3: p = 0.0105
  Group 1 vs 2: p = 0.0297
  Group 3 vs 2: p = 0.0043

Days since injury: 
group1 group2 meandiff p-adj   lower  upper  reject
     0      1   2.6196 0.0124  0.4157 4.8234   True
     0      2   0.6472 0.7536  -1.036 2.3304  False
     0      3   4.8104 0.0344  0.2463 9.3745   True
     1      2  -1.9724 0.1475 -4.3697  0.425  False
     1      3   2.1908 0.6519 -2.6821 7.0637  False
     2      3   4.1632 0.0986 -0.4974 8.8238  False

Time to RTP:
group1 group2 meandiff p-adj   lower    upper  reject
     0      1  -7.2887 0.3749 -18.9914   4.414  False
     0      2   2.0256 0.9326  -6.7282 10.7793  False
     0      3   41.284    0.0  18.8143 63.7536   True
     1      2   9.3143 0.2302  -3.3521 21.9806  False
     1      3  48.5726    0.0  24.3097 72.8356   True
     2      3  39.2584 0.0001  16.2722 62.2446   True

headache_severity: 
group1 group2 meandiff p-adj   lower   upper  reject
     0      1  -1.5163 0.0012 -2.5615 -0.4712   True
     0      2   1.3705 0.0001  0.5722  2.1687   True
     0      3   1.1552  0.514 -1.0093  3.3197  False
     1      2   2.8868    0.0  1.7498  4.0237   True
     1      3   2.6715  0.016  0.3606  4.9824   True
     2      3  -0.2153 0.9944 -2.4255   1.995  False

HBI_total: 
group1 group2 meandiff p-adj   lower    upper  reject
     0      1  -6.8861 0.0038 -12.0754 -1.6968   True
     0      2   8.3885    0.0   4.4921  12.285   True
     0      3   8.2705  0.181  -2.2777 18.8186  False
     1      2  15.2746    0.0    9.651 20.8983   True
     1      3  15.1566 0.0034   3.8558 26.4573   True
     2      3  -0.1181    1.0 -10.8866 10.6504  False


---

## Unadjusted Cox PH

|           |coef       |exp(coef)    |se(coef)    | coef lower 95%  | coef upper 95% | exp(coef) lower 95%   | exp(coef) upper 95%   | p-value |
|-----------|-----------|-------------|------------|-----------------|----------------|-----------------------|-----------------------|---------|
|covariate  |           |             |            |                 |                |                       |                       |         |
|grouping_0 |-0.5882    |  0.5553     | 0.17       |    -0.92        |   -0.26        |        0.4002         |            0.7706     | 0.0004  |
|grouping_2 |-0.7262    |  0.4837     | 0.18       |    -1.08        |   -0.37        |        0.3393         |            0.6897     | 0.0001  |
|grouping_3 |-1.3974    |  0.2472     | 0.39       |    -2.16        |   -0.63        |        0.1153         |            0.5301     | 0.0003  |

--- 

## KM Curve


---

## Adjusted Cox PH

|           |coef       |exp(coef)    |se(coef)    | coef lower 95%  | coef upper 95% | exp(coef) lower 95%   | exp(coef) upper 95%   | p-value |
|-----------|-----------|-------------|------------|-----------------|----------------|-----------------------|-----------------------|---------|
|covariate  |           |             |            |                 |                |                       |                       |         |
|grouping_0 |-0.8041    |  0.5553     | 0.17       |    -0.92        |   -0.26        |        0.4002         |            0.7706     | 0.0004  |
|grouping_2 |-0.9173    |  0.4837     | 0.18       |    -1.08        |   -0.37        |        0.3393         |            0.6897     | 0.0001  |
|grouping_3 |-1.4876    |  0.2472     | 0.39       |    -2.16        |   -0.63        |        0.1153         |            0.5301     | 0.0003  |
|anxiety hx |-0.0118    |  0.2472     | 0.39       |    -2.16        |   -0.63        |        0.1153         |            0.5301     | 0.0003  |
|sleep prob hx|0.1393  |  0.2472     | 0.39       |    -2.16        |   -0.63        |        0.1153         |            0.5301     | 0.0003  |
|time_since_injury|-0.0762|0.2472     | 0.39       |    -2.16        |   -0.63        |        0.1153         |            0.5301     | 0.0003  |




                          coef  exp(coef)  se(coef)  coef lower 95%  coef upper 95%  exp(coef) lower 95%  exp(coef) upper 95%  cmp to       z       p  -log2(p)
covariate                                                                                                                                                      
grouping_0             -0.8041     0.4475    0.1707         -1.1388         -0.4695               0.3202               0.6253     0.0 -4.7098  0.0000   18.6212
grouping_2             -0.9173     0.3996    0.1899         -1.2896         -0.5450               0.2754               0.5798     0.0 -4.8296  0.0000   19.4797
grouping_3             -1.4876     0.2259    0.4223         -2.3154         -0.6598               0.0987               0.5169     0.0 -3.5223  0.0004   11.1907
anxiety                -0.0118     0.9883    0.2096         -0.4226          0.3990               0.6553               1.4903     0.0 -0.0563  0.9551    0.0663
history_sleep_problems  0.1393     1.1494    0.2115         -0.2752          0.5537               0.7594               1.7397     0.0  0.6587  0.5101    0.9711
time_since_injury      -0.0762     0.9266    0.0114         -0.0986         -0.0538               0.9061               0.9476     0.0 -6.6592  0.0000   35.0804


---

## Cox PH HR figure 


---



1. Update adjusted cox PH table
2. Add figure captions for cox PH tables
3. Interpret cox ph results
4. Add in KM curve
5. Interpret KM curve
6. Add in Cox PH HR figure
7. Clean code and add in
8. Add in original abstract

