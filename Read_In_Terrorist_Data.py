"""
This File loads in our intial data set.
Step 1 remove columns that we deemed unnecessary
Step 2 Filter data from 2000 to 2019
"""
import pandas as pd
import matplotlib.pyplot as plt

#Change path to your local computer
Path = 'C:\\Users\\Grant\\Desktop\\Random\\CS_Group_Project\\'
terrordata = pd.read_excel(
     Path + 'GDT_1970_2019.xlsx',
     engine='openpyxl')

time = terrordata.groupby(['iyear', 'imonth']).count()['iday']

col_remove = ['eventid', 'approxdate', 'extended', 'resolution', 'provstate', 'city', 'vicinity', 'location',
              'summary', 'crit1', 'crit2', 'crit3', 'alternative', 'alternative_txt', 'multiple', 
              'attacktype2', 'attacktype2_txt', 'attacktype3', 'attacktype3_txt', 'corp1', 'target1', 
            'targtype2', 'targtype2_txt', 'targsubtype2', 'targsubtype2_txt', 'corp2', 'target2', 'natlty2', 
              'natlty2_txt', 'targtype3', 'targtype3_txt', 'targsubtype3', 'targsubtype3_txt', 'corp3', 
              'target3', 'natlty3', 'natlty3_txt', 'gsubname', 'gname2', 'gsubname2', 'gname3', 'gsubname3', 
              'guncertain1', 'guncertain2', 'guncertain3', 'individual', 'claimmode', 'claimmode_txt', 'claim2', 
              'claimmode2', 'claimmode2_txt', 'claim3', 'claimmode3', 'claimmode3_txt', 'compclaim', 'weaptype2',
              'weaptype2_txt', 'weapsubtype2', 'weapsubtype2_txt', 'weaptype3', 'weaptype3_txt', 'weapsubtype3',
              'weapsubtype3_txt', 'weaptype4', 'weaptype4_txt', 'weapsubtype4', 'weapsubtype4_txt', 'weapdetail',
              'propcomment', 'divert', 'kidhijcountry', 'ransomnote', 'addnotes', 'scite1', 'scite2', 'scite3', 'dbsource', 
              'INT_LOG', 'INT_IDEO', 'INT_MISC', 'INT_ANY', 'related']



#Plot that shows number of events over time
time_plot = time.plot.line(figsize= (16, 6))
time_plot.set_title('Number of Terrorist Attacks Over Time')
time_plot.set_xlabel('Year, Month')
time_plot.set_ylabel('Number of Terrorist Attacks')

#remove columns
terrordata = terrordata.drop(columns=col_remove)

#export results
Last_Two_Decades = terrordata[terrordata['iyear'] >= 2000]
Last_Two_Decades.to_csv( Path + 'GDT_2000_2019.csv',index=False)

print("done!")
