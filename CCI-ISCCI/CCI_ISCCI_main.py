Created on Mon Dec 15 2021
@author: Fardad Mousavi

import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import math
import time
import CCI_calc as CCI_calc
import ISCCI_calc as ISCCI_calc

##### reading data from CMS MEDPAR
CMS_data = pd.read_excel(r'diagnosis.xlsx')
CMS_data_POA = pd.read_excel(r'POA_diagnosis.xlsx')

# Cleaning NAN
CMS_data_POA.fillna(0, inplace= True)
### Present on Admission (POA) day filtering - CMS_data_POA_filtered is the diagnosis for POA
CMS_data_POA_num = np.where(CMS_data_POA == 'Y', 1, 0)
CMS_data_POA_num
CMS_data_POA_filtered = np.where(CMS_data_POA == 'Y', CMS_data, 'fardadNPOA')

#Hierarchical Calculations

choice = []
while choice != 'CCI' or choice != 'ISCCI':
    choice = input('Would you like to calculate CCI or ISCCI? ')
    if choice == 'CCI':
        Same_cath_tup, wscore = CCI_calc()
        break
    elif choice == 'ISCCI':
        Same_cath_tup, wscore = ISCCI_calc()
        break
        
POA_choice = []

while POA_choice != 'yes' or POA_choice != 'no':
    POA_choice = input('Dou like to calculate the index for admission day? yes or no')
    if POA_choice == 'yes':
        print(f'{choice} index for admission day is being calculated')
        DCa = np.array(CMS_data_POA_filtered)
        break
    elif POA_choice == 'no':
        print(f'{choice} index for the whole stay time')
        DCa = np.array(CMS_data.fillna('0'))
        break

SC = np.zeros(np.shape(DCa))
SC_in = np.zeros(np.shape(DCa))-1

for t,k in enumerate(Same_cath_tup):
    
    for y in k:
        if 'x' in y:
            e = y.replace('x','')
            for w,x in enumerate(DCa):
                for p,r in enumerate(x):
                    if e in r:

                        SC[w][p] = wscore[y]
                        SC_in[w][p] = t
        elif 'x' not in y:
            for z,u in enumerate(DCa):
                for v,n in enumerate(u):
                    if y == n:
                        SC[z][v] = wscore[y]
                        SC_in[z][v] = t

for d,g in enumerate(SC_in):
    
    if 9 in g and 10 in g:
        SC[d][list(g).index(9)] = 0

    if 8 in g and 14 in g:
        SC[d][list(g).index(8)] = 0
        
    if 13 in g and 15 in g:
        SC[d][list(g).index(13)] = 0
                   
ind = SC.sum(1)

score = DataFrame (ind)
if choice == 'CCI':
    if POA_choice == 'yes':
        
        CMS_data ['CCI_POA'] = score
        
        CMS_data.to_csv('CCI_scores_POA.csv')
    else:
        CMS_data ['CCI_NOPOA'] = score
        
        CMS_data.to_csv('CCI_scores_NOPOA.csv')

elif choice == 'ISCCI':
    
    if POA_choice == 'yes':
        
        CMS_data ['ISCCI_POA'] = score

        CMS_data.to_csv('ISCCI_scores_POA.csv')
        
    else:
        CMS_data ['ISCCI_NOPOA'] = score

        CMS_data.to_csv('ISCCI_scores_NOPOA.csv')

print('Data is saved')
