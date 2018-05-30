'''
Created on 03-Mar-2018
@author: MohammedHussain
'''
import pandas as pd
from pandas import ExcelWriter 


def write_to_excel(exl_list,cols):
    
    df1 = pd.DataFrame(exl_list, columns=cols)
    writer = ExcelWriter('static/download/URLLookupService.xlsx')
    df1.to_excel(writer,'URLLookUpService',index= False)
    writer.save()
   