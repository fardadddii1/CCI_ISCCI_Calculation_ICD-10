##### ISCCI codes
def ISCCI_calc():
    wscore ={}
    Myocardial_infarction = 'I21x, I22x, I252'
    MI = pd.unique(Myocardial_infarction.split(', '))
    ws_MI = dict(zip(MI, [2]*len(MI)))
    wscore.update(ws_MI)
    #print (f'Myocardial_infarction = {MI}')
    Congestive_heart_failure = 'I099, I110, I130, I132, I255, I420, I425, I426, I427, I428, I429, I43x, I50x, P290'
    CHF = pd.unique(Congestive_heart_failure.split(', '))
    ws_CHF = dict(zip(CHF, [2]*len(CHF)))
    wscore.update(ws_CHF)
    #print (f'Congestive_heart_failure = {CHF}')
    Peripheral_vascular_disease = 'A5201, I70x, I71x, I731, I7389, I739, I75x, I771, I777x, I790, K551, K558, K559, Z9582x, Z959, 04R'
    PVD = pd.unique(Peripheral_vascular_disease.split(', '))
    ws_PVD = dict(zip(PVD, [0]*len(PVD)))
    wscore.update(ws_PVD)
    #print (f'Peripheral_vascular_disease = {PVD}')
    Cerebrovascular_disease = 'G45x, G46x, H340, I60, I61, I62, I63, I64, I65, I66, I67, I68, I69x'
    CD = pd.unique(Cerebrovascular_disease.split(', '))
    ws_CD = dict(zip(CD, [1]*len(CD)))
    wscore.update(ws_CD)
    #print (f'Cerebrovascular_disease = {CD}')
    Dementia = 'F00, F01, F02, F03x, G30x, G311, G3101, G3109, G3183'
    DT = pd.unique(Dementia.split(', '))
    ws_DT = dict(zip(DT, [2]*len(DT)))
    wscore.update(ws_DT)
    #print (f'Dementia = {DT}')
    Chronic_pulmonary_disease = 'I272, I278x, I279, J40, J41, J42, J43, J44, J45, J46, J47x, J60, J61, J62, J63, J64, J65, J66, J67x, J684, J701, J703'
    CPD = pd.unique(Chronic_pulmonary_disease.split(', '))
    ws_CPD = dict(zip(CPD, [1]*len(CPD)))
    wscore.update(ws_CPD)
    #print (f'Chronic_pulmonary_disease = {CPD}')
    Rheumatic_disease = 'M05x, M06x, M315, M316, M32, M33, M34x, M35x, M353, M360'
    RD = pd.unique(Rheumatic_disease.split(', '))
    ws_RD = dict(zip(RD, [2]*len(RD)))
    wscore.update(ws_RD)
    #print (f'Rheumatic_disease = {RD}')
    Peptic_ulcer_disease = 'K25, K26, K27, K28x'
    PUD = pd.unique(Peptic_ulcer_disease.split(', '))
    ws_PUD = dict(zip(PUD, [0]*len(PUD)))
    wscore.update(ws_PUD)
    #print (f'Peptic_ulcer_disease = {PUD}')
    Mild_liver_disease = 'B18x, K700, K701, K702x, K703x, K709, K713, K714, K715, K717, K73x, K74x, K752, K753, K754, K755, K756, K757, K758, K759, K760, K761, K762, K763, K764, K7689, K769, k77x, Z944'
    MLD = pd.unique(Mild_liver_disease.split(', '))
    ws_MLD = dict(zip(MLD, [0]*len(MLD)))
    wscore.update(ws_MLD)
    #print (f'Mild_liver_disease = {MLD}')
    Diabetes_without_chronic_complications = 'E101x, E1063x, E1064, E1065, E1066, E1067, E1068, E1069, E108, E109, E110x, E1163x, E1164, E1165, E1166, E1167, E1168, E1169, E118, E119, E130, E131, E1363x, E1364, E1365, E1366, E1367, E1368, E1369, E138, E139'
    DWOCC = pd.unique(Diabetes_without_chronic_complications.split(', '))
    ws_DWOCC = dict(zip(DWOCC, [0]*len(DWOCC)))
    wscore.update(ws_DWOCC)
    #print (f'Diabetes_without_chronic_complications = {DWOCC}')
    Diabetes_with_chronic_complications = 'E102, E103, E104, E105x, E10610, E10611, E10612, E10613, E10614, E10615, E10616, E10617, E10618, E10619, E1062x, E112, E113, E114, E115x, E11610, E11611, E11612, E11613, E11614, E11615, E11616, E11617, E11618, E11619, E1162x, E132, E133, E134, E135x, E13610, E13611, E13612, E13613, E13614, E13615, E13616, E13617, E13618, E13619, E1362x'
    DWCC = pd.unique(Diabetes_with_chronic_complications.split(', '))
    ws_DWCC = dict(zip(DWCC, [1]*len(DWCC)))
    wscore.update(ws_DWCC)
    #print (f'Diabetes_with_chronic_complications = {DWCC}')
    Hemiplegia_or_paraplegia = 'G041, G114, G801, G802, G81x, G82x, G830, G831, G832, G833, G834, G839'
    HOP = pd.unique(Hemiplegia_or_paraplegia.split(', '))
    ws_HOP = dict(zip(HOP, [1]*len(HOP)))
    wscore.update(ws_HOP)
    #print (f'Hemiplegia_or_paraplegias = {HOP}')
    Renal_disease = 'E082x, E102x, E112x, I120, I129, I130, I131x, N03x, N052, N053, N054, N055, N056, N057, N059, N062, N063, N064, N065, N072, N073, N074, N0725, N08, N171, N172, N18x, N19x, N250, Z4822, Z49x, Z940, Z992'
    RLD = pd.unique(Renal_disease.split(', '))
    ws_RLD = dict(zip(RLD, [0]*len(RLD)))
    wscore.update(ws_RLD)
    #print (f'Renal_disease = {RLD}')
    Any_malignancy = 'C00, C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C20, C21, C22, C23, C24, C25, C26x, C30, C31, C32, C33, C34x, C37, C38, C39, C40, C41, C43x, C45, C46, C47, C48, C49, C50, C51, C52, C53, C54, C55, C56, C57, C58x, C60, C61, C62, C63, C64, C65, C66, C67, C68, C69, C70, C71, C72, C73, C74, C75, C76x, C81, C82, C83, C84, C85x, C86x, C88x, C90, C91, C92, C93, C94, C95, C96x, C7Ax, C4Ax, D45x'
    AM = pd.unique(Any_malignancy.split(', '))
    ws_AM = dict(zip(AM, [2]*len(AM)))
    wscore.update(ws_AM)
    #print (f'Any_malignancy = {AM}')
    Moderate_or_severe_liver_disease = 'I851x, I864, K704x, K711x, K7151, K7210, K7211, K7290, K7291, K765, K766, K767, K7681'
    MOSLD = pd.unique(Moderate_or_severe_liver_disease.split(', '))
    ws_MOSLD = dict(zip(MOSLD, [0]*len(MOSLD)))
    wscore.update(ws_MOSLD)
    #print (f'Moderate_or_severe_liver_disease = {MOSLD}')
    Metastatic_solid_tumor = 'C77, C78, C79, C80, C801, C7Bx'
    MST = pd.unique(Metastatic_solid_tumor.split(', '))
    ws_MST = dict(zip(MST, [5]*len(MST)))
    wscore.update(ws_MST)
    #print (f'Metastatic_solid_tumor = {MST}')
    AIDS_HIV = 'B20x, B9735, Z21, O987x'
    AH = pd.unique(AIDS_HIV.split(', '))
    ws_AH = zip(AH, [0]*len(AH))
    wscore.update(ws_AH)
    #print (f'Metastatic_solid_tumor = {AH}')
    Same_cath_tup = [MI,CHF,PVD,CD,DT,CPD,RD,PUD,MLD,DWOCC,DWCC,HOP,RLD,AM,MOSLD,MST,AH]
    
    return Same_cath_tup, wscore
