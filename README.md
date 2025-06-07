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

1. Univariable comparisons via ANOVA and Chi X.
2. Cox Proportional Hazards model including univariable associated variables
3. Kaplan Meier curve
4. Logistic regression predicting +Ex/+Sleep group

---

# Results

**Table 1:** Demographics and injury characteristics for patients enrolled in the study. 
|                               |           | Missing   | Overall       | +Ex/+Sleep    | +Ex/-Sleep    | -Ex/+Sleep    | -Ex/-Sleep    |
|-------------------------------|-----------|-----------|---------------|---------------|---------------|---------------|---------------|
| n                             |           |           | 335           | 46            | 9             | 184           | 96            |           
| Days since injury, mean (SD)  |           | 0         | 8.64 (5.27)   | 10.59 (5.21)  | 12.78 (5.43)  | 7.97 (4.98)   | 8.61 (5.51)   |
| Sex, n (%)                    | female    |           | 208 (62.09)   | 25 (54.35)    | 4 (44.44)     | 124 (67.39)   | 55 (57.29)    | 
|                               | male      |           | 127 (37.91)   | 21 (45.65)    | 5 (55.56)     | 60 (32.61)    | 41 (42.71)    |           
| age, mean (SD)                |           | 1         | 14.48 (2.26)  | 14.32 (2.28)  | 14.27 (2.92)  | 14.56 (2.30)  | 14.41 (2.14)  | 
| concussion history, n (%)     | No        |           | 190 (56.72)   | 24 (52.17)    | 7 (77.78)     | 101 (54.89)   | 58 (60.42)    | 
|                               | Yes       |           | 145 (43.28)   | 22 (47.83)    | 2 (22.22)     | 83 (45.11)    | 38 (39.58)    |           
| Number of prior concussions, mean (SD)|   | 0         | 0.67 (0.93)   | 0.65 (0.79)   | 0.67 (1.41)   | 0.70 (0.98)   | 0.60 (0.85)   |      
| Time to symptom resolution, mean (SD)|    | 0         | 21.46 (23.47) | 12.85 (10.51) | 58.33 (89.40) | 21.02 (20.49) | 22.96 (15.34) |    
| Presisting Sytmptoms, n (%)   | No        |           | 268 (80.00)   | 44 (95.65)    | 4 (44.44)     | 148 (80.43)   | 72 (75.00)    |     
|                               | Yes       |           | 67 (20.00)    | 2 (4.35)      | 5 (55.56)     | 36 (19.57)    | 24 (25.00)    |           
| Time to RTP, mean (SD)        |           | 39        | 31.04 (26.41) | 22.87 (12.31) | 71.44 (89.90) | 30.16 (20.13) | 32.19 (24.88) |    
| anxiety hx, n (%)             | No        |           | 309 (92.24)   | 45 (97.83)    | 9 (100.00)    | 174 (94.57)   | 81 (84.38)    |     
|                               | Yes       |           | 26 (7.76)     | 1 (2.17)      | 0 (0.00)      | 10 (5.43)     | 15 (15.62)    |          
| depression hx, n (%)          | No        |           | 321 (95.82)   | 44 (95.65)    | 9 (100.00)    | 178 (96.74)   | 90 (93.75)    |     
|                               | Yes       |           | 14 (4.18)     | 2 (4.35)      | 0 (0.00)      | 6 (3.26)      | 6 (6.25)      |          
| headaches, n (%)              | No        |           | 70 (20.90)    | 27 (58.70)    | 1 (11.11)     | 36 (19.57)    | 6 (6.25)      |     
|                               | Yes       |           | 265 (79.10)   | 19 (41.30)    | 8 (88.89)     | 148 (80.43)   | 90 (93.75)    |           
| headache_severity (0 to 10), mean (SD)|   | 0         | 2.95 (2.61)   | 1.22 (1.97)   | 3.89 (3.22)   | 2.73 (2.52)   | 4.10 (2.46)   |    
| history of sleep problems, n (%) | No     |           | 306 (91.34)   | 44 (95.65)    | 6 (66.67)     | 179 (97.28)   | 77 (80.21)    |   
|                               | Yes       |           | 28 (8.36)     | 2 (4.35)      | 2 (22.22)     | 5 (2.72)      | 19 (19.79)    |           
|                               | Missing   |           | 1 (0.30)      | 0 (0.00)      | 1 (11.11)     | 0 (0.00)      | 0 (0.00)      |           
| BESS_total, mean (SD)         |           | 14        | 7.15 (5.58)   | 4.41 (4.36)   | 8.11 (4.94)   | 6.93 (5.24)   | 8.76 (6.24)   |     
| HBI_total, mean (SD)          |           | 4         | 19.58 (12.94) | 10.95 (10.79) | 26.11 (11.37) | 17.84 (11.94) | 26.23 (12.55) |  
| HBI_total_parent, mean (SD)   |           | 37        | 15.19 (11.60) | 7.29 (7.24)   | 28.43 (12.86) | 13.99 (10.84) | 20.26 (11.64) |    
| hbi_somatic, mean (SD)        |           | 4         | 8.91 (5.89)   | 5.11 (4.91)   | 12.89 (5.13)  | 7.99 (5.31)   | 12.02 (5.85)  |    
| hbi_cognitive, mean (SD)      |           | 4         | 10.67 (8.14)  | 5.84 (6.63)   | 13.22 (7.48)  | 9.85 (7.78)   | 14.21 (8.07)  |  





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


