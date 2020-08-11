import pandas as pd
import os
from datetime import date

def store(id, name):
    if not os.path.exists('Attendance-'+str(date.today().month)+'-'+str(date.today().year)+'.xlsx'):
        df = pd.DataFrame(columns=['Id', 'Name','Attendance'])
        df.to_excel('Attendance-'+str(date.today().month)+'-'+str(date.today().year)+'.xlsx', index=False)

    df1 = pd.read_excel('Attendance-'+str(date.today().month)+'-'+str(date.today().year)+'.xlsx' )
   

    x = df1['Id']== id
    ab = df1[x]
    
    result = df1.index[x]

    # att = df1.loc[result, 'Attendance']

    # if att.dropna().empty:
    #     att = 1
    # else:
    #     att+=1
    
    if ab.empty:        
        df1 = df1.append(pd.DataFrame([[id, name, 1]], columns=['Id', 'Name','Attendance']))
        df1.to_excel('Attendance-'+str(date.today().month)+'-'+str(date.today().year)+'.xlsx', index=False)
        
    
    else:
        df1.loc[result,'Attendance'] += 1
        df1.to_excel('Attendance-'+str(date.today().month)+'-'+str(date.today().year)+'.xlsx', index=False)
            
    

