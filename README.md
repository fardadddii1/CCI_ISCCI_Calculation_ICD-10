# Calculate Charlson Comorbidty Index and Ischemic Stroke Comorbity Index in Python
### This repository contains codes for calculating Charlson Comorbidty Index and Ischemic Stroke Comorbity Index

*Prepared by Fardad Mpusavi at SUNY Buffalo, Dec. 2021*

It is programmed to account for hierarchical calcualtion of the scores, quoting from literature:

" Calculation of the maximum score is based on a hierarchy where diabetes with complications supersedes diabetes without complications; moderate or severe liver disease supersedes mild liver disease; and metastatic solid tumor supersedes any malignancy"

The file is based on ICD-10-CM codes, but works with ICD-10 as well. The function are written to be readable and you can change the weights to make your own index. For ISchaemic Stroke comorbidity weights I used Table 2 of https://bit.ly/3PfhKEz. The program has been tested on over 30,000 observations and run time was 23 seconds. The output scores are validated with clinicians to ensure the accuracy. If you need to know the definition of codes in your file, use my webscraping code. 

### Requirements:
Python3

### Dependencies:

- Pandas
- Numpy


